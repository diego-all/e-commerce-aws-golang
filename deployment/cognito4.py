from aws_cdk import (
    Stack,
    aws_cognito as cognito,
    Duration,
    RemovalPolicy,
    App
)
from constructs import Construct

class SummerCognitoStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # ========================================================================
        # 1. CREACIÓN DEL USER POOL (GRUPO de USUARIOS)
        # ========================================================================
        user_pool = cognito.UserPool(self, "SummerUserPool",
            user_pool_name="summer",
            
            # Registro automático habilitado (Self Sign-up)
            self_sign_up_enabled=True,
            
            # Opciones de inicio de sesión = Solo correo electrónico
            sign_in_aliases=cognito.SignInAliases(
                email=True
            ),
            
            # Verificación y confirmación asistidas por Cognito (Mensajes automáticos)
            # Permite que Cognito envíe automáticamente mensajes para verificar y confirmar
            auto_verify=cognito.AutoVerifiedAttrs(
                email=True
            ),
            
            # Atributo obligatorio = email
            standard_attributes=cognito.StandardAttributes(
                email=cognito.StandardAttribute(
                    required=True,
                    mutable=True
                )
            ),
            
            # Política de contraseñas: 8 caracteres (sin requisitos de complejidad)
            password_policy=cognito.PasswordPolicy(
                min_length=8,
                require_lowercase=False,
                require_uppercase=False,
                require_digits=False,
                require_symbols=False,
                temp_password_validity=Duration.days(7)
            ),
            
            # Autenticación multifactor = Sin MFA
            mfa=cognito.Mfa.OFF,
            
            # Recuperación automática de cuentas: Solo correo electrónico
            account_recovery=cognito.AccountRecovery.EMAIL_ONLY,
            
            # Verificación de los cambios de atributo:
            # Mantiene el valor del atributo original activo cuando hay una actualización pendiente
            # keep_original_attributes=[
            #     "email"
            # ],
            
            # Configurar el envío de mensajes = Enviar correo electrónico con Cognito
            email=cognito.UserPoolEmail.with_cognito(),
            
            # Política de eliminación (Solo para desarrollo: elimina el recurso al destruir el stack)
            removal_policy=RemovalPolicy.DESTROY
        )

        # ========================================================================
        # 2. DOMINIO DE COGNITO
        # ========================================================================
        # Nota: El domain_prefix debe ser único a nivel global en la región de AWS.
        user_pool.add_domain("SummerDomain",
            cognito_domain=cognito.CognitoDomainOptions(
                domain_prefix="summer-app-dev-unique" 
            )
        )

        # ========================================================================
        # 3. CLIENTE DE LA APLICACIÓN (APP CLIENT) CON CONFIGURACIÓN AVANZADA
        # ========================================================================
        user_pool.add_client("SummerAppClient",
            user_pool_client_name="summer",
            
            # Secreto de cliente = No generar secreto (para clientes públicos/SPAs)
            generate_secret=False, 
            
            # Flujos de autenticación seleccionados
            auth_flows=cognito.AuthFlow(
                user_srp=True,        # ALLOW_USER_SRP_AUTH
                custom=True,          # ALLOW_CUSTOM_AUTH
                user_password=False   # No habilitado explícitamente en el resumen
            ),
            
            # Duración de la sesión del flujo de autenticación = 3 minutos
            auth_session_validity=Duration.minutes(3),
            
            # Vencimiento de los Tokens
            refresh_token_validity=Duration.days(30), # 30 días
            access_token_validity=Duration.days(1),   # 1 día
            id_token_validity=Duration.days(1),       # 1 día
            
            # Configuración de Seguridad y Errores
            enable_token_revocation=True,             # Habilitar revocación de token
            prevent_user_existence_errors=True,       # Evitar errores de existencia de usuarios
            
            # Integración de la aplicación (OAuth / Hosted UI)
            o_auth=cognito.OAuthSettings(
                flows=cognito.OAuthFlows(
                    authorization_code_grant=True,
                    implicit_code_grant=True
                ),
                # URL de devolucion de llamadas (Callback) permitidas
                callback_urls=["https://localhost:3000"],
                # URL de cierre de sesión (Logout)
                logout_urls=["https://localhost:3000"],
                # Ámbitos de OpenID Connect = OpenID y Correo electrónico
                scopes=[
                    cognito.OAuthScope.OPENID,
                    cognito.OAuthScope.EMAIL
                ]
            ),
            
            # Permisos de lectura/escritura de atributos (Configuración final)
            read_attributes=cognito.ClientAttributes().with_standard_attributes(
                email=True, 
                email_verified=True
            ),
            write_attributes=cognito.ClientAttributes().with_standard_attributes(
                email=True
            ),
            
            # Proveedores de identidad = Grupo de usuarios de Cognito
            supported_identity_providers=[
                cognito.UserPoolClientIdentityProvider.COGNITO
            ]
        )


# ========================================================================
# CORRECCIÓN: PUNTO DE ENTRADA FUERA DE LA CLASE (SIN IDENTACIÓN)
# ========================================================================
app = App()

# Instanciamos el Stack para que CDK pueda renderizarlo
SummerCognitoStack(app, "SummerCognitoStack")

# Sintetiza la aplicación para generar los artefactos de CloudFormation
app.synth()