---
title: Db2 Sequence NEXT VALUE Guide
lang: en
layout: post
audio: false
translated: false
generated: true
image: false
---

In IBM Db2, **`NEXT VALUE FOR`** (sometimes written as `NEXTVAL`) is used to retrieve the next number from a **sequence object**. Sequences are database objects that generate numeric values, typically used for primary keys, surrogate keys, or any case where you need unique, incrementing values.

---

### How It Works

* A **sequence** is created using `CREATE SEQUENCE`. It has attributes such as `START WITH`, `INCREMENT BY`, `MAXVALUE`, `CYCLE` (whether to wrap around), and `CACHE`.
* Each time you call `NEXT VALUE FOR sequence_name`, Db2 increments the sequence and returns the new value.
* Unlike identity columns, sequences are independent of any particular table. You can use them across multiple tables or applications.

---

### Example

```sql
-- Create a sequence starting from 100, incrementing by 1
CREATE SEQUENCE my_seq
  START WITH 100
  INCREMENT BY 1
  NO CYCLE;

-- Use it in a query
SELECT NEXT VALUE FOR my_seq FROM sysibm.sysdummy1;

-- Insert into a table
INSERT INTO employees (id, name)
VALUES (NEXT VALUE FOR my_seq, 'Alice');
```

If you run the `SELECT` multiple times, you’ll get 100, 101, 102, and so on.

---

### Key Notes

* **`CURRVAL` equivalent**: Db2 also supports `PREVIOUS VALUE FOR` to retrieve the most recently generated value in your session.
* **Concurrency**: Each session/thread gets unique values. Sequence values are not rolled back, even if the transaction fails, to ensure uniqueness.
* **Caching**: If you define `CACHE`, Db2 pre-allocates values in memory for performance. But if the database restarts, cached values may be lost (gaps can appear).
* **Usage in DML**: You can use `NEXT VALUE FOR` in `INSERT`, `UPDATE`, or `SELECT` statements, but not in `CHECK` constraints or default expressions directly (depends on Db2 version).

---

✅ In short: `NEXT VALUE FOR` in Db2 increments the sequence and gives you the next available number, ensuring uniqueness and consistency across sessions.

Would you like me to also show you **how this differs from identity columns** in Db2?