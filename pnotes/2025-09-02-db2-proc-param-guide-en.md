---
title: Db2 Stored Procedure Parameter Guide
lang: en
layout: post
audio: false
translated: false
generated: true
image: false
---

In IBM Db2, **stored procedures** are database routines you can call with `CALL`. They can accept input parameters, output parameters, or both (IN, OUT, INOUT).

---

### How to Call a Stored Procedure

The basic syntax is:

```sql
CALL procedure_name (param1, param2, ...);
```

If the procedure has output parameters, you must provide host variables (in embedded SQL) or local variables (in SQL PL/anonymous blocks) to capture the results.

---

### Parameter Types

1. **IN**

   * You pass a value into the procedure.
   * The procedure cannot change this value for the caller.
   * Example: a user ID to look up.

2. **OUT**

   * The procedure writes a value back to the caller.
   * You must supply a variable to hold the returned result.
   * Example: a calculated balance.

3. **INOUT**

   * The variable is both input and output.
   * You pass in an initial value, and the procedure can modify it before returning it.
   * Example: incrementing a counter.

---

### Example

Suppose we have a procedure:

```sql
CREATE PROCEDURE get_customer_balance
    (IN p_cust_id INT, OUT p_balance DECIMAL(10,2))
LANGUAGE SQL
BEGIN
    SELECT balance
    INTO p_balance
    FROM customers
    WHERE cust_id = p_cust_id;
END
```

You would call it like this:

```sql
-- In an interactive SQL client
CALL get_customer_balance(101, ?);

-- In SQL PL block
DECLARE v_balance DECIMAL(10,2);
CALL get_customer_balance(101, v_balance);
```

Here:

* `101` is the **IN** parameter.
* `v_balance` receives the **OUT** parameter result.

---

✅ So, in Db2 stored procedures:

* `IN` = input only.
* `OUT` = output only.
* `INOUT` = both directions.

Would you like me to also show you how to call these from **Java (JDBC)** or **Python (ibm\_db)**?