---
title: "Understanding Privileges and Authorities in IBM Db2"
lang: en
layout: post
audio: false
translated: false
generated: true
---

IBM Db2 provides a robust set of privileges and authorities to control access and operations on database objects. These privileges are categorized based on the type of object (e.g., database, schema, table, view, index) and the actions allowed (e.g., SELECT, INSERT, UPDATE). Below, I’ll outline the main types of privileges in Db2, including those related to `ROUTEAUTH`, schema, alias, table, and others, and explain how to check privileges for a grantee using the appropriate authorization (auth) tables.

### Types of Privileges in IBM Db2

Db2 privileges are divided into several categories, including database-level, schema-level, table/view-level, and object-specific privileges. Here’s a breakdown of the key privilege types relevant to your query:

1. **Database-Level Privileges** (stored in `SYSCAT.DBAUTH`):
   - These apply to the entire database and include:
     - **BINDADD**: Ability to create new packages in the database.
     - **CONNECT**: Ability to connect to the database.
     - **CREATETAB**: Ability to create tables.
     - **DBADM**: Database administration authority, granting broad control over the database.
     - **IMPLSCHEMA**: Ability to implicitly create schemas.
     - **DATAACCESS**: Access to all data in the database.
     - **ACCESSCTRL**: Ability to grant/revoke privileges.
     - **SQLADM**, **WLMADM**, **EXPLAINAUTH**, etc.: Administrative privileges for specific tasks.
   - These are high-level authorities typically assigned to administrators or specific users.

2. **Schema-Level Privileges** (stored in `SYSCAT.SCHEMAAUTH`):
   - Apply to a specific schema, which is a logical grouping of objects (tables, views, etc.).
   - Privileges include:
     - **CREATEIN**: Ability to create objects (e.g., tables, views) within the schema.
     - **ALTERIN**: Ability to alter objects in the schema (e.g., modify table definitions).
     - **DROPIN**: Ability to drop objects in the schema.
   - Example: A user with `CREATEIN` on schema `TEST` can create tables in that schema.

3. **Table and View Privileges** (stored in `SYSCAT.TABAUTH`):
   - Apply to specific tables or views. Privileges include:
     - **SELECT**: Read data from the table/view.
     - **INSERT**: Add new rows to the table.
     - **UPDATE**: Modify existing rows (can be restricted to specific columns).
     - **DELETE**: Remove rows from the table.
     - **ALTER**: Modify the table’s definition (e.g., add columns).
     - **INDEX**: Create indexes on the table.
     - **REFERENCES**: Create foreign key constraints referencing the table.
     - **CONTROL**: Full authority over the table, including the ability to drop it and grant privileges.
   - Example: `GRANT SELECT, INSERT ON MY_SCHEMA.MY_TABLE TO USER1`.

4. **Alias Privileges**:
   - Aliases in Db2 are alternative names for tables or views. Privileges on aliases are indirectly managed through the underlying table or view. No specific privilege is unique to aliases; instead, privileges are checked against the base table/view referenced by the alias.
   - For example, granting `SELECT` on an alias grants `SELECT` on the underlying table. You don’t need special authority to create an alias unless it’s in a schema not owned by the user (in which case `DBADM` or `CREATEIN` is required).

5. **ROUTEAUTH (Routine Authorization)**:
   - This applies to privileges on routines (e.g., stored procedures, user-defined functions) and is stored in `SYSCAT.ROUTINEAUTH`.
   - Privileges include:
     - **EXECUTE**: Ability to execute the routine.
     - **WITH GRANT OPTION**: Ability to grant the `EXECUTE` privilege to others.
   - Example: `GRANT EXECUTE ON PROCEDURE MY_SCHEMA.MY_PROC TO USER1`.

