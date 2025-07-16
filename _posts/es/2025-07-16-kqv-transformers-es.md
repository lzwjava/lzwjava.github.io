---
audio: false
generated: false
lang: es
layout: post
title: Cómo aprendí el mecanismo KQV en los transformers
translated: true
---

Después de leer [Mecanismo K, Q, V en Transformers](https://lzwjava.github.io/notes/2025-06-02-attention-kqv-en), de alguna manera entendí cómo funcionan K, Q y V.

Q significa Query, K significa Key y V significa Value. Para una oración, la Query es una matriz que almacena el valor de un token que necesita preguntar a otros tokens. La Key representa la descripción de los tokens, y el Value representa la matriz de significado real de los tokens.

Tienen formas específicas, por lo que es necesario conocer sus dimensiones y detalles.

Entendí esto alrededor de principios de junio de 2025. Lo aprendí por primera vez alrededor de finales de 2023. En ese momento, leí artículos como [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/), pero no entendí mucho.

Después de aproximadamente dos años, ahora me resulta más fácil de entender. Durante estos dos años, me centré en el trabajo de backend y en preparar mis exámenes de grado asociado, y no leí ni aprendí mucho sobre aprendizaje automático. Sin embargo, de vez en cuando reflexioné sobre estos conceptos mientras conducía o hacía otras cosas.

Esto me recuerda el efecto del tiempo. Podemos aprender muchas cosas a primera vista, incluso si no comprendemos mucho. Pero de alguna manera, esto desencadena un punto de partida para nuestro pensamiento.

Con el tiempo, descubrí que, para el conocimiento y el descubrimiento, es difícil pensar o entender las cosas la primera vez. Pero más tarde, parece más fácil aprender y saber.

Una razón es que en la era de la IA, es más fácil aprender porque puedes profundizar en cualquier detalle o aspecto para resolver tus dudas. También hay más videos relacionados con la IA disponibles. Más importante aún, ves que tantas personas están aprendiendo y construyendo proyectos sobre eso, como [llama.cpp](https://github.com/ggml-org/llama.cpp).

La historia de Georgi Gerganov es inspiradora. Como un nuevo aprendiz de aprendizaje automático que comenzó alrededor de 2021, tuvo un impacto poderoso en la comunidad de IA.

Este tipo de cosas volverá a suceder una y otra vez. Por lo tanto, para el aprendizaje por refuerzo y el conocimiento más reciente de IA, aunque aún no puedo dedicarles mucho tiempo, creo que puedo encontrar algo de tiempo para aprender rápidamente y tratar de pensar mucho en ellos. El cerebro hará su trabajo.