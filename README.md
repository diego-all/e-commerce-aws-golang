# E-Commerce - Golang + NextJS (AWS Cloud)

dlob !!mfa



## Back-End

### Lenguaje y Entorno de Desarrollo
* **Golang**: Lenguaje principal (Curso básico inicial)
* **Visual Studio Code**: Editor de código
* **GitHub**: Control de versiones y repositorio

### Bases de Datos y Herramientas de Desarrollo
* **HeidiSQL**: Cliente de gestión de bases de datos
* **Postman**: Pruebas y documentación de APIs

### Servicios en la Nube (AWS)
* **AWS RDS**: Servicio de bases de datos relacionales
* **AWS IAM**: Gestión de roles y permisos de acceso
* **AWS Cognito**: Autenticación y gestión de usuarios
* **AWS Lambda**: Computación serverless
* **AWS S3**: Almacenamiento de archivos y objetos
* **AWS CloudWatch**: Monitoreo y registro de logs
* **AWS API Gateway**: Exposición y gestión de APIs públicas
* **AWS Secrets Manager**: Almacenamiento seguro de credenciales y secretos

---

## Front-End

### Framework y Entorno
* **Next.js**: Framework de React para el desarrollo web

### Herramientas de Pruebas
* **Insomnia**: Cliente para pruebas de APIs

### Despliegue e Infraestructura
* **Netlify**: Plataforma de alojamiento y despliegue continuo



AYUDA MEMORIA DE MIS FAVORITOS (APPS DE AWS EN LA PARTE SUPERIOR)



    cdk synth --app "python3 cognito4.py" --profile bold-free-tier




Stack ARN:
arn:aws:cloudformation:us-east-1:800445863816:stack/SummerCognitoStack/8ecc8980-50e8-11f1-8045-12a714253e55



Stack ARN: arn:aws:cloudformation:us-east-1:800445863816:stack/SummerCognitoStack/8ecc8980...

Los tres recursos quedaron creados en AWS:

AWS::Cognito::UserPool — el User Pool "summer"
AWS::Cognito::UserPoolDomain — dominio summer-app-dev-unique
AWS::Cognito::UserPoolClient — el App Client "summer"


El conflicto ocurre por la forma en que CDK sabe qué archivo ejecutar. Por defecto, CDK busca un archivo de configuración llamado cdk.json en la raíz de la carpeta. Como no lo tienes ahí, cuando tú ejecutas un comando en la terminal (por ejemplo: cdk deploy), tienes que pasarle explícitamente el archivo de la app usando el parámetro -a (o --app).

Si ejecutas: cdk deploy -a "python3 cognito4.py"

Y luego ejecutas: cdk deploy -a "python3 rds_mysql.py"

¿Qué pasará? No habrá un conflicto en AWS (se crearán ambos servicios de forma independiente), pero el contenido de la carpeta local cdk.out se va a sobrescribir en cada ejecución. Cuando lances el de RDS, borrará o ignorará los metadatos generados previamente para Cognito en tu máquina local.

    # Para trabajar con Cognito sin afectar nada más:
    cdk synth -a "python3 cognito4.py" -o cdk_cognito.out
    cdk deploy -a "python3 cognito4.py" -o cdk_cognito.out

    # Para trabajar con tu nueva RDS de MySQL:
    cdk synth -a "python3 rds_mysql.py" -o cdk_rds.out --profile bold-free-tier
    cdk deploy -a "python3 rds_mysql.py" -o cdk_rds.out --profile bold-free-tier

    

OPORTUNIDAD: 


- tema de seguridad implicito con las politicas(bucket).


        REGISTRO (una vez por usuario)
        Hosted UI --> Cognito User Pool "summer"
                            | al confirmar el correo (trigger Post Confirmation)
                            v
                    Lambda summerUser (Go)
                            |-- lee credenciales --> Secrets Manager (SummerUserDbSecret)
                            '-- INSERT en users ---> RDS MySQL "summer"
                    (sus logs van a CloudWatch)

        SUBIR IMAGEN
        curl / Postman / Next.js --PUT + access_token--> API Gateway --> S3
                                        autorizador Cognito valida el token (firma, expiración, scope openid)
                                        API Gateway asume api_gateway_role (permiso s3:PutObject)

        VER IMAGEN
        Navegador --GET--> S3 directo (política pública del bucket, sin API Gateway ni login)


    Puntos clave:

Cognito guarda los usuarios y entrega tokens. El Hosted UI es su pantalla de login.
API Gateway no ejecuta código. Valida el token y reenvía el PUT a S3, usando el segmento {folder} de la URL como nombre del bucket y {object} como nombre del archivo.
La Lambda solo se ejecuta al confirmar un usuario, y copia su correo y su sub a MySQL.
El Identity Pool y sus roles existen pero este flujo no los usa.


### Terraform

    terraform fmt
    terraform validate
    terraform plan -out=tfplan
    terraform apply tfplan



### Cognito Test

Abre esta URL en el navegador. Es la misma de antes con response_type=token:

https://summer-app-dev-unique.auth.us-east-1.amazoncognito.com/login?client_id=3lejofgfifede3r4nrf7vaqfl2&response_type=token&scope=aws.cognito.signin.user.admin+email+openid&redirect_uri=https://localhost:3000


