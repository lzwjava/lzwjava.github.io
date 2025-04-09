---
title: SQL Query to List Indexes in IBM Db2
lang: en
layout: post
audio: false
translated: false
generated: true
---

In IBM Db2, you can query the system catalog views to find information about a table's existing indexes. The primary catalog view for indexes is `SYSCAT.INDEXES`. This view contains details about all indexes in the database, including the table they belong to, the columns they index, and their properties (e.g., unique or non-unique).

Here’s how you can check the existing indexes for a specific table:

### SQL Query to List Indexes
Use the following query to retrieve index information for a specific table:

```sql
SELECT 
    INDNAME, 
    TABSCHEMA, 
    TABNAME, 
    COLNAMES, 
    UNIQUERULE, 
    INDEXTYPE
FROM 
    SYSCAT.INDEXES
WHERE 
    TABNAME = 'YOUR_TABLE_NAME'
    AND TABSCHEMA = 'YOUR_SCHEMA_NAME';
```

#### Explanation of Columns
- **`INDNAME`**: The name of the index.
- **`TABSCHEMA`**: The schema of the table.
- **`TABNAME`**: The name of the table.
- **`COLNAMES`**: The columns included in the index (prefixed with `+` for ascending or `-` for descending).
- **`UNIQUERULE`**: Indicates if the index is unique (`U` for unique, `D` for duplicate-allowed, `P` for primary key).
- **`INDEXTYPE`**: The type of index (e.g., `REG` for regular, `CLUS` for clustering).

#### Example
To find the indexes for a table named `EMPLOYEES` in the schema `MY_SCHEMA`:
```sql
SELECT 
    INDNAME, 
    TABSCHEMA, 
    TABNAME, 
    COLNAMES, 
    UNIQUERULE, 
    INDEXTYPE
FROM 
    SYSCAT.INDEXES
WHERE 
    TABNAME = 'EMPLOYEES'
    AND TABSCHEMA = 'MY_SCHEMA';
```

### Notes
1. **Case Sensitivity**: Table and schema names in Db2 are typically uppercase in the catalog unless explicitly created with quotes (e.g., `"employees"`). So, use `'EMPLOYEES'` instead of `'employees'` unless you’re sure of the casing.
2. **Schema**: If you don’t specify `TABSCHEMA`, you might get results for tables with the same name in different schemas. To find your schema, you can check your current schema with:
   ```sql
   SELECT CURRENT SCHEMA FROM SYSIBM.SYSDUMMY1;
   ```
3. **Permissions**: You need appropriate privileges to query `SYSCAT.INDEXES`. Typically, `SELECT` access on the catalog views is granted to most users.

### Alternative: Using `DESCRIBE`
For a quick check in some Db2 environments (e.g., Db2 LUW), you can use the `DESCRIBE` command to see indexes, though it’s less detailed:
```sql
DESCRIBE INDEXES FOR TABLE schema_name.table_name SHOW DETAIL;
```

#### Example
```sql
DESCRIBE INDEXES FOR TABLE MY_SCHEMA.EMPLOYEES SHOW DETAIL;
```

This command lists indexes but might not be available or as comprehensive in all Db2 editions (e.g., Db2 on z/OS).

### Sample Output
For the query on `SYSCAT.INDEXES`, you might see something like:
```
INDNAME        TABSCHEMA  TABNAME    COLNAMES       UNIQUERULE  INDEXTYPE
-------------  ---------- ---------- -------------- ----------- ---------
EMP_ID_IDX     MY_SCHEMA  EMPLOYEES  +EMPLOYEE_ID   U           REG
EMP_NAME_IDX   MY_SCHEMA  EMPLOYEES  +LAST_NAME     D           REG
```
- `EMP_ID_IDX` is a unique index on `EMPLOYEE_ID`.
- `EMP_NAME_IDX` is a non-unique index on `LAST_NAME`.

### If You Want All Indexes in the Database
Omit the `WHERE` clause:
```sql
SELECT 
    INDNAME, 
    TABSCHEMA, 
    TABNAME, 
    COLNAMES, 
    UNIQUERULE, 
    INDEXTYPE
FROM 
    SYSCAT.INDEXES
ORDER BY 
    TABSCHEMA, TABNAME, INDNAME;
```

