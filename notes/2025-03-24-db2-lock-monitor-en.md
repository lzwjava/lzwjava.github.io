---
title: Monitoring Lock Activity in Db2
lang: en
layout: post
audio: false
translated: false
generated: true
---

I'll expand on how to monitor lock activity in Db2 using various tools and commands.

### Using db2pd Command

The `db2pd` command is a non-intrusive diagnostic tool that provides real-time information:

```
db2pd -locks detailed
```

This provides detailed lock information including:
- Lock holder details (application handle, authorization ID)
- Lock wait details
- Lock object type (table, row, etc.)
- Lock state (share, exclusive, etc.)
- Lock duration

For more specific lock information:
```
db2pd -transactions
db2pd -applications
db2pd -locks show detail
```

### Using Administrative Views and Table Functions

#### SYSIBMADM.SNAPLOCK View
```sql
SELECT 
    AGENT_ID, 
    TABSCHEMA, 
    TABNAME, 
    LOCK_OBJECT_TYPE, 
    LOCK_MODE, 
    LOCK_STATUS, 
    LOCK_ESCALATION 
FROM SYSIBMADM.SNAPLOCK
WHERE TABNAME = 'YOUR_TABLE_NAME'
```

#### MON_LOCKWAITS Table Function
```sql
SELECT 
    APPLICATION_HANDLE, 
    APPLICATION_NAME, 
    LOCK_OBJECT_TYPE, 
    LOCK_MODE, 
    LOCK_WAIT_START_TIME, 
    LOCK_WAIT_ELAPSED_TIME 
FROM TABLE(MON_LOCKWAITS(-2)) AS LOCKWAITS
```

#### MON_GET_LOCKS Table Function
```sql
SELECT 
    APPLICATION_HANDLE, 
    LOCK_OBJECT_TYPE, 
    LOCK_NAME, 
    LOCK_MODE, 
    LOCK_STATUS 
FROM TABLE(MON_GET_LOCKS(NULL, -2)) AS T
```

### Using ADMIN_GET_TAB_INFO Table Function
To see which applications are holding locks on specific tables:

```sql
SELECT 
    TABSCHEMA, 
    TABNAME, 
    LOCK_COUNT, 
    LOCK_WAIT_COUNT, 
    LOCK_WAIT_TIME, 
    LOCK_ESCAL_COUNT 
FROM TABLE(ADMIN_GET_TAB_INFO('', '', -2)) AS T
```

### Identify Locking Applications

```sql
SELECT 
    APPL_ID, 
    AGENT_ID, 
    APPL_NAME, 
    AUTHID, 
    LOCK_WAIT_TIME, 
    LOCKS_WAITING 
FROM TABLE(MON_GET_CONNECTION(NULL, -2)) AS CONN
WHERE LOCKS_WAITING > 0
```

### Solving Lock Contention

After identifying the lock issues:

1. **Force applications if necessary**:
   ```
   db2 force application (application-handle)
   ```

2. **Adjust isolation levels** for problematic transactions:
   ```sql
   SET CURRENT ISOLATION = CS; -- Cursor Stability
   ```

3. **Modify application behavior**:
   - Reduce transaction duration
   - Use row-level locking instead of table-level
   - Add WITH UR to read-only queries

4. **Configure lock timeouts**:
   ```sql
   UPDATE DB CFG FOR database_name USING LOCKTIMEOUT 30
   ```

These monitoring techniques help identify lock contention issues in your Db2 database so you can resolve them effectively.