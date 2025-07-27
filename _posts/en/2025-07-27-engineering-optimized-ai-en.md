---
audio: false
generated: false
image: false
lang: en
layout: post
title: Optimizing Software Engineering for AI
translated: false
---

In this blog, I utilized hundreds of scripts to assist with translation, playground, frontmatter maintenance, and Telegram bots. I believe this development approach might represent the future of software engineering optimized for AI.

I don't rely much on Python module functionality, nor do I want to structure code like a large Java Spring project.

I worked as a contractor for several banking projects in recent years. I have observed impressive banking architecture, microservices, effective multi-country design to eliminate duplication as much as possible, a robust fundamental framework built on top of Spring, and strong governance with centralized configuration.

While their banking architecture is impressive, if we were to start today, I would consider optimizing for LLM/AI. This would involve better context engineering, improved separation of contexts, and prioritizing AI-first thinking over human-centric design. Although Spring offers multiple levels and good abstraction, it can be challenging for LLM/AI to navigate.

I believe we should aim for flatter structures, similar to a flat organization. This means using just two levels: the first level calls the second level. In a function, it's better to call another 50 functions directly rather than having 50 nested levels or stacks. AI/LLM struggle to judge or infer overly complex, nested structures, but they excel at handling smaller functions of 100 to 200 lines of code. Python is well-suited for calling and importing from other files.

One reason Python code is easier than Java is that its dependency management is simple. You just need to use `pip install` to add a dependency. With Maven, you need to write the dependency in a POM XML file and then use `mvn compile` to let Maven download the dependencies.

Another reason for Python's simplicity is that its code can be directly run without hassle.

Though starting with Java 11, the `java` command can directly execute single-file source-code programs without needing to compile them separately using `javac`. However, often for Java projects, they are large, so one has to run them with `mvn spring-boot:run` along with some properties configuration.

A third reason is that Python's module design is simple; you can use `from` and `import` to easily import code from other files.

For now, many AI chatbots can run Python code directly in the chatbot window, like Grok.

When comparing 100 Java files, each with around 1000 lines of code, to some simple Python scripts, it is not a fair comparison. For this kind of project, I would prefer to have 1000 Python files, each with around 100 lines of code.

It is acceptable to select lines of code or a function to edit. However, you need to know where to select. Why not let this task be handled by AI to make our lives easier? So, we just need to use "select all" to select all the code and tell AI/LLM how to edit.

For Python, it is easier to use `if __name__ == "__main__":` to run and test functions in a file. It is also easier for other Python files to call the functions inside this file without needing to run the test.

This is context engineering optimized for AI. Could we approach it in other ways? AI/LLM is auto-regressive. However, when we use Copilot or Claude Code, we don't know how the AI Software Agent helps us. They should think about it instead of us.

Could we, on the user side, arrange code specifically to reduce token usage? For this point, the approach of having 1000 Python files with each 100 lines of code is good for this purpose. Because you can verify functions and code files easily before letting other Python code call them.

But one problem is that if you want to change several files of code together, it is not easy to do so. For a simple way, you can copy the code to AI chatbots and let them tell you how to edit code in these files.

Possibly, we don't need to use the number of lines to separate functions or logic. But we should do it to separate logic into small functions. We can do this by naturally separating them by type of logic, so they appear shorter.

Why do we want Software Engineering Optimized for AI? Because AI is powerful, we should optimize everything for AI and then let AI help software engineering as much as possible.

It is possible not just for code, but for any text too. Suppose we are very picky editors; we don't want AI to edit our large texts at once. We want to check paragraph by paragraph. For code, we can tolerate minor errors or bugs. For text, we can tolerate them because most readers are not so picky.

But code is different in that sometimes, even a minor error can lead to the complete malfunction of a large project.

For XML or YAML files, we probably don't need to separate them as much because they are already highly structured.

And for HTML files, we should do some separation. Instead of writing hundreds of JavaScript files together with hundreds of HTML files, making it easy to exceed 1000 lines of code, we should use `import` for JavaScript to manage this. For JavaScript code, we can use the above ways to separate.

We want to structure code in ways that let AI help us easily add, edit, delete, and run code. This is the beginning. Think of a day when all code can be generated or fixed by AI easily. The world will be highly digitalized.

Imagine myself writing 100 big software projects and providing APIs to connect with others. This includes my daily agenda; I am, myself, like a 1000-employee tech company nowadays. They are customized for my needs, to earn money or spend money for my benefits. This is really amazing.