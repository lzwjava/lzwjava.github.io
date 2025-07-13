---
audio: false
generated: false
lang: en
layout: post
title: Thoughts about Multi-Region Software Development
translated: false
---

For international companies, there are often projects that serve multiple regions' people, like Singapore, Hong Kong, UK, USA, and China.

I have worked on some projects that serve multiple regions' users. Doing it right in backend projects is not easy.

For Standard Chartered Bank, there is the SC Mobile India app, SC Mobile Hong Kong app, etc. They basically give countries their own apps. They probably use different apps, different backend servers, and some features are different but with the same design language.

This is probably wrong to do that. In the first years, it seems simple or doable. But after a decade, they will know it is very painful. The maintenance cost or synchronization cost, the testing cost—there are tons of duplicate efforts.

However, for Facebook, Google, or Apple Pay, it is kind of simple. Someone may say they are not financial apps; they have some compliance rules that need to be followed. It is not true. The compliance often means the database server, or the database, or some data that government departments want to check or for audit companies to do audits.

However, other efforts are the same. The software is very flexible. We should let code be in the same repository, we should use data source configuration to host different regions' data, and we should share the same code, same design, same workflow, and same testing as much as possible.

Apple Pay is a good example of this. The App Store is also a good example of this. They serve every country too.

There are probably some projects in big tech companies that use continents to separate, like Asia and Pacific area, North America. For these too.

The first thing when doing multi-region development is to know what's different, what's the compliance that we must follow, and how to reduce duplicate efforts as much as possible.

For text-to-speech, Google Cloud needs to train different languages. They provide different models and different languages for it. For languages, the differences between languages are their sounds, their pronunciation, and their character appearance. The former means when using Google Cloud to do text-to-speech, we need to use different models. For their character appearance, that means when doing PDF generation, we need to be careful about its font selection.

For multi-region projects, in Spring Boot projects, we can use its aliases and different object initialization to do so. We can use properties or YAML configuration smartly. We can put all different logic based on region into some specific modules or classes.

And for code hosting, different branches for different countries seem easy at first, but after some years, you will know how painful it is. You need to git cherry-pick for other regions. And you need to test again in another branch. Whenever doing every small change, you need to synchronize to branches. And as time goes by, if we don't put our effort into minimizing the code or logic differences, the differences in the code between multiple regions or countries become large enough to be impossible to fix.

The good news is that now AI can help us to refactor or write better code, or fix the multi-region code design issues. No matter how big the mistake is, when we fix it, it is a small mistake.