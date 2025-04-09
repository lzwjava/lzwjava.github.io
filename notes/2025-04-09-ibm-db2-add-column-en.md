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