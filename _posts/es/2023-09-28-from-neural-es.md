---
audio: false
generated: false
image: false
lang: es
layout: post
title: De la red neuronal a GPT
translated: true
---

### Videos de YouTube

Andrej Karpathy - Construyamos GPT: desde cero, en código, explicado paso a paso.

Umar Jamil - Attention is all you need (Transformer) - Explicación del modelo (incluyendo matemáticas), Inferencia y Entrenamiento

StatQuest con Josh Starmer - Redes Neuronales Transformer, la base de ChatGPT, ¡Explicado claramente!

Pascal Poupart - CS480/680 Clase 19: Mecanismos de Atención y Redes Transformer

The A.I. Hacker - Michael Phi - Guía Ilustrada de la Red Neuronal Transformer: Una explicación paso a paso

### Cómo aprendo

Después de haber leído la mitad del libro *"Neural Networks and Deep Learning"*, comencé a replicar el ejemplo de red neuronal para reconocer dígitos escritos a mano. Creé un repositorio en GitHub: [https://github.com/lzwjava/neural-networks-and-zhiwei-learning](https://github.com/lzwjava/neural-networks-and-zhiwei-learning).

Esa es la parte realmente difícil. Si alguien puede escribirlo desde cero sin copiar ningún código, es porque lo entiende muy bien.

Mi código replicado aún carece de la implementación de *update_mini_batch* y *backprop*. Sin embargo, al observar cuidadosamente las variables en las fases de carga de datos, propagación hacia adelante y evaluación, obtuve una comprensión mucho mejor de los vectores, la dimensionalidad, las matrices y la forma de los objetos.

Y comencé a aprender la implementación de GPT y el *transformer*. Mediante el *embedding* de palabras y la codificación posicional, el texto se convierte en números. Luego, en esencia, no hay diferencia con una red neuronal simple para reconocer dígitos escritos a mano.

La charla de Andrej Karpathy *"Let's build GPT"* es muy buena. Explica las cosas muy bien.

La primera razón es que realmente parte desde cero. Primero vemos cómo se genera el texto, que al principio es difuso y aleatorio. La segunda razón es que Andrej puede explicar las cosas de manera muy intuitiva. Andrej trabajó en el proyecto *nanoGPT* durante varios meses.

Acabo de tener una nueva idea para evaluar la calidad de una charla: ¿puede el autor escribir realmente estos códigos? ¿Por qué no entiendo algo y qué tema omite el autor? Más allá de los diagramas y animaciones elegantes, ¿cuáles son sus deficiencias y defectos?

Volviendo al tema del aprendizaje automático en sí, como menciona Andrej: el *dropout*, las conexiones residuales, la *Self-Attention*, la *Multi-Head Attention* y la *Masked Attention*.

Al ver más videos como los anteriores, comencé a entender un poco más.

Mediante la codificación posicional con funciones *seno* y *coseno*, obtenemos ciertos pesos. Con el *embedding* de palabras, convertimos las palabras en números.

$$
    PE_{(pos,2i)} = \sin(pos/10000^{2i/d_{model}}) \\
    PE_{(pos,2i+1)} = \cos(pos/10000^{2i/d_{model}})
$$

> *The pizza came out of the oven and it tasted good.*

En esta oración, ¿cómo sabe el algoritmo si se refiere a *pizza* u *horno*? ¿Cómo calculamos las similitudes para cada palabra en la oración?

Queremos un conjunto de pesos. Si usamos la red *transformer* para realizar la tarea de traducción, cada vez que ingresamos una oración, puede generar la oración correspondiente en otro idioma.

Sobre el producto punto aquí: una razón por la que lo usamos es porque considera todos los números en el vector. ¿Qué pasaría si usáramos el producto punto al cuadrado? Primero calcularíamos el cuadrado de los números y luego haríamos el producto punto. ¿Y si hiciéramos algún tipo de producto punto inverso?

Sobre el *masking* aquí: cambiamos los números de la mitad de la matriz a infinito negativo. Luego usamos *softmax* para que los valores estén entre 0 y 1. ¿Qué pasaría si cambiáramos los números de la parte inferior izquierda a infinito negativo?

### Plan

Seguir leyendo código, artículos y viendo videos. Solo divertirse y seguir mi curiosidad.

[https://github.com/karpathy/nanoGPT](https://github.com/karpathy/nanoGPT)

[https://github.com/jadore801120/attention-is-all-you-need-pytorch](https://github.com/jadore801120/attention-is-all-you-need-pytorch)