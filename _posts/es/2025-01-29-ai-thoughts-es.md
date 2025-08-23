---
audio: false
generated: false
image: false
lang: es
layout: post
title: Flujos de trabajo de IA, editores de código y disrupción de plataformas
translated: true
---

### Tabla de contenidos

1. [Reflexiones sobre IA](#reflexiones-sobre-ia)
   - La IA carece de inteligencia o profundidad real
   - El aprendizaje automático es cálculo aplicado avanzado
   - Los LLM tienen dificultades con formatos de archivo estructurados
   - El código abierto elimina el secreto tecnológico
   - Las herramientas basadas en texto serán las primeras afectadas por la IA

2. [Nuevas plataformas impulsadas por flujos de trabajo de IA](#nuevas-plataformas-impulsadas-por-flujos-de-trabajo-de-ia)
   - Los flujos de trabajo de IA automatizan la generación de contenido multilingüe
   - Los usuarios envían solicitudes para conversión de formatos
   - Las plataformas permiten refinamiento y resumen de contenido
   - Flujos de trabajo de IA personalizables mediante ajustes de palabras clave
   - La IA maneja transformaciones de contenido de extremo a extremo

3. [La próxima dirección de los editores de código con IA](#la-próxima-dirección-de-los-editores-de-código-con-ia)
   - La integración en la nube es crucial para flujos de CI/CD
   - Las pruebas A/B mejoran el contenido generado por IA
   - RLHF se extiende a comentarios de implementación en el mundo real
   - La retroalimentación humana refina salidas imperfectas de IA
   - Optimizar solicitudes supera la corrección de salidas


## Reflexiones sobre IA

*Última actualización en agosto de 2025*

- Satya Nadella mencionó la paradoja de Jevons. Vale la pena aprenderla.

- Yin Wang: No hay "inteligencia" en la inteligencia artificial, no hay "neural" en las redes neuronales, no hay "aprendizaje" en el aprendizaje automático y no hay "profundidad" en el aprendizaje profundo. Lo que realmente funciona en este campo se llama "cálculo". Prefiero llamar a este campo "computación diferenciable", y el proceso de construcción de modelos se llama "programación diferenciable".

- Yin Wang: El aprendizaje automático es realmente útil, incluso se podría decir que es una teoría hermosa, ¡porque es simplemente cálculo con un nuevo aspecto! Es la teoría antigua y grandiosa de Newton y Leibniz, pero en una forma más simple, elegante y poderosa. El aprendizaje automático es básicamente el uso del cálculo para derivar y ajustar algunas funciones, y el aprendizaje profundo es el ajuste de funciones más complejas.

- Actualmente, los modelos de lenguaje grandes no pueden filtrar por lenguaje de archivo como YAML o Python. Sin embargo, una parte significativa de la información en el mundo real se organiza de esta manera. Esto significa que podríamos entrenar modelos de lenguaje grandes utilizando archivos.

- Para entrenar modelos de lenguaje grandes, podríamos desarrollar un sistema que encuentre coincidencias exactas. Tal vez podríamos combinar el algoritmo de búsqueda KMP (Knuth-Morris-Pratt) con la arquitectura transformer para mejorar las capacidades de búsqueda.

- No hay secretos tecnológicos. El código abierto revelará todos los secretos que se guardan celosamente.

- La IA afectará muchas herramientas, incluidas las indirectas. La gente dice que no necesitarán Figma para dibujar prototipos, que irán directamente al código. Creo que Postman será similar; la gente usará directamente Python u otros scripts para llamar o probar APIs.

- Una razón por la que no usamos Postman o Figma en la era de la IA es que sus funcionalidades no pueden generarse mediante texto. Además, carecen de un atajo como comando + K para activar el reemplazo de componentes.

- Las interfaces de usuario se están convirtiendo en una barrera en la era de la IA. ¿Por qué actualizar Postman para que sea compatible con IA y probar aplicaciones cuando podemos usar directamente la biblioteca requests de Python u otros lenguajes de programación para probar código, ya que estos últimos estarán potenciados por IA?

- ¿Por qué actualizar Figma para que sea compatible con IA y crear interfaces de usuario cuando la generación de interfaces basadas en código, potenciada por IA, ofrece un enfoque más directo y potencialmente más poderoso?

- Los LLM cambiarán primero las aplicaciones relacionadas con texto, como Google, motores de búsqueda, editores de texto y herramientas de escritura, Quizlet, Zendesk, DeepL, Medium, WordPress, Trello, Asana, Gmail, GitHub, Goodreads, Duolingo y Feedly.

- Por el contrario, es poco probable que los LLM revolucionen tecnologías como Git, Linux, ffmpeg, teléfonos móviles, hardware, navegadores, sistemas operativos o llamadas de voz y video. Estas tecnologías son centradas en código, y su código no es fácilmente generable por IA, a diferencia de herramientas de prueba de APIs como Postman.

- Las tecnologías con más código son difíciles de revolucionar con IA, como OpenOffice, MySQL, Mozilla Firefox, Chromium, VLC Media Player, Qt Framework, LLVM/Clang y GNOME. Si la IA pudiera ayudar a hacer estas tecnologías, no serían reemplazadas. La IA debería ayudar a crear mejores tecnologías, y para eso necesitará más poder de cómputo para generar la misma magnitud de código.

- Hay dos formas en que los LLM pueden traer cambio: primero, alterando el contenido o los datos dentro de una plataforma o software, como la traducción de contenido en apps como TikTok; segundo, reemplazando directamente ciertos softwares o plataformas, como Postman o Google Search, incluyendo Google Translate.

- Hay dos formas en que las herramientas de audio con IA pueden traer cambio: primero, alterando el contenido o datos dentro de una plataforma o software, como generar audiolibros para Audible; segundo, reemplazando directamente ciertos softwares o plataformas, por ejemplo, apps de cantar, ya que la IA ahora puede realizar las mismas tareas que los humanos, haciendo más fácil que la gente cante como hobby.

- Hay varias formas de medir cómo la IA impacta el software o plataformas actuales. Una es medir cuántos datos o contenido pueden ser generados o mejorados por IA, ya sea parcial o completamente. Otra es medir cuánto código puede ser escrito o mejorado por IA, ya sea parcial o completamente. Esto significa que usamos lo que genera la IA para mejorar las plataformas actuales. Además, la IA puede ayudar a inventar nuevos softwares y plataformas.

- Hay tres tipos de productos: productos de IA generativa, productos que usan APIs de productos de IA generativa y otros productos.

- Una idea de producto es usar IA para acumular información en tiempo real, noticias o actualizaciones de plataformas sociales como Reddit, GitHub Trending, Twitter Trending, Quora Trending y Zhihu Trending. Los usuarios pueden usar solicitudes para personalizar el feed o incluso agregar cuentas sociales específicas.

- Hay cinco tipos importantes de datos: texto, imagen, audio, video y código.

- Otros tipos importantes de datos incluyen numéricos, geoespaciales, biométricos, de sensores, transaccionales, metadatos, series de tiempo, estructurados, no estructurados, semiestructurados, de salud, ambientales, de registros, de red y de comportamiento.

- Google sigue siendo mejor para la indexación de sitios web, especialmente si quieres descargar software o un documento de un sitio específico. Funciona como una búsqueda por dominio. No lo usas para encontrar información, sino para navegar a otros sitios y realizar tareas. Un LLM puede no tener los enlaces de descarga más recientes.

- Google funciona como una búsqueda por dominio; si quieres ir a un sitio de repositorio Maven para verificar la versión más reciente, puedes usarlo.

- Google sigue siendo útil para búsqueda de imágenes, mientras que los LLM sobresalen en generación de texto. Aún así, la gente prefiere imágenes reales para verificar detalles de hardware, dimensiones, formas de objetos o la apariencia de una persona.

- Los chatbots de IA son populares porque el texto es más difícil de procesar que las imágenes. La gente prefiere imágenes reales sobre las generadas por IA, ya que las imágenes son más fáciles de entender de un vistazo. Sin embargo, la generación de imágenes con IA tiene potencial sin explotar: los usuarios podrían pedirle a la IA que muestre diferentes ángulos, haga zoom en caras o amplíe detalles de placas de circuitos. Como la gente trabaja principalmente con texto en lugar de imágenes, hay un gran margen de crecimiento en herramientas de imágenes con IA.

- La IA sobresale en explicar conceptos y facilitar la comprensión. Además, los usuarios pueden hacer preguntas sobre cualquier detalle específico. Esta es probablemente la utilidad más significativa de las herramientas de IA.

- Usé IA para aprender sobre modelos de lenguaje grande. El momento en que me ayudó a entender K, Q y V fue maravilloso.

- La razón por la que prefiero usar Ubuntu desde el lanzamiento de los LLM es que las aplicaciones ricas y coloridas de macOS me resultan menos atractivas. Prefiero escribir mis programas y hacer todo a través de la terminal y texto.

- La IA puede evaluarse por qué tan bien puede actualizar un archivo pom.xml o requirements.txt a la versión más reciente, actualizar bibliotecas y realizar verificaciones. Este proceso puede involucrar una cantidad significativa de trabajo y a veces puede ser complejo.

- En la era de la IA, los lenguajes de programación que tienen mejor rendimiento y robustez son más importantes y serán más populares, mientras que la sintaxis es menos importante. Esto se debe a que los LLM ayudarán a generar código, lo que lo hace menos engorroso siempre y cuando el programa se ejecute bien.

- La gente tiende a leer todo de los chatbots de IA porque es fácil de aprender, pueden hacer preguntas sobre cualquier aspecto, el formato es consistente y la calidad suele estar entre las mejores que se encuentran en Internet.

- Pero la información no es solo texto. Puedes leer la mayoría de la información textual de los chatbots de IA, pero pierdes el sitio web original, su diseño y formato, sus imágenes explicativas y diseño web.

- Los sitios web con mucha interacción es poco probable que sean cambiados significativamente por la IA, como juegos web, Google Docs, Google Sheets y herramientas de colaboración como Zoom o Slack. Son centrados en código y no solo en texto.

- Es fácil cometer errores tipográficos o requiere esfuerzo elaborar solicitudes para chatbots de IA. Por eso un banco digital completamente dirigido por IA, una app de trading digital o redes sociales con IA con un simple cuadro de chat a menudo no funcionan. Los botones tradicionales, navegación por páginas y diseños en aplicaciones móviles son más convenientes.

- [Cómo vivo bien en la era de la IA y blockchain](./ai-blockchain-en)


---

## Nuevas plataformas impulsadas por flujos de trabajo de IA

*08.01.2025*

- Los flujos de trabajo son sistemas donde los modelos de lenguaje grande (LLM) y herramientas se orquestan a través de rutas de código predefinidas.[^1]

- Imagina una nueva plataforma, como TikTok, Quora, X, Threads, Instagram, WhatsApp, Facebook, LinkedIn, Reddit o YouTube, completamente impulsada por traducción con IA.

- Cada publicación o respuesta creada por los usuarios puede guardarse en un solo idioma. La plataforma traducirá automáticamente el contenido a 20 idiomas, permitiendo a los usuarios verlo en su idioma preferido.

- Más allá de la traducción, otras funciones con IA, como resumen, generación de audio y generación de video, jugarán un papel clave. Esencialmente, el usuario envía el contexto de la solicitud, y la plataforma se encarga del resto.

- Los usuarios pueden subir texto, imágenes, audio o videos, y la plataforma convertirá automáticamente el contenido a otros formatos. Los usuarios pueden decidir cómo desean recibir ese contenido (por ejemplo, como texto, imágenes, audio o video).

- Las plataformas pueden generar resúmenes automáticamente, con diferentes tipos de resumen disponibles en múltiples idiomas.

- En cualquier texto, imagen, audio o video en la plataforma, la IA puede ayudar a generar, refinar, mejorar, corregir, resumir, expandir, convertir a otros formatos o imaginar nuevas formas del contenido.

- Los usuarios pueden personalizar la plataforma usando palabras clave como "inglés" o "divertido" para ajustar el estilo de los flujos de trabajo de IA en plataformas como TikTok. Una vez configurado, la IA adaptará el contenido en consecuencia.


---

[^1]: Construyendo agentes efectivos, [Anthropic](https://www.anthropic.com/research/building-effective-agents)

---

## La próxima dirección de los editores de código con IA

*08.01.2025*

Recientemente, estaba trabajando en agregar una tubería `xelatex` a GitHub Actions.

Encontré un problema con el paquete `fontawesome5` en el flujo de GitHub. La solución proporcionada por 4o-mini (instalar TeX Live 2021 y usar `tlmgr install fontawesome5`) no funcionó para mí. Sin embargo, 4o sugirió un mejor enfoque: actualizar a TeX Live 2023 y seguir usando `tlmgr` para instalar `fontawesome5`. Aunque esto no resolvió completamente el problema, cambiar a TeX Live 2023 mejoró significativamente la situación.

Usé ChatGPT para ayudar a resolver el problema. Para más detalles, consulta [Qué puede hacer ChatGPT O1 que 4o-mini no puede](./o1-en).

En este punto, no usé editores como Cursor o Windsurf, aunque los probé en otro proyecto. El problema con estos editores de código es que solo capturan la salida de pruebas locales, lo que limita su funcionalidad en entornos en la nube.

En flujos de trabajo como GitHub Actions, trabajos de Jenkins o cualquier flujo de implementación o prueba de código, los editores de código necesitan una mejor integración. Deben proporcionar interacción fluida con la nube y los procesos de CI/CD.

Esta integración también aplica a otras herramientas de creación de contenido, ya sea para texto, imágenes, audio o video. Estas herramientas deben integrarse con sistemas de pruebas A/B. Las herramientas de IA podrían generar contenido, y las herramientas de pruebas A/B podrían proporcionar retroalimentación. Esta dinámica es similar al Aprendizaje por Refuerzo con Retroalimentación Humana (RLHF), donde los modelos de IA mejoran con el tiempo basándose en retroalimentación del mundo real.

Este concepto de extender RLHF más allá de solo las salidas del modelo, hacia entornos de prueba e implementación en el mundo real, parece una dirección prometedora para mejorar tanto editores de código como herramientas de creación de contenido impulsadas por IA.

La prueba puede ser instantánea o prolongada, y puede ser automatizada o asistida por humanos. Si las pruebas son automatizadas, como pruebas A/B de usuario para una herramienta de IA, aún involucran retroalimentación humana, pero el proceso está automatizado. Por ejemplo, podemos hacer que la computadora verifique resultados diariamente o cada hora basándose en los resultados de pruebas A/B para mejorar el proceso de creación. De manera similar, para trabajos de Jenkins o GitHub Actions, podemos hacer que la computadora verifique después de que se completen sus tareas.

Si hay asistencia humana, la retroalimentación no puede ser completamente entendida por la máquina y a menudo es algo vaga. Por ejemplo, cuando las herramientas de IA crean contenido como imágenes o videos, los humanos podrían señalar que el contenido no es lo suficientemente divertido o que un detalle específico debería mejorarse. Las máquinas aún tienen un largo camino por recorrer para que todo sea perfecto, y si algo es "perfecto" a menudo es subjetivo, dependiendo del gusto individual. Es la retroalimentación humana lo que ayuda a mejorar las cosas.

En teoría, todas las reglas definidas por humanos pueden escribirse como solicitudes. Hay solicitudes de usuario y solicitudes del sistema. Deberíamos centrarnos en mejorar las solicitudes en lugar de corregir la salida cada vez.