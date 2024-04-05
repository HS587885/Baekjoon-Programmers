SELECT
    SUBSTRING(DATETIME, 12, 2) AS "HOUR",
    COUNT(*) AS "COUNT"
FROM
    ANIMAL_OUTS
WHERE
    SUBSTRING(DATETIME, 12, 2) BETWEEN '09' AND '19' 
GROUP BY
    SUBSTRING(DATETIME, 12, 2)
ORDER BY
    HOUR;
