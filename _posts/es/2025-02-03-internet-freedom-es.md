---
audio: false
generated: false
image: false
lang: es
layout: post
title: El viaje hacia la libertad en internet
translated: true
---

Este post se actualizó en agosto de 2025.

---

## Viaje

De 2010 a 2013, utilicé Goagent y la herramienta de proxy SwitchyOmega para sortear el GFW.

Entre 2014 y 2015, utilicé Qujing (曲径) para proxy y seguí a su autor en Twitter, quien ahora vive en Japón.

De junio de 2016 a julio de 2018, utilicé Digital Ocean para alojar mi servidor proxy de shadowsocks.

A partir de 2019, comencé a usar https://zhs.cloud.

En marzo de 2023, comencé a usar una tarjeta SIM de Macao en mi teléfono móvil para acceder a Internet sin proxy o VPN. Esto costaba alrededor de 150 CNY al mes por 20 GB de datos móviles, y utilicé este método durante aproximadamente un año.

En 2024, volví a usar Outline Manager con mi servidor proxy de shadowsocks, experimentando con varios proveedores de cloud.

En febrero de 2025, mi configuración preferida es Outline Manager con un servidor de Aliyun Hong Kong para uso diario y un servidor no Hong Kong (como Singapur o Japón) para herramientas de IA. Mantengo la misma configuración de reglas de proxy utilizada en Shadowrocket o Clash.

A partir de junio de 2025, comencé a usar un script de Python en mi computadora portátil para seleccionar automáticamente un servidor proxy cada 10 minutos según los resultados de las pruebas de velocidad. El script prioriza los servidores de Singapur sobre los de Hong Kong para usar herramientas de IA. Para más detalles, consulte [Automatización de la gestión de proxy Clash](/clash-en). Para el proveedor de cloud VPN, seguí usando https://zhs.cloud.

Además, en iOS, volví a usar una tarjeta SIM de Macao, costando 150 CNY al mes por 20 GB de datos. También compré 5 GB adicionales de datos tres veces por 20 MOP cada uno, totalizando alrededor de 200 CNY por 35 GB de datos en mi teléfono móvil.

Ha funcionado muy bien durante los últimos 2 meses. Espero poder seguir usando este método para navegar por Internet hasta que me vaya de China para trabajar en el extranjero.

## La Diferencia Comparada con la Reversión de la Miopía

Un desafío es luchar contra el GFW, que es hecho por humanos. El otro es abordar los principios del funcionamiento del músculo ocular.

Es fácil medir la efectividad de una solución de proxy. Sin embargo, revertir la miopía requiere tiempo para determinar si el globo ocular está cambiando.

## Similitudes con la Reversión de la Miopía

Una similitud es que tanto una solución de proxy como los anteojos con una reducción de 200 grados suelen funcionar bien. Una implica acceder a Internet, y la otra implica mejorar la visión. Ambas abordan problemas muy importantes.

El principio subyacente es que si entendemos cómo funciona el GFW y encontramos una manera de sortearlo, la solución debería ser sencilla.

## Razonamiento y Matices

Todavía no entiendo completamente cómo funciona el GFW. Cuando la IP de mi servidor proxy es bloqueada, ahora tengo más formas de investigar la causa.

Puedo verificar si el bloqueo ocurre en la red celular o en el ancho de banda doméstico. Si es la red celular, puedo verificar si es en 4G o 5G.

De manera similar, si mi miopía no mejora después de seis meses o un año, necesito investigar si hay diferencias entre mis ojos. También necesito considerar si he estado viendo las cosas apenas con claridad sin forzar mis ojos durante la mayor parte del año.

## Estado Actual

Mi servidor proxy funciona actualmente muy bien. Las velocidades de descarga en mi teléfono alcanzan los 80 Mbps, y las velocidades de subida alcanzan los 50 Mbps al conectarme al servidor proxy de Hong Kong. Lo mismo ocurre en mi computadora portátil.

Utilizo las mismas configuraciones de proxy en mi computadora portátil y teléfonos, y funcionan perfectamente. Normalmente, uso un servidor proxy para visitar sitios fuera de China, y uso un servidor no HK para herramientas de IA.

## Recuperación

Si las cosas se rompen, mi método de recuperación es simple. Solo necesito cambiar la IP elástica de mi servidor proxy de Aliyun Hong Kong y subir la nueva URL del proxy al almacenamiento en la nube. Esto significa que necesito ejecutar dos scripts, lo que tarda aproximadamente 1 minuto, y mi computadora portátil y teléfonos pueden actualizar la dirección del servidor proxy.

## Arrepentimiento

Luché con el GFW demasiadas veces y durante demasiado tiempo. Probé muchos protocolos de proxy, sabiendo que serían detectados por el GFW y bloqueados. Sin un servidor proxy confiable, es difícil configurar un proxy en un router OpenWrt.

Una cosa de la que me arrepiento es no haber aprendido las técnicas de los proveedores de proxy antes, como [zhs.cloud](https://zhs.cloud). Ahora conozco la mayoría de sus secretos.

Lo otro es que cada vez que mi servidor proxy era bloqueado, no pensaba demasiado al respecto. Parecía que solo necesitabas configurar un nuevo servidor proxy para obtener una nueva IP que no hubiera sido bloqueada. Pero eso era un pensamiento superficial.

## Métricas

Me arrepiento de no haber usado Speedtest antes. Conocía el nombre de la herramienta hace mucho tiempo, pero no aprendí a usarla cuidadosamente.

Es bueno usar Speedtest a menudo al conectarse a estaciones de señal móvil 5G o 4G o a una red de banda ancha doméstica.

Para revertir la miopía, es lo mismo. Compré un gráfico ocular en forma de C y un gráfico ocular estándar.

Sin medición, no hay mejora. Medir las cosas te ayuda a aprender. Usar Speedtest a menudo me ayuda a descubrir que en una red 5G, es fácil superar los 100 Mbps, mientras que en una red de banda ancha doméstica, es difícil superar los 100 Mbps.

## Todavía es Temprano

¿Caerá el muro del GFW en los próximos años? Es difícil decirlo.

Cuando, después de revertir mi miopía durante dos años, le dije a mi amigo que mi método de reversión necesitaba ser mejorado y que necesitaba usar anteojos con 200 grados menos que mi receta real en lugar de 150 grados menos.

Él dijo que no había problema, que estaba bien, que no era una pérdida de tiempo, y que todavía era temprano. Sí. Estas cosas son fundamentales. Como la miopía, las personas deberían descubrirlo antes. Todd Becker compartió este descubrimiento en YouTube en 2014, y los videos obtuvieron más de 1 millón de visitas. Y ahora es 2025, ¿cuántas personas realmente lo conocen en el mundo? Supongo que serán menos de 10 mil.