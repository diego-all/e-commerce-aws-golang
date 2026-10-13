# E-commerce - Golang + NextJS (AWS Cloud)

- Duracion: 34 Horas
- Abril / 2023
- Go 1.20


## Sección 1: Introducción


### 1. Introducción

- Backend en Go
- 8 servicios de AWS (Lambda, S3, Secret Manager, Cognito, API Gateway, Cloudwatch, RDS)
- Postman, Github

https://github.com/ptilotta/gambit


https://pablotilotta.com/  Creando una red social como twitter en GO y React.  Maestria en AWS RDS:

https://www.youtube.com/c/PabloTilottaMaster


Frontend NextJS

- 

Por que aparece una e en visual studio que no se deja quitar como en los simpsons?


## Sección 2: Curso de Golang desde 0


### 2. Lineamientos de Go

- Es un lenguaje seguro por su fuertemente tipado que ayuda a evitar errores.

- Este lenguaje hereda su core de C++ con sintaxis mejorada y muy amigable.

- Go fue pensado para aprovechar los ultimos avances en hardware, los multiprocesadores, enormes cantidades de memoria y el paralelismo.

- Go es un lenguaje compilado, generando archivos .exe portables a cualquier sistema operativo y version (Su exe contiene todo lo necesario para ejecutarse).
Cuando se hace un build de la aplicacion toma todas las dependencias y paquetes usados por la app y los mete dentro del exe para poder ejecutarlos en cualquier plataforma.

- Go demostro  ser el lenguaje ideal para grandes desarrollos con miles y miles de usuarios concurrentes y millones de transacciones.
(Si se escribe la misma aplicacion en otro lenguaje como python o node.js ya se consumen mas recursos.)

"Ahorra dinero en servidores, proporcion 1 servidor de Go por 10 en otro lenguaje."

- Go es facil de entender, su sintaxis es clara y mejorada con respecto a otro lenguajes.  "Simplista, es mucho mas facil que python, ha simplificado, han eliminado estructuras.

- En Go no hace falta ';' puntos y comas.

- El compilador arroja advertencias, ante variables desclaradas no utilizadas, y paquetes importados no utilizados.

- **Las funciones en Go pueden devovler mas de un valor.**  (Poder recibir una lista de valores diferentes)

- Se puede desarrollar en Go tanto instrucciones sincronicas como asincronicas. (No esta tan pensado como podria ser un node.js con las promesas, los async, awaits, pero tiene las estructuras necesarias para trabajar de manera asincrona).

- Solo existe la instrucción For para iteraciones (no existe While, ni Do Until, ni nada similar). (Recorrer colecciones de datos)

- Go no es un lenguaje orientado a objetos, y resuelve lo que conocemos como POO, con estructuras, Funciones, Metodos e interfaces) Y dentro no van a tener no solo propiedades sino que van a poder tener funciones, metodos y demas. ENr ealidad en Go no existe la diferencia entre metodo y funcion. Para todo lo que tiene que ver con rutinas Go lo llama funciones, y puede ser que esas funciones devuelvan o no valores. SIno devuelve valores se entiende como que son metodos. ??????

- El scope de variables, metodos y funciones se determinan con nombres en mayusculas y minusculas.

Ejemplo: Realmente se trata de un metodo ya que no retorna ninguna lista de argumentos de respuesta 

    func LeoSupport_Mensajes(w http.ResponseWriter, r *http.Request){

    }


### 3. Instalando Go


### 4. Configurando Go y el entorno


GOROOT: Carpeta root donde esta instalado el interprete de Go y los paquetes necesarios.
GO PATH


### 5. Instalando Y configurando Git & GiHub



### 6. Instalando y configurando visual studio code


Plugin go snippets


### 7. Inicializando nuestro proyecto de Go y el main



### 8. Hola Mundo en Go 



### 9. Inicio con Variables e importacion de paquetes


Line feed y los carriers return CRLF



### 10. Resto variables

La premisa de go es el performance, es decir que se ocupe le menor cantidad de memoria posible.

 
### 11. Funciones





### 12. Condicionales


	if os := runtime.GOOS; os == "Linux." {

	} else {

	}

Comprimir.
Para que el ejecutable pese lo menos posible.


### 13. Ejercicio 01

1. Crear un paquete nuevo llamado 'ejercicios'
2. Crear un archivo GO en ese paquete llamado 'ejercio01.go'
3. Crear una funcion publica, que devuelva 2 valores (int y string)y que reciba de parametro un valor 'string'
4. El parametro de tipo String recibido debera ser convertido a entero y si el entero es > a 100, el string retornado debe decir "Es mayor a 100" de lo contrario, devolver el mensaje "Es menor a 100".
5. El valor numerico entero retornado debe corresponder al string convertido
6. En main.go, llamar a dicha funcion asignandola a 2 variables y luego mostrar dichas variables por consola.
7. Grabar, ejecutar y luego subir todo a Github.


## 14. Captura de datos por pantalla


Los puede leer de muchas fuentes de datos, de archivos , de dispositivos tipo conectores de datos, lectores de codigo de barras, etc

stdin: en cualquier sistema es el teclado.
stdout: en cualquier sistema es la pantalla.

	scanner := bufio.NewScanner(os.Stdin)





### 15. Iteraciones


### 16. Ejercicio 02


1. Crear un archivo Go en el paquete ejercicios llamado ejercicio02.go
2. Crear una funcion Publica, que pida por teclado un numero, valide si hay error o no (y si hay error que vuelva a pedirle).
3. En base al numero recibido crear la tabla numerica del mismo. De 1 al 10 y la muestre por pantalla.
4. En main, llamar a dicha funcion.
5. Grabar, ejecutar y luego subir todo a Github.


### 17. Manejo de archivos



### 18. Funciones anonimas y Closures

No es un tema muy digerible, no es un tema muy facil a veces cuesta buscar un caso de uso.


Las funciones se pueden asignar a una variable, pasar por parametro, se pueden devolver por parametro. En node.js tambien se trabaja con funciones anonimas y son muy utiles, por que no necesito ir creando funciones dentro del codigo por que de esa manera estaria perdiendo el scope de muchas variables y de mucha informacion.

**Funciones anonimas**: una funcion que noo tiene un nombre y que puede ser asignada tanto a una variable, como pasarse por parametro, 

    func Calculos() {

        var numero3 int = 32
        var numero4 int = 243

        suma := func(numero1 int, numero2 int) int {
            return numero1 + numero2 + numero3 + numero4
        }

        fmt.Println(suma(10, 25))

    }

Todo es debido al scope, ya que numero3 y numero4 estan en la misma funcion calculos. Se crearon para tener un codigo mucho mas acotado, 

En el otro ejemplo se ve como una sobrecarga de metodos que se veia en otros lenguajes, aunque la sobrecarga de funciones lo que hacia y lo que permitia es que cambiar la cantidad y los tipos de parametros recibidos.

**En este caso no, se esta reinventando el calculo** 

    func Calculos() {

        var numero3 int = 32
        var numero4 int = 243

        calculo := func(numero1 int, numero2 int) int {
            return numero1 + numero2 + numero3 + numero4
        }

        fmt.Println(calculo(10, 25))

        calculo = func(numero1 int, numero2 int) int {
            return numero1 * numero2 * numero3
        }

        fmt.Println(calculo(10, 25))
    }

Todo esto que hubiera costado hacer 2 funciones por afuera, se hace en una misma funcion, utilizando funciones anonimas.

Tambien se podria devolver una funcion, esto es factible, se puede hacer que Calculos() devuelva una funcion, y donde se este llamando a Calculos() la variable la cual se asigna va a ser creada como una funcion anonima y se va a poder interactuar y darle toda una logica, 

    func Calculos() func(int, int) int {
        ...
    }

**Closure:** Al aprecer es una funcion que retorna otra funcion.

¿Cual es la ventaja del Closure?
El tema del ofuscamiento del codigo.     ?????

Tanto numero como secuencia lo va a inicializar la priemra vez y luego va a quedar oculto. 

> "Segun Pablo, hay casos de uso para emplear un closure, a lo largo de su vida profesional no tuvo la necesidad de usar esto, pero a veces se tiene una caja de herramientas llena de herramientas y no siempre se usa todo, pero es importante saber que se dispone de esto, por que van a existir determinados casos de uso donde se debe jugar con esto."


### 19. Recursión


La recursion es una funcion que se llama a si misma n veces. Se vaa exponer como publica para que pueda ser llamada desde main 


Lo primero que debemos contruir cuando trabajamos con recursion es la salida de la recursion, para que no se nos quede colgada la funcion, 












### 20. Array & Slices 



### 21. Mapas en Go


### 22. Estructuras (POO)



### 23. Interfaces (POO)



### 24. Defer, Panic & Recover



### 25. Go Routines (Async)



### 26 Channels (Async)



### 27. WebServer



### 28. Middlewares


## Sección 3 : Backend - Inicio de Desarrollo


### 29. Inicio de Backend

Cuenta en AWS:

- RDS:
- EC2 (Security group para la base de datos)
- Cognito: Manejar el login y la seguridad de usuarios.
- Secret Manager: Alojar las credenciales de la base de datos.
- IAM: Perfiles, Roles.
- Lambdas: Como configurar, como subir o compilar.
- API Gateway: Se le va añadir una capa de API Gateway a las lambdas. Hara que las lambdas sean publicas y van a  recibir peticiones, como cualquier API normal
- Bucket S3: Para subir las imagenes, la del producto y la del avatar.
- Tecnica de API Gateway directo a S3.

- Desarrollar una API de tipo REST que va a ser un trigger de cognito cuando el usuario confirma su email va a disparar una API de lambda que va a ejecutar el reigstro en una base de datos. 

- Luego la API HTTP normal que es el desarrollo de todo el backend.

**Objetivo:** No es aprender a hacer un backend, sino aprender todos estos servicios de AWS mencionados y perfeccionar el desarrollo en lenguaje Go.


