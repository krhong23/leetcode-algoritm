-- 175. Combine Two Tables
-- Write an SQL query to report the first name, last name, city, and state of each person in the Person table.
-- If the address of a personId is not present in the Address table, report null instead.
-- Return the result table in any order.
SELECT firstName, lastName, city, state
  FROM Person AS p LEFT JOIN Address AS a ON p.personId = a.personId

SELECT firstName, lastName, city, state
  FROM Person AS p, Address AS a
 WHERE p.personId = a.personId
 UNION
SELECT firstName, lastName, null, null
  FROM Person p
 WHERE p.personId NOT IN (SELECT a.personId FROM Address AS a)