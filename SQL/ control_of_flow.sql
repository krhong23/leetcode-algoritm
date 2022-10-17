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