---
audio: false
lang: en
layout: post
title: On Big Companies
translated: false
generated: false
---

Big companies are just like big programs. For a big company with 100,000 employees and 50,000 contractors, they are just like a big program with 150,000 methods.

Dario Amodei said that talent density is much more important than the number of talents. Two hundred very talented people can beat 1,000 talented people with 800 ordinary people.

Dario Amodei also mentioned that big companies have so many procedures and processes because they don't trust their employees or contractors. So they need to check a lot and control a lot.

One thing about big companies is that they are afraid to make mistakes. One reason is that they have grown so big to be worth 300 billion or 1 trillion dollars; they must have made tons of mistakes and grown from that. However, when they are successful, they are averse to taking risks and making mistakes again.

It is like a big program that doesn't like bugs and tries to eliminate any bugs, especially security bugs, particularly in big banks.

Startups are fast, but the resources of a startup are much less, and the brand of a startup is not established; they don't have the trust of big companies.

In China, young talented people still want to go to big companies after graduation and struggle to do so. In Silicon Valley, there are so many startups, some of which are doing well even at the start with just ideas.

Some companies do like 20 years and still struggle, probably been removed from the stock market, and some companies are valued at 5 billion or 10 billion just when they are a few months old.

It says that [Mira Murati’s Thinking Machines Lab is worth $12B in seed round](https://techcrunch.com/2025/07/15/mira-muratis-thinking-machines-lab-is-worth-12b-in-seed-round/). And [Ilya Sutskever's Safe Superintelligence raises $2B at $32B](https://techcrunch.com/2025/04/12/openai-co-founder-ilya-sutskevers-safe-superintelligence-reportedly-valued-at-32b/).

So using established time to measure a startup is not a good indicator; it is better to measure it by what the team is, who the founders are, and what area they are in.

In my solo startup, I just need to use 1 minute to deploy my backend server and use 5 minutes to fix a minor bug and deploy. It is direct and fast. For big companies, it takes 1 week to prepare the deployment request, get approvals from managers, do the deployment with the IT team, and do health checks.

Though the actual time spent might be 8 hours, if we measure it, it is still 1 week from preparing the deployment to the final health check.

For fixing a minor bug and deploying, it takes two weeks to do so. You get the ticket to investigate, do analysis and testing, then review, merge the code, report to test teams to test, and then deploy.

Big companies like to enforce their policies on all teams or projects. Because for a big company with 200,000 people, those policies or internal processes that apply to only 10,000 people don't get much meaning or result. For some internal processes, big companies need to invest people or money to develop tools to support them. So if it serves only a tiny proportion of staff, the return doesn't justify the investment.

Another downside of big companies is that often no one gets punished for big mistakes.

In my startup, once I got a half-million investment to hire 9 people, and after 2 months, I had to let them go and lost that money. I did 50 small software projects with part-time engineers to earn that money back to give to the investor.

That's a very intensive and painful memory. And that made me remember that lesson all the time.

In a notable case within a large corporation, it was observed that there were no significant repercussions for those involved. Some senior managers and many of the recently hired employees were let go. It remains unclear whether this was related to a rapid and substantial hiring spree.

One contributing factor to this outcome is the cumbersome and numerous processes within large companies. Engineers who had been with the company for six months to a year were unable to make significant contributions. The timeline typically included two months to grasp the basics, three months to become acquainted with the projects, three months navigating through tedious procedures or testing, and finally, two months of productive work that impacted users.

Assuming an eight-hour workday, two months of actual productive work did not yield substantial results. The department's budget was depleted, and the user base did not expand as anticipated, leading to further layoffs.

It appeared that no valuable lessons were learned from this experience. Initially, a group of managers decided on a rapid and extensive hiring strategy, which seemed unnecessary at the time. Blaming the entire group of managers was not feasible, nor was it practical to dismiss only those who had been with the company for a short period, especially when other managers and technical leads had been part of the team for six to eight years.

The managing director did not gain much insight from the situation, as this was just one of three departments under their supervision, and their compensation remained unchanged. Even within the team, those not directly responsible were unable to learn from the experience, echoing Steve Jobs' remarks on consulting. Consequently, no one absorbed the lesson necessary to form an exceptional team capable of delivering outstanding results for users.

For startups, it seems a much better case. Because it is really serious. Some of the founders who lose or fail are really having a hard time, especially the honest ones.

For individuals with integrity, it can be deeply disheartening to lose substantial investment funds, ranging from millions to hundreds of millions of dollars, and end up with little to show for it—perhaps just a rudimentary product or a user base that, despite its size, generates minimal revenue.

Paul Graham wrote an essay before, [Hiring is Obsolete](https://paulgraham.com/hiring.html).

But what do big companies do well? One is long-termism. They tend to do things for the long term. For some good big companies, their project designs are quite good; they use microservices to avoid the mistake of becoming a big monolithic program after a decade. And they have governance teams to make some foundational frameworks and unify the development practices for the whole team.

Processes or procedures are not inherently bad. But they often make things complicated and slow. We don't find the Java unified code format unpleasant because there is a Spotless or Checkstyle plugin to help. These plugins have good design and are easy to use.

Another thing is that big companies tend to make some tools or projects for internal use, for front officers. But that user base is just hundreds or 10,000. That user base is very limited.

I think that we better use external tools for that purpose. If a tool is really great for one bank, it is probably good for 200 banks. And that can make that company a unicorn.

Tiancheng Lou, Pony.ai founder, says that why companies need to be independent is that it is more efficient. That's true.

And big companies tend to use experience to give rewards to employees. While the market rewards the result or execution for startup teams. They are actually very different.

Working in big companies is like learning in school. You progress from primary school to middle school, then to universities. In startups, however, there are more ups and downs, and there is more flexibility as you move from one idea or market to another.

For big companies, the benefit of being risk-averse is that their products are relatively stable with no apparent bugs or downtime. That's good.

But like AI, actually, a lot of users are ok to those product that's not so stable for the early, like deepseek. We know that deepseek down a lot around Feb March of 2025 when it gains a lot of attentino. but after some time, it becomes better and no users seem have much problem of that.

So it depends. Sometimes, for innovative products, we need to get them to market quickly, even if they have some issues. Users can understand.

If we think about the process, we can be more careful. We should better categorize our deployment types. Some types of changes are okay to deploy quickly, while others are not. For testing, we should categorize which parts of the testing we need to perform for regression testing for the changed code, and which parts we do not. The same applies to SonarQube checking.

In big companies, it is certain that many checks, tests, or approvals are unnecessary. We might let engineers do their work, and since the system has all the records, we can select some to review.

We should also eliminate all manager approvals. What knowledge do managers have that engineers do not? Could this knowledge be written into code to approve or reject the requests automatically?

Because everything is slow there, workers are unlikely to change things. The change from a big monolithic project to microservices for a project that has run for a decade might take two years. 

For software, code and logic are tightly intertwined, especially in well-designed systems. Thus, the development, testing, or collaboration involved can be substantial.

That's why scaling a team suddenly often doesn't work. If there is a microservice architecture that is loosely coupled, then the output of the team may be proportional to the number of team members. If there is a monolithic project that is tightly coupled, then the output of the team may only increase by 30% if we double the size of the team working on it.

Due to its slow pace, it can sometimes be difficult to determine whether an employee or contractor is incapable or if the system is too complex and cumbersome for new joiners. In one case I observed, someone had been with the company for four months and accomplished very little, merely changing a few lines of code to submit a pull request. Moreover, the quality of the code was poor as he did not understand it well. His English was also very weak, and he could only communicate by pasting screenshots and using basic English to ask questions.

Regarding stability, I see that big companies tend to have multiple team members work on duplicate tasks. For example, for task A and task B, they do not assign two team engineers to work separately on task A and task B. Instead, they have both work on parts of task A and task B so that these two engineers know what the other is doing. This makes the team more stable, as it prevents a situation where only one person knows a lot about large parts of the code and has been working on that for several years without collaboration. Then, if that person leaves the company, no one else can work on it.

Another thing big companies do well is maintain cash flow and profit discipline. The reason is that as they grow larger, they often face substantial financial crises. This is probably the most important thing they prioritize. They have learned this the hard way and have ingrained these practices into their operations. Even when they are making profits of 10 billion USD or 30 billion USD a year, they continue to optimize their workforce and conduct layoffs.

One of my colleagues told me that big companies operate with a monopoly on certain products that require a lot of labor or time to build. That makes sense. They don't rely on speed but on their size, resources, and brand.

How to surive in big companies? One is that do more, less talk. This is my deliver manager in an outsourcing vendor told me. 

The second thing is to follow what others do; it is safe. Becoming an average engineer on the team is safe, just like being an average person on the street—neither too outstanding nor too neglected, but right in the middle.

I have to say there are many big companies. Some have more than 200,000 employees, while others have around 20,000. There are also good big companies and poor-performing ones. Appearance or market cap sometimes doesn't reveal much. They can rise significantly in a few years, as Nvidia has recently, or they can suddenly collapse, like Credit Suisse.

