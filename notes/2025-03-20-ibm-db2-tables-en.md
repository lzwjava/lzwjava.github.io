---
title: Count Tables in IBM DB2 Using DBeaver
lang: en
layout: post
audio: false
translated: false
generated: true
---

To determine the number of tables in a database in IBM DB2 using DBeaver and SQL, you can execute a specific SQL query against the system catalog. In IBM DB2, the `SYSCAT.TABLES` system catalog view contains metadata about all tables in the database. Here’s how you can do it:

### Steps to Find the Number of Tables

1. **Connect to the Database in DBeaver**  
   When you use DBeaver, ensure you are connected to the specific IBM DB2 database you want to query. DBeaver establishes a connection to a single database, and the queries you run will apply to that database’s context.

2. **Query the `SYSCAT.TABLES` View**  
   The `SYSCAT.TABLES` view includes information about all table-like objects in the database, such as tables, views, aliases, and more. To count only the tables, you need to filter by the `TYPE` column, where `'T'` represents actual tables.

3. **Write the SQL Query**  
   Use the following SQL query to count the number of tables:
   ```sql
   SELECT COUNT(*) 
   FROM SYSCAT.TABLES 
   WHERE TYPE = 'T';
   ```
   - `COUNT(*)` calculates the total number of rows that match the condition.
   - `SYSCAT.TABLES` is the system catalog view.
   - `WHERE TYPE = 'T'` ensures that only tables (not views or other objects) are counted.

4. **Execute the Query in DBeaver**  
   Open the SQL editor in DBeaver, paste the query, and run it. The result will be a single number representing the total number of tables in the database.

### Important Notes
- **Scope of the Query**: Since `SYSCAT.TABLES` is database-specific in IBM DB2, this query will count all tables in the database you are connected to in DBeaver, across all schemas.
- **Including All Tables**: This query includes both user-created tables and system tables (e.g., those in schemas like `SYSIBM` or `SYSCAT`). If you want to count only user tables, you can exclude system schemas by adding a condition, such as:
   ```sql
   SELECT COUNT(*) 
   FROM SYSCAT.TABLES 
   WHERE TYPE = 'T' 
   AND TABSCHEMA NOT IN ('SYSIBM', 'SYSCAT', 'SYSSTAT', 'SYSFUN', 'SYSPROC', 'SYSIBMADM');
   ```
   However, since your question doesn’t specify excluding system tables, the simpler query above is sufficient.
- **Table Types**: The `TYPE = 'T'` filter ensures that only persistent tables are counted, excluding views (`TYPE = 'V'`), aliases, or temporary tables (which are typically not stored in `SYSCAT.TABLES`).

### Final Answer
To know how many tables are in your IBM DB2 database using DBeaver and SQL, execute this query in DBeaver’s SQL editor:
```sql
SELECT COUNT(*) FROM SYSCAT.TABLES WHERE TYPE = 'T';
```
This will return the total number of tables in the database.

---

In DB2, a database management system, **tabname** and **tabschema** are terms commonly associated with identifying tables within the database, particularly in the context of system catalog tables like `SYSCAT.TABLES`.

- **tabschema**: This refers to the schema name of a table. A schema in DB2 is a namespace or collection of database objects (such as tables, views, and indexes) that helps organize and manage them. The `TABSCHEMA` column in the system catalog specifies the schema to which a particular table belongs.

- **tabname**: This refers to the name of the table itself within its schema. The `TABNAME` column in the system catalog stores the individual name of the table, unique within its schema.

### Key Difference
The primary difference between **tabname** and **tabschema** is that **tabschema** identifies the schema (the organizational group or namespace) that contains the table, while **tabname** identifies the specific table within that schema. Together, they form a fully qualified table name (e.g., `schema_name.table_name`), which uniquely identifies a table in the database, especially when multiple schemas might contain tables with the same name.

### Example
In the `SYSCAT.TABLES` system catalog table:
- If a table is listed with `TABSCHEMA = 'EMPLOYEE'` and `TABNAME = 'DETAILS'`, the schema name is `EMPLOYEE`, and the table name within that schema is `DETAILS`. The fully qualified name would be `EMPLOYEE.DETAILS`.

Thus, in DB2, **tabschema** refers to the schema name of a table, while **tabname** refers to the name of the table within that schema.

---

To address the query "how it differs to MySQL?" in the context of `tabname` and `tabschema` from DB2, let's explore how these concepts compare and contrast with their equivalents in MySQL.