6. **Other Object-Specific Privileges**:
   - **Index Privileges** (`SYSCAT.INDEXAUTH`):
     - **CONTROL**: Ability to drop or modify an index. Automatically granted to the index creator.
   - **Column Privileges** (`SYSCAT.COLAUTH`):
     - **UPDATE**: Ability to update specific columns in a table.
     - **REFERENCES**: Ability to reference specific columns in foreign key constraints.
   - **Package Privileges** (`SYSCAT.PACKAGEAUTH`):
     - **BIND**: Ability to bind a package.
     - **EXECUTE**: Ability to execute a package.
   - **Sequence Privileges**:
     - **USAGE**: Ability to use the sequence in queries.
     - **ALTER**: Ability to modify the sequence.
   - **Role Privileges** (`SYSCAT.ROLEAUTH`):
     - Privileges granted to roles, which can then be assigned to users or groups.

7. **Authorities**:
   - Higher-level authorities like `SYSADM` (system administrator), `SYSCTRL`, and `SYSMAINT` are not stored in catalog views but are managed at the instance level and grant broad control over the database or system.

### Checking Privileges for a Grantee

To check privileges for a specific grantee (user, group, or role), you query the relevant system catalog views in Db2. The grantee can be a user, group, or role, identified by their authorization ID. Below are SQL queries to check privileges for a grantee across the relevant authorization tables.

#### 1. **Database-Level Privileges (`SYSCAT.DBAUTH`)**
To check database-level privileges for a grantee (e.g., `USER1`):
```sql
SELECT grantee, granteetype,
       bindaddauth, connectauth, createtabauth, dbadmauth,
       externalroutineauth, implschemaauth, loadauth,
       nofenceauth, quiesceconnectauth, securityadmauth,
       sqladmauth, wlmadmauth, explainauth, dataaccessauth,
       accessctrlauth, createsecureauth
FROM syscat.dbauth
WHERE grantee = 'USER1';
```
- **Columns**:
  - `GRANTEE`: The user, group, or role.
  - `GRANTEETYPE`: `U` (user), `G` (group), or `R` (role).
  - Privilege columns (e.g., `CONNECTAUTH`, `DBADMAUTH`) return `Y` (granted), `N` (not granted), or `G` (granted with grant option).

#### 2. **Schema Privileges (`SYSCAT.SCHEMAAUTH`)**
To check schema-level privileges for a grantee:
```sql
SELECT grantee, granteetype, schemaname,
       alterinauth, createinauth, dropinauth
FROM syscat.schemaauth
WHERE grantee = 'USER1';
```
- **Columns**:
  - `SCHEMANAME`: The schema name.
  - `ALTERINAUTH`, `CREATEINAUTH`, `DROPINAUTH`: `Y` (granted), `N` (not granted), or `G` (granted with grant option).

#### 3. **Table/View Privileges (`SYSCAT.TABAUTH`)**
To check table or view privileges for a grantee:
```sql
SELECT grantee, granteetype, tabschema, tabname,
       controlauth, alterauth, deleteauth, indexauth,
       insertauth, selectauth, updateauth, refauth
FROM syscat.tabauth
WHERE grantee = 'USER1';
```
- **Columns**:
  - `TABSCHEMA`, `TABNAME`: Schema and name of the table/view.
  - Privilege columns (e.g., `SELECTAUTH`, `INSERTAUTH`): `Y`
  - (granted), `N` (not granted), or `G` (granted with grant option).

#### 4. **Routine Privileges (`SYSCAT.ROUTINEAUTH`)**
To check privileges for routines (e.g., stored procedures, functions):
```sql
SELECT grantee, granteetype, schemaname, routinename,
       executeauth
FROM syscat.routineauth
WHERE grantee = 'USER1';
```
- **Columns**:
  - `SCHEMANAME`, `ROUTINENAME`: Schema and name of the routine.
  - `EXECUTEAUTH`: `Y` (granted), `N` (not granted), or `G` (granted with grant option).

#### 5. **Index Privileges (`SYSCAT.INDEXAUTH`)**
To check index privileges:
```sql
SELECT grantee, granteetype, tabschema, tabname, indname,
       controlauth
FROM syscat.indexauth
WHERE grantee = 'USER1';
```
- **Columns**:
  - `INDSCHEMA`, `INDNAME`: Schema and name of the index.
  - `CONTROLAUTH`: `Y` (granted) or `N` (not granted).

