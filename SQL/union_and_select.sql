-- 1965. Employees With Missing Information
-- Write an SQL query to report the IDs of all the employees with missing information.
-- The information of an employee is missing if:
-- The employee's name is missing,
-- or The employee's salary is missing.
-- Return the result table ordered by employee_id in ascending order.
SELECT employee_id FROM Employees WHERE employee_id NOT IN (SELECT employee_id From Salaries)
UNION
SELECT employee_id FROM Salaries WHERE employee_id NOT IN (SELECT employee_id From Employees)
ORDER BY employee_id;