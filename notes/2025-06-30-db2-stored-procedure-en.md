---
title: Db2 Stored Procedure Example Explained
lang: en
layout: post
audio: false
translated: false
generated: true
---

Below is an example of an IBM Db2 stored procedure script, followed by a detailed explanation of its components and functionality.

### Example Db2 Stored Procedure Script
```sql
-- Create a stored procedure to retrieve employee details by department
CREATE PROCEDURE GetEmployeeDetailsByDept (IN dept_id INTEGER)
    LANGUAGE SQL
    SPECIFIC GetEmpByDept
    DETERMINISTIC
    READS SQL DATA
BEGIN
    -- Declare variables
    DECLARE v_employee_id INTEGER;
    DECLARE v_first_name VARCHAR(50);
    DECLARE v_last_name VARCHAR(50);
    DECLARE v_salary DECIMAL(10,2);
    
    -- Declare cursor to fetch employee details
    DECLARE emp_cursor CURSOR WITH RETURN TO CALLER FOR
        SELECT employee_id, first_name, last_name, salary
        FROM employees
        WHERE department_id = dept_id
        ORDER BY last_name;
    
    -- Open the cursor
    OPEN emp_cursor;
    
    -- Optional: Error handling
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        SIGNAL SQLSTATE '75000'
        SET MESSAGE_TEXT = 'Error retrieving employee details';
    END;
END;
```

### Explanation of the Stored Procedure

#### 1. **Purpose of the Stored Procedure**
This stored procedure, `GetEmployeeDetailsByDept`, retrieves employee details (ID, first name, last name, and salary) from an `employees` table for a specified department ID. It uses a cursor to return a result set to the caller, which is useful for applications that need to process multiple rows.

#### 2. **Components of the Script**

- **CREATE PROCEDURE**: Defines the stored procedure with the name `GetEmployeeDetailsByDept`. The `IN dept_id INTEGER` specifies an input parameter (`dept_id`) that filters employees by department.

- **LANGUAGE SQL**: Indicates that the procedure is written in SQL, which is the standard for Db2 stored procedures.

- **SPECIFIC GetEmpByDept**: Assigns a unique name (`GetEmpByDept`) to the procedure for internal reference, useful when multiple procedures have the same name but different parameters.

- **DETERMINISTIC**: Specifies that the procedure always returns the same output for the same input, allowing Db2 to optimize execution by caching results.

- **READS SQL DATA**: Indicates that the procedure only reads data from the database and does not modify it.

- **BEGIN ... END**: Encloses the procedure’s logic.

#### 3. **Variable Declarations**
- The procedure declares four variables (`v_employee_id`, `v_first_name`, `v_last_name`, `v_salary`) to store intermediate data. These are not used in this example but could be used for additional logic (e.g., looping through results).

#### 4. **Cursor Definition**
- A cursor (`emp_cursor`) is defined to fetch rows from the `employees` table where the `department_id` matches the input `dept_id`.
- The `WITH RETURN TO CALLER` clause ensures the result set is returned to the calling application (e.g., a Java or Python program).
- The `ORDER BY last_name` sorts the results alphabetically by last name.

#### 5. **Cursor Operation**
- The `OPEN emp_cursor` statement executes the query and makes the result set available for the caller to fetch.

#### 6. **Error Handling**
- The `DECLARE EXIT HANDLER FOR SQLEXCEPTION` block catches any SQL errors (e.g., if the `employees` table doesn’t exist or there’s a permission issue).
- It signals a custom error with SQLSTATE `75000` and a descriptive message.

#### 7. **Assumptions**
- The procedure assumes an `employees` table exists with columns `employee_id` (INTEGER), `first_name` (VARCHAR), `last_name` (VARCHAR), `salary` (DECIMAL), and `department_id` (INTEGER).

### How to Call the Procedure
To execute this stored procedure in a Db2 environment, you can use:
```sql
CALL GetEmployeeDetailsByDept(10);
```
This retrieves all employees in department 10. The calling application (e.g., a SQL client or program) can then fetch the result set from the cursor.

### Example Use Case
Suppose you have an `employees` table:
```sql
CREATE TABLE employees (
    employee_id INTEGER,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    salary DECIMAL(10,2),
    department_id INTEGER
);
```
If the table contains:
| employee_id | first_name | last_name | salary  | department_id |
|-------------|------------|-----------|---------|---------------|
| 1           | John       | Doe       | 50000.00| 10            |
| 2           | Jane       | Smith     | 60000.00| 10            |
| 3           | Bob        | Johnson   | 55000.00| 20            |

Calling `CALL GetEmployeeDetailsByDept(10)` would return:
| employee_id | first_name | last_name | salary   |
|-------------|------------|-----------|----------|
| 1           | John       | Doe       | 50000.00 |
| 2           | Jane       | Smith     | 60000.00 |

### Additional Notes
- **Performance**: Using a cursor is efficient for returning result sets, but ensure proper indexing on `department_id` for large tables.
- **Error Handling**: The example includes basic error handling; in production, you might add more specific handlers (e.g., for `NOT FOUND` conditions).
- **Security**: Ensure the caller has appropriate permissions to access the `employees` table.
- **Modifications**: You can extend the procedure to include additional logic, like aggregating salaries or filtering by other criteria.

If you need a different type of Db2 stored procedure (e.g., one that updates data or uses loops), let me know, and I can provide another example!