### 30. Creando la cuenta de AWS

Creada en Marzo de 2025

    dposadallanoe@gmail.com
    Vv0!!
    b0ld



### 31. Recorrido por Billing

Tilotta paga en promedio 42 a 50 USD.

Base de datos Aurora que se tiene en modalidad serverless 2. (Tiene un costo bastante elevado para ser una base de datos es lo que se utiliza)

RDS es el mas costoso  46,90 USD

2 secretos en secret manager 0,80 USD.

API gateway no tiene costo por que tiene una free tier de miles de peticiones.

CloudWAtch (Se tienen 10 alarmas para crear metricas)

Cognito (5 user pools gratuitos)

Lambdas se tienen 400 k segundos en la free tier. 


**AWS orientado a Datos**

https://www.udemy.com/course/aws-orientado-a-datos/?couponCode=PLOYALTY0923

Slack y Discord

**Norte de Virginia es el datacenter que tinee mayor seguridad y mayor observabilidad.**





### 32. Descarga e instalacion de Postman


## Seccion 5: Backend - Cognito


### 33. Primeros pasos con cognito


Esta la base de seguridad del login de usuarios. Lo que no quita que no vayamos a tener en una base de datos una tabla de usuarios, que la vamos a tener que ir de alguna manera indirectamente sincronizando con cognito. Cada vez que un usuario se registre, 

Luego vamos a desarrollar una lambda que va a capturar los datos, cuando el usuario ya ha veirifcado su mail, cognito, va a disparar un trigger hacia una lambda que nos va a enviar los datos que ese usuario, mediante el token y demas.

Y nosotros vamos a registrar a ese usuario en nuestra base de datos. Luego vamos a tener endpoints de modificacion de datos del usuario, que eso va a interactuar directamente el front con el backend a nivel API para modificar los datos usuario, para borrar un usuario, para listar usuarios, y pra traer los datos de un usuario determinado. Pero todo nace en cognito, 


En la siguiente clase se va a crear el grupo de usuarios para gambit.

- Crear grupo de usuarios

EN principio se tiene un ID de grupo de usuarios

us-east-1_jdfksdjfksdf

- ARN: Se configura en la aplicacion para poder acceder a ese grupo de usuarios.

- Estado de la confirmacion

En cada mail que envia amazon hay un link, que permite hacerle click y uno termina confirmando la identidad.

Una vez que el usuario esta confirmado con su identidad para Amazon, ese usuario esta en estado de habilitado y confirmado.

Nosotros para nuestro ecommerce vamos a tomar como validos los usuarios que ya estan confirmados.

Que figuren aqui no significa que vyamos a hacer nada con ellos, simplemente es un registo. 
Es como si fuera base de datos de usuario que la va manteniendo Amazon, pero nosotros vamos a tener nuestra propia base de datos de usuario.

Pero hay empresas que con tener estos datos aqui les basta. No tienen por que crear una base de datos, ni tabla de usuarios, sino que lo manejan directamente desde Amazon y desde aqui tienen todo.

Tambien tengo la posibilidad e importar usuarios si tengo un CSV con los datos de un usuario.

- Grupos
- Experiencia de inicio de sesion: se configura cual es el dato principal para iniciar sesion.
- Identidades federadas: son las identidades externas como Facebook, Google, Amazon, Apple.

A veces uno va a un sistema y me permite Loggearme con mis credenciales de Google o con mi Perfil de Facebook. eso tambien se le puede añadir a nuestro grupo de usuarios y cuando desarrollemos el login, vamos a poder introducir esto.

Ademas cognito cuando uno se loggea devuelve una serie de datos entre los cuales esta el Access token que esta en un formato como nosotros lo conocemos  como JSON Web Token.
En amazon cognito se llama Access Token, y ese token es el que nosotros vamos a utilizar para enviar a la API y para obtener la validacion de cognito.

Cuando se desarrollen las APIS, van a ver cuando se configure **la API Gateway,** que vasn a tener la posibilidad de decirle que esa peticion va a tener que estar autenticada con cognito.
Y aca es donde nosotros vamos a enviar en el header como cualquier API, el token authorization como 


Este token tiene una expiracion,

Como es mucho el trabajo que vamos a tener que ir haciendo, no tenia sentido meterle en el medio identidades federadas y ademas 


- Experiencia de inscripcion: Aqui lo que se tiene es la verificacion y confirmacion asistida por cognito. Permitir que congnito envie automaticamente mensajes para verificar y confirmar.

**Esta habilitado** Obviamente por que vamos a querer que nos envie un mensaje de habilicion y confirmacion de mail, y los atributos pendientes de verificacion, 

Enviar un mensaje de correo electronico o verificar la direccion de correo electronico.

- Atributos obligatorios : email

- Atributos personalizados: Es como si estuvieran diseñando una tabla de base de datos, 

- Registro automatico, 

- Mensajeria: default (cognito)

- Region (SES): Simple email service.

- Direccion de correo electronico del remitente.

- SMS: Tiene costo elevado

- PLantillas de mensajes

Integracion de aplicaciones

Es importante nos indica cual es el dominio para cuando queramos interactuar con cognito desde la aplicacion cliente.

- Srvidores de recursos: Autenticacion OAuth 2.0

- Personalizacion de la interfaz de usuario alojada. ( CSS Personalizado)
Se puede configurar un logo, un CSS personalizado. Cognito nos da una aplicacion para Loggear.
En caso de que no se desee desarrollador un frontend.
Cognito nos da una aplicacion para que nosotros hagamos lo que necesitamos.



- Clientes para aplicaciones y analisis.

Id de cliente
Flujos de autenticacion
ALLOW_CUSTOM_AUTH
ALLOW_REFRESH_TOKEN_AUTH
ALLOW_USER_SRP_AUTH


- Permisos de lectura y escritura de atributos

Si nosotros vamos a hacer que nuestra base de usuarios trabaje directamente con cognito.




### 34. Instalador de Gambit.exe

  Private Sub txtToken_TextChanged(sender As Object, e As EventArgs) Handles txtToken.TextChanged
        Dim t, tf As String
        Dim desde, hasta As Integer
        t = txtToken.Text
        desde = InStr(1, t, "access_token=")
        hasta = InStr(desde, t, "&token_type=") - 13
        tf = t.Substring(desde + 12, hasta - desde)
        Clipboard.SetText(tf)
        MessageBox.Show(tf)
 
 End Sub




### 35. Creando nuestro grupo de usuarios y configurandolo

Vamos a crear nuestro grupo de usuarios.

hacerlo con identidades federadas.

Opciones de inicio de sesion = correo electronico

Politica de contraseñas: 8 caracteres

Autenticacion multifactor = sin MFA

recuperacion automatica de cuentas = Habilitar la recuperacion automatica de cuentas

metodo de entrega de los mensajes de recuperacion de cuentas de usuario = solo correo electronnico

Registro automatico = habilitar el registor automatico

Verifricacion y confirmacion asistidas por Cognito = permitir que cognito envie automaticamente mensajes para verificar y confirmar - Recomendado.

Enviar mensaje de correo electronico, verificar la direccion de correo electronico

- Verificacion de los cambios de atributo

Mantener el valor del atributo original activo cuando hay una actualizacion pendiente - recomendado

Direccion de correo electronico

Atributo obligatorio = email

Configuar el envio de mensajes = Enviar correo elctronico con cognito


Integracion de la aplicacion  

- Nombre del grupo de usuarios = summer

- Paginas de autenticacion alojadas = Usarla interfaz de usuario alojada de Cognito

- Dominio 

INTERESANTE PROAR EL DOMINIO PERSONALIZADO

- Utilizar un dominio de Cognito = https://summer

- Cliente de aplicacion inicial = Cliente publico

- Nombre del cliente de la aplicacion = summer


Secreto de cliente = No generar secreto de cliente ( No justifica ya que tiene un costo adicional en secret manager)

- URL de devolucion de llamadas permitidas = https://localhost:3000


- Configuracion avanzada del cliente y la aplicacion

Seleccionar flujos de autenticacion

ALLOW_USER_SRP_AUTH
ALLOW_CUSTOM_AUTH
ALLOW_USER_SRP_AUTH

Duracion de la sesion del flujo de autenticacion = 3 minutos

Vencimiento del token de actualizacion = 30 dias

Vencimiento del token de acceso = 1 dia

Vencimiento del token id = 1 dia


Habilitar revocacion de token = true

Evitar errores de aexistencia de usuarios = true

- Proveedores de identidad = grupo de usuarios de cognito


- Ambitos de Open ID Connect = OpenID y Correo electronico

s

### 36. Probando la aplicacion de Login y obteniendo el JWT


Ya se tiene un grupo de usuarios, vamos a probar la aplicacion y a hacer un registro.


En amazon Cognito

Grupo de usuarios actual
    Clientes de Aplicacion    ==>  Ver pagina de inicio de sesion.

    Hacemos click en sign up

Se diligencia con un correo y contraseña.


Se recibe a la carpeta de spam del correo com asunto: Verify your new account
no-reply@verificationemail.com
The verification code to your new account is 248350

Y envian un verification code
y me lleva a: https://localhost:3000/?code=27a0fe50-09c1-4082-985b-5900ecc28c12

Se confirma la cuenta y ya ha creado el usuario.

    This site can’t provide a secure connection
    localhost sent an invalid response.
    ERR_SSL_PROTOCOL_ERROR


Este error es muy comun por que no se tiene ninguna aplicacion puesta en localhost:3000

?code=27a0fe50-09c1-4082-985b-5900ecc28c12 Este codigo es el codigo de mi usuario de la aplicacion.

Que es lo que nos estaba pasando automaticamente cuando ibamos a la aplicacion?
Como todavia el token estaba vigente, nos mostraba simplemente el ID del usuario, el nombre del usuario.

