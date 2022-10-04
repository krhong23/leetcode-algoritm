-- 1141. User Activity for the Past 30 Days I
-- Write an SQL query to find the daily active user count for a period of 30 days ending 2019-07-27 inclusively.
-- A user was active on someday if they made at least one activity on that day.
-- Return the result table in any order.
  SELECT activity_date AS day, COUNT(DISTINCT user_id) AS active_users
    FROM Activity
GROUP BY activity_date
  HAVING activity_date <= '2019-07-27' AND activity_date > '2019-06-27'