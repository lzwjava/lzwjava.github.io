---
title: UNIQUERULE Values in IBM Db2 
lang: en
layout: post
audio: false
translated: false
generated: true
---

In the IBM Db2 system catalog view `SYSCAT.INDEXES`, the `UNIQUERULE` column indicates the uniqueness property of an index. The possible values for `UNIQUERULE` are:

- **`D`**: Duplicates are allowed (non-unique index).
- **`P`**: Primary key index (unique, associated with the table's primary key constraint).
- **`U`**: Unique index (enforces uniqueness but is not a primary key).

You mentioned "D, P, D" in your question, which seems like a typo or a misinterpretation of the output. I assume you meant to ask about the values `D`, `P`, and possibly `U` appearing in the results of your query. Let me clarify what each value represents:

---

### `UNIQUERULE` Values Explained
1. **`D` (Duplicates Allowed)**:
   - The index does not enforce uniqueness.
   - Multiple rows can have the same value(s) in the indexed column(s).
   - Example: A regular index created without the `UNIQUE` keyword.
   - Use case: Speeding up queries without restricting data.

   **Example**:
   ```sql
   CREATE INDEX idx_dept ON employees (department_id);
   ```
   If `department_id` can have duplicates, `UNIQUERULE` will be `D`.

2. **`P` (Primary Key)**:
   - The index enforces uniqueness and is tied to the table's primary key constraint.
   - Automatically created when you define a primary key on a table.
   - Only one primary key index can exist per table.
   - Use case: Ensuring a unique identifier for each row.

   **Example**:
   ```sql
   CREATE TABLE employees (
       employee_id INT NOT NULL,
       PRIMARY KEY (employee_id)
   );
   ```
   The index backing the primary key will have `UNIQUERULE = 'P'`.

3. **`U` (Unique Index)**:
   - The index enforces uniqueness but is not a primary key.
   - Created explicitly with the `CREATE UNIQUE INDEX` statement.
   - Use case: Enforcing uniqueness on columns other than the primary key (e.g., email addresses).

   **Example**:
   ```sql
   CREATE UNIQUE INDEX idx_email ON employees (email);
   ```
   Here, `UNIQUERULE` will be `U`.

---

### Sample Output Interpretation
Running your query:
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

You might see:
```
INDNAME        TABSCHEMA  TABNAME    COLNAMES       UNIQUERULE  INDEXTYPE
-------------  ---------- ---------- -------------- ----------- ---------
PK_EMPLOYEES   MY_SCHEMA  EMPLOYEES  +EMPLOYEE_ID   P           REG
IDX_EMAIL      MY_SCHEMA  EMPLOYEES  +EMAIL         U           REG
IDX_DEPT       MY_SCHEMA  EMPLOYEES  +DEPARTMENT_ID D           REG
```

- **`PK_EMPLOYEES`**: `UNIQUERULE = 'P'` → Primary key index on `employee_id`.
- **`IDX_EMAIL`**: `UNIQUERULE = 'U'` → Unique index on `email`.
- **`IDX_DEPT`**: `UNIQUERULE = 'D'` → Non-unique index on `department_id`.

---

### Why No Repeated "D, P, D"?
The values `D`, `P`, and `U` appear individually for each index in the result set, not as a sequence like "D, P, D." Each row represents one index, and `UNIQUERULE` will be one of these values based on how the index was defined. If you saw something like "D, P, D" in your output, it might be a misunderstanding of multiple rows or a formatting issue in how the results were displayed.

---

### Quick Reference
| UNIQUERULE | Meaning             | Created By                     |
|------------|---------------------|--------------------------------|
| D          | Duplicates allowed  | `CREATE INDEX` (non-unique)    |
| P          | Primary key         | `PRIMARY KEY` constraint       |
| U          | Unique index        | `CREATE UNIQUE INDEX`          |

Let me know if you have a specific output you’d like me to interpret or if you need further clarification!