---
title: Adding a Column to an Existing Table in IBM Db2
lang: en
layout: post
audio: false
translated: false
generated: true
---

To add a column to an existing table in IBM Db2, you use the `ALTER TABLE` statement with the `ADD COLUMN` clause. Here’s the basic syntax:

```sql
ALTER TABLE table_name
ADD COLUMN column_name data_type [constraints];
```

### Example
Suppose you have a table named `employees` and you want to add a column called `phone_number` with a data type of `VARCHAR(15)`:

```sql
ALTER TABLE employees
ADD COLUMN phone_number VARCHAR(15);
```

### Key Points
1. **Table Name**: Replace `table_name` with the name of your existing table.
2. **Column Name**: Specify the new column name (e.g., `phone_number`).
3. **Data Type**: Define the data type (e.g., `VARCHAR`, `INTEGER`, `DATE`, etc.).
4. **Constraints (Optional)**: You can add constraints like `NOT NULL`, `DEFAULT`, or `CHECK` if needed. For example:
   ```sql
   ALTER TABLE employees
   ADD COLUMN phone_number VARCHAR(15) NOT NULL DEFAULT 'N/A';
   ```

5. **Existing Data**: When you add a column, Db2 will populate it with `NULL` values for existing rows unless you specify a `DEFAULT` value.

### Notes
- You need appropriate permissions (e.g., `ALTER` privilege) on the table to perform this operation.
- If the table is large, this operation might take some time and could lock the table, depending on the Db2 version and configuration.

Let me know if you need help with a specific example or additional details!

---

The error you're encountering (`SQLCODE=-104, SQLSTATE=42601`) in IBM Db2 indicates a syntax issue with your `ALTER TABLE` statement. Specifically, `BIGINT(8)` is not a valid syntax in Db2. Unlike some other databases (e.g., MySQL), Db2 does not use a length or precision specifier like `(8)` with the `BIGINT` data type. In Db2, `BIGINT` is a fixed 8-byte integer type that can store values from `-2^63` to `2^63-1`, and you simply declare it as `BIGINT` without additional parameters.

### Correct Syntax
To add a `BIGINT` column with a `NOT NULL` constraint, use this:

```sql
ALTER TABLE table_name
ADD COLUMN column_name BIGINT NOT NULL;
```

### Example
If your table is called `employees` and you want to add a column `employee_id` as a `BIGINT` that cannot be null:

```sql
ALTER TABLE employees
ADD COLUMN employee_id BIGINT NOT NULL;
```

### Why the Error Occurred
- The `(8)` in `BIGINT(8)` is invalid in Db2 because `BIGINT` doesn't take a length argument. This syntax might be familiar from other databases like MySQL, where it specifies display width, but Db2 doesn't support it.
- The parser encountered `BIGINT(8)` and flagged it as an "unexpected token," leading to the `SQLCODE=-104` error.

### Fixing the Issue
1. Remove the `(8)` from your statement.
2. If you need to specify a default value (since `NOT NULL` requires existing rows to have a value), add a `DEFAULT` clause. For example:

```sql
ALTER TABLE employees
ADD COLUMN employee_id BIGINT NOT NULL DEFAULT 0;
```

Without a `DEFAULT`, adding a `NOT NULL` column to a table with existing rows will fail because Db2 won't know what value to assign to the new column for those rows.

### Steps to Resolve
- If your table has no rows yet, simply use:
  ```sql
  ALTER TABLE table_name
  ADD COLUMN column_name BIGINT NOT NULL;
  ```
- If your table already has rows, include a `DEFAULT` value:
  ```sql
  ALTER TABLE table_name
  ADD COLUMN column_name BIGINT NOT NULL DEFAULT 0;
  ```

### Verification
After running the statement, you can verify the column was added with:
```sql
DESCRIBE TABLE table_name;
```

Let me know if you still encounter issues or need further clarification!