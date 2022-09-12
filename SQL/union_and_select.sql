-- 1965. Employees With Missing Information
-- Write an SQL query to report the IDs of all the employees with missing information.
-- The information of an employee is missing if:
-- The employee's name is missing,
-- or The employee's salary is missing.
-- Return the result table ordered by employee_id in ascending order.
  SELECT employee_id
    FROM Employees
   WHERE employee_id NOT IN (SELECT employee_id From Salaries)
   UNION
  SELECT employee_id
    FROM Salaries
   WHERE employee_id NOT IN (SELECT employee_id From Employees)
ORDER BY employee_id;

-- 1795. Rearrange Products Table
-- Write an SQL query to rearrange the Products table so that each row has (product_id, store, price).
-- If a product is not available in a store, do not include a row with that product_id and store combination in the result table.
-- Return the result table in any order.
SELECT product_id, 'store1' as 'store' , store1 as 'price'
  FROM Products
 WHERE store1 IS NOT NULL
 UNION
SELECT product_id, 'store2' as 'store' , store2 as 'price'
  FROM Products
 WHERE store2 IS NOT NULL
 UNION
SELECT product_id, 'store3' as 'store' , store3 as 'price'
  FROM Products
 WHERE store3 IS NOT NULL