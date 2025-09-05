---
title: Db2 Replace Function Basics Guide
lang: en
layout: post
audio: false
translated: false
generated: true
image: false
---

In IBM Db2, `CREATE OR REPLACE FUNCTION` is a convenient way to define or update a user-defined function (UDF) without worrying about whether it already exists. Here’s how it works:

---

### 1. Purpose

* **`CREATE FUNCTION`**: Creates a new user-defined function.
* **`CREATE OR REPLACE FUNCTION`**: If the function already exists, Db2 drops the old version and replaces it with the new definition. If it doesn’t exist, it simply creates it.

This avoids having to manually `DROP FUNCTION` before redefining it.

---

### 2. Behavior

* Db2 **drops and re-creates** the function under the covers. This means:

  * The function’s **signature** (name + parameter types) must match the existing function to be replaced.
  * Any **dependent objects** (like views, triggers, other routines) may be invalidated and revalidated automatically.
  * If dependencies cannot be revalidated, you may get errors and need to recompile those objects manually.
* Permissions granted to the old function are **not preserved**; you need to re-grant them after replacement.

---

### 3. Syntax Example

```sql
CREATE OR REPLACE FUNCTION my_schema.add_tax (price DECIMAL(10,2))
RETURNS DECIMAL(10,2)
LANGUAGE SQL
DETERMINISTIC
NO EXTERNAL ACTION
RETURN price * 1.07;
```

If `my_schema.add_tax` already exists, Db2 will replace it with this new definition.

---

### 4. Restrictions

* You can only replace **user-defined functions** (not built-in ones).
* You cannot use `OR REPLACE` for **inline SQL PL functions** in some older Db2 versions (support depends on edition and version — Db2 LUW vs Db2 for z/OS).
* If the new definition is **incompatible** (e.g., changing return type in a way that breaks dependencies), you’ll get errors.
* `OR REPLACE` does not preserve **authorizations** (GRANTs must be reissued).

---

### 5. Best Practices

* Always test `OR REPLACE FUNCTION` in development first, especially if other objects depend on the function.
* Keep your GRANT statements in version-control so you can reapply them after replacement.
* If you need to change parameter signatures, use `DROP FUNCTION` followed by `CREATE FUNCTION` instead.

---

Would you like me to also show you how this differs between **Db2 LUW (Linux/Unix/Windows)** and **Db2 for z/OS**? The details vary a bit depending on the platform.