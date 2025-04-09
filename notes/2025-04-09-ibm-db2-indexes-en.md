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