---
audio: false
generated: false
image: false
lang: es
layout: post
title: Optimización de costos de traducción con Markdown basado en párrafos
translated: true
---

Mi blog de Jekyll usa Markdown para escribir párrafos. Después de escribir en inglés, uso herramientas de IA como DeepSeek o Mistral para traducir a otros ocho idiomas. Aunque ya son económicas, aún hay margen de mejora.

A veces, solo edito una palabra o un párrafo, y luego todo el texto de una publicación se traduce a los otros ocho idiomas. En este caso, el uso de tokens es alto. Si solo traduzco un párrafo de nuevo, el uso de tokens será menor, especialmente para publicaciones largas.

Sin embargo, aún quiero usar Markdown para registrar mis ideas. Usar una base de datos para mantener y actualizar las publicaciones no es conveniente. Usar YAML o JSON podría ser demasiado engorroso también.

La clave es identificar las diferencias entre el texto antes y después de la edición. Si usamos un enfoque basado en párrafos, significa usar el carácter de nueva línea "\n" para dividir el texto.

Necesito saber qué párrafos han cambiado y cuáles no después de la edición. Necesitamos conocer los mapeos uno a uno de los párrafos entre el texto antes y después de la edición.

Usamos un enfoque basado en párrafos porque queremos actualizar las traducciones realizadas por los modelos de IA. Si usamos oraciones, podría no ser tan preciso.

Para Markdown, podría ser más importante usar el análisis de Markdown para sincronizar las traducciones basadas en elementos de Markdown.

Pero si no hay bloques de código ni sintaxis especial de Markdown, podemos usar un enfoque basado en párrafos.

Para un enfoque simple basado en párrafos, tenemos dos arreglos de párrafos y necesitamos saber cómo coinciden.

Al comparar cualquier párrafo en estos dos arreglos, hay dos resultados posibles: son iguales o diferentes. Si son diferentes, hay varios casos: ambos son recién añadidos, el de la izquierda es recién añadido o el de la derecha es recién añadido.

Solo quiero ahorrar costos, por lo que quiero reducir el uso de tokens. No necesito nada más. Solo necesito traducir cada párrafo, almacenar el resultado en caché y la próxima vez, para cada párrafo, primero buscaré el resultado de la traducción. Si no existe, entonces necesitaré traducirlo de nuevo.

Para Markdown, es un poco más complicado. No quiero traducir bloques de código. Por lo tanto, podemos usar primero una biblioteca de análisis de Markdown para tratar los bloques de código y el texto normal de manera diferente.