---
audio: false
generated: false
lang: es
layout: post
title: Pensamientos sobre el desarrollo de software multi-regional
translated: true
---

Para empresas internacionales, a menudo hay proyectos que sirven a personas de múltiples regiones, como Singapur, Hong Kong, Reino Unido, EE. UU. y China.

He trabajado en algunos proyectos que atienden a usuarios de múltiples regiones. Hacerlo bien en proyectos de backend no es fácil.

Para el Standard Chartered Bank, hay aplicaciones como SC Mobile India y SC Mobile Hong Kong. Para McDonald's, hay versiones como McDonald's China y McDonald's EE. UU. Para Starbucks, hay Starbucks EE. UU. y Starbucks China. En esencia, proporcionan a diferentes países sus propias aplicaciones. Estas aplicaciones probablemente utilizan diferentes servidores backend y tienen algunas características diferentes, pero mantienen el mismo lenguaje de diseño.

Probablemente esto esté mal. En los primeros años, parece simple o factible. Pero después de una década, sabrán que es muy doloroso. El costo de mantenimiento o sincronización, el costo de pruebas: hay toneladas de esfuerzos duplicados.

Sin embargo, para Facebook, Google o Apple Pay, es algo simple. Alguien puede decir que no son aplicaciones financieras; tienen algunas reglas de cumplimiento que deben seguirse. No es cierto. El cumplimiento a menudo significa el servidor de base de datos, o la base de datos, o algunos datos que los departamentos gubernamentales quieren verificar o que las empresas de auditoría deben auditar.

Sin embargo, otros esfuerzos son los mismos. El software es muy flexible. Deberíamos permitir que el código esté en el mismo repositorio, deberíamos usar la configuración de fuentes de datos para alojar datos de diferentes regiones y deberíamos compartir el mismo código, el mismo diseño, el mismo flujo de trabajo y las mismas pruebas en la medida de lo posible.

Apple Pay es un buen ejemplo de esto. La App Store también es un buen ejemplo de esto. Ellos también atienden a cada país.

Probablemente haya algunos proyectos en grandes empresas tecnológicas que usan continentes para separar, como Asia y la región del Pacífico, Norteamérica. Para estos también.

Lo primero al hacer desarrollo multi-regional es saber qué es diferente, qué cumplimiento debemos seguir y cómo reducir los esfuerzos duplicados en la mayor medida posible.

Para el texto a voz, Google Cloud necesita entrenar diferentes idiomas. Proporcionan diferentes modelos y diferentes idiomas para ello. Para los idiomas, las diferencias entre idiomas son sus sonidos, su pronunciación y su apariencia de caracteres. Lo primero significa que al usar Google Cloud para hacer texto a voz, necesitamos usar diferentes modelos. Para su apariencia de caracteres, eso significa que al hacer generación de PDF, debemos tener cuidado con la selección de fuentes.

Para proyectos multi-regional, en proyectos de Spring Boot, podemos usar sus alias y diferentes inicializaciones de objetos para hacerlo. Podemos usar propiedades o configuración YAML de manera inteligente. Podemos poner toda la lógica diferente basada en la región en algunos módulos o clases específicas.

Y para el alojamiento de código, diferentes ramas para diferentes países parecen fáciles al principio, pero después de algunos años, sabrás lo doloroso que es. Necesitas hacer git cherry-pick para otras regiones. Y necesitas probar de nuevo en otra rama. Cada vez que haces un pequeño cambio, necesitas sincronizarlo a las ramas. Y con el tiempo, si no ponemos nuestro esfuerzo en minimizar el código o la lógica diferente, las diferencias en el código entre múltiples regiones o países se vuelven lo suficientemente grandes como para ser imposibles de arreglar.

La buena noticia es que ahora la IA puede ayudarnos a refactorizar o escribir mejor código, o corregir los problemas de diseño de código multi-regional. No importa cuán grande sea el error, cuando lo arreglamos, es un error pequeño.

No solo para la codificación, el despliegue y el mantenimiento de lanzamiento, sino también para la extensibilidad. Considera cómo agregar un nuevo país o región. ¿Cuánto esfuerzo requerirá eso? Si es mínimo o solo implica alguna configuración, entonces nuestro diseño es excelente. Si toma unos meses, eso también es aceptable. Si toma varios años, ¿todavía procederemos con eso?

En el ensayo de Yin Wang, [Sobre Linux, Windows y Mac](https://www.yinwang.org/blog-cn/2013/03/07/linux-windows-mac), mencionó que un diseñador de Adobe le dijo que pasaron dos años migrando de Windows a macOS.

¿Apoyar una nueva región requerirá dos años de adaptación? Para algunos proyectos, podría ser así. Esto es una consideración de diseño crítica.

El mundo se está volviendo más conectado. No importa qué país o región se apunte inicialmente, también debemos considerar otras regiones. Es mejor hacerlo bien desde el principio. Para las empresas internacionales establecidas, es recomendable desarrollar productos de software para al menos dos países o regiones desde el principio. Mantén esta mentalidad multi-regional desde el comienzo. Si tenemos más recursos de ingeniería, podemos apoyar más países o regiones.