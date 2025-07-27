---
audio: false
lang: en
layout: post
title: Software Engineering Optimized For AI
translated: false
generated: false
image: false
---

In this blog, I utilized hundreds of scripts to assist with translation, playground, frontmatter maintenance, and Telegram bots. I believe this development approach might represent the future of software engineering optimized for AI.

I don't rely much on Python module functionality, nor do I want to structure code like a large Java Spring project.

I told my previous team lead that while their banking architecture is impressive, if we were to start today, I would consider optimizing for LLM/AI. This would involve better context engineering, improved separation of contexts, and prioritizing AI-first thinking over human-centric design. While Spring offers multiple levels and good abstraction, it can be challenging for LLM/AI to navigate.

I believe we should aim for flatter structures, similar to a flat organization. This means using just two levels: the first level calls the second level. In a function, it's better to call another 50 functions directly rather than having 50 nested levels or stacks. AI/LLM struggle to judge or infer overly complex, nested structures, but they excel at handling smaller functions of 100 to 200 lines of code. Python is well-suited for calling and importing from other files.

One reason for Python code is easier than java is that its dependecny is easy. You just need to use pip install to add a dependency. With maven, you need to write dependency in POM XML and then use mvn compile to let the maven download the dependencies.

Another reason for Python's simplicity is that it's code can be directly run without hassle. 

Though starting with Java 11, the java command can directly execute single-file source-code programs without needing to compile them separately using javac. But that often for java project it is large, so one have to run it with mvn spring-boot:run with some properties config.

And third reason in my point is that python module design is simple that you use from and import to import code from other files easily. 

For now , many AI chatbots can run python code directly in the chatbot window, like Grok.

While when we compare to 100 java files , each with around 1000 lines of code to some simple python script, it is not fair. For this kind of project, I would like to have 1000 python files, each with around 100 lines of code. 

It is ok to select linse of code or a function to edit. However, you need to know where to select. Why don't let this task hang over to AI to make our life easier. So we just need to use select all to select all the code, and tell AI/LLM how to edit.

And for python, it is easier to use if __name=="main" then to run and test functions in a file. And it is easier for other python files to call the functions inside this file without needing to run test.

This is context engineering optimized for AI. Could we approach it with other ways? AI/LLM is auto-regressive. However, when we use Copilot or Claude Code , we don't know how the AI Software Agent help us to do. They should think about it instead of us.

Could we in user side to arrange code sepecifially to reduce token usage. For this points, the ways about 1000 python files with each 100 lines of code is good for this purpose. Because you can verify functions and code files easily before let other python code to call them.

But one problem is that if you want to change several files of code together, it is not easy to do so. For a simple way, you can copy the code to AI chatbots, and let them tell you how to edit code in these files. 

Possibly, we don't need to use number of lines to separate functions or logic. But we better do it to seprate logic to small functions. We do it by naturally sperate them with kind of logic , so they can appear shorter. 




