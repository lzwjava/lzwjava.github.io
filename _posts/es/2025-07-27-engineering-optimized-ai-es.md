---
audio: false
generated: false
image: false
lang: es
layout: post
title: Optimización de la ingeniería de software para IA
translated: true
---

En este blog, utilicé cientos de scripts para ayudar con la traducción, el playground, el mantenimiento de frontmatter y los bots de Telegram. Creo que este enfoque de desarrollo podría representar el futuro de la ingeniería de software optimizada para la IA.

No dependo mucho de la funcionalidad de los módulos de Python, ni quiero estructurar el código como un gran proyecto de Java Spring.

Le dije a mi anterior líder de equipo que, aunque su arquitectura bancaria es impresionante, si empezáramos hoy, consideraría optimizar para LLM/IA. Esto implicaría una mejor ingeniería de contexto, una mejor separación de contextos y priorizar el pensamiento centrado en la IA sobre el diseño centrado en el ser humano. Aunque Spring ofrece múltiples niveles y buena abstracción, puede ser difícil para la LLM/IA navegar por ellos.

Creo que deberíamos apuntar a estructuras más planas, similares a una organización plana. Esto significa usar solo dos niveles: el primer nivel llama al segundo nivel. En una función, es mejor llamar a otras 50 funciones directamente en lugar de tener 50 niveles o pilas anidadas. La IA/LLM tienen dificultades para juzgar o inferir estructuras complejas y anidadas, pero se desempeñan bien manejando funciones más pequeñas de 100 a 200 líneas de código. Python es adecuado para llamar e importar de otros archivos.

Una razón por la que el código de Python es más fácil que el de Java es que su gestión de dependencias es simple. Solo necesitas usar `pip install` para agregar una dependencia. Con Maven, necesitas escribir la dependencia en un archivo POM XML y luego usar `mvn compile` para que Maven descargue las dependencias.

Otra razón de la simplicidad de Python es que su código se puede ejecutar directamente sin problemas.

Aunque a partir de Java 11, el comando `java` puede ejecutar directamente programas de código fuente de un solo archivo sin necesidad de compilarlos por separado usando `javac`. Sin embargo, a menudo, para proyectos de Java, son grandes, por lo que hay que ejecutarlos con `mvn spring-boot:run` junto con alguna configuración de propiedades.

Una tercera razón es que el diseño de módulos de Python es simple; puedes usar `from` e `import` para importar fácilmente código de otros archivos.

Por ahora, muchos chatbots de IA pueden ejecutar código de Python directamente en la ventana del chatbot, como Grok.

Al comparar 100 archivos de Java, cada uno con alrededor de 1000 líneas de código, con algunos scripts de Python simples, no es una comparación justa. Para este tipo de proyecto, preferiría tener 1000 archivos de Python, cada uno con alrededor de 100 líneas de código.

Es aceptable seleccionar líneas de código o una función para editar. Sin embargo, necesitas saber dónde seleccionar. ¿Por qué no dejar que esta tarea sea manejada por la IA para facilitarnos la vida? Así que solo necesitamos usar "seleccionar todo" para seleccionar todo el código y decirle a la IA/LLM cómo editarlo.

Para Python, es más fácil usar `if __name__ == "__main__":` para ejecutar y probar funciones en un archivo. También es más fácil para otros archivos de Python llamar a las funciones dentro de este archivo sin necesidad de ejecutar la prueba.

Esto es ingeniería de contexto optimizada para la IA. ¿Podríamos abordarlo de otras maneras? La IA/LLM es autorregresiva. Sin embargo, cuando usamos Copilot o Claude Code, no sabemos cómo el Agente de Software de IA nos ayuda. Deberían pensar en ello en lugar de nosotros.

¿Podríamos, desde el lado del usuario, organizar el código específicamente para reducir el uso de tokens? Para este punto, el enfoque de tener 1000 archivos de Python con cada uno 100 líneas de código es bueno para este propósito. Porque puedes verificar funciones y archivos de código fácilmente antes de permitir que otros códigos de Python los llamen.

Pero un problema es que si quieres cambiar varios archivos de código juntos, no es fácil hacerlo. Para una manera simple, puedes copiar el código a los chatbots de IA y dejar que te digan cómo editar el código en estos archivos.

Posiblemente, no necesitemos usar el número de líneas para separar funciones o lógica. Pero deberíamos hacerlo para separar la lógica en funciones pequeñas. Podemos hacerlo separándolas naturalmente por tipo de lógica, para que parezcan más cortas.

¿Por qué queremos Ingeniería de Software Optimizada para la IA? Porque la IA es poderosa, deberíamos optimizar todo para la IA y luego dejar que la IA ayude a la ingeniería de software tanto como sea posible.

No es solo posible para el código, sino también para cualquier texto. Supongamos que somos editores muy exigentes; no queremos que la IA edite nuestros grandes textos de una vez. Queremos revisar párrafo por párrafo. Para el código, podemos tolerar errores o fallos menores. Para el texto, podemos tolerarlos porque la mayoría de los lectores no son tan exigentes.

Pero el código es diferente en el sentido de que a veces, incluso un error menor puede llevar al mal funcionamiento completo de un gran proyecto.

Para archivos XML o YAML, probablemente no necesitemos separarlos tanto porque ya están altamente estructurados.

Y para archivos HTML, deberíamos hacer alguna separación. En lugar de escribir cientos de archivos de JavaScript junto con cientos de archivos HTML, haciendo que sea fácil superar las 1000 líneas de código, deberíamos usar `import` para JavaScript para gestionarlo. Para el código de JavaScript, podemos usar los métodos anteriores para separarlo.

Queremos estructurar el código de manera que la IA nos ayude fácilmente a agregar, editar, eliminar y ejecutar código. Este es el comienzo. Imagina un día en el que todo el código pueda ser generado o corregido por la IA fácilmente. El mundo estará altamente digitalizado.

Imagina que yo escribo 100 grandes proyectos de software y proporciono APIs para conectarme con otros. Esto incluye mi agenda diaria; yo mismo soy como una empresa tecnológica de 1000 empleados en la actualidad. Están personalizados para mis necesidades, para ganar dinero o gastar dinero para mi beneficio. Esto es realmente asombroso.