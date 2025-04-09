---
title: Find the Primary Key in IBM Db2
lang: en
layout: post
audio: false
translated: false
generated: true
---

In IBM Db2, you can retrieve information about a table's **primary keys** and **foreign keys** by querying the system catalog views. The key views are:

- **`SYSCAT.TABCONST`**: Contains information about table constraints (e.g., primary keys, foreign keys).
- **`SYSCAT.KEYCOLUSE`**: Lists the columns involved in constraints like primary keys and foreign keys.
- **`SYSCAT.REFERENCES`**: Provides details about foreign key relationships.

Below are the steps and queries to find primary keys and foreign keys for a specific table.

---

### 1. Find the Primary Key of a Table
The primary key is a type of constraint stored in `SYSCAT.TABCONST` with a `TYPE` of `'P'`. You can join it with `SYSCAT.KEYCOLUSE` to get the column names.

#### Query
```sql
SELECT 
    TC.CONSTNAME AS PRIMARY_KEY_NAME,
    KC.COLNAME AS COLUMN_NAME,
    KC.COLSEQ AS COLUMN_POSITION
FROM 
    SYSCAT.TABCONST TC
JOIN 
    SYSCAT.KEYCOLUSE KC
    ON TC.CONSTNAME = KC.CONSTNAME 
    AND TC.TABSCHEMA = KC.TABSCHEMA 
    AND TC.TABNAME = KC.TABNAME
WHERE 
    TC.TABNAME = 'YOUR_TABLE_NAME'
    AND TC.TABSCHEMA = 'YOUR_SCHEMA_NAME'
    AND TC.TYPE = 'P'
ORDER BY 
    KC.COLSEQ;
```

#### Explanation
- **`TC.CONSTNAME`**: Name of the primary key constraint.
- **`KC.COLNAME`**: Name of the column in the primary key.
- **`KC.COLSEQ`**: Position of the column in the primary key (for composite keys).
- **`TC.TYPE = 'P'`**: Filters for primary key constraints.
- Replace `'YOUR_TABLE_NAME'` and `'YOUR_SCHEMA_NAME'` with your table and schema names.

#### Example
For a table `EMPLOYEES` in schema `MY_SCHEMA`:
```sql
SELECT 
    TC.CONSTNAME AS PRIMARY_KEY_NAME,
    KC.COLNAME AS COLUMN_NAME,
    KC.COLSEQ AS COLUMN_POSITION
FROM 
    SYSCAT.TABCONST TC
JOIN 
    SYSCAT.KEYCOLUSE KC
    ON TC.CONSTNAME = KC.CONSTNAME 
    AND TC.TABSCHEMA = KC.TABSCHEMA 
    AND TC.TABNAME = KC.TABNAME
WHERE 
    TC.TABNAME = 'EMPLOYEES'
    AND TC.TABSCHEMA = 'MY_SCHEMA'
    AND TC.TYPE = 'P'
ORDER BY 
    KC.COLSEQ;
```

#### Sample Output
```
PRIMARY_KEY_NAME  COLUMN_NAME   COLUMN_POSITION
----------------  ------------  ---------------
PK_EMPLOYEES      EMPLOYEE_ID   1
```

---

### 2. Find the Foreign Keys of a Table
Foreign keys are stored in `SYSCAT.TABCONST` with a `TYPE` of `'F'`. You can join with `SYSCAT.KEYCOLUSE` for the columns and `SYSCAT.REFERENCES` for the referenced table and columns.