Como se soluciona, como hago yo para obtener el token?

Beuno, tenemos que venir a editar el valor de out aqui, ene ste lugar donde dice tipos, 




- Editar páginas de inicio de sesión administradas

Aca donde dice: Tipos de concesión de OAuth 2.0

Nosotros teniamos configurado la concesión de código de autorización.

Vamos a tener que seleccionar concesión implicita : POr que de esta manera se esta indicando que yo necesito obtener un token de acceso. Sino, no me lo permite por el resutlado.

Vamos a la aplicacion, y ahora me va a aparecer el token:

    https://summer-app-dev-unique.auth.us-east-1.amazoncognito.com/login?client_id=2lorekrb6p8a0cue50im377msk&response_type=token&scope=email+openid&redirect_uri=https%3A%2F%2Flocalhost%3A3000


POr que todavia estoy dentro de la hora de token , cuando el token expire hay si me va a pedir nuevamente el usuario y contraseña para loggearme.

en este caso detecta que por la cookie que yo tengo grabada, mi token todavia no está expirado y simplemente me lo está mostrando. Bueno, yo les di una aplicacion paara que los usarios de Windows y deje el codigo necesario para los que no usan windows puedan hacer un  pequeño script.



## Sección 6: Backend - RDS

### 37. Introduccion a AWS RDS

Vamos a tener quecrear una base de datops de mySQL

Lo que importa es **clusters de base de datos.**

- Instancias reservadas: Pago por adelantado

- Instantaneas (Backups o snapshots, son las imagenes de nuestra base de datos)
Vamos a tener que configurar una cantidad de dias de retenciones
Amazon automaticamente aunque no lo queremos va a hacer un snapshot diario minimo a la base de datos para tener una copia de seguridad por si pasa algo.

- Eventos recientes: son los eventos que han ocurrido en la base de datos, si hubo alguna falla, si hubo algun cambio y nosotros tenemos despues suscripciones, eventos que nosotros podemos decirle que ante un evento dispare un mensaje hacia un servicio que es el **SNS**, el Simple Notification System o services que me permite en base a los mensajes que recibe luego en un esquema de topicos y suscriptores, añadirle los sucriptores que yo quiera.
SI yo quiero que ese mensaje me llegue por mail, agregaré un suscription de mail y si quiero que me envie un mensaje via HTTP o a un WebHook por ejemplo.

Yo lo uso habitualmente para enviar mensajes a canales de Slack a nivel de empresa para enterarnos de que hubo eventos, por ejemplo el evento de Fail Over o cuandouna base tiene una falla y me entero inmediatamente cuando se dispara ese evento.

- Luego cada base de acuerdo al motor va a tener un grupo de parametros y un grupo de opciones. 
La diferencia es que las opciones van a instancias yu los parametros van a clusters.

Un cluster puede tener n instancias de base de datos en su interior.

NO se va a profundizar mucho en esto por que para esto hay un curso que es **Amazon orientado a datos**, donde ahi explico detalladamente cada una de estas opciones.

- Grupo de subredes: Es por donde va a estar conectada nuestra base de datos.

- Plataformas compatibles (VPC): tiene que ver con la conectividad hacia la base de datos.


Aurora serverless version 2 y tiene un costo elevado.

**Amazon RDS**

Panel

Bases de datos

Editar de consultas

Información sobre rendimiento

Instantaneas: (Publica)

    privilege-escalation-1760880625
    privilege-escalation-1760880642
    db-employees
    nimbus-assistant-test-vulnerable-db
    wildllama-prod
    wordpressdb
    

Exportaciones en Amazon S3: Si hemos hecho una exportacion de S3 a una snapshoot lo que hace es grabar en formato abierto, me graba una carpeta por cada base por cada tabla,y dentro tenemos la informacion en formato parquet. Es un formato especial para grabar datos en s3, y pueden ser leidos con un lenguaje parecido al SQL. El alojamiento en S3, es el mas aconomico que hay (Datos de uso poco frecuente, data de log, data historica), A su vez existe Glacier, que es alojamiento en frio total, donde ya los datos pasan a alojamiento en cinta. Por eso es tan economico, pero lo que es muy costoso es acceder luego a la información.

Es cuando nosotros por motivos legales, tenemos que alojar y guardar informacion por muchos años, pero que nunca o casi nunca la vamos a acceder, estamos obligados a guardarla, pero no vamos a acceder a esa informacion. (Glacier es el alojamiento mas economico que existe, para vartios teras y teras de datos.)

Copia de Seguridad automatizadas

Instancias reservadas

Proxies


Grupo de subredes

Grupo de parametros

Grupos de opciones

Versiones de Motor personalizadas


Eventos

Suscripciones a eventos


### 38. Creando nuestra base de datos (MySQl)

Crear base de datos

    Aurora (MySQl Compatible) No tiene una free tier
    MySQL (SELECCIONAR ESTE)

No habilitar el multi AZ

Plantillas: capa gratuita

Identificador de instancias: summer

nombre de usuario maestro: root

contraseña maestra: summer

configuracion de la instancia:db.t3.micro o db.t2.micro

SDD de uso general (gp2)

almacenamiento asignado: 20 GiB

Habilitar escalado automaticao de almacenamiento = False

Conectividad 

No se conecte a un recurso informatico EC2 = True

Tipo de red : IPv4

VPC: Default

Grupo de subredes de al base de datos: Default

Acceso publico = True

Nota: Se colocará publica para que pueda ser accedida por fuera de la VPC.
Desde la VPC van a poder acceder a la base de datos.
Inclusive las lambdas van a poder acceder a la base de datos sin tener que pasar por una VPC.
Mas que por la VPC default y por las subredes default.

Grupo de seguridad: Elegir existente (Default)

Zona de disponibilidad:  Sin preferencia

Proxy de RDS : deshabilitado

Entidad de certificacion: (predeterminado)

Autenticacion de bases de datos:

Autenticacion con contraseña = Yes

Configuracion adicional

Opciones de base de datos

Nombre de la base de datos inicial = summer

Grupo de parametros = Default

Grupo de opciones = Default

Copia de seguridad

Habilitar las copias de seguridad automatizadas = True

Periodo de retencion de copia de seguridad: 7 dias 

Periodo de copia de seguridad = Sin preferencia

Copiar las etiquetas  en las instantaneas = True


Replicacion de copias de seguridad

Habilitar la replicacion en otra region de AWS = False

Exportaciones de registros = False

> Nota:Seleccionar los tipos de registros que desee publicar en Amazon CloudWatch Logs
Logs de auditoria
Registro de errores
Log general
Log de consulta lentas


Mantenimiento 

habilitar actualizacion automatica de versiones secundarias = False

Periodo de mantenimiento = sin preferencia

Proteccion contra la eliminacion = False



### 39. Descargando e instalando Heidy SQL
 

https://www.heidisql.com/


### 40. Nos conectamos a la base de datos y mddificamos el security group



### 41. Descargar gambit.sql



### 42. Instalando Gambit.sql

Son los archivos DDL para la base de datos.
ALT + X en DBeaver.


## Sección 7: Backend - Secret Manager

colocar en favoritos

### 43. Introduccion a secret manager


Permite rotar, administrar y recuperar secretos de forma sencilla durante sus ciclos de vida.

Por que habla de rotar? por que los secretos que nosotros grabemos, esas passwords. Hay una funcionalidad que podemos decirle a Amazon de que esa password la vaya regenerando a un periodo determinado. Si nuestra aplicacion se conecta a secrets para recuperar la password, es una combinacion perfecta, si alguien tiene que administrar la base de datos en forma manual, irá a seguir secret manager capturara el valor actual de la password de root y se conectara con Heidy SQL a la base.

$ 0.40 por secreto al mes
$ 0.05 por 10000 llamadas a la API

Cuando se crea un secreto, la forma de acceder a ese secreto es pegarle a una API interna que tiene pasandole los parametros y nos devuelve el secreto. Lo hacer de manera muy rapida, es realmente rapidisimo, no le genera un delay a la aplicacion.

Es fundamental esto por que si aqui hubiera un delay enj aplicacion de alto rendmiento seria un cuello de botella.



### 44. Creación de un secreto que tenga las credenciales de la base.


- Amazon RDS
- Document DB: Similar a MongoDB.
- RedShift
- Credenciales para otra base de datos
- Otro tipo de secreto

Funcion de rotacion de lambda

Desarrollar la lambda 1que va a terminar trabajando con cognito como triger 
y que va a grabar el registro de usuario en la base de datos.




## Sección 8: Backend - Lambda con Go para manejo de usuarios


### 45. Introducción a Lambdas y caracteristicas para el desarrollo en Go.


Las lambdas son en definitiva codigo o funciones que podemos ejecutar.

AWS Lambda
Ejecute código sin administrar servidores.


Funciones que se corren sin servidor, Lo que nos permite amazon es desarrollar y no preocuparnos por que hardware corre debajo, y ese es el servicio de lambdas.
Podemos hacer aplicaciones, APis REST, muchas cosas desde lambda sin estar preocupados por que servidor, cuanta memoria, que velocidad de red, como vamos a hacer para manejar la concurrencia, todo eso lo maneja lambda sin ningun tipo de problema.

Nos permite desarrollar en distintos lenguajes, podemos crear desde 0 o utilizar un proyecto que ya tiene de muestra amazon de distintos tipos de desarrollo,  en distintos tipos deLenguaje, o usar una imagen del contenedor de lo que tiene que ver con Dokcer y Kubernetes.


**La nueva estrategia de AWS (Segunda y tercera imagen): Al darse cuenta de esto, AWS decidió que no tenía sentido mantener un entorno exclusivo llamado "Go". En su lugar, introdujeron los entornos "Amazon Linux" (Custom Runtimes). Estos entornos son sistemas operativos limpios diseñados para ejecutar cualquier binario nativo que tú subas (ya sea programado en Go, Rust, C++, etc.).**


