SELECT
    market_status,
    COUNT(*) AS total_coins,
    AVG(current_price) AS average_price
FROM crypto_market_data
GROUP BY market_status
ORDER BY average_price DESC;
