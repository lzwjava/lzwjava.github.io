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

---

The error you're encountering (`SQLCODE=-193`) in IBM Db2 occurs because you're trying to add a `NOT NULL` column to an existing table without specifying a `DEFAULT` value, and the table likely already contains rows. In Db2, when you add a new column with a `NOT NULL` constraint to a table that has existing data, you **must** provide a `DEFAULT` value. This is because Db2 needs to populate the new column with a value for all existing rows, and `NOT NULL` prohibits null values. Without a `DEFAULT`, Db2 doesn't know what to put in those rows, resulting in the error.

### Why This Happens
- The `NOT NULL` constraint means the column cannot contain null values.
- If the table is empty (no rows), adding a `NOT NULL` column without a `DEFAULT` is fine because there’s nothing to populate.
- If the table has rows, Db2 requires a `DEFAULT` value to fill the new column for those existing rows.

### How to Fix It
Add a `DEFAULT` clause to your `ALTER TABLE` statement to specify a value for existing rows. For a `BIGINT` column, a common default might be `0`, but you can choose any value that makes sense for your use case.

#### Corrected Syntax
```sql
ALTER TABLE table_name
ADD COLUMN column_name BIGINT NOT NULL DEFAULT 0;
```

### Example
If your table is `employees` and you’re adding a column `employee_id`:
```sql
ALTER TABLE employees
ADD COLUMN employee_id BIGINT NOT NULL DEFAULT 0;
```
This will:
- Add the `employee_id` column as a `BIGINT`.
- Set it to `NOT NULL`.
- Populate it with `0` for all existing rows.

### Alternative Solutions
1. **If You Don’t Want a Default Value**:
   - Add the column without `NOT NULL`, then update it manually and add the constraint later:
     ```sql
     ALTER TABLE table_name
     ADD COLUMN column_name BIGINT;
     
     UPDATE table_name
     SET column_name = 0;  -- Or another value

     ALTER TABLE table_name
     ALTER COLUMN column_name SET NOT NULL;
     ```

2. **If the Table Should Be Empty**:
   - If you believe the table should have no rows and this error is unexpected, check the row count:
     ```sql
     SELECT COUNT(*) FROM table_name;
     ```
   - If it’s empty, the original command (`ADD COLUMN column_name BIGINT NOT NULL`) should work without a `DEFAULT`.

### Key Notes
- Choose a `DEFAULT` value that aligns with your data model (e.g., `-1`, `0`, or another meaningful number).
- After adding the column, you can update the values as needed:
  ```sql
  UPDATE table_name
  SET column_name = <new_value>
  WHERE <condition>;
  ```

Let me know if you need help picking a default value or troubleshooting further!