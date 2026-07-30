import os
from aws_cdk import (
    Stack,
    aws_rds as rds,
    aws_ec2 as ec2,
    Duration,
    RemovalPolicy,
    SecretValue,
    App,
    Aws
)
from constructs import Construct

class SummerRdsStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # ========================================================================
        # 1. CONECTIVIDAD: USO DE LA VPC POR DEFECTO
        # ========================================================================
        # Según el curso, se utiliza la VPC por defecto ("VPC: Default")
        vpc = ec2.Vpc.from_lookup(self, "DefaultVpc", is_default=True)

        # ========================================================================
        # 2. CONFIGURACIÓN DEL GRUPO DE SEGURIDAD (SECURITY GROUP)
        # ========================================================================
        # Se crea un grupo de seguridad asociado a la VPC por defecto.
        # Para que sea accesible de forma pública como menciona la nota del curso:
        db_security_group = ec2.SecurityGroup(self, "SummerDBSecurityGroup",
            vpc=vpc,
            description="Grupo de seguridad para la base de datos de Summer",
            allow_all_outbound=True
        )
        
        # Opcional pero recomendado para que puedas ingresar desde tu IP pública externa:
        db_security_group.add_ingress_rule(
            peer=ec2.Peer.any_ipv4(), # Cambiar por tu IP fija en producción por seguridad
            connection=ec2.Port.tcp(3306),
            description="Permitir conexion externa al puerto MySQL"
        )

        # ========================================================================
        # 3. CREACIÓN DE LA INSTANCIA DE BASE DE DATOS (RDS MYSQL)
        # ========================================================================
        # Definición del motor de base de datos MySQL (Versión 8.0)
        db_engine = rds.DatabaseInstanceEngine.mysql(
            version=rds.MysqlEngineVersion.VER_8_0
        )

        # Instancia de la Base de Datos con especificaciones de capa gratuita (Free Tier)
        rds.DatabaseInstance(self, "SummerMySQLInstance",
            engine=db_engine,
            # Tipo de instancia: db.t3.micro (Elegible en la capa gratuita de AWS)
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE3,
                ec2.InstanceSize.MICRO
            ),
            vpc=vpc,
            # Forzar la selección a subredes públicas para que coincida con la VPC por defecto
            vpc_subnets=ec2.SubnetSelection(subnet_type=ec2.SubnetType.PUBLIC),
            # Configurar el acceso público como True para desarrollo
            publicly_accessible=True,
            # Asignar el grupo de seguridad creado previamente
            security_groups=[db_security_group],
            
            # Credenciales maestras (Asignación manual según requerimientos)
            # Nota: En producción se recomienda no harcodear contraseñas y usar Secrets Manager de forma automática.
            credentials=rds.Credentials.from_password(
                username="root",
                password=SecretValue.unsafe_plain_text(os.environ.get("DB_PASSWORD", "summer2026"))
            ),
            
            # Identificador único de la instancia en la consola de AWS
            instance_identifier="summer",
            # Nombre de la base de datos inicial
            database_name="summer",
            
            # Almacenamiento asignado: 20 GiB (SSD uso general gp2)
            allocated_storage=20,
            storage_type=rds.StorageType.GP2,
            
            # Habilitar escalado automático de almacenamiento = False
            max_allocated_storage=20, # Al igualarlo al allocated_storage, evita el auto-scaling
            
            # Copia de seguridad y backups automáticos
            backup_retention=Duration.days(7), # Periodo de retención de copia de seguridad: 7 días
            
            # Mantenimiento
            auto_minor_version_upgrade=False, # Habilitar actualización automática de versiones secundarias = False
            
            # Eliminación y protección
            # Al ser un entorno de desarrollo/aprendizaje se puede configurar para destruir al borrar el Stack
            removal_policy=RemovalPolicy.DESTROY, 
            deletion_protection=False # Protección contra la eliminación = False
        )


# ========================================================================
# PUNTO DE ENTRADA FUERA DE LA CLASE (Alineado con tu referencia)
# ========================================================================
app = App()

# Instanciamos el Stack pasando el entorno dinámico que cdk inyecta desde tu --profile
SummerRdsStack(
    app, 
    "SummerRdsStack",
    env={
        "account": os.environ.get("CDK_DEFAULT_ACCOUNT"),
        "region": os.environ.get("CDK_DEFAULT_REGION")
    }
)

# Sintetiza la aplicación para generar las plantillas de CloudFormation
app.synth()