### DB2: `tabschema` and `tabname`
In IBM DB2, tables are organized within a database using a two-part naming convention:
- **`tabschema`**: This represents the schema name, which acts as a namespace within a single database. A schema groups related database objects (like tables, views, etc.) and allows for multiple schemas to coexist within the same database.
- **`tabname`**: This is the name of the table within a specific schema. Together, `tabschema.tabname` uniquely identifies a table in the database.

For example, within a DB2 database, you might have `schema1.table1` and `schema2.table1`, where `schema1` and `schema2` are distinct schemas within the same database, each containing a table named `table1`. This structure is reflected in DB2's system catalog table `SYSCAT.TABLES`, where:
- `TABSCHEMA` is the column for the schema name.
- `TABNAME` is the column for the table name.

### MySQL: `TABLE_SCHEMA` and `TABLE_NAME`
In MySQL, the organization of tables differs due to its architectural approach:
- **`TABLE_SCHEMA`**: In MySQL, this refers to the database name. MySQL treats the terms "database" and "schema" as synonymous, meaning each database is effectively a schema. There is no additional schema layer within a database as in DB2.
- **`TABLE_NAME`**: This is the name of the table within a specific database. Tables are identified using the format `database_name.table_name`.

For instance, in MySQL, you might have `db1.table1` and `db2.table1`, where `db1` and `db2` are separate databases, each containing a table named `table1`. This structure is visible in MySQL's `information_schema.tables` view, where:
- `TABLE_SCHEMA` corresponds to the database name.
- `TABLE_NAME` corresponds to the table name within that database.

### Key Differences
Here’s how `tabname` and `tabschema` in DB2 differ from their MySQL counterparts:

1. **Terminology**:
   - **DB2**: Uses `tabschema` for the schema name and `tabname` for the table name.
   - **MySQL**: Uses `TABLE_SCHEMA` for the database (schema) name and `TABLE_NAME` for the table name. MySQL does not have direct equivalents named `tabschema` or `tabname`, but the concepts align with `TABLE_SCHEMA` and `TABLE_NAME` in its metadata.

2. **Architectural Structure**:
   - **DB2**: A database can contain multiple schemas, each acting as a namespace for tables. This allows for greater flexibility within a single database, such as having multiple `schema.table` combinations (e.g., `schema1.table1` and `schema2.table1`) sharing the same database resources.
   - **MySQL**: Each database is an independent entity equivalent to a schema, and tables reside directly within it. There is no nesting of schemas within a database. To achieve a similar separation as in DB2, you would need multiple databases (e.g., `db1.table1` and `db2.table1`), each isolated from the others.

3. **Table Identification**:
   - Both systems use a two-part naming convention:
     - DB2: `schema_name.table_name`
     - MySQL: `database_name.table_name`
   - However, in DB2, the schema is a subset of the database, while in MySQL, the database itself serves as the schema.

4. **System Catalog Scope**:
   - **DB2**: The `SYSCAT.TABLES` catalog is specific to the current database you’re connected to, so `TABSCHEMA` lists schemas within that database only.
   - **MySQL**: The `information_schema.tables` view provides metadata across all databases on the server, allowing you to query table information from multiple databases in a single query.

### Practical Implications
- In DB2, you can organize tables into multiple schemas within a single database, which is useful for access control, organization, or modular design within one database environment.
- In MySQL, achieving similar separation requires creating separate databases, as there’s no schema layer within a database. Each database operates independently, and switching between them requires changing the active database context (e.g., using `USE db_name`).

### Summary
In DB2, `tabschema` refers to the schema name within a database, and `tabname` is the table name within that schema. In MySQL, the equivalent concepts are `TABLE_SCHEMA` (the database name) and `TABLE_NAME` (the table name within that database). While both systems use a two-part identifier for tables—`schema.table` in DB2 and `database.table` in MySQL—the key difference lies in their organizational structures: DB2 supports multiple schemas within a database, whereas MySQL equates databases with schemas, with no further nesting within a database.

---

To modify the given SQL query to select only tables whose names start with 'F', let’s break it down step by step.

The original query is:

```sql
SELECT *
FROM SYSCAT.TABLES 
WHERE TYPE = 'T';
```

This query retrieves all columns from the `SYSCAT.TABLES` system catalog table in a DB2 database, filtering for rows where `TYPE = 'T'`. In DB2, the `TYPE` column in `SYSCAT.TABLES` indicates the object type, and 'T' represents tables. So, this query lists all tables in the database.

Now, we need to add a condition to filter for table names that start with 'F'. In `SYSCAT.TABLES`, the column that stores the table name is `TABNAME`. To match table names beginning with 'F', we can use the `LIKE` operator, which allows pattern matching in SQL. The pattern `'F%'` means any string that starts with 'F' followed by zero or more characters (the `%` is a wildcard).

