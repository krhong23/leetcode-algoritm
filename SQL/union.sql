-- 175. Combine Two Tables
-- Write an SQL query to report the first name, last name, city, and state of each person in the Person table.
-- If the address of a personId is not present in the Address table, report null instead.
-- Return the result table in any order.
-- case1. Using LEFT JOIN
SELECT firstName, lastName, city, state
  FROM Person AS p LEFT JOIN Address AS a ON p.personId = a.personId
-- case2. Using Union
SELECT firstName, lastName, city, state
  FROM Person AS p, Address AS a
 WHERE p.personId = a.personId
 UNION
SELECT firstName, lastName, null, null
  FROM Person p
 WHERE p.personId NOT IN (SELECT a.personId FROM Address AS a)

-- 1581. Customer Who Visited but Did Not Make Any Transactions
-- Write an SQL query to find the IDs of the users who visited without making any transactions and the number of times they made these types of visits.
-- Return the result table sorted in any order.
-- case1. Using Subquery
  SELECT customer_id, COUNT(*) AS count_no_trans
    FROM Visits
   WHERE visit_id NOT IN (SELECT visit_id FROM Transactions)
GROUP BY customer_id
-- case2. Using Left Join
  SELECT customer_id, count(v.visit_id) AS count_no_trans
    FROM Visits AS v LEFT JOIN Transactions AS t ON v.visit_id = t.visit_id
   WHERE t.visit_id IS NULL
GROUP BY customer_id

-- 1148. Article Views I
-- Write an SQL query to find all the authors that viewed at least one of their own articles.
-- Return the result table sorted by id in ascending order.
  SELECT DISTINCT author_id AS id
    FROM Views
   WHERE author_id = viewer_id
ORDER BY author_id

-- 197. Rising Temperature
-- Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
-- Return the result table in any order.
SELECT w1.id AS 'Id'
  FROM Weather w1 JOIN Weather AS w2 ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
   AND w1.temperature > w2.temperature
