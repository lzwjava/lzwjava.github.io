---
title: An Constraint Issue in IBM DB2 
lang: en
layout: post
audio: false
translated: false
generated: true
---

In IBM Db2, the error `SQLCODE=-270` with `SQLSTATE=42997` indicates that a function or feature used in your statement is not supported in the specific context or environment you're working in. In this case, the statement:

```sql
ALTER TABLE table_name
ADD CONSTRAINT constraint_name PRIMARY KEY (column_name);
```

is causing the error because certain Db2 environments—particularly **Db2 for z/OS**—do not support adding a primary key constraint directly to an existing table using `ALTER TABLE ... ADD CONSTRAINT` if the table was not originally created with a primary key or if specific conditions aren't met. This restriction is more common in Db2 for z/OS than in Db2 LUW (Linux, UNIX, Windows), where this syntax is generally supported.

---

### Why This Happens
In Db2 for z/OS:
- You cannot add a primary key to an existing table using `ALTER TABLE ... ADD CONSTRAINT PRIMARY KEY` unless the table is empty or certain prerequisites (like an existing unique index) are in place.
- The error `42997` often relates to a limitation in the database's current configuration, version, or the table's state (e.g., it may require a unique index to be pre-created).

In contrast, Db2 LUW typically allows this operation as long as the column is `NOT NULL` and contains unique values.

---

### How to Fix It
The fix depends on your Db2 environment (z/OS or LUW) and the table's current state. Since you’re hitting this error, I’ll assume you’re on **Db2 for z/OS** (where this limitation is more common) and provide a workaround. If you’re on Db2 LUW, let me know, and I’ll adjust the solution.

#### Workaround for Db2 for z/OS
To add a primary key to an existing table in Db2 for z/OS:
1. **Ensure Prerequisites**:
   - The column (e.g., `column_name`) must be `NOT NULL`.
   - The column must have unique values.
   - A unique index must exist on the column before adding the primary key.

2. **Steps**:
   - **Step 1**: Check if the column is `NOT NULL` and unique.
   - **Step 2**: Create a unique index on the column.
   - **Step 3**: Add the primary key constraint using the existing unique index.

---

#### Detailed Steps

##### Step 1: Verify Column Properties
- Check if `column_name` is `NOT NULL`:
  ```sql
  SELECT COLNAME, NULLS 
  FROM SYSCAT.COLUMNS 
  WHERE TABNAME = 'TABLE_NAME' 
  AND TABSCHEMA = 'YOUR_SCHEMA_NAME';
  ```
  If `NULLS = 'Y'`, make it `NOT NULL`:
  ```sql
  ALTER TABLE table_name
  ALTER COLUMN column_name SET NOT NULL;
  ```
  (If there are `NULL` values, update them first, e.g., `UPDATE table_name SET column_name = 0 WHERE column_name IS NULL;`.)

- Check for duplicates:
  ```sql
  SELECT column_name, COUNT(*) 
  FROM table_name 
  GROUP BY column_name 
  HAVING COUNT(*) > 1;
  ```
  If duplicates exist, resolve them (e.g., delete or update duplicate rows).

##### Step 2: Create a Unique Index
Create a unique index on `column_name`:
```sql
CREATE UNIQUE INDEX idx_column_name
ON table_name (column_name);
```
- Replace `idx_column_name` with a unique index name (e.g., `idx_emp_id`).
- This index ensures uniqueness and will be used to enforce the primary key.

##### Step 3: Add the Primary Key
Now, add the primary key constraint using the unique index:
```sql
ALTER TABLE table_name
ADD PRIMARY KEY (column_name);
```
- In Db2 for z/OS, you may not need to specify a constraint name explicitly; the system will generate one (e.g., `SQLxxxxxxxxxxxxxx`).
- If you want a specific name, some versions allow:
  ```sql
  ALTER TABLE table_name
  ADD CONSTRAINT constraint_name PRIMARY KEY (column_name);
  ```
  But if `SQLCODE=-270` persists, omit the `CONSTRAINT` clause and let Db2 handle it.

---

#### Example
For a table `employees` with column `employee_id`:
1. Ensure `employee_id` is `NOT NULL` and unique:
   ```sql
   ALTER TABLE employees
   ALTER COLUMN employee_id SET NOT NULL;
   ```
   (Resolve any `NULL`s or duplicates first.)

2. Create a unique index:
   ```sql
   CREATE UNIQUE INDEX idx_emp_id
   ON employees (employee_id);
   ```

3. Add the primary key:
   ```sql
   ALTER TABLE employees
   ADD PRIMARY KEY (employee_id);
   ```

---

### If the Table Has Data
If the table already has rows:
- The unique index creation will fail if duplicates exist (`SQLCODE=-803`). Resolve duplicates first.
- After creating the index, the `ALTER TABLE ... ADD PRIMARY KEY` should succeed.

---

### Verify the Primary Key
Check that the primary key was added:
```sql
SELECT 
    TC.CONSTNAME AS PRIMARY_KEY_NAME,
    KC.COLNAME AS COLUMN_NAME
FROM 
    SYSCAT.TABCONST TC
JOIN 
    SYSCAT.KEYCOLUSE KC
    ON TC.CONSTNAME = KC.CONSTNAME 
    AND TC.TABSCHEMA = KC.TABSCHEMA 
    AND TC.TABNAME = KC.TABNAME
WHERE 
    TC.TABNAME = 'TABLE_NAME'
    AND TC.TABSCHEMA = 'YOUR_SCHEMA_NAME'
    AND TC.TYPE = 'P';
```

---

### Alternative: Recreate the Table (Last Resort)
If the above workaround doesn’t work due to version-specific restrictions or other issues:
1. Export the table data:
   ```sql
   EXPORT TO employees_data.del OF DEL SELECT * FROM employees;
   ```
2. Drop the table:
   ```sql
   DROP TABLE employees;
   ```
3. Recreate it with the primary key:
   ```sql
   CREATE TABLE employees (
       employee_id INT NOT NULL,
       PRIMARY KEY (employee_id)
   );
   ```
4. Import the data:
   ```sql
   LOAD FROM employees_data.del OF DEL INSERT INTO employees;
   ```

This is more disruptive and should only be used if the direct `ALTER` approach fails.

---

### Notes
- **Db2 Version**: The exact behavior depends on your Db2 version and platform (z/OS, LUW, etc.). If you can share your Db2 version (`SELECT GETVARIABLE('SYSIBM.VERSION') FROM SYSIBM.SYSDUMMY1;`), I can refine the solution.
- **Permissions**: Ensure you have `ALTER` privileges on the table.
- **Indexes**: Adding a primary key implicitly creates a unique index if one doesn’t exist, but pre-creating it avoids the `42997` error in z/OS.

Let me know if you still get errors or need help with a specific step!