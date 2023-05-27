SELECT
    r.part_number,
    r.manufacturer,
    r.price AS price_previous,
    s.price AS price_current,
    CASE
        WHEN r.price < s.price THEN 'Previous Price is Better'
        WHEN r.price > s.price THEN 'Current Price is Better'
        ELSE 'Prices are Equal'
    END AS price_comparison
FROM
    result1 r
INNER JOIN
    sample_supplier1 s ON r.part_number = s.part_number AND r.manufacturer = s.manufacturer
WHERE
    r.price > 0 AND s.price > 0