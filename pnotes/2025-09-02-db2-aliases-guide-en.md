---
title: Db2 Aliases Simplified Guide
lang: en
layout: post
audio: false
translated: false
generated: true
image: false
---

In IBM Db2, an **alias** is essentially an alternative name (a shortcut) for a database object, most often a **table** or **view**. It allows you to refer to an object using a different name than its base name, which can simplify queries, improve portability, or support application requirements.

Here’s how it works in practice:

---

### 1. Purpose of Aliases

* **Simplify references**: You can create an alias with a shorter or more convenient name.
* **Schema transparency**: If your application should not care which schema a table lives in, you can create an alias in your own schema that points to the base object in another schema.
* **Portability**: Applications referencing aliases don’t have to change if the underlying base object moves to another schema or even another database (in Db2 for z/OS, you can point to remote objects).
* **Security & abstraction**: Users can be given access to aliases rather than directly to base objects, hiding schema details.

---

### 2. Syntax

Basic syntax to create an alias:

```sql
CREATE ALIAS my_alias FOR schema_name.table_name;
```

Example:

```sql
CREATE ALIAS emp_alias FOR hr.employees;
```

Now you can query:

```sql
SELECT * FROM emp_alias WHERE dept = 'SALES';
```

---

### 3. Types of Aliases

* **Simple table/view alias**: Points to a table or view in the same or another schema.
* **Remote alias (Db2 for z/OS)**: Can reference a table or view in another Db2 subsystem, enabling location transparency.
* **Synonyms (older concept, mostly replaced by aliases)**: Db2 historically supported synonyms, but aliases are more flexible.

---

### 4. Key Characteristics

* Aliases don’t duplicate data—they just provide an alternative name.
* Dropping an alias does not affect the underlying table or view.
* Multiple aliases can point to the same object.
* Permissions on an alias may differ from the underlying table (depending on how you grant rights).

---

### 5. Alias vs Column/Table Aliasing in SQL

* The `CREATE ALIAS` statement defines a permanent database object.
* The `AS` keyword in a `SELECT` statement (like `SELECT col1 AS c FROM mytable`) is a **query-level alias**, temporary and only valid within that SQL statement.

---

👉 For example:

```sql
-- Permanent alias
CREATE ALIAS sales_q1 FOR accounting.sales_2025_q1;

-- Query-time alias
SELECT s.amount, s.date
FROM accounting.sales_2025_q1 AS s;
```

---

Would you like me to also explain the **differences between Db2 aliases and views**, since they’re often confused?