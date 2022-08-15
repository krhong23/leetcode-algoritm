-- 1873. Calculate Special Bonus
-- Write an SQL query to calculate the bonus of each employee.
-- The bonus of an employee is 100% of their salary if the ID of the employee is an odd number and the employee name does not start with the character 'M'.
-- The bonus of an employee is 0 otherwise.
-- Return the result table ordered by employee_id.
-- case1. Using IF
  SELECT employee_id, IF(employee_id%2 = 1 AND name NOT LIKE 'M%', salary, 0) as bonus
    FROM Employees
ORDER BY employee_id;
-- case2. Using CASE WHEN
  SELECT employee_id,
    CASE
        WHEN employee_id%2 = 1 AND name NOT LIKE 'M%' THEN salary
        ELSE 0
  END AS bonus
    FROM Employees
ORDER BY employee_id;