#### Query
```sql
SELECT 
    TC.CONSTNAME AS FOREIGN_KEY_NAME,
    KC.COLNAME AS COLUMN_NAME,
    KC.COLSEQ AS COLUMN_POSITION,
    R.REFTABSCHEMA AS REFERENCED_SCHEMA,
    R.REFTABNAME AS REFERENCED_TABLE,
    R.REFKEYNAME AS REFERENCED_KEY_NAME
FROM 
    SYSCAT.TABCONST TC
JOIN 
    SYSCAT.KEYCOLUSE KC
    ON TC.CONSTNAME = KC.CONSTNAME 
    AND TC.TABSCHEMA = KC.TABSCHEMA 
    AND TC.TABNAME = KC.TABNAME
JOIN 
    SYSCAT.REFERENCES R
    ON TC.CONSTNAME = R.CONSTNAME 
    AND TC.TABSCHEMA = R.TABSCHEMA 
    AND TC.TABNAME = R.TABNAME
WHERE 
    TC.TABNAME = 'YOUR_TABLE_NAME'
    AND TC.TABSCHEMA = 'YOUR_SCHEMA_NAME'
    AND TC.TYPE = 'F'
ORDER BY 
    TC.CONSTNAME, KC.COLSEQ;
```

#### Explanation
- **`TC.CONSTNAME`**: Name of the foreign key constraint.
- **`KC.COLNAME`**: Name of the column in the foreign key.
- **`KC.COLSEQ`**: Position of the column in the foreign key (for composite keys).
- **`R.REFTABSCHEMA`**: Schema of the referenced table.
- **`R.REFTABNAME`**: Name of the referenced table.
- **`R.REFKEYNAME`**: Name of the referenced constraint (usually the primary key of the referenced table).
- **`TC.TYPE = 'F'`**: Filters for foreign key constraints.

#### Example
For a table `DEPARTMENTS` in schema `MY_SCHEMA`:
```sql
SELECT 
    TC.CONSTNAME AS FOREIGN_KEY_NAME,
    KC.COLNAME AS COLUMN_NAME,
    KC.COLSEQ AS COLUMN_POSITION,
    R.REFTABSCHEMA AS REFERENCED_SCHEMA,
    R.REFTABNAME AS REFERENCED_TABLE,
    R.REFKEYNAME AS REFERENCED_KEY_NAME
FROM 
    SYSCAT.TABCONST TC
JOIN 
    SYSCAT.KEYCOLUSE KC
    ON TC.CONSTNAME = KC.CONSTNAME 
    AND TC.TABSCHEMA = KC.TABSCHEMA 
    AND TC.TABNAME = KC.TABNAME
JOIN 
    SYSCAT.REFERENCES R
    ON TC.CONSTNAME = R.CONSTNAME 
    AND TC.TABSCHEMA = R.TABSCHEMA 
    AND TC.TABNAME = R.TABNAME
WHERE 
    TC.TABNAME = 'DEPARTMENTS'
    AND TC.TABSCHEMA = 'MY_SCHEMA'
    AND TC.TYPE = 'F'
ORDER BY 
    TC.CONSTNAME, KC.COLSEQ;
```

#### Sample Output
```
FOREIGN_KEY_NAME  COLUMN_NAME  COLUMN_POSITION  REFERENCED_SCHEMA  REFERENCED_TABLE  REFERENCED_KEY_NAME
----------------  -----------  ---------------  -----------------  ----------------  -------------------
FK_DEPT_EMP       EMP_ID       1                MY_SCHEMA          EMPLOYEES         PK_EMPLOYEES
```

---

### Notes
1. **Case Sensitivity**: Table and schema names in the catalog are typically uppercase unless created with quotes (e.g., `"employees"`). Use `'EMPLOYEES'` instead of `'employees'` unless you know the exact casing.
2. **Current Schema**: To find your current schema:
   ```sql
   SELECT CURRENT SCHEMA FROM SYSIBM.SYSDUMMY1;
   ```
3. **Permissions**: You need `SELECT` privileges on the `SYSCAT` views to run these queries.
4. **No Primary/Foreign Keys**: If the query returns no rows, the table has no primary key (`TYPE = 'P'`) or foreign key (`TYPE = 'F'`) defined.

---

### Verify with `DESCRIBE` (Limited)
In some Db2 environments, you can use:
```sql
DESCRIBE TABLE schema_name.table_name;
```
This may show basic constraint info, but it’s less detailed and not always available across all Db2 platforms.

Let me know if you need help with a specific table or interpreting the output!