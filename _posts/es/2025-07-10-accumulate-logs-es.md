---
audio: false
generated: false
lang: es
layout: post
title: Beneficios de Acumular Registros
translated: true
---

Cuando trabajaba como contratista para un banco singapurense, usábamos Pivotal Cloud Foundry para servir los microservicios. En ese momento, comencé a acumular registros mientras trabajaba en la empresa.

Han pasado varios años, y aún creo que es una de las mejores formas de ayudarme a trabajar o hacer ingeniería de software. Con el tiempo, en mi directorio de registros, hay cientos de archivos de registro.

No tengo subdirectorios específicos ni nombres formales de archivos de registro para ellos. A veces, simplemente uso el nombre de la tarea de JIRA como prefijo del nombre del archivo de registro o esa característica. Luego, agrego un número al sufijo. Es como mutual-fund-1.log, mutual-fund-2.log, etc. Esto significa que en el microservicio de fondos mutuos, tengo ese registro al ejecutar ese microservicio.

A veces, al trabajar en proyectos que sirven a múltiples regiones, agregaré ese país como sufijo, como mutual-fund-cn-1.log, mutual-fund-sg-1.log.

Los nombres de los archivos de registro son algo casuales. Porque en ese momento, necesitaba enfocarme en las pilas de errores o las llamadas de funciones circundantes.

Los registros de los programas importan. Todos lo saben. Sin embargo, quiero exagerar la importancia de acumular registros en lugar de solo observarlos en la consola y dejarlos ir.

Sabrás más conveniencia cuando el proyecto esté en marcha. Tendrás más tiempo para encontrar los registros anteriores. Es posible que necesites saber si ocurrió una llamada previa a un procedimiento almacenado de base de datos similar. Es posible que necesites saber si ocurrió el mismo error antes. Es posible que necesites recordar cómo solucionar este problema la última vez.

Hay toneladas de detalles en un gran proyecto o en decenas de microservicios. Y los errores, excepciones o problemas ocurren una y otra vez.

El registro es como el documento de ejecución de un programa. Y son generados automáticamente por el programa sin escritura humana. Y para los desarrolladores, estos registros son legibles.

Por lo tanto, al comenzar una nueva tarea o solucionar un nuevo error, tienes cientos de registros en tus manos para solucionar este nuevo error. No estás solo.

¿Por qué los acumulamos? Porque las cosas o el conocimiento se olvidan fácilmente.

Hubo un progreso de la civilización humana cuando se inventó el papel. Y cuando se inventaron las computadoras, hubo otro nivel de civilización humana. Tomar notas en papel es como acumular registros en computadoras.

No solo para los humanos, sino también para los chatbots de IA, las herramientas de LLM, estos registros se están volviendo cada vez más importantes. GreptimeDB, una base de datos para la recolección y análisis unificados de datos de observabilidad (métricas, registros y trazas) establecida en 2022, no es una coincidencia.

¿Por qué no lo hice antes? Después de trabajar como contratista para grandes bancos, necesitaba hacer más colaboración y trabajar en proyectos más grandes. Antes de eso, la mayor parte del tiempo en la startup o mi período de startup, trabajé solo. Cuando trabajé en LeanCloud antes, trabajé en la aplicación de mensajería LeanChat durante aproximadamente la mitad del tiempo.

Y cuando entré en el mundo corporativo más formal, el desarrollo de los proyectos era diferente a mi proyecto personal o de startup. Tenían entornos de prueba SIT, UAT. Y el entorno de producción a menudo solo estaba abierto a ciertos compañeros de equipo pequeños. Obtener los registros de ellos y solucionar problemas se volvía largo y algo tedioso. Y ejecutar un proyecto lleva tiempo, y la tubería de Jenkins a menudo necesita media hora para ejecutarse.

Por lo tanto, no puedo ejecutar o probar el programa como una mosca. No puedo hacer un despliegue simplemente escribiendo un comando en mi computadora personal y subiendo el código al servidor para ejecutarlo.

Por lo tanto, de alguna manera me hace acumular registros para tener más contexto para manejar tareas. Es mejor solucionar problemas a la primera. Es mejor verificar nuestra solución en solo unas pocas veces. No podemos obtener fácilmente los registros del programa que se está ejecutando en una nube o en el servidor de la empresa, por lo que es mejor copiarlos y guardarlos en la computadora portátil local, para hacer el análisis.

Y ahora, para mis proyectos personales, también acumulo los registros. Se ha convertido en un hábito. Después de trabajar en grandes empresas durante algunos años, de alguna manera tengo más paciencia o estrategia para hacer que mis proyectos sean más grandes y duraderos. Por lo tanto, sé que necesitaré estos registros con el tiempo.

Alguien puede decir que solo necesitas tener un código elegante y un proyecto funcional. No necesitas acumular los registros o las pilas de errores. Está bien. Cuando tenemos un error o una nueva característica, podemos ejecutar el programa para obtener los registros actuales. No necesitamos los registros del proceso de desarrollo. Son como los registros detallados de experimentos científicos. A primera vista, parece estar bien. Pero a largo plazo, si un día quieres trabajar en ello nuevamente, o quieres compartirlo, o dejar que otros lo asuman, puede que no sea bueno.

Creo que aquí puede haber buenas oportunidades. En las empresas, ¿por qué no animamos a cada desarrollador a compartir sus registros acumulados? En los proyectos de código abierto, también deberíamos tener eso. No encontramos los registros de los demás atractivos porque no los conocemos. Perdemos el contexto al guardar esos registros. Y dentro de ellos, parecen haber toneladas de mensajes irrelevantes o triviales.

Pero el esfuerzo de acumular registros es trivial. Es solo copiar y pegar cada vez que vemos algunos registros, especialmente aquellos registros de error. ¿Y si lo hacemos de manera automatizada? Es una buena idea registrar los registros en un directorio cada vez que ejecutamos un proyecto, como aquellos proyectos Spring Boot.

El mundo se vuelve cada vez más digital, por lo que acumular registros de programas digitales es como acumular libros en el mundo físico.