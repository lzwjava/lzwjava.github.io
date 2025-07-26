---
audio: false
generated: false
image: true
lang: es
layout: post
title: Un ingeniero exigente sobre las herramientas de codificación de IA
translated: true
---

Recientemente, logré ejecutar con éxito Claude Code, por lo que quiero compartir mi viaje de selección de herramientas. También he recopilado algunos [consejos de herramientas de IA](ai-tips-en) en el camino.

Me uní tarde a adoptar Claude Code.

[Claude Code](https://www.anthropic.com/news/claude-3-5-sonnet) se lanzó alrededor del final de febrero de 2025.

No logré probarlo hasta hace poco. Una razón es que requiere la API de Anthropic, que no admite tarjetas de crédito Visa chinas.

Otra razón es que [Claude Code Router](https://github.com/musistudio/claude-code-router) se hizo disponible, lo que hizo que mi intento reciente fuera exitoso.

Sigo escuchando elogios sobre él. Probé el CLI de Gemini en julio de 2025, pero lo abandoné después de varios intentos fallidos para que arreglara mi código.

También probé Aider, otro agente de software. Dejé de usar Cursor después de aproximadamente seis meses porque muchos de sus complementos basados en VSCode no funcionaban correctamente. Experimenté brevemente con Cline, pero no lo adopté.

Utilizo el complemento Copilot en VSCode con un modelo personalizado, Grok 3 beta a través de OpenRouter, que funciona bien.

No creo que Claude Code cambie mis hábitos, pero como puedo ejecutarlo con éxito y tengo la paciencia de probarlo unas cuantas veces más, veré cómo me siento en las próximas semanas.

Soy un usuario exigente con 10 años de experiencia en ingeniería de software. Espero que las herramientas sean excelentes en uso real. No me dejo llevar por la marca, solo me importa la utilidad diaria.

Después de usar Claude Code para corregir la gramática de este post, he descubierto que funciona bien en ciertos escenarios. Aunque aprecio la IA para la asistencia gramatical (incluso escribí un script en Python para llamar a las APIs de LLM con este propósito), he notado un patrón frustrante: incluso cuando solicito correcciones mínimas, las herramientas siguen mostrando numerosas sugerencias gramaticales para revisión. Este proceso de verificación manual anula el propósito de la automatización. Como compromiso, ahora dejo que la IA maneje ensayos completos, aunque este enfoque limita mis oportunidades de aprendizaje, ya que no veo las correcciones específicas que se están realizando.

Lo que más me impresionó fue cómo Claude Code muestra los cambios: mostrando comparaciones antes y después similares a los diffs de git, lo que facilita mucho la revisión de las ediciones.

{: .centered }
![](assets/images/claude/claude-code.jpg){: .responsive }
*Fuente: Captura de pantalla propia*{: .caption }

{: .centered }
![](assets/images/claude/claude-fix.jpg){: .responsive }
*Fuente: Captura de pantalla propia*{: .caption }