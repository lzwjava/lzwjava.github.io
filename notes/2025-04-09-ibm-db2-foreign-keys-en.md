---
title: Check Foreign Keys in IBM Db2
lang: en
layout: post
audio: false
translated: false
generated: true
---

If the query you provided returns an empty result set, it means there are no foreign key constraints defined on the `DEPARTMENTS` table in the `MY_SCHEMA` schema. This could be because:
- No foreign keys exist on that table.
- The table name or schema name is misspelled or doesn’t match the actual case (Db2 is case-sensitive in catalog lookups).
- You’re looking in the wrong schema.

I’ll simplify the query and provide alternative methods to check for foreign keys (and confirm the table’s constraints) in IBM Db2.

---

### Simplified Query to Check Foreign Keys
Here’s a simpler version of the query to list foreign keys for the `DEPARTMENTS` table:

```sql
SELECT 
    CONSTNAME AS FOREIGN_KEY_NAME,
    COLNAME AS COLUMN_NAME,
    REFTABNAME AS REFERENCED_TABLE
FROM 
    SYSCAT.TABCONST TC
JOIN 
    SYSCAT.KEYCOLUSE KC
    ON TC.CONSTNAME = KC.CONSTNAME 
    AND TC.TABSCHEMA = KC.TABSCHEMA 
    AND TC.TABNAME = KC.TABNAME
WHERE 
    TC.TABNAME = 'DEPARTMENTS'
    AND TC.TABSCHEMA = 'MY_SCHEMA'
    AND TC.TYPE = 'F';
```

#### What This Does
- Lists only the foreign key name, column name, and referenced table.
- Omits some details (like `COLSEQ` and `REFTABSCHEMA`) for simplicity.
- Still joins `SYSCAT.TABCONST` (constraints) and `SYSCAT.KEYCOLUSE` (columns in constraints).

#### If Still Empty
If this returns no rows, there are no foreign keys on `DEPARTMENTS`.

---

### Alternative Ways to Check

#### 1. Check All Constraints on the Table
To confirm whether *any* constraints (not just foreign keys) exist on `DEPARTMENTS`, use:
```sql
SELECT 
    CONSTNAME AS CONSTRAINT_NAME,
    TYPE AS CONSTRAINT_TYPE,
    TABNAME
FROM 
    SYSCAT.TABCONST
WHERE 
    TABNAME = 'DEPARTMENTS'
    AND TABSCHEMA = 'MY_SCHEMA';
```

- **`TYPE`** values:
  - `'P'`: Primary key
  - `'F'`: Foreign key
  - `'U'`: Unique constraint
  - `'C'`: Check constraint
- If this returns no rows, the table has no constraints at all.
- If it shows only `'P'` or `'U'`, there’s a primary key or unique constraint but no foreign keys.

#### Example Output
```
CONSTRAINT_NAME  CONSTRAINT_TYPE  TABNAME
---------------  ---------------  ---------
PK_DEPT          P                DEPARTMENTS
```
- This would mean `DEPARTMENTS` has a primary key but no foreign keys.

---

#### 2. Check Table Existence and Schema
Verify that `DEPARTMENTS` exists in `MY_SCHEMA`:
```sql
SELECT 
    TABNAME, 
    TABSCHEMA 
FROM 
    SYSCAT.TABLES 
WHERE 
    TABNAME = 'DEPARTMENTS' 
    AND TABSCHEMA = 'MY_SCHEMA';
```
- If this returns no rows, the table doesn’t exist in that schema, or the name/schema is incorrect.
- Db2 stores names in uppercase unless created with quotes (e.g., `"departments"`). Try `'DEPARTMENTS'` if `'departments'` fails.

---

#### 3. List All Foreign Keys in the Schema
To see if foreign keys exist elsewhere in `MY_SCHEMA` (maybe on a different table):
```sql
SELECT 
    TC.TABNAME AS TABLE_NAME,
    TC.CONSTNAME AS FOREIGN_KEY_NAME,
    KC.COLNAME AS COLUMN_NAME,
    R.REFTABNAME AS REFERENCED_TABLE
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
    TC.TABSCHEMA = 'MY_SCHEMA'
    AND TC.TYPE = 'F';
```
- This shows all foreign keys in the schema, helping you confirm if they’re defined on other tables.

---

#### 4. Check Current Schema
If you’re unsure of the schema, check your current schema:
```sql
SELECT CURRENT SCHEMA FROM SYSIBM.SYSDUMMY1;
```
- If it’s not `MY_SCHEMA`, adjust your queries or set the schema:
  ```sql
  SET SCHEMA MY_SCHEMA;
  ```

---

### Why Your Original Query Returned Empty
- **No Foreign Keys**: The most likely reason is that `DEPARTMENTS` has no foreign key constraints.
- **Case Sensitivity**: `TABNAME` and `TABSCHEMA` must match the exact case in the catalog (usually uppercase).
- **Schema Mismatch**: You might be querying the wrong schema.

---

### Next Steps
1. Run the simplified query:
   ```sql
   SELECT 
       CONSTNAME, 
       COLNAME, 
       REFTABNAME
   FROM 
       SYSCAT.TABCONST TC
   JOIN 
       SYSCAT.KEYCOLUSE KC
       ON TC.CONSTNAME = KC.CONSTNAME 
       AND TC.TABSCHEMA = KC.TABSCHEMA 
       AND TC.TABNAME = KC.TABNAME
   WHERE 
       TC.TABNAME = 'DEPARTMENTS'
       AND TC.TABSCHEMA = 'MY_SCHEMA'
       AND TC.TYPE = 'F';
   ```
2. If empty, check all constraints:
   ```sql
   SELECT CONSTNAME, TYPE, TABNAME 
   FROM SYSCAT.TABCONST 
   WHERE TABNAME = 'DEPARTMENTS' 
   AND TABSCHEMA = 'MY_SCHEMA';
   ```
3. Confirm the table exists:
   ```sql
   SELECT TABNAME, TABSCHEMA 
   FROM SYSCAT.TABLES 
   WHERE TABNAME = 'DEPARTMENTS' 
   AND TABSCHEMA = 'MY_SCHEMA';
   ```

---

### If You Want to Add a Foreign Key
If you expected a foreign key and none exists, you can add one. For example, if `DEPARTMENTS` has a `manager_id` column referencing `employee_id` in an `EMPLOYEES` table:
```sql
ALTER TABLE DEPARTMENTS
ADD CONSTRAINT fk_manager
FOREIGN KEY (manager_id)
REFERENCES EMPLOYEES (employee_id);
```

Let me know the results of these queries or if you need help adding  adding a foreign key!