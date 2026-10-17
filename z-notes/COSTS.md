# Costs



A. El costo por el uso de IPs Públicas IPv4 (El factor más común)
Desde febrero de 2024, AWS realiza un cobro global por cada dirección IPv4 pública que se encuentre en uso en tu cuenta, incluso si el recurso asociado pertenece a la capa gratuita.

Costo aproximado: $0.005 USD por hora por cada IP pública asignada.


Cognito




RDS


Acota el Security Group: En lugar de ec2.Peer.any_ipv4(), cambia esa línea para que solo permita tu dirección IP pública actual (por ejemplo: ec2.Peer.ipv4('YOUR_IP/32')). Esto evita que bots ataquen tu base de datos y generen tráfico innecesario.


Secret Manager

$ 0.40 por secreto al mes
$ 0.05 por 10000 llamadas a la API

Se tiene un periodo de prueba de 30 dias disponible.



Lo que muestran tus capturas


El grueso del costo no es la instancia. La anomalía de $1.44 en RDS tiene como usage type ExtendedSupport:Yr1-Yr2:MySQL8.0, y $1.30 de esos $1.44 vienen de ahí. Es el cargo de Extended Support por usar MySQL 8.0, que ya salió del soporte estándar. Si creas la instancia con MySQL 8.4, ese cargo desaparece.
RDS no está en tu Free Tier. La pantalla de Free Tier lista 6 servicios (KMS, Glue, CloudWatch, Lambda) y al filtrar rds o aurora no aparece nada. Tampoco tienes créditos ($0.00). EC2 tampoco aparece en esa lista, así que no asumas que una instancia EC2 sería gratis.
Los $0.03 de VPC probablemente son IPv4 públicas, que AWS cobra por hora.




