---
audio: false
generated: false
lang: es
layout: post
title: Pensamientos sobre el desarrollo multi-regional
translated: true
---

Para empresas internacionales, a menudo hay proyectos que sirven a personas de múltiples regiones, como Singapur, Hong Kong, Reino Unido, EE. UU. y China.

He trabajado en algunos proyectos que atienden a usuarios de múltiples regiones. Hacerlo bien en proyectos de backend no es fácil.

Para el Standard Chartered Bank, existe la aplicación SC Mobile India, la aplicación SC Mobile Hong Kong, etc. Básicamente, dan a cada país su propia aplicación. Probablemente usen diferentes aplicaciones, diferentes servidores backend y algunas características son diferentes, pero con el mismo lenguaje de diseño.

Probablemente esté mal hacerlo así. En los primeros años, parece simple o factible. Pero después de una década, sabrán que es muy doloroso. El costo de mantenimiento o sincronización, el costo de pruebas—hay toneladas de esfuerzos duplicados.

Sin embargo, para Facebook, Google o Apple Pay, es algo simple. Alguien puede decir que no son aplicaciones financieras; tienen algunas reglas de cumplimiento que deben seguir. No es cierto. El cumplimiento a menudo significa el servidor de base de datos, o la base de datos, o algunos datos que los departamentos gubernamentales quieren verificar o que las empresas de auditoría realicen auditorías.

Sin embargo, otros esfuerzos son los mismos. El software es muy flexible. Deberíamos permitir que el código esté en el mismo repositorio, deberíamos usar la configuración de fuentes de datos para alojar datos de diferentes regiones y deberíamos compartir el mismo código, el mismo diseño, el mismo flujo de trabajo y las mismas pruebas en la medida de lo posible.

Apple Pay es un buen ejemplo de esto. La App Store también es un buen ejemplo de esto. Ellos atienden a cada país también.

Probablemente haya algunos proyectos en grandes empresas tecnológicas que usan continentes para separar, como Asia y la región del Pacífico, Norteamérica. Para estos también.

Lo primero al hacer desarrollo multi-regional es saber qué es diferente, cuál es el cumplimiento que debemos seguir y cómo reducir los esfuerzos duplicados en la mayor medida posible.

Para el texto a voz, Google Cloud necesita entrenar diferentes idiomas. Proporcionan diferentes modelos y diferentes idiomas para ello. Para los idiomas, las diferencias entre idiomas son sus sonidos, su pronunciación y su apariencia de caracteres. Lo primero significa que al usar Google Cloud para hacer texto a voz, necesitamos usar diferentes modelos. Para su apariencia de caracteres, eso significa que al hacer generación de PDF, debemos tener cuidado con la selección de fuentes.

Para proyectos multi-regional, en proyectos de Spring Boot, podemos usar sus alias y diferentes inicializaciones de objetos para hacerlo. Podemos usar propiedades o configuración YAML de manera inteligente. Podemos poner toda la lógica diferente basada en la región en algunos módulos o clases específicas.

Y para el alojamiento de código, diferentes ramas para diferentes países parecen fáciles al principio, pero después de algunos años, sabrás lo doloroso que es. Necesitas hacer git cherry-pick para otras regiones. Y necesitas probar de nuevo en otra rama. Cada vez que haces un pequeño cambio, necesitas sincronizarlo con las ramas. Y con el tiempo, si no ponemos nuestro esfuerzo en minimizar las diferencias de código o lógica, las diferencias en el código entre múltiples regiones o países se vuelven lo suficientemente grandes como para ser imposibles de corregir.

La buena noticia es que ahora la IA puede ayudarnos a refactorizar o escribir mejor código, o corregir los problemas de diseño de código multi-regional. No importa cuán grande sea el error, cuando lo corregimos, es un error pequeño.