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

-- 627. Swap Salary
-- Write an SQL query to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa) with a single update statement and no intermediate temporary tables.
-- case1. Using CASE WHEN
UPDATE Salary
   SET
       sex =
       CASE sex
           WHEN 'f' THEN 'm'
           ELSE 'f'
       END ;
-- case2. Using IF
UPDATE Salary
   SET sex = IF(sex='f', 'm', 'f');

-- 196. Delete Duplicate Emails
-- Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id.
-- Note that you are supposed to write a DELETE statement and not a SELECT one.
-- After running your script, the answer shown is the Person table.
-- The driver will first compile and run your piece of code and then show the Person table.
-- The final order of the Person table does not matter.
-- case1. Using WHERE
DELETE p1
  FROM Person p1, Person p2
 WHERE p1.email = p2.email
   AND p1.id > p2.id;
-- case2. Using Not In
DELETE FROM Person
 WHERE id NOT IN
       (
           SELECT *
             FROM
                  (
                        SELECT MIN(id)
                          FROM Person
                      GROUP BY Email
                  ) AS p
       );