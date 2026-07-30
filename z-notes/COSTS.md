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

