---
title: IBM DB2 Table SQL
lang: en
layout: post
audio: false
translated: false
generated: true
---

Certainly! Below is a Python script that generates a `CREATE TABLE` SQL statement for an existing table in IBM Db2. This script assumes you have access to the Db2 database and can execute SQL queries to retrieve the necessary metadata.

### Python Script to Generate `CREATE TABLE` SQL

```python
import ibm_db

def generate_create_table_sql(schema_name, table_name, conn):
    # Query to get column details
    query = f"""
    SELECT COLNAME, TYPENAME, LENGTH, SCALE, NULLS, DEFAULT, IDENTITY
    FROM SYSCAT.COLUMNS
    WHERE TABSCHEMA = '{schema_name}' AND TABNAME = '{table_name}'
    ORDER BY COLNO;
    """

    # Execute the query
    stmt = ibm_db.exec_immediate(conn, query)
    result = ibm_db.fetch_assoc(stmt)

    # Start constructing the CREATE TABLE statement
    create_table_sql = f"CREATE TABLE {schema_name}.{table_name} (\n"

    while result:
        colname = result['COLNAME']
        typename = result['TYPENAME']
        length = result['LENGTH']
        scale = result['SCALE']
        nulls = 'NOT NULL' if result['NULLS'] == 'N' else 'NULL'
        default = f"DEFAULT {result['DEFAULT']}" if result['DEFAULT'] else ''
        identity = 'GENERATED ALWAYS AS IDENTITY' if result['IDENTITY'] == 'Y' else ''

        # Construct the column definition
        col_def = f"    {colname} {typename}"
        if length:
            col_def += f"({length}"
            if scale:
                col_def += f", {scale}"
            col_def += ")"
        col_def += f" {nulls}"
        if default:
            col_def += f" {default}"
        if identity:
            col_def += f" {identity}"

        create_table_sql += col_def + ",\n"
        result = ibm_db.fetch_assoc(stmt)

    # Remove the last comma and add the closing parenthesis
    create_table_sql = create_table_sql.rstrip(",\n") + "\n);"

    return create_table_sql

# Example usage
if __name__ == "__main__":
    # Replace with your actual database connection details
    dsn = "DATABASE=your_db;HOSTNAME=your_host;PORT=your_port;PROTOCOL=TCPIP;UID=your_uid;PWD=your_pwd;"
    conn = ibm_db.connect(dsn, "", "")

    schema_name = 'your_schema'
    table_name = 'your_table'

    create_table_sql = generate_create_table_sql(schema_name, table_name, conn)
    print(create_table_sql)

    # Close the connection
    ibm_db.close(conn)
```

### Instructions

1. **Install IBM Db2 Driver**: Ensure you have the IBM Db2 driver installed. You can install it using pip:
   ```bash
   pip install ibm_db
   ```

2. **Database Connection**: Update the `dsn` variable with your actual database connection details.

3. **Run the Script**: Execute the script to generate the `CREATE TABLE` SQL statement for the specified table.

### Additional Considerations

- **Constraints and Indexes**: This script does not include primary keys, foreign keys, or indexes. You would need to query additional system catalog tables to retrieve this information and add it to the `CREATE TABLE` statement.
- **Error Handling**: Add error handling as needed to manage database connection issues or query execution errors.

Would you like further customization or assistance with any part of this script?

---

If you can use DBeaver to export the table structure to a JSON file, you can then use that JSON file to construct the `CREATE TABLE` SQL statement. Here's how you can achieve this:

### Steps to Export Table Structure to JSON using DBeaver

1. **Open DBeaver**: Connect to your IBM Db2 database.
2. **Navigate to the Table**: Find the table whose structure you want to export.
3. **Export as JSON**: Right-click on the table and select the option to export the table structure as JSON. Save the JSON file to your local machine.

### Python Script to Construct `CREATE TABLE` SQL from JSON

Once you have the JSON file, you can use the following Python script to read the JSON file and construct the `CREATE TABLE` SQL statement:

```python
import json

def generate_create_table_sql_from_json(json_file_path):
    # Load the JSON file
    with open(json_file_path, 'r') as file:
        table_data = json.load(file)

    # Extract table and schema name
    schema_name = table_data.get('schema')
    table_name = table_data.get('name')

    # Start constructing the CREATE TABLE statement
    create_table_sql = f"CREATE TABLE {schema_name}.{table_name} (\n"

    # Iterate over columns to construct the column definitions
    for column in table_data.get('columns', []):
        colname = column.get('name')
        typename = column.get('type')
        length = column.get('length')
        scale = column.get('scale')
        nulls = 'NOT NULL' if column.get('nullable') == False else 'NULL'
        default = f"DEFAULT {column.get('default')}" if column.get('default') else ''
        identity = 'GENERATED ALWAYS AS IDENTITY' if column.get('identity') == True else ''

        # Construct the column definition
        col_def = f"    {colname} {typename}"
        if length:
            col_def += f"({length}"
            if scale:
                col_def += f", {scale}"
            col_def += ")"
        col_def += f" {nulls}"
        if default:
            col_def += f" {default}"
        if identity:
            col_def += f" {identity}"

        create_table_sql += col_def + ",\n"

    # Remove the last comma and add the closing parenthesis
    create_table_sql = create_table_sql.rstrip(",\n") + "\n);"

    return create_table_sql

# Example usage
if __name__ == "__main__":
    json_file_path = 'path_to_your_json_file.json'
    create_table_sql = generate_create_table_sql_from_json(json_file_path)
    print(create_table_sql)
```

### Instructions

1. **Export JSON**: Use DBeaver to export the table structure to a JSON file.
2. **Update File Path**: In the script, update the `json_file_path` variable with the path to your exported JSON file.
3. **Run the Script**: Execute the script to generate the `CREATE TABLE` SQL statement.

### Additional Considerations

- **JSON Structure**: Ensure the JSON file contains the necessary details such as column names, data types, lengths, scales, nullability, defaults, and identity settings.
- **Constraints and Indexes**: If the JSON file includes information about constraints and indexes, you can extend the script to include them in the `CREATE TABLE` statement.

Would you like further customization or assistance with any part of this process?