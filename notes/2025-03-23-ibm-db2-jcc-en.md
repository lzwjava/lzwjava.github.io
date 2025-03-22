---
title: DB2 JDBC Driver
lang: en
layout: post
audio: false
translated: false
generated: true
---

I'll show you how to use the DB2 JDBC driver (db2jcc.jar) in Java to connect to and work with an IBM DB2 database.

```java
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

/**
 * This class demonstrates how to use IBM DB2 JDBC driver (db2jcc.jar)
 * to connect to a DB2 database and perform various SQL operations.
 */
public class DB2JDBCExample {

    // JDBC connection parameters
    private static final String DRIVER = "com.ibm.db2.jcc.DB2Driver";
    private static final String URL = "jdbc:db2://hostname:port/database_name";
    private static final String USER = "your_username";
    private static final String PASSWORD = "your_password";
    
    private Connection connection = null;
    
    /**
     * Establishes a connection to the DB2 database
     */
    public void connect() throws SQLException, ClassNotFoundException {
        // Load the DB2 JDBC driver
        Class.forName(DRIVER);
        
        // Establish the connection
        connection = DriverManager.getConnection(URL, USER, PASSWORD);
        System.out.println("Connected to DB2 database successfully!");
    }
    
    /**
     * Closes the database connection
     */
    public void disconnect() {
        if (connection != null) {
            try {
                connection.close();
                System.out.println("Database connection closed");
            } catch (SQLException e) {
                System.err.println("Error closing connection: " + e.getMessage());
            }
        }
    }
    
    /**
     * Executes a basic query
     */
    public void executeBasicQuery() throws SQLException {
        String sql = "SELECT employee_id, first_name, last_name, salary FROM employees";
        
        try (Statement stmt = connection.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            
            System.out.println("Employee List:");
            while (rs.next()) {
                int id = rs.getInt("employee_id");
                String firstName = rs.getString("first_name");
                String lastName = rs.getString("last_name");
                double salary = rs.getDouble("salary");
                
                System.out.println(id + ": " + firstName + " " + lastName + " ($" + salary + ")");
            }
        }
    }
    
    /**
     * Executes a query with parameter binding
     */
    public List<Employee> findEmployeesByDepartment(int departmentId) throws SQLException {
        List<Employee> employees = new ArrayList<>();
        String sql = "SELECT employee_id, first_name, last_name, salary " +
                     "FROM employees WHERE department_id = ?";
        
        try (PreparedStatement pstmt = connection.prepareStatement(sql)) {
            pstmt.setInt(1, departmentId);
            
            try (ResultSet rs = pstmt.executeQuery()) {
                while (rs.next()) {
                    Employee emp = new Employee();
                    emp.setId(rs.getInt("employee_id"));
                    emp.setFirstName(rs.getString("first_name"));
                    emp.setLastName(rs.getString("last_name"));
                    emp.setSalary(rs.getDouble("salary"));
                    employees.add(emp);
                }
            }
        }
        
        return employees;
    }
    
    /**
     * Executes a complex query with subquery and grouping
     */
    public void executeComplexQuery() throws SQLException {
        String sql = "WITH dept_stats AS (" +
                     "    SELECT department_id, AVG(salary) as avg_salary " +
                     "    FROM employees " +
                     "    GROUP BY department_id" +
                     ") " +
                     "SELECT e.employee_id, e.first_name, e.last_name, e.salary, " +
                     "       d.department_name, ds.avg_salary, " +
                     "       (e.salary - ds.avg_salary) as salary_diff " +
                     "FROM employees e " +
                     "JOIN departments d ON e.department_id = d.department_id " +
                     "JOIN dept_stats ds ON e.department_id = ds.department_id " +
                     "WHERE e.salary > ds.avg_salary * 1.2 " +
                     "ORDER BY salary_diff DESC";
        
        try (Statement stmt = connection.createStatement();
             ResultSet rs = stmt.executeQuery(sql)) {
            
            System.out.println("Employees with salary more than 20% above department average:");
            while (rs.next()) {
                int id = rs.getInt("employee_id");
                String firstName = rs.getString("first_name");
                String lastName = rs.getString("last_name");
                double salary = rs.getDouble("salary");
                String deptName = rs.getString("department_name");
                double avgSalary = rs.getDouble("avg_salary");
                double diff = rs.getDouble("salary_diff");
                
                System.out.printf("ID: %d, Name: %s %s, Salary: $%.2f, Dept: %s, " +
                                 "Dept Avg: $%.2f, Diff: $%.2f%n",
                                 id, firstName, lastName, salary, deptName, avgSalary, diff);
            }
        }
    }
    
    /**
     * Demonstrates transaction management
     */
    public void executeTransaction() throws SQLException {
        // Save the current auto-commit state
        boolean autoCommit = connection.getAutoCommit();
        
        try {
            // Disable auto-commit to start a transaction
            connection.setAutoCommit(false);
            
            // First operation: Update salary
            String updateSql = "UPDATE employees SET salary = salary * 1.1 WHERE department_id = ?";
            try (PreparedStatement pstmt = connection.prepareStatement(updateSql)) {
                pstmt.setInt(1, 10); // Department ID
                int rowsUpdated = pstmt.executeUpdate();
                System.out.println(rowsUpdated + " employee salaries updated");
            }
            
            // Second operation: Log the salary update
            String insertLogSql = "INSERT INTO salary_update_log(department_id, update_date, percentage) " +
                                 "VALUES (?, CURRENT TIMESTAMP, 10)";
            try (PreparedStatement pstmt = connection.prepareStatement(insertLogSql)) {
                pstmt.setInt(1, 10); // Department ID
                pstmt.executeUpdate();
                System.out.println("Salary update logged");
            }
            
            // If everything is successful, commit the transaction
            connection.commit();
            System.out.println("Transaction committed successfully");
            
        } catch (SQLException e) {
            // If there's an error, roll back the transaction
            connection.rollback();
            System.err.println("Transaction rolled back due to error: " + e.getMessage());
            throw e;
        } finally {
            // Restore the original auto-commit state
            connection.setAutoCommit(autoCommit);
        }
    }
    
    /**
     * Executes a batch update for better performance
     */
    public void executeBatchUpdate(List<Employee> employees) throws SQLException {
        String sql = "INSERT INTO employees(first_name, last_name, email, hire_date, department_id, salary) " +
                     "VALUES (?, ?, ?, ?, ?, ?)";
        
        try (PreparedStatement pstmt = connection.prepareStatement(sql)) {
            
            // Disable auto-commit for better batch performance
            connection.setAutoCommit(false);
            
            for (Employee emp : employees) {
                pstmt.setString(1, emp.getFirstName());
                pstmt.setString(2, emp.getLastName());
                pstmt.setString(3, emp.getEmail());
                pstmt.setDate(4, emp.getHireDate());
                pstmt.setInt(5, emp.getDepartmentId());
                pstmt.setDouble(6, emp.getSalary());
                
                // Add the parameters to the batch
                pstmt.addBatch();
            }
            
            // Execute the batch
            int[] updateCounts = pstmt.executeBatch();
            
            // Commit the transaction
            connection.commit();
            
            System.out.println("Batch insert completed: " + updateCounts.length + " employees added");
            
        } catch (SQLException e) {
            connection.rollback();
            System.err.println("Batch update failed: " + e.getMessage());
            throw e;
        } finally {
            connection.setAutoCommit(true);
        }
    }
    
    /**
     * Main method to demonstrate JDBC operations
     */
    public static void main(String[] args) {
        DB2JDBCExample example = new DB2JDBCExample();
        
        try {
            // Connect to the database
            example.connect();
            
            // Execute a basic query
            example.executeBasicQuery();
            
            // Execute a parameterized query
            List<Employee> marketingEmployees = example.findEmployeesByDepartment(20);
            System.out.println("Found " + marketingEmployees.size() + " employees in Marketing department");
            
            // Execute a complex query
            example.executeComplexQuery();
            
            // Execute a transaction
            example.executeTransaction();
            
        } catch (ClassNotFoundException e) {
            System.err.println("DB2 JDBC driver not found: " + e.getMessage());
        } catch (SQLException e) {
            System.err.println("Database error: " + e.getMessage());
        } finally {
            // Always disconnect when done
            example.disconnect();
        }
    }
    
    /**
     * Simple Employee class for the examples
     */
    public static class Employee {
        private int id;
        private String firstName;
        private String lastName;
        private String email;
        private java.sql.Date hireDate;
        private int departmentId;
        private double salary;
        
        // Getters and setters
        public int getId() { return id; }
        public void setId(int id) { this.id = id; }
        
        public String getFirstName() { return firstName; }
        public void setFirstName(String firstName) { this.firstName = firstName; }
        
        public String getLastName() { return lastName; }
        public void setLastName(String lastName) { this.lastName = lastName; }
        
        public String getEmail() { return email; }
        public void setEmail(String email) { this.email = email; }
        
        public java.sql.Date getHireDate() { return hireDate; }
        public void setHireDate(java.sql.Date hireDate) { this.hireDate = hireDate; }
        
        public int getDepartmentId() { return departmentId; }
        public void setDepartmentId(int departmentId) { this.departmentId = departmentId; }
        
        public double getSalary() { return salary; }
        public void setSalary(double salary) { this.salary = salary; }
    }
}

```

