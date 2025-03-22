---
title: IBM DB2 SQL Advanced Operations
lang: en
layout: post
audio: false
translated: false
generated: true
---

I'll teach you some advanced SQL operations in IBM DB2. Let's dive into nested queries, complex conditions, and advanced grouping techniques.

## Nested Queries (Subqueries)

Subqueries are queries embedded within other queries, often used in WHERE, HAVING, or FROM clauses.

### In WHERE Clause:
```sql
SELECT employee_id, last_name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```
This returns employees with salary above the average.

### Correlated Subquery:
```sql
SELECT d.dept_name, e.last_name
FROM departments d
WHERE EXISTS (
    SELECT 1 
    FROM employees e 
    WHERE e.dept_id = d.dept_id 
    AND e.salary > 100000
);
```
This finds departments that have at least one employee earning over $100,000.

### In FROM Clause (Derived Tables):
```sql
SELECT dept_name, avg_salary
FROM (
    SELECT d.dept_name, AVG(e.salary) as avg_salary
    FROM departments d
    JOIN employees e ON d.dept_id = e.dept_id
    GROUP BY d.dept_name
) AS dept_stats
WHERE avg_salary > 75000;
```

## Complex WHERE Conditions

### Using CASE in WHERE:
```sql
SELECT product_id, product_name, price
FROM products
WHERE 
    CASE 
        WHEN category = 'Electronics' THEN price < 1000
        WHEN category = 'Furniture' THEN price < 500
        ELSE price < 200
    END;
```

### Multiple Conditions with Combinations:
```sql
SELECT *
FROM orders
WHERE 
    (status = 'Pending' AND created_date > CURRENT DATE - 7 DAYS)
    OR
    (status = 'Processing' AND created_date > CURRENT DATE - 14 DAYS)
    OR
    (customer_id IN (SELECT customer_id FROM premium_customers));
```

### Using BETWEEN and IN:
```sql
SELECT order_id, customer_id, total_amount
FROM orders
WHERE 
    order_date BETWEEN '2024-01-01' AND '2024-03-31'
    AND
    shipping_method IN ('Express', 'Priority')
    AND
    total_amount > 1000;
```

## Advanced GROUP BY Operations

### GROUP BY with ROLLUP:
```sql
SELECT 
    COALESCE(region, 'All Regions') as region,
    COALESCE(country, 'All Countries') as country,
    SUM(sales) as total_sales
FROM sales_data
GROUP BY ROLLUP(region, country);
```
This produces subtotals for each group level and a grand total.

### GROUP BY with CUBE:
```sql
SELECT 
    COALESCE(year, 0) as year,
    COALESCE(quarter, 0) as quarter,
    COALESCE(product_line, 'All Products') as product_line,
    SUM(revenue) as total_revenue
FROM sales_data
GROUP BY CUBE(year, quarter, product_line);
```
This generates all possible combinations of the specified dimensions.

### GROUPING SETS:
```sql
SELECT 
    product_category,
    region,
    SUM(sales) as total_sales
FROM sales_data
GROUP BY GROUPING SETS(
    (product_category, region),
    (product_category),
    (region),
    ()
);
```
This specifies multiple grouping combinations in a single query.

## Common Table Expressions (CTEs)

```sql
WITH regional_sales AS (
    SELECT region, SUM(amount) as total_sales
    FROM orders
    GROUP BY region
),
top_regions AS (
    SELECT region
    FROM regional_sales
    ORDER BY total_sales DESC
    FETCH FIRST 3 ROWS ONLY
)
SELECT o.order_id, o.customer_id, o.amount
FROM orders o
JOIN top_regions tr ON o.region = tr.region
WHERE o.amount > 1000;
```

## Advanced JOINS

### Self JOIN:
```sql
SELECT e.employee_id, e.last_name as employee, m.last_name as manager
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.employee_id;
```

### Multiple JOINS with Complex Conditions:
```sql
SELECT 
    c.customer_name,
    p.product_name,
    o.order_date,
    SUM(od.quantity * od.unit_price) as line_total
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_details od ON o.order_id = od.order_id
JOIN products p ON od.product_id = p.product_id
WHERE 
    o.order_date > '2024-01-01'
    AND p.category IN ('Electronics', 'Appliances')
    AND c.country = 'USA'
GROUP BY c.customer_name, p.product_name, o.order_date
HAVING SUM(od.quantity * od.unit_price) > 500
ORDER BY line_total DESC;
```

## Window Functions

```sql
SELECT 
    dept_id,
    employee_id,
    salary,
    AVG(salary) OVER (PARTITION BY dept_id) as dept_avg_salary,
    salary - AVG(salary) OVER (PARTITION BY dept_id) as diff_from_avg,
    RANK() OVER (PARTITION BY dept_id ORDER BY salary DESC) as salary_rank
FROM employees;
```

Would you like me to elaborate on any of these techniques or provide more specific examples for a particular DB2 scenario?