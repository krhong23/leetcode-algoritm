-- 1141. User Activity for the Past 30 Days I
-- Write an SQL query to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively.
-- A user was active on someday if they made at least one activity on that day.
-- Return the result table in any order.
-- case 01)
  SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
    FROM Activity
GROUP BY activity_date
HAVING activity_date <= '2019-07-27' AND activity_date > '2019-06-27'
-- case 2)
  SELECT activity_date AS day, COUNT(DISTINCT(user_id)) AS active_users
    FROM activity
   WHERE DATEDIFF('2019-07-27', activity_date) <30 AND activity_date<='2019-07-27'
GROUP BY 1

-- 1693. Daily Leads and Partners
-- Write an SQL query that will, for each date_id and make_name, return the number of distinct lead_id's and distinct partner_id's.
-- Return the result table in any order.
  SELECT date_id, make_name, COUNT(DISTINCT lead_id) AS 'unique_leads', COUNT(DISTINCT partner_id) AS 'unique_partners'
    FROM DailySales
GROUP BY date_id, make_name

-- 1729. Find Followers Count
-- Write an SQL query that will, for each user, return the number of followers.
-- Return the result table ordered by user_id.
  SELECT user_id, COUNT(follower_id) AS 'followers_count'
    FROM Followers
GROUP BY user_id
ORDER BY user_id

-- 586. Customer Placing the Largest Number of Orders
-- Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.
-- The test cases are generated so that exactly one customer will have placed more orders than any other customer.
  SELECT customer_number
    FROM (SELECT COUNT(order_number) AS CNT, customer_number FROM Orders GROUP BY customer_number) AS T1
ORDER BY CNT DESC
   LIMIT 1

-- 511. Game Play Analysis I
-- Write an SQL query to report the first login date for each player.
-- Return the result table in any order.
  SELECT player_id, MIN(event_date) AS first_login
    FROM Activity
GROUP BY player_id