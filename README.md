# E-Commerce - Golang + NextJS (AWS Cloud)



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

    