## Setting Up the DB2 JDBC Driver

Before using the code, you need to set up the DB2 JDBC driver:

1. **Download the driver**: You need the DB2 JDBC driver (db2jcc.jar) which can be found in your DB2 installation directory or downloaded from IBM's website.

2. **Add the driver to your project**:
   - For Maven projects, add this dependency:
     ```xml
     <dependency>
         <groupId>com.ibm.db2</groupId>
         <artifactId>jcc</artifactId>
         <version>11.5.8.0</version> <!-- Use appropriate version -->
     </dependency>
     ```
   - For Gradle projects:
     ```gradle
     implementation 'com.ibm.db2:jcc:11.5.8.0'
     ```
   - For non-build-tool projects, add the JAR to your classpath.

## Key Features of the Example Code

The sample code demonstrates several important DB2 JDBC operations:

1. **Basic connection management**: Properly loading the driver and establishing/closing connections
2. **Simple queries**: Executing basic SELECT statements
3. **Parameterized queries**: Using PreparedStatement to avoid SQL injection
4. **Complex queries**: Executing queries with CTEs, JOINs, and subqueries
5. **Transaction management**: Properly handling commits and rollbacks
6. **Batch operations**: Efficiently inserting multiple records
7. **Error handling**: Appropriate exception handling and resource cleanup

## Configuration Tips

- **Connection pooling**: For production applications, consider using a connection pool like HikariCP or Apache DBCP2 instead of creating new connections for each operation.
- **SSL connections**: If you need to connect securely, append `:sslConnection=true;` to your connection URL.
- **Connection URL formats**:
  - Default: `jdbc:db2://hostname:port/database_name`
  - With properties: `jdbc:db2://hostname:port/database_name:propertyName=value;`

Would you like me to explain any specific part of this code in more detail?