https://localhost:3000/#id_token=eyJraWQiOiJLeU1BRlNuTFZ0QmlwTUdEWkJva2pEM1hvVjhVSXorNFBQTC9ycjNYNTM0PSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiT01yUkxRV3pQUlczcktmWW5hTjAxZyIsInN1YiI6IjQ0MjgzNDA4LTIwNzEtNzAxZC05YjdhLTEzYzU1MjgzNjgzZiIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tL3VzLWVhc3QtMV9oWW1XTGJGdnAiLCJjb2duaXRvOnVzZXJuYW1lIjoiNDQyODM0MDgtMjA3MS03MDFkLTliN2EtMTNjNTUyODM2ODNmIiwiYXVkIjoiM2xlam9mZ2ZpZmVkZTNyNG5yZjd2YXFmbDIiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTc5MjIxMDU2NSwiZXhwIjoxNzkyMjk2OTY1LCJpYXQiOjE3OTIyMTA1NjYsImp0aSI6ImU1ZDBjNzI0LWQwMjQtNDMwNS1hYWQ3LWZlOWE2OTAyZWY1ZiIsImVtYWlsIjoiZHBvc2FkYWxsYW5vQGdtYWlsLmNvbSJ9.gjFTo-bBNlqlHtC00FzRj80Vovt60d0LfH-u0NFMydZ8u97DgvW1Kntr5d4a1xh3jDE12N2OQPOQfJWMCPLr-BwmywF_iKpNOuGx70SsQrqqYuK2gA1GvMtJTe8I7GwOJ5FQjQq9Bg37kK2Ops3Ev5re105W253BbAoxwH_3TIeYZazLqC9spSj-vTPyoaUx7RdfpvDR5D6TJj7hRLE76ykvsfH_YEUQ_MI-a2o1HHSs6y4lHhVYGmSs24nfVgxDss6znu8-eI_0IQuAcEAS64EBRQs663Dxfnx_thMEbsFpLk1gkIG8OD920vl4LparFAei24-Gws66waVt-Z0YpQ&access_token=eyJraWQiOiJCSWFqY3NBLzRGOVd4dEJ1TFZBMWpuZVpYVEtRTHAxSGpFZ1JiR0tublQ4PSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI0NDI4MzQwOC0yMDcxLTcwMWQtOWI3YS0xM2M1NTI4MzY4M2YiLCJ0b2tlbl91c2UiOiJhY2Nlc3MiLCJzY29wZSI6ImF3cy5jb2duaXRvLnNpZ25pbi51c2VyLmFkbWluIG9wZW5pZCBlbWFpbCIsImF1dGhfdGltZSI6MTc5MjIxMDU2NSwiaXNzIjoiaHR0cHM6Ly9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbS91cy1lYXN0LTFfaFltV0xiRnZwIiwiZXhwIjoxNzkyMjk2OTY1LCJpYXQiOjE3OTIyMTA1NjYsInZlcnNpb24iOjIsImp0aSI6IjU0OWU5YWExLTU1ZWQtNDE5My04YTk4LTVkNzcyYjM3NjNmNiIsImNsaWVudF9pZCI6IjNsZWpvZmdmaWZlZGUzcjRucmY3dmFxZmwyIiwidXNlcm5hbWUiOiI0NDI4MzQwOC0yMDcxLTcwMWQtOWI3YS0xM2M1NTI4MzY4M2YifQ.IBExD98sLK7FYRpIZrlgV9j7IUwKbY_S40x0V2B6Vil86qzh7asTKnfZ1br3jJ-tyHnSWkZOreyE6UyeBPhRFbYU9Eu18y1XQYVPkvMmLFoJrrkVSLGikuf6uxD8UYv006KidqO7zfY5_gZAtXxI4R-X8HOgx3A6IVrewoQT3EECEct8svugkBYsG3DyAIXxy-RDz23oCxY99t4TdB2IV2FobqedVJN2IF8mxV9k2twTugHPJKZE3yRxHw-4uXle9h7zPAXUgyOSgdvFaQG2Eq9skZ-TWJBBDtmzC4IB1FM3vdQ5d8grxfjjTCk-SgZTEfWGUTBTqxpeqguWieEfzA&expires_in=86400&token_type=Bearer




### JWT


{
  "kid": "KyMAFSnLVtBipMGDZBokjD3XoV8UIz+4PPL/rr3X534=",
  "alg": "RS256"
}

{
  "at_hash": "OMrRLQWzPRW3rKfYnaN01g",
  "sub": "44283408-2071-701d-9b7a-13c55283683f",
  "email_verified": true,
  "iss": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_hYmWLbFvp",
  "cognito:username": "44283408-2071-701d-9b7a-13c55283683f",
  "aud": "3lejofgfifede3r4nrf7vaqfl2",
  "token_use": "id",
  "auth_time": 1792210565,
  "exp": 1792296965,
  "iat": 1792210566,
  "jti": "e5d0c724-d024-4305-aad7-fe9a6902ef5f",
  "email": "dposadallano@gmail.com"
}

{
  "e": "AQAB",
  "kty": "RSA",
  "n": "1hGXRFxDtDwJ4XPhVp5LiNREn_0jG02aGZNcRJ340i6QVOjTnjiwiL_mMSgKDQsRyuGbpLIiNFoCRYjF7IWF0Y3R4lzWnOE6oL4DZDS36Sxh8wNaenEF5eBhS6l15P26NhmOpemoUpG8DxQeqNh7rJkFoJ50xBgQEBx9n3LffUY92DCEq45DDOsQnGp1JMmogLAALV-IVN-QmjhHGJ94moWebFC9XYgCmTWn5tELm9FmldxfNonTIT95MdLfyrjqLYFjv1EnmEt-nYTAgAB4NUTgGLXW9qBbH1xiR-mIll6TO5NjEXXLuLZXdfzBFbTzvu6wsFbrlTWtZe7j3pK6KQ"
}

de donde sale esta public key?




### ### MySQL


    mysql -h summer.c87semo4ses5.us-east-1.rds.amazonaws.com -u root -p summer \
    -e "SHOW TABLES; SELECT User_UUID, User_Email, User_Status FROM users;"

    passwd summer2026