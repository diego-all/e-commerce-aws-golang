
Si eso responde bien y desde el e-commerce sigue apareciendo un error de CORS, revisa primero el token. Cuando el authorizer de Cognito rechaza un token vencido o inválido, la respuesta 401/403 sale sin cabeceras CORS y el navegador la reporta como error de CORS aunque el problema sea la autenticación. Para ese caso sirven los aws_api_gateway_gateway_response que te ofrecí antes, y te los agrego cuando quieras.


aws_api_gateway_gateway_response






Previo a validar con postman el funcionamiento de la API gateway


La lambda requiere un permiso para acceder al secret manager (System manager).

Sí, el permiso ya está: summer_backend_ssm en lambda_backend.tf es el equivalente al “Gambit Secret Manager”

Lo que sí falta es el código Go, que sigue llamando a Secrets Manager.



Ese ?code=... aparece porque el login usó response_type=code, el flujo de código de autorización, que no devuelve el token directamente. El profesor usó el flujo implícito, que sí lo devuelve en la URL como #access_token=.... Tu cliente de Cognito ya permite ambos flujos, así que tienes dos opciones.

Abre esta URL en el navegador. Es la misma de antes con response_type=token:

https://summer-app-dev-unique.auth.us-east-1.amazoncognito.com/login?client_id=3lejofgfifede3r4nrf7vaqfl2&response_type=token&scope=aws.cognito.signin.user.admin+email+openid&redirect_uri=https://localhost:3000



Problemas de seguridad que vi

Ya que estás en desarrollo, te conviene corregir esto:

Credenciales en los logs. Tu log imprime el DSN completo: root:summer2026@tcp(...). Eso queda en CloudWatch con retención “Never expire”. Elimina ese fmt.Println y cambia esa contraseña, porque ya está expuesta (y también la pegaste aquí).
Usuario root para la Lambda. Crea un usuario de base de datos con permisos limitados.
SQL Injection. En category.go y signup.go concatenas strings directamente en el SQL. Usa consultas parametrizadas:
go
   Db.Exec("INSERT INTO category (Categ_Name, Categ_Path) VALUES (?, ?)", c.CategName, c.CategPath)



ValidoToken no verifica la firma. Solo decodifica y revisa exp. Cualquiera puede fabricar un JWT con tu sub y pasar como admin si el API Gateway no lo valida antes. Asegúrate de que el authorizer JWT de API Gateway esté activo en esa ruta, o verifica la firma contra el JWKS de Cognito.
Tokens expuestos. Pegaste un id_token y access_token reales aquí. Expiran en 24 h (expires_in=86400), pero conviene cerrar sesión/revocarlos si es posible.



hay como un tapado para que no funcione el token se coloca supuestamente el id_token pero se encesita el acces token.



La solución más adecuada para tu caso es la Opción 2: devolver tkj.Sub en auth.go. Con eso no dependes de qué token pegues en Postman.

Por qué es la más adecuada

En el curso, el docente usa el access_token, que trae el campo username. Tú estás usando el id_token, que no trae username sino cognito:username. Por eso tu Username llega vacío y la consulta busca User_UUID = ''.

El sub aparece en ambos tokens y es el mismo valor que guardaste como User_UUID en la base de datos (44283408-2071-701d-9b7a-13c55283683f).

Cambio en auth.go


