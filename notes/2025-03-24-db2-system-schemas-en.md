---
title: Db2’s Built-in System Schemas
lang: en
layout: post
audio: false
translated: false
generated: true
---

Db2’s built-in system schemas—such as **SYSCAT**, **SYSIBM**, and **SYSFUN**—contain metadata, system catalog views, and built-in functions. You can query these schemas to retrieve information about database objects, optimize queries, and manage the database. Here’s how you can use them:

---

## 1. **SYSCAT Schema (System Catalog Views)**
The **SYSCAT** schema contains catalog views that provide metadata about tables, indexes, columns, and other database objects. 

### 🔹 Example Queries:
#### List all tables in the database:
```sql
SELECT TABNAME, TABSCHEMA 
FROM SYSCAT.TABLES
WHERE TYPE = 'T';
```

#### Get details about a specific table:
```sql
SELECT COLNAME, TYPENAME, LENGTH 
FROM SYSCAT.COLUMNS
WHERE TABNAME = 'EMPLOYEE';
```

#### Find all indexes on a table:
```sql
SELECT INDNAME, COLNAMES
FROM SYSCAT.INDEXES
WHERE TABNAME = 'EMPLOYEE';
```

---

## 2. **SYSIBM Schema (System Catalog Tables)**
The **SYSIBM** schema contains base system catalog tables (lower-level metadata). 

### 🔹 Example Queries:
#### Retrieve all database schemas:
```sql
SELECT SCHEMANAME FROM SYSIBM.SYSSCHEMAS;
```

#### Get column details from a table:
```sql
SELECT NAME, COLTYPE, LENGTH
FROM SYSIBM.SYSCOLUMNS
WHERE TBNAME = 'EMPLOYEE';
```

---

## 3. **SYSFUN Schema (System Functions)**
The **SYSFUN** schema contains built-in functions such as mathematical, string, and date functions.

### 🔹 Example Queries:
#### Get the current timestamp:
```sql
SELECT SYSFUN.CURRENT_TIMESTAMP FROM SYSIBM.SYSDUMMY1;
```

#### Calculate the square root of a number:
```sql
SELECT SYSFUN.SQRT(25) FROM SYSIBM.SYSDUMMY1;
```

#### Convert a string to uppercase:
```sql
SELECT SYSFUN.UPPER('hello') FROM SYSIBM.SYSDUMMY1;
```

---

## 📌 **Additional Notes:**
- **SYSCAT views** are preferred over **SYSIBM tables** for metadata queries because they are more user-friendly.
- **SYSDUMMY1** is a special table used to run functions that require a `FROM` clause.
- You can join **SYSCAT.TABLES** with **SYSCAT.COLUMNS** to get detailed metadata in a single query.

Would you like to explore specific system schemas further? 🚀