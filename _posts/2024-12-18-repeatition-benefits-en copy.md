---
layout: post  
title: "The Benefits of Repetition in Programming"
---

```bash
export PATH=/opt/homebrew/opt/ruby/bin:/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:"$HOME/Library/Python/3.9/bin":/Library/TeX/texbin:/Users/lzwjava/bin:/Users/lzwjava/platform-tools:/Users/lzwjava/Downloads/google-cloud-sdk/bin
```

Do not use a variable here, 

`"$HOME/Library/Python/3.9/bin"`

```bash
export PATH=/opt/homebrew/opt/ruby/bin:/opt/homebrew/opt/openjdk/bin:/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/lzwjava/Library/Python/3.9/bin:/Library/TeX/texbin:/Users/lzwjava/bin:/Users/lzwjava/platform-tools:/Users/lzwjava/Downloads/google-cloud-sdk/bin
```

It seems like the home directory `/Users/lzwjava` is repeated too much here, but the latter version is much cleaner and more readable.

Repetition can be helpful in programming. We don’t always need to extract or simplify everything with functions or variables.

Additionally, the home directory is unlikely to change frequently.