Amazon Linux 2023 (o en su defecto Amazon Linux 2, aunque la 2023 es la más reciente y recomendada).

Nota: Internamente, AWS identifica a este entorno con el identificador provided.al2023.

Arquitectura: Puedes seleccionar x86_64 o arm64 (esta última aprovecha los procesadores Graviton de AWS, que son más económicos y rápidos para Go).


Una de las cosas que se deben saber es que Go es uno de los pocos lenguajes que maneja lambda de modo compilada, que significa que nosotros vamos a tener que compilar nuestra solucion dentro del exe va a estar todo lo necesario, todas las dependencias que vamos a necesitar para que corran, por que imageinese que nosotros utilizamos paquetes que si no tenemos forma de decirle a la lambda que ese codigo queestamos implementando utiliza un paquete externo como el SDK de Amazon u otros paquetes externos como el manejo de base de datos, no va a saber que hacer Amazon, entonces Go es compilado, mientras que Python, node.js y otros lenguajes son interpretados. 

Significa que vamos en esos lenguajes se sube el codigo asi crudo como esta, y luego hay otra parte de las lambdas que son las capas.

Las capas es loq ue se usa por ejemplo en python para subir las librerias de dependencias, 
No va a ser nuestro caso, no nos vamos a tener que preocupar por las capas por que repito, Go va a ser un lenguaje cmpilado, internamente en su exe va a tener todo lo necesario para funcionar. 

Arquitectura x_86_64 

Permisos

Rol de ejecucion

Tenemos la posibilidad de crear roles, por que la lambda tiene que ejecutar, tiene que funcionar, con un rol determinado, o tenemos un rol creado y lo asignamos o permitimos que la lambda cree un rol.



Configuracion avanzada

En caso de tener una base privada

- Habilitar la firma de codigo
- Habilitar URL de la funcion
- Habilitar etiquetas
- Habilitar VPC

En caso de tner una base privada, no publica, puedo decirle que se va a conectar a traves de la VPC.( se habilitara y se usara la VPC DEfault para conectarme a la bvase de datos, 


Son las 6 sub redes para conectarme a mi base de datos, 

Seleccionar security group por default.

Avanzar con el registro de usuarios.


### 46. Creación de Lambda y modificacion del rol IAM

Crear la funcion lambda que vamos a usar como Trigger de cognito cuando un usuario confirma su mail.
Esa lambda va a recibir esos datos y los va a registrar en la base de datos como un insert en la tabla de un usuario nuevo.

Vamos a hacer click en crear una funcion, se va a llamar SummerUser se le v a indicar que es de tipo Go, es decir Amazon Linux 2.


Arquitectura x_86_64 


Rol de ejecucion: creacion de un nuevo rol con permisos basicos de lambda.

Luego lo vamos a modificar vamos a ver como modificarlo.

Y la configuracion avanzada se deja como esta.

habilitar firma de codigo = No
Habilitar URL de la funcion = No
Habilitar etiquetas = No
Habilitar VPC = No

Por que no hace falta crear una VPC para coenctarse a la base de datos.
Vamos a crear la funcion y aqui se esta creando y cuando aparece en verde ya tenemos nuestra lambda.

Por ahora no tiene nada, no se tiene ni siquiera un codigo para subirle.

Controlador: La funcion de entrada de nuestro desarrollo.  (main)

Recordar que la funcion de entrada de cualquier aplicacion de Go es main 


Luego no hay que añadirle capas, 


Ahora en la aprted e configuracion. 


Monitorear: Las metricas de CLoudWatch

Editar la configuracion básica: 

Memoria: 128 MB

Almacenamiento efimero: 512 MB

Igualmente hay toda una capa gratuita que no la vamos a llegar a consumir.

Tiempo de espera = 15 mins

Uso de rol existente: ej: service-role/summerUser-role-qt60vmww  (se va a modificar en unos minutos)


**Desencadenador, mas adelante cuando ya se tenga la lambda desarrollada** 

Se tiene un permiso de Amazon CloudWatch Logs

Destino : No hay destino, eso es si tenemos una cadena de lambdas, se tiene una lambda que termina y le pasa a la otra lambda.


URL de funcion: se va a usar cuando se tenga la lambnda principal. Esto vendria ser como disponibilizarla publicamente la API Gateway.

Por supuesto todas las modificaciones se van a hacer desde la opcion de API Gateway.

Variables de entorno es muy importante por que si mi lambda va a recibir variables de entorno con valores.

"el nombre del secret donde tiene que leer las credenciales de la base de datos"

Una es dinamica a traves de un json que puede ser variable
y otra son las variables de entorno, no son dinamicas una vez que esten configuradas con su valor.

A no ser que uno vuelva a modificar el valor, esta variable queda como una constante, aunque diga que es variable.

SI yo quiero una lambda reciba parametros y que en base a esos parametros funcione de manera diferente cada vez, lo voy a tener que hacer como port json.

Nuestras lambdas pueden o no tener esos parametros variables.

de ehcho esta lambda que se va a desarrollar primero no tiene parametros json, sino que tiene variables de entorno


- Etiquetas: si queremos etiquetar nuestro recurso. para que se usan? un desarrollo X, que tiene un nombre, que implica varios recursos a todos se le coloca la misma etiqueta para identificar todos los recursos que se llevo ese desarrolloo, es util para eso y para muchas cosas mas. 

- VPC no tenemos ninguna VPC configurada por que nuestra base es publica y la puedo acceder desde cualquier 
lado sin necesidad de una VPC.

- Herramientas de monitoreo y operaciones: me dice lo que tenemos, los registros y metricas que estan habilitados en Cloud Watch.

- Concurrencia: (Realmente no lo usa)
Simultaneidad de cuenta no reservada = 1000
1000 personas accediendo al mismo momento a la lambda.


- Invocacion asincrona (reintentos)
Antiguedad maxima del eventos (Cuando pasaron 6 horas, ese evento ya no tiene reintentos)

Si uno quiere que una lambda corra en determinado horario, y sabiendo que a la hora ya no nos sirve. Se puede ajustar la antiguedad maxima del evento, para que no haga mas reintentos por que quizas a la hora viene otra pegada a esa misma lambda desde otroservicio. 

- Forma de codigo: No lo vamos a usar.

- Proxy de base de datos (No tenemos ningun proxy creado) Tenemos nuestro motor de MySQL sin proxys.

- Sistema de archivos: Por si nosotros queremos agregar a nuestra Lambda un sistema de archivo, por que 
nuestra lambda tiene que grabar en disco algo, o leer de disco, Aqui podemos agregar a un sistema de archivo para conectar a nuestra lambda una VP determinada, Recuerden que es un serverless, no tenemos control ni acceeso a nada de lo que ocurre en el hardware, 

¿Entonces que pasa cuando nuestra lambda tiene que grabar un archivo?
tenemos la posibilidad de agregar un sistema de archivos, nosotros no lo vamos a usar para nada en este desarrollo.

- Maquinas de estado: Nos permite crear step function que es un poco lo que le decia antes,  Una lambda que si fallo se llama otra, pero si el resultado anduvo bien, puede llamar otra diferente.
Crear como una logica de ejecucion y maquinas de estado. No lo vamos a utilizar.


Que vamos a utilizar
Configuracion general.
Permisos
URL de funcion
Variables de entorno

Ir a permisos vemos que esta nuestro rol, hacemos click y vamos al panel de IAM, abre nuestro rol, nos dice que tiene una politica asociada, y esa politica es lo que tiene de b asico de ejecucion las lambdas, 
Que es ni mas ni menos lo que vimos, la posibilidad de crear logs streams dentro de Cloud Watch y ahi poder grabar todo lo que tenemos que haacer.

**Pero aqui vamos a tener que añadirle un permiso mas** Se hace click en añadir permiso, > Asociar politicas

Y buscar el servicio de Secret Manager, 

Si nosotros no le decimos a nuestro rol, que tiene permisos para leer Secret Manager, cuando desde nuestra lambda, quiera ir al servicio de Ssecret Manager, obtener el script va a dar un error de permiso,, la lambda no va a funcionar.  

Entonces aqui, ademas del rol basico de lambda, vamos a tener que buscar la palabra secret, le damos secret y aqui tenemos el servicio de SEcret Manager, lo tildamos agregamos los permisos y aqui vamos que ya  tenemos los permisos de secret manager, cuales? todos los permisos habidos y por haber.

**Rol de ejecucion**

Y aqui en rol de ejecucion por recursos,  y aca cuando venimos y buscamos secret manager, vemos que tenem,os alojados el acceso a todos los recursos de secret manager, 



### 47. Creación del proyecto en Github y clonación en PC Local

Lambda de registro de usuarios

Github


/gambituser

/gambit va a ser el segundo repositorio y va a tner toda la APi de todo el backend.

Recordar que son 2 lambdas que se van a desarrollar. La mas pequeña es la oprimera que tendra que ver con el registro de usuarios.

Aca no hay endpoints, ni resouesta HTTP ni nada sino que va a ser una reswpuesta HHTTP full, entre el cognito y la lambda, 



### 48. Iniciando el desarrollo en GO


En que se diferencia el desarrollo de una lambda de amazon y eld esarrollo normal de Go?

Aca en el main no puedo colocar el codigo, sino que desde aqui tengo que indicarle la llamada a una funcion que es la que va a tener todo el procesamiento.

    go get github.con/aws/aws-lambda-go/lambda

tenemops una lambda como disparardor como trigger de cognito.

La estructura basica de cualquier basica en Go que se desarrolle es esta:

se tiene que importar el paquete de lambdas, 


import (
	lambda "github.com/aws/aws-lambda-go/lambda"
)

La funcion main va a llamar a otra funcion que ejecuta la lambda.

yu aca sse van a recibir los parametros propios de la ña,ndas, por que estass


Imaghinese que nosotros tenemos esta lambda como disparador, como trogger de cognito, 

Cuando un usuario registrdo confirma su mail en cognito, va a disparar el llamado a esta lambda, y le va a pasar parametros obviamente o sino no nos sirve de nada. 
que parametros? el registro del usuario.
Cuando tengamos los datos del usuario, 

el userid que le crea cognito, que es un userid bastante textenso, no es sinmplente un numero,

Vamos a poder registrar con su mail, y con su nombre todos los datos dentro de nuestyra base de datos, 



Otra cosa que si vamos a tener que importar, si estsmoa hablando de evento.
Estamos hablando de que esto va a ser el trigger de cognito, vamos a tener que exportar un paquete mas que es el paquete de eventos. Sino no va a tener las funciones y propiedades necesarias.


Vamos a estar jugando con los eventos de amazon.

github.com/aws/aws-lambda-go/events"


**EjecutoLambda** va a recibir el evento:

Va a recibir la informacion del evento, y dentro vamos a procesar todo ese evento.


Es el contexto,  es algo medio complejo de comprender para los que nunca usaron contextos, pero en lo que es muli ejecucion,  lo que es multihilos, lo que es una ejecucion encadenada de varias funciones, 

Los contextos nos permiten un ambito de dialogo,  com para poder manejar variables, manejar consignas, timeouts y mucha informacion,  que va a ordernar, es como un director de orquesta 

Nosotros lo vamosoa utilizar simplemente para mendionarlo como parametro,  por que es obligtorio  de las lambdas pero internamente,  no vamos a trabajar con contextos,  

Asio que no se preocupen simplemente copien como se va a escribir ahora,  

Lo definimos como parametro,  es obligatorio, pero internamente lo vamos a usar solo para el inicio de sesion. Como parametro tambien, recibe ese contexto y se lo pasa solo como inicio de sesion, a Amazon por que vamos a tener que iniciar sesion, hay todo un tema de autenticacion, cuando nuestra lambda quiere comenzar a trabajar, y el segundo parametro que vamos a definir es el event, que va a pertenecer a avents, y aca vamos a tener todos los tipos de eventos, por que? por que en Amazon tenemos muchisimos servicios, 

Yo estoy recibiendo un evento perod e que servicio?

Hay un evento por cada cosa que ocurra con mi userPool, y aqui tenemos el eventos.

    event events.CognitoEventUserPoolsPostConfirmation) 