Since the original query already has a `WHERE` clause (`TYPE = 'T'`), we need to combine the existing condition with the new one using `AND`. This ensures that both conditions—selecting only tables (`TYPE = 'T'`) and table names starting with 'F' (`TABNAME LIKE 'F%'`)—are satisfied.

Thus, the modified query becomes:

```sql
SELECT *
FROM SYSCAT.TABLES 
WHERE TYPE = 'T' AND TABNAME LIKE 'F%';
```

### Additional Considerations
- **Case Sensitivity**: In DB2, table names are typically stored in uppercase unless they were created with delimiters (e.g., `"MyTable"`). The `LIKE` operator in DB2 is case-sensitive by default, so `'F%'` will match names starting with an uppercase 'F'. If table names might be in mixed case, you could use `UPPER(TABNAME) LIKE 'F%'` to make the comparison case-insensitive. However, since the question doesn’t specify this requirement and uppercase is the common convention, we’ll stick with `'F%'`.
- **Schema**: The query searches across all schemas because no `TABSCHEMA` condition is specified. If you needed tables from a specific schema, you’d add something like `AND TABSCHEMA = 'MY_SCHEMA'`, but the question doesn’t indicate this.
- **Correctness**: The `SYSCAT.TABLES` view and columns `TYPE` and `TABNAME` are standard in DB2, and the syntax using `LIKE` with `%` is appropriate for this task.

### Final Query
The modified SQL query to select all tables whose names start with 'F' is:

```sql
SELECT *
FROM SYSCAT.TABLES 
WHERE TYPE = 'T' AND TABNAME LIKE 'F%';
```

This query will return all columns for rows in `SYSCAT.TABLES` where the object is a table (`TYPE = 'T'`) and the table name begins with 'F' (`TABNAME LIKE 'F%'`).

---

To determine what table names (TABNAME) are associated with a specific schema (TABSCHEMA) in an IBM DB2 database, you need to query the `SYSCAT.TABLES` system catalog view. This view contains metadata about all tables, views, and other objects in the database, with columns such as `TABSCHEMA` (the schema name) and `TABNAME` (the table name), among others.

The provided query:

```sql
SELECT * 
FROM SYSCAT.TABLES 
WHERE TYPE = 'T' AND TABNAME LIKE 'F%';
```

selects all columns from `SYSCAT.TABLES` where the object type is a table (`TYPE = 'T'`) and the table name starts with 'F' (`TABNAME LIKE 'F%'`). While this query retrieves information about tables across all schemas that match these conditions, it doesn’t directly address the question of finding table names for a specific schema.

To find the table names within a given schema, you should filter the results by the `TABSCHEMA` column instead of `TABNAME`. Here’s how you can do it:

### Solution
Use the following SQL query to list all table names for a specific schema:

```sql
SELECT TABNAME 
FROM SYSCAT.TABLES 
WHERE TABSCHEMA = 'your_schema_name' AND TYPE = 'T';
```

- **Explanation of the query components:**
  - `SELECT TABNAME`: Retrieves only the table names. You can modify this to `SELECT *` if you want additional details like creation time or other metadata.
  - `FROM SYSCAT.TABLES`: Queries the system catalog view that stores table information.
  - `WHERE TABSCHEMA = 'your_schema_name'`: Filters the results to include only tables in the specified schema. Replace `'your_schema_name'` with the actual schema name you’re interested in (e.g., `'MYSCHEMA'`).
  - `AND TYPE = 'T'`: Ensures that only tables are returned, excluding views, aliases, or other object types.

### Important Notes
- **Case Sensitivity**: In DB2, schema and table names are typically stored in uppercase unless they were created with double quotes (e.g., `"MySchema"`). For example, if you created a schema with `CREATE SCHEMA MYSCHEMA`, you would use `'MYSCHEMA'` in the query. If unsure, check the exact schema name by querying `SYSCAT.SCHEMATA` or `SYSCAT.TABLES`.
- **Multiple Tables**: A schema can contain multiple tables, so this query may return several rows, each representing a table name in the specified schema.

### Example
If you want to find all table names in a schema called `HR`, you would run:

```sql
SELECT TABNAME 
FROM SYSCAT.TABLES 
WHERE TABSCHEMA = 'HR' AND TYPE = 'T';
```

This might return a result like:
```
TABNAME
--------
EMPLOYEES
DEPARTMENTS
JOBS
```

Thus, to know what table names a specific schema has in an IBM DB2 database, use the query above with the appropriate schema name substituted.

