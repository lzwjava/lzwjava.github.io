---
audio: false
lang: en
layout: post
title: Benifits of Accumulating Logs
translated: false
generated: false
---

When I work as a contractor for a Singaproean bank, we are using Pivotal Cloud Foundry to serve the microservices. At that time, I start to accumulate logs when working in a compnay. 

Several years passes, I still think it is one of best ways to help me work or do software engineering. As time goes by, in my logs directory, there are hundreds of log files.

I don't have sepefic subdirectory or formal log file names for those. Sometimes, I juse that jira task name to be my log file name prefix or that feature. And then I add number to the suffix. It is like mutual-fund-1.log, mutual-fund-2.log etc. It means in mutual fund microservice, I have that log when running that microservice. 

Sometimes, when working the project that serve multiple regions, I will add that country as suffix, like mutual-fund-cn-1.log, mutual-fund-sg-1.log.

The file names of logs are somehow causual. Because at that time, I need to focus on error stack or the surroudning function calling.

The logs of the programs matters. Everyone knows. However, I want to overate more importance about accumulating logs instead of just watching them in console and let them go.

You will know more convenience when the project going on. You have more times to find the previous logs. You may need to know whether similar database store procedure calling happen before. You may need to know whether the same error happens before. You may need to recall back how to fix this problem last time.

There are tons of detail in a big project or tens of microservices. And the errors, exceptions or problems are happening again and again.

The log is just like the running document of a program. And they are genenrated by program automatically without human writting. And for developers, these logs are readable. 

So when starting a new task or fix a new bug, you have hundreds of logs in your hand to fix this new bug. You are not alone.

Why we accumulate them? Because things or knowledge are easily been forgoten.

There are human civilization progress when the paper is inventing. And when computer are invented, there are another level of human civilization. 

Not just for humans, but for ai chatbots, llm tooling, these logs are becoming more and more important. The GreptimeDB, a database for the unified collection and analysis of observability data (metrics, logs, and traces) established in 2022 is not a coincidence. 

Why I don't do that before, after I work as a contractor for big banks, I need to do more collaboration and do the bigger project. Before that, most of the time in the startup or my startup period, I work sololy. 

When I work at LeanCloud before, I work on the IM app LeanChat for like half of the time. 

And when I go into more formal corporate world, development of the projects are differnt to my peronsal project or startup project. They have SIT, UAT testing development. And the production development are often just open to certain small team peers. Getting the logs of them and fixing problems become long and somewhat tedious. And running a project spends time, and the jenkins pipeline often need half an hour to run.

So I can't run or test the program like a fly. I can't do a deployment by simply typing a command in my personal computer and upload code to the server for running. 

So it somehow let me accumulate logs to have more context to handle tasks. We better at first shot to fix problems. We better verify our fix for just few times. We are not easy to get the program that running in a cloud or the server of company, we better copy it and save in the local laptop, to do analysis.

And now, for my personal project, I will accumulate the logs too. It becomes a habit. After working in big companies for some years, I somehow have more patience or stragety to make my project bigger and longer. So I know I need these logs as time goes by.

The world become digital and digital, so accumulating Logs of digital program are just like accumulating books in a physical world.



