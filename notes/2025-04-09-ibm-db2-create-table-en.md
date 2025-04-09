---
title: Creating a Table in IBM Db2
lang: en
layout: post
audio: false
translated: false
generated: true
---

Creating a table in IBM Db2 involves using SQL statements. Below are the steps and examples for creating a table and creating a table based on another table in a different schema.

### Creating a Table in IBM Db2

To create a table in IBM Db2, you use the `CREATE TABLE` statement. Here's an example:

```sql
CREATE TABLE my_schema.my_table (
    column1 INTEGER PRIMARY KEY,
    column2 VARCHAR(50),
    column3 DATE
);
```

In this example:
- `my_schema` is the schema where the table will be created.
- `my_table` is the name of the table.
- `column1`, `column2`, and `column3` are the columns in the table with their respective data types.

### Creating a Table Based on Another Table in Another Schema

To create a table based on another table in a different schema, you can use the `CREATE TABLE AS` statement. This allows you to create a new table with the same structure and data as an existing table. Here's an example:

```sql
CREATE TABLE my_schema.new_table AS (
    SELECT * FROM another_schema.existing_table
) WITH NO DATA;
```

In this example:
- `my_schema.new_table` is the new table being created.
- `another_schema.existing_table` is the existing table in another schema.
- `WITH NO DATA` specifies that the new table should have the same structure as the existing table but without copying the data. If you want to copy the data as well, you can omit this clause.

### Additional Considerations

- Ensure you have the necessary permissions to create tables in the specified schema.
- Adjust the data types and constraints as needed for your specific use case.
- You can also specify additional options such as indexes, constraints, and storage settings when creating a table.

Would you like more detailed examples or explanations on any specific part of this process?