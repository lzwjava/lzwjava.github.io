---
title: Add Constraint in IBM Db2
lang: en
layout: post
audio: false
translated: false
generated: true
---

If the `employees` table already exists in IBM Db2 and you want to add a primary key to it, you can use the `ALTER TABLE` statement with the `ADD CONSTRAINT` clause. Since the table was created without a primary key, you can add one to the `employee_id` column, provided that:
- The `employee_id` column is defined as `NOT NULL`.
- The values in `employee_id` are unique (no duplicates).

Here’s how to add a primary key to an existing table.

---

### Syntax to Add a Primary Key
```sql
ALTER TABLE table_name
ADD CONSTRAINT constraint_name PRIMARY KEY (column_name);
```

- **`table_name`**: The name of the existing table (`employees` in your case).
- **`constraint_name`**: A name for the primary key constraint (e.g., `pk_employees`). This must be unique within the schema.
- **`column_name`**: The column to designate as the primary key (`employee_id`).

---

### Example
To add a primary key on the `employee_id` column of the `employees` table:
```sql
ALTER TABLE employees
ADD CONSTRAINT pk_employees PRIMARY KEY (employee_id);
```

---

### Prerequisites
Before running the `ALTER TABLE` statement, ensure:
1. **Column is `NOT NULL`**:
   - The `employee_id` column must already be defined as `NOT NULL`. If it’s not, you’ll need to modify it first (see below).
2. **No Duplicate Values**:
   - The `employee_id` column must contain unique values for all rows. If duplicates exist, the command will fail with an error (e.g., `SQL0803N`).
3. **No Existing Primary Key**:
   - A table can have only one primary key. If a primary key already exists, you’ll need to drop it first (not applicable here since you indicated there’s no primary key).

---

### Steps to Add a Primary Key

#### 1. Verify `NOT NULL` on `employee_id`
Check if `employee_id` is `NOT NULL`:
```sql
SELECT COLNAME, NULLS 
FROM SYSCAT.COLUMNS 
WHERE TABNAME = 'EMPLOYEES' 
AND TABSCHEMA = 'YOUR_SCHEMA_NAME';
```
- If `NULLS = 'Y'` for `employee_id`, you need to make it `NOT NULL`:
  ```sql
  ALTER TABLE employees
  ALTER COLUMN employee_id SET NOT NULL;
  ```
  Note: If the column contains `NULL` values, you must first update them to non-`NULL` values (e.g., `UPDATE employees SET employee_id = 0 WHERE employee_id IS NULL;`).

#### 2. Check for Duplicates
Ensure `employee_id` has no duplicate values:
```sql
SELECT employee_id, COUNT(*) 
FROM employees 
GROUP BY employee_id 
HAVING COUNT(*) > 1;
```
- If this returns rows, you have duplicates. You’ll need to resolve them (e.g., by updating or deleting duplicate rows) before adding the primary key.

#### 3. Add the Primary Key
Run the `ALTER TABLE` statement:
```sql
ALTER TABLE employees
ADD CONSTRAINT pk_employees PRIMARY KEY (employee_id);
```

---

### Potential Errors and Fixes
1. **Error: Column is not `NOT NULL` (`SQL0544N`)**:
   - If `employee_id` allows `NULL` values, set it to `NOT NULL` first (as shown above).
2. **Error: Duplicate Values (`SQL0803N`)**:
   - If `employee_id` has duplicates, identify and fix them:
     ```sql
     SELECT employee_id, COUNT(*) 
     FROM employees 
     GROUP BY employee_id 
     HAVING COUNT(*) > 1;
     ```
     Then, update or delete duplicates. For example:
     ```sql
     DELETE FROM employees 
     WHERE employee_id IN (
         SELECT employee_id 
         FROM employees 
         GROUP BY employee_id 
         HAVING COUNT(*) > 1
     ) 
     AND ROWID NOT IN (
         SELECT MIN(ROWID) 
         FROM employees 
         GROUP BY employee_id 
         HAVING COUNT(*) > 1
     );
     ```
3. **Error: Primary Key Already Exists (`SQL0603N`)**:
   - If the table already has a primary key, check it:
     ```sql
     SELECT CONSTNAME 
     FROM SYSCAT.TABCONST 
     WHERE TABNAME = 'EMPLOYEES' 
     AND TABSCHEMA = 'YOUR_SCHEMA_NAME' 
     AND TYPE = 'P';
     ```
     If you need to replace it, drop the existing primary key first:
     ```sql
     ALTER TABLE employees
     DROP PRIMARY KEY;
     ```

---

### Verify the Primary Key
After adding the primary key, confirm it was created:
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
    TC.TABNAME = 'EMPLOYEES'
    AND TC.TABSCHEMA = 'YOUR_SCHEMA_NAME'
    AND TC.TYPE = 'P';
```

#### Expected Output
```
PRIMARY_KEY_NAME  COLUMN_NAME
----------------  -----------
PK_EMPLOYEES      EMPLOYEE_ID
```

---

### Notes
- **Schema Name**: Replace `'YOUR_SCHEMA_NAME'` with your actual schema (e.g., `DB2INST1`). Find your current schema with:
  ```sql
  SELECT CURRENT SCHEMA FROM SYSIBM.SYSDUMMY1;
  ```
- **Permissions**: You need `ALTER` privilege on the table or appropriate authority (e.g., `DBADM`).
- **Impact**: Adding a primary key creates an underlying unique index, which may affect performance for large tables.

Let me know if you encounter any errors or need help resolving duplicates!