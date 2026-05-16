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


### 38.  


## Sección 7: Backend - Secret Manager


## Sección 8: Backend - Lambda con Go para manejo de usuarios


## Sección 9: APi Gateway directo a s3 para alojar imagenes


## Sección 10: Backend - Lambda Principal


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

