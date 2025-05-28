---
title: Injective Functions
lang: en
layout: post
audio: false
translated: false
generated: true
---

In mathematics, the term "injective" refers to a function or mapping between two sets where distinct elements of the first set map to distinct elements of the second set. In other words, no two different elements in the domain (the first set) are mapped to the same element in the codomain (the second set).

This property is also known as "one-to-one." If a function \\( f \\) is injective, then for any two elements \\( x \\) and \\( y \\) in the domain, if \\( f(x) = f(y) \\), then it must be the case that \\( x = y \\). This ensures that each element in the codomain is mapped by at most one element in the domain.

---

To understand why a linear transformation \\( T \\) is injective if its kernel contains only the zero vector, let's break down the definitions and implications:

1. **Kernel of a Transformation**: The kernel of a linear transformation \\( T: V \rightarrow W \\) (denoted as \\( \ker(T) \\)) is the set of all vectors in \\( V \\) that are mapped to the zero vector in \\( W \\). Mathematically, \\( \ker(T) = \{ v \in V \mid T(v) = 0 \} \\).

2. **Injective Transformation**: A linear transformation \\( T \\) is injective (or one-to-one) if different vectors in \\( V \\) map to different vectors in \\( W \\). In other words, if \\( T(u) = T(v) \\), then \\( u = v \\).

Now, let's connect these two concepts:

- Suppose \\( \ker(T) = \{0\} \\). This means the only vector in \\( V \\) that maps to the zero vector in \\( W \\) is the zero vector itself.

- To show that \\( T \\) is injective, assume \\( T(u) = T(v) \\). By the linearity of \\( T \\), we have \\( T(u) - T(v) = T(u - v) = 0 \\).

- Since \\( \ker(T) = \{0\} \\), \\( T(u - v) = 0 \\) implies that \\( u - v = 0 \\), which means \\( u = v \\).

Thus, if \\( \ker(T) = \{0\} \\), the transformation \\( T \\) is injective. This is because the only solution to \\( T(v) = 0 \\) is \\( v = 0 \\), ensuring that no two distinct vectors in \\( V \\) are mapped to the same vector in \\( W \\).

