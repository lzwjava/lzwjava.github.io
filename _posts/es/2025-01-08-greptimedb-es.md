---
audio: false
generated: false
image: false
lang: es
layout: post
title: Las empresas deben proporcionar contexto de IA para facilitar la integración
translated: true
---

Tengo un amigo que trabaja en Greptime DB, y he estado pensando en cómo integrar rápidamente su producto en sistemas existentes.

## Contexto

Un enfoque potencial es proporcionar más contexto de IA. Greptime DB podría organizar su documentación de una manera compatible con herramientas de IA como ChatGPT, simplificando el proceso de integración.

Greptime DB ofrece documentación en [https://greptime.com](https://greptime.com), pero me pregunto si herramientas como ChatGPT o DeepSeek pueden procesar eficientemente todas las páginas de su documentación. Además, una gran cantidad de información está dispersa en repositorios de GitHub, problemas, documentos internos, documentos públicos y otros fragmentos de conocimiento oculto que no están explícitamente documentados.

Para abordar esto, Greptime DB podría necesitar crear varios GPT especializados. Por ejemplo, podrían crear prompts como este:

```

### Docs de Greptime:
La documentación oficial está disponible en: [https://docs.greptime.com](https://docs.greptime.com)

* [Guía de inicio rápido](https://docs.greptime.com/getting-started/quick-start)
* [Guía del usuario](https://docs.greptime.com/user-guide/overview)
* [Demostraciones](https://github.com/GreptimeTeam/demo-scene)
* [Preguntas frecuentes](https://docs.greptime.com/faq-and-others/faq)

### URLs de repositorios:
Aquí están los directorios y archivos clave desde la raíz del repositorio de GreptimeDB:

1. [benches](https://github.com/GreptimeTeam/greptimedb/tree/main/benches)
2. [docs](https://github.com/GreptimeTeam/greptimedb/tree/main/docs)
3. [src](https://github.com/GreptimeTeam/greptimedb/tree/main/src)
4. [test](https://github.com/GreptimeTeam/greptimedb/tree/main/test)
5. [third_party](https://github.com/GreptimeTeam/greptimedb/tree/main/third_party)
6. [tools](https://github.com/GreptimeTeam/greptimedb/tree/main/tools)

Archivos clave adicionales:

7. [Cargo.lock](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.lock)
8. [Cargo.toml](https://github.com/GreptimeTeam/greptimedb/tree/main/Cargo.toml)
9. [LICENSE](https://github.com/GreptimeTeam/greptimedb/tree/main/LICENSE)
10. [Makefile](https://github.com/GreptimeTeam/greptimedb/tree/main/Makefile)
11. [README.md](https://github.com/GreptimeTeam/greptimedb/tree/main/README.md)
12. [NOTICE](https://github.com/GreptimeTeam/greptimedb/tree/main/NOTICE)

Por favor, busca en estos recursos antes de responder a cualquier consulta del usuario.

```

Esto permitiría a los usuarios interactuar con un chatbot basado en GPT que responde preguntas basadas en la documentación, asegurando respuestas más precisas.

Vamos a crear este GPT: [https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration](https://chatgpt.com/g/g-677e87121d448191b0813ca28425ce38-greptimedb-integration)

No pude responder esta pregunta,

```
¿De qué trata `greptimedb/src/query/src/query_engine/context.rs`?
```

## Agente

Imagino una herramienta llamada `greptimedb-agent` para simplificar el proceso de integración.

Imagina ejecutar un comando simple como:

```bash
pip install greptimedb-agent
greptimedb-agent
```

`greptimedb-agent` recopilaría inteligentemente información sobre el sistema actual, como los detalles de la máquina y el código existente, para comprender el contexto y decidir cómo integrar mejor Greptime DB.

Este comando actualizaría automáticamente tu código para integrar Greptime DB, reemplazando sin problemas tu base de datos actual con Greptime DB en solo unos pocos pasos.