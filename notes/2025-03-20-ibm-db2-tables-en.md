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