Let me know if you need help interpreting the results or refining the query!

---

In IBM Db2, you can create an index on a table using the `CREATE INDEX` statement. Indexes improve query performance by allowing faster data retrieval, especially for columns frequently used in `WHERE`, `JOIN`, or `ORDER BY` clauses. Below is the syntax and explanation for creating an index, along with examples.

---

### Basic Syntax
```sql
CREATE [UNIQUE] INDEX index_name
ON table_name (column_name [ASC | DESC], ...)
[options];
```

#### Key Components
- **`[UNIQUE]`**: Optional. Ensures no duplicate values are allowed in the indexed column(s). Omit this if duplicates are allowed.
- **`index_name`**: The name you give to the index (must be unique within the schema).
- **`table_name`**: The name of the table where the index will be created.
- **`column_name`**: The column(s) to index. You can specify multiple columns for a composite index.
- **`[ASC | DESC]`**: Optional. Specifies the sort order (ascending or descending). Default is `ASC`.
- **`[options]`**: Additional options like `CLUSTER`, `INCLUDE`, or storage specifications (optional, depending on needs).

---

### Examples

#### 1. Create a Simple Index
To create an index on the `employee_id` column of the `employees` table:
```sql
CREATE INDEX idx_employee_id
ON employees (employee_id);
```
- This creates a non-unique index, allowing duplicate `employee_id` values.

#### 2. Create a Unique Index
To create a unique index on the `email` column (no duplicate emails allowed):
```sql
CREATE UNIQUE INDEX idx_email
ON employees (email);
```
- If duplicate values exist in `email`, this will fail with an error.

#### 3. Create a Composite Index
To create an index on multiple columns, such as `last_name` and `first_name`:
```sql
CREATE INDEX idx_name
ON employees (last_name, first_name);
```
- This is useful for queries filtering or sorting by both columns.

#### 4. Create an Index with Descending Order
To create an index on `hire_date` in descending order:
```sql
CREATE INDEX idx_hire_date
ON employees (hire_date DESC);
```
- Helpful for queries like `ORDER BY hire_date DESC`.

#### 5. Create a Clustered Index (Optional)
A clustered index determines the physical order of data in the table (only one per table):
```sql
CREATE INDEX idx_employee_id_clust
ON employees (employee_id)
CLUSTER;
```
- Note: Use this sparingly, as it reorganizes the table physically.

---

### Additional Options
- **`INCLUDE (column_name)`**: Adds non-key columns to the index for faster retrieval (Db2 LUW feature):
  ```sql
  CREATE INDEX idx_salary
  ON employees (department_id)
  INCLUDE (salary);
  ```
- **`SPECIFICATION ONLY`**: Creates the index definition without building it (for deferred population):
  ```sql
  CREATE INDEX idx_temp
  ON employees (employee_id)
  SPECIFICATION ONLY;
  ```

---

### Key Notes
1. **Permissions**: You need the `INDEX` privilege on the table or appropriate authority (e.g., `DBADM`).
2. **Existing Data**: If creating a `UNIQUE` index, the table must not already contain duplicate values in the indexed column(s), or the command will fail.
3. **Naming**: Index names must be unique within the schema.
4. **Performance**: Indexes speed up reads but can slow down writes (`INSERT`, `UPDATE`, `DELETE`) due to maintenance overhead.
5. **Verification**: After creating, check the index with:
   ```sql
   SELECT INDNAME, COLNAMES 
   FROM SYSCAT.INDEXES 
   WHERE TABNAME = 'YOUR_TABLE_NAME' 
   AND TABSCHEMA = 'YOUR_SCHEMA_NAME';
   ```

---

### Example Workflow
Suppose you have an `employees` table and want to index `department_id` for faster queries:
```sql
CREATE INDEX idx_department_id
ON employees (department_id);
```
Then verify:
```sql
SELECT INDNAME, COLNAMES 
FROM SYSCAT.INDEXES 
WHERE TABNAME = 'EMPLOYEES' 
AND TABSCHEMA = 'MY_SCHEMA';
```

#### Output
```
INDNAME           COLNAMES
----------------  -----------
IDX_DEPARTMENT_ID +DEPARTMENT_ID
```

---

Let me know if you need help with a specific index or additional options!