Si yo quiero que mi usergroup no requiera confirmacion y con el mero hecho de registrarse, con el login sin  confitmacion, dispare una lambda voy a usar otro tipo de evento. 

Aca se esta utilizando CognitoEventUserPool post confirmation, cuando el usuario confirmo .DDD

Esta funcion como es una funcion lambda le debe devolver a Amazon algo, elr esultado de como anduvo todo, si hubo un error o no.

Entonces se va a devolver 2 objetos, uno va a ser de tipo events, hay que deolver exactamente lo mismo , lo mismo

Obviamente va a tener valores, va a ser el mismo objeto pero va a tener valores,

    func EjecutoLambda(ctx context.Context, event events.CognitoEventUserPoolsPostConfirmation) (events.CognitoEventUserPoolsPostConfirmation, error) {

    }

Fundamental para las lambdas, permite grabar el CloudWatch el error, y vamos a poder hacer cosas.


Imaginese que esto fuera parte de una maquina de estados, una step functions. Donde una lambda cuando devuelve error debe ejecutar otra, osea es parte de una maquina de estados.


Paquete de aws go para inicio de sesion y demas.





### 49. Desarrollo de paquete AWSGO

Se va a crear el primer paqeute que tiene que ver con Amazon y se llamara AWS Go.


    go get -u github.com/aws/aws-sdk-go-v2/aws

    go get -u github.com/aws/aws-sdk-go-v2/config 

Tiene que ver con toda la configuracion de inicio de sesion y demas.

	Ctx = context.TODO() 

Es un contexto vacio, 

Cuando nosotrod queramso recibir la configuracion d3efaultr que tiene Amazone en nuestra cuenta.

Trae todas las confoguiraciones que tyiene Amazon dentro de nuestra cuenta y con esto vamos a trabajr dentro de nuestra lambda.

    var Cfg aws.Config

Es una estructura que tiene todo lo necesario para manejar las configuraciones de inicio de sesion.

Se va a crear una funcion exportable que se va a llamar InicializoAWS


	Ctx = context.TODO()

Retorna un no nulo es un entorno vacio. (empty context)
Aca no hay limitacion en el contexto. Se podria decir que el timeout es de 1 minuto.
Mientras se este ejecutando todo, al minuto se termina el contexto, anula las ejecuciones yu asi como hemos terminado, abandona la lambda, 

Lee el SDK default external configuration.
Lee toda la configuracion externa de lo que se tiene en la cuenta de amazon creada.


Aca esta awsgo.go


    package awsgo

    import (
        "context"

        "github.com/aws/aws-sdk-go-v2/aws"
        "github.com/aws/aws-sdk-go-v2/config"
    )

    // github.com/aws/aws-sdk-go-v2/config
    // github.com/aws/aws-sdk-go-v2/aws

    var Ctx context.Context
    var Cfg aws.Config
    var err error

    func InicializoAWS() {
        Ctx = context.TODO()
        Cfg, err = config.LoadDefaultConfig(Ctx, config.WithDefaultRegion("us-east-1"))

        if err != nil {
            panic("Error al cargar la configurations .aws/config " + err.Error())
        }

    }




Este es el programa main.go

    package main

    import (
        "context"
        "summeruser/awsgo"

        lambda "github.com/aws/aws-lambda-go/lambda"
        // go get github.com/aws/aws-lambda-go/events
        "github.com/aws/aws-lambda-go/events"
        //summeruser/awsgo
    )

    func main() {

        lambda.Start(EjecutoLambda)

    }

    func EjecutoLambda(ctx context.Context, event events.CognitoEventUserPoolsPostConfirmation) (events.CognitoEventUserPoolsPostConfirmation, error) {
        awsgo.InicializoAWS()
    }


Se va a ir agregaod paquete funcionalidad, hasta que la lambda este terminada.




### 50. Desarrollo de paquete Models

Vamos a continuar con el segundo paquete, va a ser models.

La secret Manager se apoya en estructuras, esa estryuctura se va a tener metida en models.

Se crea el archivo /models/models.go

Se van a hacer definiciones de estructuras.


Se va a definir la primera estructura que es la que se utiliza cuando secret manager se conecta a RDS y lee el secreto no solamente nos devuelve la clave del usuario principal, 
puede ser root, admin o lo que sea, sino que nos devuelve 6 valores.


	Username            string `json:"username"`
	Password            string `json:"password"`
	Engine              string `json:"engine"`
	Host                string `json:"host"`
	Port                int    `json:"port"`
	DbClusterIdentifier string `json:"dbCLusterIdentifier"`
}



Ahora una nueva estructtura que tiene que ver con el registro de usuarios.

CUando se haga la conexion a secret manager a la base, depende del evento de cognito, vamos a recibir parametros, dentro de los parametros que vamos a recibir que son muchos nos interesan 2 datos nada mas: el user email y el user id.

Que seria el id de usuario que vamos a grabar en la base de datos, se va a crear un nuevo struct llamado signup , por que va a contener los datos del registro. 


type SignUp struct {
	UserEmail string `json:"UserEmail"`
	UserUUID  string `json:"UserUUID"`
}


Recordar que la lambda tiene variables de entorno. Por ende se utiliza el paquete os.

No es buena practica llenar de codigo la funcion principal si no que se va a hacer en una funcion aparte.

Vamos a ver en la segunda lambda, la del ecommerce, esto es fundamental, por que en un e commerse se reciben muchas variables de entorno no solo una.
Ahora se va a crear una funcion que se va a llamar ValidoParametros() no recibe nada pero devuelve un boolean.


### 51. Desarrollo de paquete Secret Manager

Los secretos para la lambda estan en Secret Manager.

    go get -u github.com/aws/aws-sdk-go-v2/service/secretsmanager

Se crea la funcion GetSecret() en secretmanager.go

POr que no se le puede madnar el secret directo?

Por que es un tipo especial,no es un string normal. es un puntero de string.
Entonces se tiene que usar una funcion del paquete de amazon, recibe un string y me devuelve un puntero de string.


### 52. Desarrollo de paquete Tools & Completamos BD


Vamos a crear un paquete nuevo que se va a llamar tools. y va a tener una funcion que va a ser usada por el paquete de base de datos y se hace por una buena practica. POr que cuando se van a hacer funciones que no tienen nada que ver con ningun paquete, ni con secretmanager ni con awsgo, ni m,odels, va a ser uasada por base de datos pero no es base de datos en si misma , se hara en un paquete aparte. Va a ayudar a ordenar el codigo de mejor manera.


go get -u github.com/go-sql-driver/mysql



Secret manager me devuelve una estructura con 6 valores.

Una funcion que los agrupe en e l formato del connection string.

Conexion basica de la base de datos.



### 53. Compilamos nuestra Lambda y la subimos a AWS

Llego el turno de compilar la solucion para poder llevarla a Amazon.
El problema es que amazon solo acepta ejecutables de Go en formato Linux.
No Windows, no mac. Se debe compilar la solucion con unas instrucciones para que el ejecutable sea compatible con Linux.

EN windows se crea un .bat

**subo.bat**

git add .
git commit -m "ultimo commit"
git push

set GOOS=linux
set GOARCH=amd64
go build main.go
del main.zip
tar.exe -a -cf main.zip main


Amazon pide que las lambdas se suban zipeadas.


En linux se crea un .sh


    GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -tags lambda.norpc -o bootstrap main.go

    zip function.zip bootstrap


Para los archivos mayores de 10 MB, considere la posibilidad de cargarlos usando Amazon S3.

Funciono bien, se desplego el secret con terraform.
Y se subio la lambda desde un zip.



