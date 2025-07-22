---
audio: false
generated: true
lang: es
layout: post
title: Arquitectura AI-First para el Desarrollo Moderno
translated: true
---

Este post fue escrito con la ayuda de Grok, pero las ideas son originales.

---

### Evaluación de tus puntos

Analizaré tus puntos individualmente, evaluándolos en función de las tendencias actuales en ingeniería de software, la integración de IA/LLM (por ejemplo, herramientas como GitHub Copilot, Cursor o agentes LLM personalizados) y las implicaciones prácticas. Estás tocando una idea crítica: a medida que la IA se vuelve integral en los flujos de trabajo de desarrollo, las arquitecturas deben priorizar la amigabilidad con la IA junto con diseños centrados en el ser humano. Sin embargo, no todas las ideas son universalmente aplicables: el contexto importa y un equilibrio entre simplicidad y escalabilidad es esencial. Esbozaré acuerdos, desacuerdos y matices clave.

#### 1. La arquitectura bancaria tradicional tiene méritos, pero prioriza la optimización de IA/LLM para nuevos proyectos: enfócate en la ingeniería de contexto, separación clara y diseño centrado en IA
Estás en lo cierto en teoría. Las arquitecturas tradicionales, como las del sector bancario (asumiendo una referencia a sistemas empresariales monolíticos o en capas), destacan en confiabilidad, seguridad y mantenibilidad humana. Sin embargo, con los agentes de IA/LLM impulsando la generación, depuración y refactorización de código, una mentalidad "centrada en IA" es cada vez más relevante. Esto implica diseñar para las limitaciones de los LLM, como ventanas de contexto limitadas (por ejemplo, 128k tokens en GPT-4o), modularizando el código para garantizar que los detalles críticos encajen dentro de esos límites.

- **Fortalezas**: La separación clara de preocupaciones (por ejemplo, flujos de datos distintos, prompts o límites de API) permite que la IA razone de manera más efectiva. Por ejemplo, herramientas de IA como LangChain o agentes personalizados prosperan con contextos bien definidos e aislados en lugar de lógica entrelazada.
- **Matices**: El diseño centrado en el ser humano sigue siendo vital: la IA aún requiere supervisión humana para dominios complejos como las finanzas, donde el cumplimiento normativo y la seguridad son fundamentales. Un modelo híbrido puede ser óptimo: optimizado para IA en tareas repetitivas, optimizado para humanos en lógica crítica.
- **En general**: Estoy de acuerdo en gran medida; esta tendencia es evidente en los microservicios y arquitecturas serverless impulsados por IA.

#### 2. Spring ofrece abstracciones robustas, pero plantea desafíos para la comprensión de IA/LLM
Tienes razón aquí. Spring (y marcos de Java similares como Micronaut) es ideal para entornos empresariales con características como inyección de dependencias, AOP y abstracciones en capas (por ejemplo, controladores -> servicios -> repositorios). Excelente para equipos grandes gestionados por humanos, estos pueden abrumar a los LLM debido a la indirección y el código de plantilla.

- **Fortalezas**: Los LLM a menudo tienen dificultades con pilas de llamadas profundas o comportamientos implícitos (por ejemplo, anotaciones @Autowired), lo que resulta en alucinaciones o análisis incompletos. La investigación sobre generación de código de IA indica tasas de error más altas en bases de código excesivamente abstractas.
- **Matices**: No todas las abstracciones son perjudiciales: las interfaces, por ejemplo, mejoran la capacidad de prueba, lo que ayuda indirectamente a la IA en tareas como la generación de mocks. Sin embargo, el exceso de capas infla el contexto, complicando el rastreo de la lógica para los LLM.
- **En general**: Estoy totalmente de acuerdo; hay un cambio hacia marcos más ligeros (por ejemplo, Quarkus) o enfoques sin marco para mejorar la compatibilidad con la IA.

#### 3. Favorece estructuras más planas, similares a organizaciones planas: limita a 2 niveles, donde el primer nivel llama al segundo, evitando pilas profundas con 50 niveles
Esta es una idea convincente para la simplicidad, aunque no universalmente ideal. Las estructuras más planas (por ejemplo, un orquestador de nivel superior que invoca múltiples funciones pequeñas) reducen el anidamiento, ayudando a los LLM a evitar errores de razonamiento en pilas de llamadas complejas. Esto refleja el encadenamiento de funciones directo que a menudo se ve en scripts de Python.

- **Fortalezas**: El código más plano reduce la carga cognitiva para la IA: los LLM rinden mejor con razonamiento lineal o paralelo que con recursión profunda. La analogía de la "organización plana" se mantiene: como las startups, el código plano es más adaptable para modificaciones de IA.
- **Matices**: Invocar numerosas funciones desde un solo punto puede generar "código espagueti" sin una organización disciplinada (por ejemplo, nombres claros o modularización). En sistemas más grandes, una jerarquía mínima (3-4 niveles) evita el caos. Si bien los agentes de IA como Devin manejan bien las estructuras planas, pueden surgir problemas de rendimiento sin una orquestación adecuada.
- **En general**: Estoy parcialmente de acuerdo; el aplanamiento es beneficioso donde sea factible, pero la escalabilidad debe probarse. Esto se alinea con las tendencias de programación funcional en el desarrollo impulsado por IA.

