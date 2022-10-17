-- 1393. Capital Gain/Loss
-- Write an SQL query to report the Capital gain/loss for each stock.
-- The Capital gain/loss of a stock is the total gain or loss after buying and selling the stock one or many times.
-- Return the result table in any order.
  SELECT stock_name,
         SUM(CASE
                WHEN operation = 'Buy' THEN -price
                ELSE price
             END) AS 'capital_gain_loss'
    FROM Stocks
GROUP BY stock_name

-- 1407. Top Travellers
-- Write an SQL query to report the distance traveled by each user.
-- Return the result table ordered by travelled_distance in descending order,
-- if two or more users traveled the same distance, order them by their name in ascending order.
  SELECT name, IFNULL(distance, 0) AS 'travelled_distance'
    FROM Users AS a
         LEFT JOIN (  SELECT user_id, SUM(distance) 'distance'
                        FROM Rides
                    GROUP BY user_id) AS b
                ON a.id = b.user_id
ORDER BY distance DESC, name ASC