**Despliegue**


Existen tres formas principales de empaquetar y desplegar una Lambda en Go:

1. Archivo ZIP (Lo que estás haciendo actualmente):

Compilas el binario con GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -tags lambda.norpc -o bootstrap main.go y empaquetas la raíz en function.zip.

Ventaja: Muy liviano, arranque en frío (cold start) ultra rápido y simple de integrar en Terraform con source_code_hash.

2. Imagen de Contenedor (Docker/ECR):

Empaquetas tu ejecutable en una imagen Docker ligera (ej. basada en alpine o scratch) y la subes a Amazon ECR.

Ventaja: Ideal si el binario o las dependencias sobrepasan los límites de un ZIP, o si estandarizas todo el deployment de tu compañía con imágenes OCI/Docker.

3. Frameworks de Despliegue (Serverless Framework / AWS SAM):

Automatizan la compilación del paquete Go y la creación de la infraestructura subyacente mediante comandos de CLI como sam deploy o sls deploy.

Para tu caso actual con Terraform, la estrategia de ZIP sigue siendo la mejor opción y la más eficiente.





### 54. Configurar Trigger de Cognito como disparador de la Lambda

Configurar la variable de entorno en la lambda:
SecretName = gambit

Esta en AWS Secret Manager

Agregar desencadenador (trigger)

Se necesita Cognito y RDS.



Cognito > Grupo de Usuarios

En cognito en propiedades del grupo de usuarios se debe 

Agregar el desencadenador o trigger para la lambda.

Aue es lo que va a pasar cuando ocurra cualquiera de estas 4 cosas.

- Registro
- Autenticacion
- Autenticacion personalizada
- Mensajeria

Se va a usar **Registro**

Por que la autenticacion seria disparar trigge4r cuando el usuario se loggea. Puede ser muy util para otro tipo de lambda y otro tipo de funcionalidad.
En este caso lo unico que queremos hacer es registrar el usuario, 

Una vez que se tiene registro se va a tner que elegir, En que eventos?

- Desencadenador de antes del registro
**- Desencadenador de despues de la confirmacion**
- Desencadenador de migrar usuario

Funcion Lambda:

Asignar una función lambda.
summer

Finalmente se da click en **Agregar desencadenador de Lambda**


Y una vez que se tiene el desencadenador de lambda configurado, se va a tener que crear un pool de identidades. Lo que aqui se llama identidader federadas.

Se habia mencionado que no se iba a usar por que no se iba a realizar una autenticacion con facebook o google, etc.
Pero tenemos que crear una identidad federada de gambit para que pueda interactuar y enviar informacion a la lambda

Se entra a identidades federadas, se crea uno nuevo para summer,


3: 34 pendiente





5: 20
 
En desencadenadores, se agrega uno y se le indica que es de tipo:

**Cognito Sync trigger**

y Luego se eligen cuales son las identidades, se elige la creada anteriormente ...

Se le da click en agregar

**Ahora ya aparece el desencadenador en la lambda**


### 55. Probamos la solución completa


Se accede a la interfaz de sign up desde 

Entrando al grupo de usuarios (user pool)  Applications > App clients

Si se quiere utilziar siempre el mismo mail sin que diga que ya existe, con agregarle un signop + y un numero.

**tilottapablo+27@gmail.com**

Se puede utilizar todas las veces que quieran 

Se va a enviar un verification code.



Me aparece este error:

    This site can’t be reached
    localhost refused to connect.
    Try:

    Checking the connection
    Checking the proxy and the firewall
    ERR_CONNECTION_REFUSED

https://localhost:3000/?code=af879e57-f766-45ab-b26d-d57f8b150238


cómo funciona Cognito como Identity Provider.


Ahora bien si me aparece el usuario registrado, y me pude autenticar.
Nunca aparecio el trigger (Cognito Sync Trigger)

Lo asigna Cognito automáticamente, no tu código ni tu base de datos. Cada vez que se crea un usuario en un User Pool, Cognito le genera un atributo estándar llamado sub (subject) — es un UUID único e inmutable que identifica a ese usuario para siempre dentro del pool, siguiendo el estándar OpenID Connect (donde sub es el claim obligatorio que identifica al sujeto del token).


mysql> select * from users;
+--------------------------------------+------------------------+----------------+---------------+-------------+---------------------+--------------+
| User_UUID                            | User_Email             | User_FirstName | User_LastName | User_Status | User_DateAdd        | User_DateUpg |
+--------------------------------------+------------------------+----------------+---------------+-------------+---------------------+--------------+
| b438a4b8-b0b1-700b-ae07-b34e35eed4d1 | dposadallano@gmail.com | NULL           | NULL          |           1 | 2026-07-29 22:18:14 | NULL         |
+--------------------------------------+------------------------+----------------+---------------+-------------+---------------------+--------------+
1 row in set (0,09 sec)



**En cognito**

User name
	
Email address
	
Email verified
	
Confirmation status
	
Status

**b438a4b8-b0b1-700b-ae07-b34e35eed4d1**
dposadallano@gmail.com
Yes
Confirmed
Enabled


Esto confirma que me pude resigtrar con cognito, valide mi mail, esto disparo por trigger la lambda, todo eld esarrollo implementado y finalmente se han guardado en la base de datos.

User_status = 1 = User
User_status = 0 = Admin


cada verz que tenga que hacer una operacion, voy a tener que loggearme como admin, cuando queira crear categorias, borrar usuarios. O modificar datos de productos. Crear productos, todo esto son atributos del admin.


Esto lo vamos a ver cuando desarrollemos el e-commerce.

Ya terminamos la primer lambda, 



Una lambda son muchos archivos, una lambda es un servidor.


No se como empaquetaban eso en Bold en un monorepo, "magia de Devops".
Repo de infra + repo de lambdas.

Economizar dinero en infra de nube. un api gateway para todos solo agregar una ruta.




## Sección 9: API Gateway directo a s3 para alojar imagenes


### 56. Creando nuestro Bucket s3

Aprender a crear un API Gateway directo a S3.


Crear un bucket s3 que va a alojar nuestras imagenes. Luego se va a crear un API Gateway, que es el servicio que me permite disponibilizar una API publica, y la vamos a configurar de manera que cuando llegue una aplicacion de tipo PUT hacia la ruta que vamos a definir.

El contenido de esta pweticion que va a ser un archivo *.jpg, o *.png, lo almacene en nuestro bucket S3 sin codigo, sin lambdas, sin nada. Hay una forma hay unos pasos, no es tan simple, pero siguiendo los pasos se logra, para configurar un API Gateway inclusive con autenticacion de Cognito.

Osea nuestro endpoint va a recibir un token, y lo va a validar para que desde afuera cualquiera no pueda pegarle.
Va a validar que sea un token valido, que no este expirado, que sea de mi grupo de usuarios de gambit, una vez que valida esto el archivo que reciba por la peticion PUT, luego vamos a ver como configurar postman para lograrlo,  ese archivo lo va a alojar en el bucket s3.

Obviamente cuando ustedes vean la parte del frontend, se va a hacer sin postman, va a enviar el avatar del usuario o la imagen del producto, las van a enviar hasta estas URLs.

Simple Storage Service (s3)

Crean un bucket desde la consola web.


Todos los objetos de este bucket son propiedad de esta cuenta, el acceso a este bucket y sus objetos se especifica a traves de politicas. 

Bloquear todo el acceso publico (Viene apagado por default) se remueve el check. por que no quiero bloquear nada, 
por que?
Mi front tiene que acceder al bucket para acceder a las imagenes. Si nosotros lo bloqueamos no va a poder acceder a las imagenes.

- Reconozco que la configuracion actual puede provocar  que este bucket y los objetos que contiene se vuelvan publicos.
**Se debe confirmar por que es un tema de seguridad**


Control de versiones del bucket, se va a dejar desactivado.


Si se desean se pueden colocar etiquetas, pero no es necesario.

Cifrado predeterminado (dejamos todo como esta)

Tipo de Clave de cifrado
- Claves administradas por Amazon S3 (SSE-S3)

Claves de Bucket
Habilitar


Configuiracion avanzada

BLoqueo de objetos
Desactivar


El nombre del bucket debe ser un nombre unico para toda la region.

summer-images**


### 57. Creando el Rol de IAM necesario con todos los permisos.

Solucion para ir directamente a un S3 a traves de un API GAteway,  vamos a ver la confiuracion del rol de IAM que vamos a necesitar.

No se va a obtener el metodo GET para obtener las imagenes.  No hace falta, vamos a ir desde front directamente a la URL a obtener las imagenes, como nuestro Bucket es publico,  las imagenes se van a poder mostrar sin problemas. 
|
Tenemos que crear un rol para que soporte todo el trabajo de API Gateway, 

Ademas luego se le va a dar un permiso para que pueda acceder a cognito.

Vamos a IAM, al menu de riles y se va a crear un nuevo rol.

Es un rol del servicio de Amazon, 

**Nota: No elegir s3, elegir directamente el servicio API GATEWAY.**

Para que me permite 


Una vez que estamos dentro, vamos a hacer click en añadir permisos 
Por ahora solo tiene permiso para cloudwatch.

En añadir poermisos se selecciona, crear politica insertada.
 
Y aca lo que vamos a hacer es ir eligiendo los servicios , y se selecciona el servicio de s3.

Una vez que se hace click en s3 se pueden filtrar las acciones, se escoge el putObject 

Se elige este Permiso exclusivamente, por que sino vamos a crear una policy enorme, por todos los permisos que tiene s3.

y vamos a elegitr el servicio de s3 la accion de GetObject.

Object  Cualquier Recurso de tipo = Object   [Cualquiera] 



Cualquier recurso va a poder acceder con esta politica a leer y a grabar objetos dentro del object

Se crea la politica con el nombre de summer_s3

E inmediatamente  le adiciona ese nombre de politica que es s3.


