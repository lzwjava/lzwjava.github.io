---
audio: false
generated: false
image: false
lang: es
layout: post
title: Flujos de trabajo de IA, editores de código y disrupción de plataformas
translated: true
---

### Tabla de Contenidos

1. [Pensamientos sobre IA](#pensamientos-sobre-ia)
   - La IA carece de inteligencia o profundidad real
   - El aprendizaje automático es cálculo aplicado avanzado
   - Los LLM tienen dificultades con formatos de archivo estructurados
   - El código abierto elimina el secreto tecnológico
   - Las herramientas basadas en texto son las primeras en ser disruptivas por la IA

2. [Nuevas Plataformas Impulsadas por Flujos de Trabajo de IA](#nuevas-plataformas-impulsadas-por-flujos-de-trabajo-de-ia)
   - Los flujos de trabajo de IA automatizan la generación de contenido multilingüe
   - Los usuarios envían indicaciones para conversión de formatos
   - Las plataformas permiten refinamiento y resumen de contenido
   - Flujos de trabajo de IA personalizables mediante configuraciones por palabras clave
   - La IA maneja la transformación de contenido de principio a fin

3. [La Próxima Dirección de los Editores de Código con IA](#la-próxima-dirección-de-los-editores-de-código-con-ia)
   - La integración en la nube es crucial para flujos de CI/CD
   - Las pruebas A/B mejoran el contenido generado por IA
   - El RLHF se extiende a la retroalimentación en entornos reales
   - La retroalimentación humana refina los resultados imperfectos de la IA
   - La optimización de indicaciones supera la corrección de resultados


## Pensamientos sobre IA

*Última actualización en agosto de 2025*

- Satya Nadella mencionó la paradoja de Jevons. Vale la pena estudiarla.

- Yin Wang: No hay "inteligencia" en la inteligencia artificial, no hay "neural" en red neuronal, no hay "aprendizaje" en aprendizaje automático y no hay "profundidad" en aprendizaje profundo. Lo que realmente funciona en este campo se llama "cálculo". Por eso prefiero llamar a este campo "computación diferenciable", y el proceso de construir modelos se llama "programación diferenciable".

- Yin Wang: El aprendizaje automático es una teoría realmente útil, incluso podría decirse que hermosa, porque ¡es simplemente cálculo con un nuevo look! Es la antigua y gran teoría de Newton y Leibniz, pero en una forma más simple, elegante y poderosa. El aprendizaje automático básicamente consiste en usar cálculo para derivar y ajustar algunas funciones, y el aprendizaje profundo es el ajuste de funciones más complejas.

- Actualmente, los modelos de lenguaje grandes no pueden filtrar por lenguajes de archivo como YAML o Python. Sin embargo, una parte importante de la información en el mundo real está organizada de esta manera. Esto significa que podríamos entrenar modelos de lenguaje grandes utilizando archivos.

- Para entrenar modelos de lenguaje grandes, podríamos desarrollar un sistema que encuentre coincidencias exactas. Tal vez podríamos combinar el algoritmo de búsqueda KMP (Knuth-Morris-Pratt) con la arquitectura transformer para mejorar las capacidades de búsqueda.

- No hay secretos tecnológicos. El código abierto revelará todos los secretos guardados.

- La IA afectará muchas herramientas, incluidas las indirectas. La gente dice que no necesitarán Figma para dibujar prototipos, sino que irán directamente al código. Creo que Postman será similar; la gente usará directamente Python u otros scripts para llamar o probar APIs.

- Una razón por la que no usaremos Postman o Figma en la era de la IA es que sus funcionalidades no pueden generarse a través de texto. Tampoco tienen un atajo como command + K para activar el reemplazo de componentes.

- Las interfaces de usuario se están convirtiendo en una barrera en la era de la IA. ¿Por qué actualizar Postman para que funcione con IA si podemos usar directamente la biblioteca requests de Python u otros lenguajes para probar código, ya que estos estarán potenciados por IA?

- ¿Por qué actualizar Figma para que funcione con IA si la generación de UI basada en código, potenciada por IA, ofrece un enfoque más directo y potente?

- Los LLM cambiarán primero las aplicaciones relacionadas con texto, como Google, motores de búsqueda, editores y herramientas de escritura, Quizlet, Zendesk, DeepL, Medium, WordPress, Trello, Asana, Gmail, GitHub, Goodreads, Duolingo y Feedly.

- Por el contrario, es poco probable que los LLM revolucionen tecnologías como Git, Linux, ffmpeg, móviles, hardware, navegadores, sistemas operativos o llamadas de voz y video. Estas tecnologías están centradas en código, y su código no es fácilmente generado por IA, a diferencia de herramientas de prueba de APIs como Postman.

- Tecnologías con más código son difíciles de revolucionar por la IA, como OpenOffice, MySQL, Mozilla Firefox, Chromium, VLC Media Player, Qt Framework, LLVM/Clang y GNOME. Si la IA pudiera ayudar a construir estas tecnologías, no serían reemplazadas. La IA debería ayudar a crear mejores tecnologías, y para ello, necesitará más poder de computación para generar la misma magnitud de código.

- Hay dos formas en que los LLM pueden generar cambios: primero, alterando el contenido o los datos dentro de una plataforma o software, como la traducción de contenido en apps como TikTok; segundo, reemplazando directamente ciertos softwares o plataformas, como Postman o Google Search, incluyendo Google Translate.

- Hay dos formas en que las herramientas de audio con IA pueden generar cambios: primero, alterando el contenido o datos dentro de una plataforma, como generar audiolibros para Audible; segundo, reemplazando directamente ciertas aplicaciones, como apps de canto, ya que la IA ahora puede hacer lo mismo que los humanos, facilitando que la gente cante como hobby.

- Hay varias formas de medir cómo la IA impacta el software actual. Una es medir cuántos datos o contenido pueden ser generados o mejorados por IA, parcial o completamente. Otra es medir cuánto código puede ser escrito o mejorado por IA. También puede ayudar a inventar nuevos softwares y plataformas.

- Hay tres tipos de productos: productos de IA generativa, productos que usan APIs de IA generativa, y otros productos.

- Una idea de producto es usar IA para acumular información en tiempo real, noticias o actualizaciones de plataformas como Reddit, GitHub Trending, Twitter Trending, Quora Trending y Zhihu Trending. Los usuarios pueden personalizar su feed con indicaciones o incluso agregar cuentas específicas.

- Hay cinco tipos de datos importantes: texto, imagen, audio, video y código.

- Otros tipos incluyen numéricos, geoespaciales, biométricos, de sensores, transaccionales, metadatos, series temporales, estructurados, no estructurados, semiestructurados, de salud, ambientales, logs, de red y de comportamiento.

- Google sigue siendo mejor para indexar sitios, especialmente si quieres descargar software o documentos de un sitio específico. Funciona como una búsqueda por dominio. No lo usas para encontrar información, sino para navegar a otros sitios y realizar tareas. Un LLM puede no tener los enlaces de descarga más recientes.

- Google funciona como una búsqueda por dominio; si quieres ir a un repositorio Maven para ver la última versión, puedes usarlo.

- Google sigue siendo útil para búsqueda de imágenes, mientras que los LLM sobresalen en generación de texto. Pero la gente prefiere imágenes reales para verificar detalles de hardware, dimensiones, formas de objetos o la apariencia de una persona.

- Los chatbots de IA son populares porque el texto es más difícil de procesar que las imágenes. La gente prefiere imágenes reales a las generadas por IA, ya que son más fáciles de entender de un vistazo. Sin embargo, la generación de imágenes con IA tiene potencial sin explotar: los usuarios podrían pedirle a la IA que muestre diferentes ángulos, enfoque en rostros o detalles de placas de circuitos. Como la gente trabaja más con texto que con imágenes, hay mucho margen de crecimiento en herramientas de imagen IA.

- La IA es excelente para explicar conceptos y facilitar el entendimiento. Además, los usuarios pueden hacer preguntas sobre cualquier detalle. Probablemente sea la mayor utilidad de las herramientas de IA.

- Usé IA para aprender sobre modelos de lenguaje grandes. El momento en que me ayudó a entender K, Q y V fue maravilloso.

- La razón por la que prefiero usar Ubuntu desde el lanzamiento de los LLM es que las apps coloridas de macOS me resultan menos atractivas. Prefiero escribir mis programas y hacer todo mediante terminal y texto.

- La IA puede evaluarse por su capacidad para actualizar un archivo pom.xml o requirements.txt a la última versión, actualizar librerías y realizar verificaciones. Este proceso puede ser laborioso y en ocasiones complejo.

- En la era de la IA, los lenguajes con mejor rendimiento y robustez son más importantes y populares, mientras que la sintaxis es menos relevante. Esto se debe a que los LLM ayudarán a generar código, haciendo que sea menos problemático siempre que el programa se ejecute bien.

- La gente tiende a leer todo de los chatbots de IA porque es fácil de aprender, pueden preguntar sobre cualquier aspecto, el formato es consistente y la calidad suele ser de las mejores en Internet.

- Pero la información no es solo texto. Puedes leer la mayoría de la información textual de los chatbots, pero pierdes el sitio original y su diseño, imágenes explicativas y estructura.

- Los sitios con mucha interacción no serán cambiados significativamente por la IA, como juegos web, Google Docs, Google Sheets y herramientas de colaboración como Zoom o Slack. Están centrados en código y no solo en texto.

- Es fácil cometer errores tipográficos o requiere esfuerzo elaborar indicaciones para los chatbots de IA. Por eso, un banco digital o app de trading impulsado completamente por IA, o una red social con una simple caja de chat, a menudo no funcionan. Los botones tradicionales, navegación por páginas y diseños en apps móviles son más convenientes.

- [Cómo vivo bien en la era de la IA y blockchain](./ai-blockchain-en)


---

## Nuevas Plataformas Impulsadas por Flujos de Trabajo de IA

*08.01.2025*

- Los flujos de trabajo son sistemas donde los modelos de lenguaje grandes (LLM) y herramientas se orquestan mediante rutas de código predefinidas.[^1]

- Imagina una nueva plataforma, como TikTok, Quora, X, Threads, Instagram, WhatsApp, Facebook, LinkedIn, Reddit o YouTube, completamente impulsada por traducción de IA.

- Cada publicación o respuesta creada por los usuarios se guarda en un solo idioma. La plataforma traducirá automáticamente el contenido a 20 idiomas, permitiendo a los usuarios verlo en su idioma preferido.

- Además de la traducción, otras funciones impulsadas por IA, como resumen, generación de audio y video, jugarán un papel clave. Básicamente, el usuario envía el contexto de la indicación, y la plataforma se encarga del resto.

- Los usuarios pueden subir texto, imágenes, audio o videos, y la plataforma los convertirá automáticamente a otros formatos. Los usuarios pueden decidir cómo recibir ese contenido (por ejemplo, como texto, imágenes, audio o video).

- Las plataformas pueden generar automáticamente resúmenes, con diferentes tipos disponibles en múltiples idiomas.

- En cualquier texto, imagen, audio o video de la plataforma, la IA puede ayudar a generar, refinar, mejorar, corregir, resumir, expandir, convertir a otros formatos o imaginar nuevas formas del contenido.

- Los usuarios pueden personalizar la plataforma con palabras clave como "inglés" o "divertido" para ajustar el estilo de los flujos de trabajo de IA en plataformas como TikTok. Una vez configurado, la IA adaptará el contenido según corresponda.


---

[^1]: Construyendo Agentes Efectivos, [Anthropic](https://www.anthropic.com/research/building-effective-agents)

---

## La Próxima Dirección de los Editores de Código con IA

*08.01.2025*

Recientemente, estaba trabajando en agregar una pipeline de `xelatex` a GitHub Actions.

Encontré un problema con el paquete `fontawesome5` en el flujo de GitHub. La solución de 4o-mini (instalar TeX Live 2021 y usar `tlmgr install fontawesome5`) no funcionó para mí. Sin embargo, 4o sugirió una mejor opción: actualizar a TeX Live 2023 y aún así usar `tlmgr` para instalar `fontawesome5`. Aunque esto no resolvió el problema por completo, el cambio a TeX Live 2023 mejoró significativamente la situación.

Usé ChatGPT para ayudar a resolver el problema. Para más detalles, revisa [Lo que ChatGPT O1 puede hacer que 4o-mini no](./o1-en).

En este punto, no usé editores como Cursor o Windsurf, aunque los probé en otro proyecto. El problema con estos editores es que solo capturan la salida local de pruebas, lo que limita su funcionalidad en entornos en la nube.

En flujos como GitHub Actions, trabajos de Jenkins o cualquier despliegue de código o flujo de pruebas, los editores deben integrarse mejor. Deben ofrecer interacción fluida con la nube y procesos de CI/CD.

Esta integración también aplica a herramientas de creación de contenido—ya sea texto, imágenes, audio o video. Estas herramientas deberían integrarse con sistemas de pruebas A/B. Las herramientas de IA podrían generar contenido, y las pruebas A/B podrían dar retroalimentación. Esta dinámica es similar al Aprendizaje por Refuerzo con Retroalimentación Humana (RLHF), donde los modelos mejoran con el tiempo basados en retroalimentación del mundo real.

Extender el RLHF más allá de solo salidas de modelo—a entornos de prueba y despliegue real—parece una dirección prometedora para editores de código y herramientas de creación basadas en IA.

Las pruebas pueden ser instantáneas o largas, y automatizadas o asistidas por humanos. Si son automatizadas, como pruebas A/B para una herramienta de IA, aún involucran retroalimentación humana, pero el proceso es automatizado. Por ejemplo, podemos hacer que la computadora revise resultados diariamente o cada hora basándose en pruebas A/B para mejorar el proceso de creación. Igualmente, en trabajos de Jenkins o GitHub Actions, podemos hacer que la computadora revise tras completarse las tareas.

Si se requiere asistencia humana, la retroalimentación no es completamente entendida por la máquina y a veces es algo vaga. Por ejemplo, cuando herramientas de IA crean imágenes o videos, los humanos pueden señalar que el contenido no es lo suficientemente divertido o que un detalle debe mejorarse. Las máquinas aún tienen camino por recorrer para lograr la perfección, y lo que es "perfecto" a menudo es subjetivo, dependiendo del gusto individual. Es la retroalimentación humana la que ayuda a mejorar.

En teoría, todas las reglas definidas por humanos pueden escribirse como indicaciones. Hay indicaciones de usuario y del sistema. Deberíamos enfocarnos en mejorar las indicaciones en lugar de corregir cada salida.