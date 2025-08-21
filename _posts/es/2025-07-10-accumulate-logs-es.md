---
audio: false
generated: false
image: false
lang: es
layout: post
title: Beneficios de acumular registros
translated: true
---

## Beneficios de Acumular Registros

Cuando trabajaba como contratista para un banco, utilizábamos una plataforma de aplicaciones multi-nube para servir a los microservicios. En ese momento, empecé a acumular registros al trabajar en la empresa.

Han pasado varios años, y sigo pensando que es una de las mejores maneras de ayudarme a trabajar o a hacer ingeniería de software. A medida que pasa el tiempo, en mi directorio de registros, hay cientos de archivos de registro.

No tengo subdirectorios específicos ni nombres de archivos de registro formales para ellos. A veces, simplemente uso el nombre de esa tarea de JIRA como prefijo de mi nombre de archivo de registro o de esa característica. Y luego le añado un número al sufijo. Es como mutual-fund-1.log, mutual-fund-2.log, etc. Significa que en el microservicio de fondos mutuos, tengo ese registro cuando ejecuto ese microservicio.

A veces, cuando trabajo en proyectos que sirven a múltiples regiones, añadiré ese país como sufijo, como mutual-fund-cn-1.log, mutual-fund-sg-1.log. Los nombres de los archivos de registro son de alguna manera informales. Porque en ese momento, necesitaba centrarme en las pilas de errores o en la llamada a la función circundante.

Los registros de los programas importan. Todo el mundo lo sabe. Sin embargo, quiero exagerar la importancia de acumular registros en lugar de simplemente verlos en la consola y dejarlos ir. Conocerás más comodidad a medida que el proyecto avance. Tendrás más tiempo para encontrar los registros anteriores. Es posible que necesites saber si antes se produjo una llamada a un procedimiento almacenado de la base de datos similar. Es posible que necesites saber si el mismo error ocurrió antes. Es posible que necesites recordar cómo solucionar este problema la última vez.

Hay toneladas de detalles en un proyecto grande o en decenas de microservicios. Y los errores, excepciones o problemas se repiten una y otra vez. El registro es como el documento en ejecución de un programa. Y son generados por el programa automáticamente sin intervención humana. Y para los desarrolladores, estos registros son legibles. Así que al empezar una nueva tarea o arreglar un nuevo error, tienes cientos de registros en tus manos para arreglar este nuevo error. No estás solo.

¿Por qué los acumulamos? Porque las cosas o el conocimiento se olvidan fácilmente.

Hubo un progreso de la civilización humana cuando se inventó el papel. Y cuando se inventaron las computadoras, hubo otro nivel de civilización humana. Guardar notas en papel es como acumular registros en las computadoras.

No solo para los humanos, sino para los chatbots de IA, las herramientas de LLM, estos registros son cada vez más importantes. GreptimeDB, una base de datos para la recopilación y el análisis unificado de datos de observabilidad (métricas, registros y trazas) establecida en 2022, no es una coincidencia.

¿Por qué no hice eso antes? Después de trabajar como contratista para grandes bancos, necesitaba colaborar más y trabajar en proyectos más grandes. Antes de eso, la mayor parte del tiempo en la startup o en mi período de startup, trabajaba solo. Cuando trabajaba en LeanCloud antes, trabajé en la aplicación de mensajería instantánea LeanChat durante aproximadamente la mitad del tiempo.

Y cuando entré en el mundo corporativo más formal, el desarrollo de los proyectos era diferente de mi proyecto personal o proyecto de startup. Tenían entornos de prueba SIT, UAT. Y el entorno de producción a menudo solo está abierto a ciertos compañeros de equipo pequeños. Obtener los registros de ellos y solucionar problemas se vuelve largo y algo tedioso. Y ejecutar un proyecto lleva tiempo, y la tubería de Jenkins a menudo necesita media hora para ejecutarse.

Así que no puedo ejecutar o probar el programa como una mosca. No puedo hacer un despliegue simplemente escribiendo un comando en mi computadora personal y subiendo código al servidor para que se ejecute.

Así que de alguna manera me permite acumular registros para tener más contexto para manejar tareas. Mejor solucionamos los problemas al primer intento. Mejor verificamos nuestra solución en solo unas pocas veces. No podemos obtener fácilmente los registros del programa que se está ejecutando en la nube o en el servidor de la empresa, así que es mejor copiarlo y guardarlo en el portátil local, para hacer análisis.

Y ahora, para mis proyectos personales, también acumularé los registros. Se convierte en un hábito. Después de trabajar en grandes empresas durante algunos años, de alguna manera tengo más paciencia o estrategia para hacer mis proyectos más grandes y más largos. Así que sé que necesito estos registros a medida que pasa el tiempo.

Alguien podría decir que solo necesitas tener código elegante y un proyecto que funcione. No necesitas acumular los registros o las trazas de pila de errores. No pasa nada. Cuando tenemos un error o una nueva característica, podemos ejecutar el programa para obtener los registros actuales. No necesitamos los registros del proceso de desarrollo. Son como los registros detallados de los experimentos científicos. A primera vista, parece que está bien. Pero a largo plazo, si un día quieres volver a trabajar en ello, o quieres compartirlo, o dejar que otros se hagan cargo, puede que no sea bueno.

Creo que podría haber buenas oportunidades aquí. En las empresas, ¿por qué no animamos a cada desarrollador a compartir sus registros acumulados? En los proyectos de código abierto, también deberíamos tener eso. No encontramos atractivos los registros de otros porque no los conocemos. Perdemos el contexto al guardar esos registros. Y dentro de ellos, parece haber toneladas de mensajes irrelevantes o triviales.

Pero el esfuerzo de acumular registros es trivial. Es solo copiar y pegar cada vez que vemos algunos registros, especialmente los registros de errores. ¿Y qué tal si lo hacemos de forma automatizada? Es una buena idea registrar los registros en un directorio cada vez que ejecutamos un proyecto, como esos proyectos de Spring Boot.

El mundo se vuelve cada vez más digital, por lo que acumular registros de programas digitales es como acumular libros en un mundo físico.