Ahora vamos a hacer lo propio pero con cognito. por que tiene una autenticacion con Cognito y se lo tenemos que añadir. 

Lo mismo, añadir permisos, crear politica insertada , se elige el servicio que es cognito identity,  

y se selecciona lo siguiente: 

(Acciones manuales)

hablitar el checkbox en : Todas las acciones de Cognito identity (cognito-identity:*)

- Enumeracion
- lectura
- Etiquetado
- Escritura

y se habilita el check en (Cualquiera de esta cuenta) "puede usar esto"

**Sirve para cualquiera de los grupos de usuario que tengo en cognito**

Se crea la politica bajo el nombre de summerCognito

Si nosotros queremos hilar mas fino, y colocarle diurectamente rl eecurso. y que solamente estas API gateway pueda grabar en el bucket que han creado se puede editar en "resource" y remover los asteristcosy colocar el bucketr especifico.


{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::*/*"
    },
    {
      "Sid": "VisualEditor1",
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::*/*"
    }
  ]
}


{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": [
        "cognito-identity:GetId",
        "cognito-identity:SetPrincipalTagAttributeMap",
        "cognito-identity:SetIdentityPoolRoles",
        "cognito-identity:ListIdentityPools",
        "cognito-identity:CreateIdentityPool",
        "cognito-identity:UnlinkIdentity",
        "cognito-identity:DeleteIdentities",
        "cognito-identity:GetOpenIdToken",
        "cognito-identity:DescribeIdentity",
        "cognito-identity:GetCredentialsForIdentity"
      ],
      "Resource": "*"
    },
    {
      "Sid": "VisualEditor1",
      "Effect": "Allow",
      "Action": "cognito-identity:*",
      "Resource": "arn:aws:cognito-identity".*:132694511939:identitypool/*"
    }
  ]
}


Ahora a configurar del lado del API Gateway donde vamos añadir este rol para que tenga todos los permisos.


### 58. Link de instrucciones detalladas de AWS 

Link de Instrucciones detalladas de AWS

El link siguiente contiene todas las instrucciones Paso a Paso para configurar una API GATEWAY para que envíe objetos a un bucket S3

    https://repost.aws/knowledge-center/api-gateway-upload-image-s3


### 59. Creando API Gateway de tipo REST

Ahora vamos a crear nuestor API Gateway, ya tenemos el rol.

Se crea una API.
Dentro de todas las posibilidades que me da se va a escoger una API REST.

>Para la ultima parte del backend se va a crear una API HTTP. Pero lo hacemos directamente desde la lambda, y luego la vamos a ir configurando. 

Esta API nueva se va a llamar SummerS3
Va a ser de tipo REST y va a ser una API Nueva.

Ahora se pueden ir configurando los metodos, los endpoints, vendrian a ser las rutas. Lo primero que se va a hacer es a la direccion / de nuestra API.
se le va a crear un recurso. Se va a llamar {folder}

El folder va a ser el nombre del bucket y luego viene el {object} que va a ser en si mismo el archivo que vamos a ir subiendo.
Se habilita API Gateway CORS (Enabled) y se crea el recurso.

Dentro de folders, se va a crear otro recurso por debajo de {folder} y este va a ser el {object} y se va a llamar object tambien. Se deben colocar las llaves por que enr ealidad son tags.
Se habilita API Gateway CORS (Enabled) y se crea el recurso.

Una vez que se tienen creados estos 2 recursos, lo que se va ahacer debajo de Object se va a crear un metodo, que seria PUT. POr que ya el bucket existe.

La configuracion de ese PUT va a ser:
Tipo de integracion: Servicio de AWS

Region: us-east-1

Servicio de AWS: Simple Storage Service (S3)

Subdominio de AWS: (Vacio)

Metodo HTTP: PUT

Tipo de acción: usar sustitución de ruta

Por que como estamos usando tags, que es {folder} y {object}. Lo que va a hacer es una sustitucion,  

Por ejemplos se va a enviar un nombre de folder que es el que se tiene creado en el bucket S3. EN object vamos a enviar un archivo, por ejemplo cualquiercosa.jpg, y en el nombre de usuario va a ir todo el nombre de usuario.jpg 

Sustitución de ruta (opcional): {bucket}/{key}

Rol de ejecucion: [Se coloca el ARN del rol de ejecucion]

Tratamiento de contenido: Paso a través

usar tiempo de espera predeterminado: Enabled

Y ya arma todo el esquema.


Ahora entran a autorizadores, se va a llamar Cognito.

Tipo: Cognito

Grupo de Usuarios: [El que se creo en los templates de terraform]

Origen del token: Authorization

POr que va a venir en el header, 

Validacion de token: (Se deja vacio)

Y listo ya se tiene el autorizador.

Para solicitud de metodo. de /{folder}/{object} - PUT - Ejecucion de metodo
En autorizacion se elige: Cognito

Validador de solicitudes: Ninguno

Clave de API obligatoria false

Una vez que se confirma solicita el ambito de OAuth.

Ambitos de OAuth: openid

Si se deja en ninguno no va a funcionar.


Ahora se clickea en solicitud de integracion.

En parametros de ruta se va a tener que modificar:
Se van a agregar las rutas que son necesarias.

Nombre: bucket
Mapeado de: method.request.path.folder

Se va a agregar la segunda rutra que es la key:

Nombre: key
Mapeado de: method.request.path.object

Ya se tienen las dos rutas agregadas que es lo que nos interesa.
POr que tiene que ir mapeando y tiene que ir descifrando.
Recordar que aca no hay una lambda debajo, entonces todo es por configuracion,
por eso es tan complejo.

Una vez que ya tenemos la solicutud de integracion.



### 60. Reglas de Politica al Bucket

    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": "*",
                "Action": [
                    "s3:GetObject",
                    "s3:ListBucket"
                ],
                "Resource": [
                    "arn:aws:s3:::gambit2-images",
                    "arn:aws:s3:::gambit2-images/*"
                ]
            }
        ]
    }


### 61. Cargando las reglas al bucket s3 


Recordar que se tiene una dependencia:


- RDS
- Lambda(Codigo)
- Cognito 
- Secrets Manager - Parameter Store
- API Gateway
- Bucket S3 (Politica)







### 62. 





### 63. 


URLs del Hosted UI

Iniciar sesión (para obtener el token):

https://summer-app-dev-unique.auth.us-east-1.amazoncognito.com/login?client_id=38h0d6file3a5hpqej1a7s2nm4&response_type=token&scope=openid+email&redirect_uri=https://localhost:3000

Registrarse (crear un usuario nuevo):

https://summer-app-dev-unique.auth.us-east-1.amazoncognito.com/signup?client_id=38h0d6file3a5hpqej1a7s2nm4&response_type=token&scope=openid+email&redirect_uri=https://localhost:3000


Se obtiene el token desde la URL.


https://localhost:3000/#id_token=eyJraWQiOiJBakZYRThPSGt5ZVJjZnZWL1hDVkt2eHFyN2pIY29hem8zV2tTemYrTnRZPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoiSHJIYkUyUmpuZU5kX19uM1JEUTRpUSIsInN1YiI6Ijg0Zjg1NGU4LWYwZDEtNzAwYy0xZmU2LWJkYmJiMWI2OTk1NiIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiaXNzIjoiaHR0cHM6Ly9jb2duaXRvLWlkcC51cy1lYXN0LTEuYW1hem9uYXdzLmNvbS91cy1lYXN0LTFfUUpaVkc0UlJxIiwiY29nbml0bzp1c2VybmFtZSI6Ijg0Zjg1NGU4LWYwZDEtNzAwYy0xZmU2LWJkYmJiMWI2OTk1NiIsImF1ZCI6IjM4aDBkNmZpbGUzYTVocHFlajFhN3Mybm00IiwiZXZlbnRfaWQiOiJiZDNmZWU5Ni01OGNkLTQ0ZjctODFkMS0zMTVjNjk3ZWE0MjEiLCJ0b2tlbl91c2UiOiJpZCIsImF1dGhfdGltZSI6MTc5MTg2NjM4NiwiZXhwIjoxNzkxOTUyNzg2LCJpYXQiOjE3OTE4NjYzODYsImp0aSI6IjQ3YTdkYTkwLWU0YTAtNGU3OS05MzkxLWU3MzZlYTE5ZGY1MSIsImVtYWlsIjoiZHBvc2FkYWxsYW5vQGdtYWlsLmNvbSJ9.gD1UZ4Ya60ouf2kKxdzJ2-3SZWlKInKq0iH4rklDs7XhHn4RO5NzNn1AVsD9_PIaopAuAL8E9gTcKGLp0bv3j8PWHFF-WPHvNmGOOV5FcPfoosiqxWGlimyUHU8LTOrAN61zSG7mPknDTA__DktVlRN4IKQa9cS9gBN4uCY7fWPegp5dKO5VJqC10BNn-g6iS97WOjApDrpp5KF39nxo-rMXR_0GZhfefhCkHk6iywrVo_YKuC0w3aRmMg0J7kyCHE5qFcNCK7F6jrULqEOOH000AvsgPy0pCNg1gPs_y36Rn0_Z9HnDjrXY_aLt7u0_UZuzYpMKOn19dOUkx5XWmQ&access_token=eyJraWQiOiIvMGw4T3o5cmgxY0IrR0tyZWMwallsaStBTzVOazRueWJsTm44MFZuOTRVPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiI4NGY4NTRlOC1mMGQxLTcwMGMtMWZlNi1iZGJiYjFiNjk5NTYiLCJpc3MiOiJodHRwczovL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tL3VzLWVhc3QtMV9RSlpWRzRSUnEiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiIzOGgwZDZmaWxlM2E1aHBxZWoxYTdzMm5tNCIsImV2ZW50X2lkIjoiYmQzZmVlOTYtNThjZC00NGY3LTgxZDEtMzE1YzY5N2VhNDIxIiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJvcGVuaWQgZW1haWwiLCJhdXRoX3RpbWUiOjE3OTE4NjYzODYsImV4cCI6MTc5MTk1Mjc4NiwiaWF0IjoxNzkxODY2Mzg2LCJqdGkiOiJhOGQ0YTllYi1lYTM4LTQwZDItYWQzOC0xNjYyNTcyODViNjUiLCJ1c2VybmFtZSI6Ijg0Zjg1NGU4LWYwZDEtNzAwYy0xZmU2LWJkYmJiMWI2OTk1NiJ9.fp4kUyheUeqrr8UPCybBj71-pXVRzaZgEOGrUHsQG_Q2CPsav9xs70_Cg8KSdOWOY63ZtxIARPqGL2gweQ1kGiQjSoygDt52rzx2V9Z41bGxZwsZGzQ1bUaESGQu6rp1Sw671VrpGWPpt7_vGVgybfpaNWUox3Q1SVcdDqd_dJRzbGwq5PTGn-pRUN7plcat4oVJeIrxVRQdhMHoIgyfU-I1R1NRVVOqYnwiLUSYrk2-UJmY8MkZqaWKrEPJfb0uS1QyDK5hhbdxMjmEjtoJKb4sqrOXZVP73vUvL8KmH6uqqW5D8-KQk_AnslPydWc0_HKr25FE7wA_T__VjFzqrQ&expires_in=86400&token_type=Bearer



Para probar la Lambda con un usuario nuevo
Abre la URL de registro y usa un alias de Gmail, por ejemplo dposadallano+test1@gmail.com, con una contraseña de 8 o más caracteres.
Escribe el código de verificación que llega al correo.
Revisa en MySQL: select * from users;



dposadallano+test1@hotmail.com


https://localhost:3000/#id_token=eyJraWQiOiJBakZYRThPSGt5ZVJjZnZWL1hDVkt2eHFyN2pIY29hem8zV2tTemYrTnRZPSIsImFsZyI6IlJTMjU2In0.eyJhdF9oYXNoIjoidWxRS1NyRkYzZktOM0xXS2lPQ0k3ZyIsInN1YiI6ImM0NTg0NDY4LTIwZjEtNzBmMi1kZjJjLTUxNDI2NDdiMDkyNCIsImVtYWlsX3ZlcmlmaWVkIjp0cnVlLCJpc3MiOiJodHRwczovL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tL3VzLWVhc3QtMV9RSlpWRzRSUnEiLCJjb2duaXRvOnVzZXJuYW1lIjoiYzQ1ODQ0NjgtMjBmMS03MGYyLWRmMmMtNTE0MjY0N2IwOTI0IiwiYXVkIjoiMzhoMGQ2ZmlsZTNhNWhwcWVqMWE3czJubTQiLCJldmVudF9pZCI6IjgyY2Q5Mzc0LWY3NjctNDE3Mi05MjY4LTk2OWVhNmViYzE5ZCIsInRva2VuX3VzZSI6ImlkIiwiYXV0aF90aW1lIjoxNzkxODY5NjY0LCJleHAiOjE3OTE5NTYwNjQsImlhdCI6MTc5MTg2OTY2NCwianRpIjoiNDY1MWM2ZTctMThlMS00MDNhLWEyYzgtYjNhMWQwMjYwNWI4IiwiZW1haWwiOiJkcG9zYWRhbGxhbm8rdGVzdDFAaG90bWFpbC5jb20ifQ.AUyfJyqerSLKFAHQn01mB6oVGH0sNGRWvOPp9NWB3aU15u7zaJykI0OUlmC53Cl2o7CnMrloDOIS0BF_tGce2KQMkgBdN7YuYBjSfgx02-Q19ArJBDtETZTMbwwVdOMPQlzzY5W21kO2AEB_38zbBeG4lAaArx3KTTliV12mfW5PFlEdNZOZBFdrgjdcedqv-iOf7rMYAa-lkU32z8-gdOlMDIjEDJsh7Dp1GK9LRD3hB9ukRcq3AyahfNqKnFI6ur2-9MZTsikBxqJSsFwPSq6v2RnpX-k4kIBECz6oRo_Eu8MmB4x5Qy8R48M4_a-8jZcHM6Vh1-x0uT61KqBdMw&access_token=eyJraWQiOiIvMGw4T3o5cmgxY0IrR0tyZWMwallsaStBTzVOazRueWJsTm44MFZuOTRVPSIsImFsZyI6IlJTMjU2In0.eyJzdWIiOiJjNDU4NDQ2OC0yMGYxLTcwZjItZGYyYy01MTQyNjQ3YjA5MjQiLCJpc3MiOiJodHRwczovL2NvZ25pdG8taWRwLnVzLWVhc3QtMS5hbWF6b25hd3MuY29tL3VzLWVhc3QtMV9RSlpWRzRSUnEiLCJ2ZXJzaW9uIjoyLCJjbGllbnRfaWQiOiIzOGgwZDZmaWxlM2E1aHBxZWoxYTdzMm5tNCIsImV2ZW50X2lkIjoiODJjZDkzNzQtZjc2Ny00MTcyLTkyNjgtOTY5ZWE2ZWJjMTlkIiwidG9rZW5fdXNlIjoiYWNjZXNzIiwic2NvcGUiOiJvcGVuaWQgZW1haWwiLCJhdXRoX3RpbWUiOjE3OTE4Njk2NjQsImV4cCI6MTc5MTk1NjA2NCwiaWF0IjoxNzkxODY5NjY0LCJqdGkiOiI4NjAwMTY3ZS0zNTA0LTQyZTktOTI3My01NTdiNTA4YWFhZDAiLCJ1c2VybmFtZSI6ImM0NTg0NDY4LTIwZjEtNzBmMi1kZjJjLTUxNDI2NDdiMDkyNCJ9.sqjQNaHTcwG-oARDk-ZxD5ld8IO4HqKa2QJvo8jIUKHgBEPL-2zYdmZ-7AR4-Q6qd_s072B3L1ZRmtOjDAaTuVMCuTYZzmF5wEO5QzW6Epaxmv2zsqPp2uY4g4uHFi6gPjr76FNwyiRIFWJh5nmJrBoNI-WFOHhlVY-JzYiH21ZwBt-s14niSoUAfejm0TX52MmdiiVNbI6BU6jxTElsKVyqxZH74RiiEB627tAnUHCclRsDPd_ScZniRtpz2bHLohE6jRMGfM5hwmEsgiYKGU3pTaRfHMq8P7l7Mf-JAJl3sKzBTzxxVb8JeB-w9qTJgNkBg-gIRQH8SOFYhSLfww&expires_in=86400&token_type=Bearer


{
  "at_hash": "ulQKSrFF3fKN3LWKiOCI7g",
  "sub": "c4584468-20f1-70f2-df2c-5142647b0924",
  "email_verified": true,
  "iss": "https://cognito-idp.us-east-1.amazonaws.com/us-east-1_QJZVG4RRq",
  "cognito:username": "c4584468-20f1-70f2-df2c-5142647b0924",
  "aud": "38h0d6file3a5hpqej1a7s2nm4",
  "event_id": "82cd9374-f767-4172-9268-969ea6ebc19d",
  "token_use": "id",
  "auth_time": 1791869664,
  "exp": 1791956064,
  "iat": 1791869664,
  "jti": "4651c6e7-18e1-403a-a2c8-b3a1d02605b8",
  "email": "dposadallano+test1@hotmail.com"
}



Hasta la primera firma. (o primer punto).



se realizan 2 curlts para subir las imagenes al bucket.


Paso 1. Crea una petición nueva en Postman. Cambia el método a PUT y pega esta URL:

https://65ktuy96tk.execute-api.us-east-1.amazonaws.com/dev/summer-images-800445863816/diego.png





Paso 1. Desde la terminal de root (donde está el perfil bold-free-tier), pídele a API Gateway los métodos de esa ruta:


root@p3rseus:/home/diegoall/courses/e-commerce-aws-golang# aws apigateway get-resource --rest-api-id 65ktuy96tk --resource-id pp7nrq --region us-east-1 --no-cli-pager --profile bold-free-tier
{
    "id": "pp7nrq",
    "parentId": "0zsomh",
    "pathPart": "{object}",
    "path": "/{folder}/{object}",
    "resourceMethods": {
        "OPTIONS": {},
        "PUT": {}
    }
}































### 60. Reglas de Politica al Bucket S3


### 61. Cargando las reglas al bucket S3


### 62. Asignando aws.cognito.sigin.user.admin 


### 63. Ultimos ajustes en CORS para el metodo PUT



### 64. Probando la solucioon desde POSTMAN


## Sección 10: Backend - Lambda Principal


### 65. 


### 66. 


## Sección 11: Backend - Categorias


## Sección 12: Backend - Productos


## Sección 13: Backend Usuarios



## Sección 14: Backend - Address



## Sección 15: Backend - Ordenes




## Sección 16: Fin de Back Office



## Sección 17: Configurando entorno - FRONTEND



## Sección 18: Inicializando proyecto - FRONTEND




## Sección 19: Sistema de autenticación - FRONTEND




## Sección 20: Menu principal - FRONTEND





## Sección 21: Panel de admin - FRONTEND



## Sección 22: Ajustes del usuario - FRONTEND
 



## Sección 23: Sistema de direcciones - FRONTEND



## Sección 24: Home - FRONTEND



## Sección 25: Buscar de productos - FRONTEND




## Sección 26: Sistema de categorias - FRONTEND
 



## Sección 27: Página de producto - FRONTEND




## Sección 28: Sistema de carrito - FRONTEND



## Sección 29: Mis pedidos - FRONTEND



## Sección 30: Deploy - FRONTEND



## Sección 31: Clase extra












- Tomar el diagrama que tengo con  chart.js y sacar un listado de temas o configuraciones.

- chart.js

- 

