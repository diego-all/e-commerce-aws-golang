
Si eso responde bien y desde el e-commerce sigue apareciendo un error de CORS, revisa primero el token. Cuando el authorizer de Cognito rechaza un token vencido o inválido, la respuesta 401/403 sale sin cabeceras CORS y el navegador la reporta como error de CORS aunque el problema sea la autenticación. Para ese caso sirven los aws_api_gateway_gateway_response que te ofrecí antes, y te los agrego cuando quieras.

aws_api_gateway_gateway_response