#### 4. Las IA/LLM tienen dificultades con estructuras anidadas complejas, destacan en funciones pequeñas (100-200 líneas); el sistema de llamadas e importaciones de Python apoya esto
Tienes toda la razón en cuanto a las capacidades de los LLM. Los modelos actuales (por ejemplo, Claude 3.5, GPT-4) destacan en tareas enfocadas y contenidas, pero fallan con la complejidad: las tasas de error aumentan más allá de ~500 líneas de contexto debido a los límites de tokens y la dispersión de atención.

- **Fortalezas**: Las funciones pequeñas (100-200 líneas) son óptimas para la IA: fáciles de solicitar, generar o refactorizar. El sistema de importaciones de Python (por ejemplo, `from module import func`) promueve la modularidad, haciéndolo más amigable para la IA que la estructura centrada en clases de Java.
- **Matices**: Si bien los LLM están avanzando (por ejemplo, con el encadenamiento de pensamiento), la lógica anidada sigue siendo un desafío. La flexibilidad de Python ayuda, pero la tipificación estática (por ejemplo, TypeScript) también puede ayudar a la IA proporcionando pistas explícitas.
- **En general**: Estoy totalmente de acuerdo; esto explica por qué los ecosistemas de ML/IA (por ejemplo, las bibliotecas de Hugging Face) a menudo adoptan el estilo modular de Python.

#### 5. Divide los archivos grandes de Java en archivos más pequeños con más funciones para facilitar las pruebas/verificación; los proyectos de Java deberían emular la estructura de Python
Esta es una dirección práctica. Las clases de Java grandes y monolíticas (por ejemplo, 1000+ líneas) son difíciles tanto para humanos como para la IA, mientras que dividirlas en archivos/funciones más pequeños mejora la granularidad.

- **Fortalezas**: Las unidades más pequeñas simplifican las pruebas unitarias (por ejemplo, con JUnit) y la verificación (la IA puede centrarse en una función a la vez), reflejando el enfoque de módulo por característica de Python. Las herramientas de construcción como Maven/Gradle lo acomodan sin problemas.
- **Matices**: El sistema de paquetes de Java ya lo soporta, pero se necesita un cambio cultural desde los monolitos de POO. No todos los proyectos de Java deberían imitar a Python: las aplicaciones críticas para el rendimiento pueden beneficiarse de cierta consolidación.
- **En general**: Estoy de acuerdo; el Java moderno (por ejemplo, con registros y clases selladas en Java 21) se está moviendo en esta dirección.

#### 6. La programación procedimental puede superar a la POO en la era de IA/LLM
Esta es una perspectiva audaz pero válida en el contexto. Los enfoques procedimentales (o funcionales), con su énfasis en flujos sencillos y funciones puras, se alinean con las fortalezas de los LLM: generar código lineal es más sencillo que manejar el estado, la herencia y el polimorfismo de la POO.

- **Fortalezas**: Las abstracciones de POO como la herencia profunda a menudo confunden a los LLM, lo que lleva a errores en el código generado. El código procedimental es más predecible y se adapta mejor a la naturaleza de coincidencia de patrones de la IA. Lenguajes como Rust (con rasgos procedimentales) y Go (enfatizando la simplicidad) reflejan esta tendencia.
- **Matices**: La POO no está obsoleta: es efectiva para modelar dominios complejos (por ejemplo, entidades financieras). Un enfoque híbrido (núcleo procedimental con envoltorios de POO) podría ser ideal. Con prompts personalizados, los LLM pueden manejar la POO, aunque lo procedimental reduce la fricción.
- **En general**: Estoy parcialmente de acuerdo; los estilos procedimentales/funcionales están ganando terreno en los flujos de trabajo de IA, pero la POO conserva valor para la mantenibilidad a largo plazo en sistemas grandes.

#### 7. Los IDE como VSCode o IntelliJ IDEA deberían ofrecer atajos para la edición de funciones/métodos asistida por IA
Tienes razón en que esto agilizaría los flujos de trabajo. Si bien los IDE actuales ofrecen un soporte parcial (por ejemplo, "Ir a la definición" de VSCode o las sugerencias en línea de Copilot), los atajos de edición asistida por IA están convirtiéndose en algo más común.

- **Fortalezas**: Seleccionar una función/método y solicitar a la IA (por ejemplo, "refactorizar esto") mejoraría la eficiencia. Herramientas como Cursor (construida sobre VSCode) ya permiten ediciones de IA específicas de región.
- **Matices**: IntelliJ IDEA ofrece "Extraer método" y asistentes de IA (a través de JetBrains AI), mientras que las extensiones de VSCode como GitHub Copilot Chat admiten consultas basadas en selección. Sin embargo, un atajo nativo "editar esta función con IA" sería una valiosa adición, probablemente en futuras actualizaciones.
- **En general**: Estoy de acuerdo; esto se alinea con la creciente tendencia de herramientas centradas en IA.

### Resumen
Tus ideas son en su mayoría precisas: adoptar arquitecturas optimizadas para IA (planas, modulares, unidades pequeñas) aborda las limitaciones reales de los LLM y puede acelerar el desarrollo. Sin embargo, extremos como diseños completamente procedimentales o demasiado planos pueden comprometer la mantenibilidad a largo plazo: el equilibrio es crucial. En dominios como las finanzas, la seguridad y el cumplimiento pueden requerir ciertas abstracciones. Tu perspectiva se alinea con las mejores prácticas emergentes en la codificación asistida por IA, donde la simplicidad beneficia tanto a humanos como a máquinas.

Si tienes ejemplos de código específicos o quieres explorar un rediseño centrado en IA, ¡no dudes en preguntar!