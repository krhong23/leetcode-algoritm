-- 182. Duplicate Emails
-- Write an SQL query to report all the duplicate emails.
-- Return the result table in any order.
  SELECT email AS Email
    FROM Person
GROUP BY email
  HAVING COUNT(*) > 1;

-- 1050. Actors and Directors Who Cooperated At Least Three Times
-- Write a SQL query for a report that provides the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.
-- Return the result table in any order.
  SELECT actor_id, director_id
    FROM ActorDirector
GROUP BY actor_id, director_id
  HAVING COUNT(*) >= 3

-- 1587. Bank Account Summary II
-- Write an SQL query to report the name and balance of users with a balance higher than 10000.
-- The balance of an account is equal to the sum of the amounts of all transactions involving that account.
-- Return the result table in any order.
  SELECT name, SUM(amount) AS 'balance'
    FROM Users AS a, Transactions AS b
   WHERE a.account = b.account
GROUP BY a.account
  HAVING SUM(amount) > 10000