#### 6. **Column Privileges (`SYSCAT.COLAUTH`)**
To check column-level privileges:
```sql
SELECT grantee, granteetype, tabschema, tabname, colname,
       privtype
FROM syscat.colauth
WHERE grantee = 'USER1';
```
- **Columns**:
  - `COLNAME`: The column name.
  - `PRIVTYPE`: `U` (UPDATE) or `R` (REFERENCES).

#### 7. **Role Privileges (`SYSCAT.ROLEAUTH`)**
To check roles assigned to a grantee:
```sql
SELECT grantee, granteetype, role
FROM syscat.roleauth
WHERE grantee = 'USER1';
```
- **Columns**:
  - `ROLE`: The name of the role assigned to the grantee.

#### 8. **Comprehensive Privilege Check**
To retrieve all privileges for a grantee across multiple object types:
```sql
SELECT DISTINCT grantee, granteetype, 'DATABASE' AS object_type
FROM syscat.dbauth WHERE grantee = 'USER1'
UNION
SELECT DISTINCT grantee, granteetype, 'SCHEMA' AS object_type
FROM syscat.schemaauth WHERE grantee = 'USER1'
UNION
SELECT DISTINCT grantee, granteetype, 'TABLE' AS object_type
FROM syscat.tabauth WHERE grantee = 'USER1'
UNION
SELECT DISTINCT grantee, granteetype, 'ROUTINE' AS object_type
FROM syscat.routineauth WHERE grantee = 'USER1'
UNION
SELECT DISTINCT grantee, granteetype, 'INDEX' AS object_type
FROM syscat.indexauth WHERE grantee = 'USER1'
UNION
SELECT DISTINCT grantee, granteetype, 'COLUMN' AS object_type
FROM syscat.colauth WHERE grantee = 'USER1'
ORDER BY grantee, granteetype, object_type;
```
This query provides a high-level overview of the grantee’s privileges across different object types.

#### 9. **Checking Group Membership for Implicit Privileges**
If a user inherits privileges through a group, you can check group membership using:
```sql
SELECT * FROM TABLE (SYSPROC.AUTH_LIST_GROUPS_FOR_AUTHID('USER1')) AS T;
```
This lists all groups (including OS groups) the user belongs to, which may have privileges in Db2. You can then query the above tables with `grantee` set to the group name.

### Notes
- **Grantee Types**: `GRANTEETYPE` is `U` (user), `G` (group), or `R` (role). Ensure you specify the correct type when querying or revoking privileges.
- **Alias Privileges**: Since aliases inherit privileges from the base table/view, query `SYSCAT.TABAUTH` for the base table/view referenced by the alias.
- **With Grant Option**: A `G` in authorization columns indicates the grantee can grant the privilege to others.
- **System Catalog Access**: Users need `SELECT` privilege on the `SYSCAT` or `SYSIBM` catalog views to query them, or they must have `DBADM` or `SYSADM` authority.
- **Sources**: The information is based on Db2’s system catalog structure and privilege management, as described in IBM documentation and community resources like Stack Overflow and DataGeek.blog.[](https://stackoverflow.com/questions/38091787/how-to-show-present-privileges-on-table-in-ibm-db2-z-os-with-sql)[](https://datageek.blog/2018/01/23/db2-basics-investigating-permissions-in-an-existing-database/)[](https://www1.columbia.edu/sec/acis/db2/db2d0/db2d039.htm)

### Example
To check all table privileges for `USER1` on table `MY_SCHEMA.MY_TABLE`:
```sql
SELECT grantee, granteetype, tabschema, tabname,
       controlauth, alterauth, deleteauth, indexauth,
       insertauth, selectauth, updateauth, refauth
FROM syscat.tabauth
WHERE grantee = 'USER1' AND tabschema = 'MY_SCHEMA' AND tabname = 'MY_TABLE';
```
This returns a row showing which privileges `USER1` has on `MY_TABLE`, with `Y`, `N`, or `G` for each privilege type.

If you need more specific queries or examples (e.g., for a particular object or grantee), let me know!