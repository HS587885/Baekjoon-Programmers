
 SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS A LEFT JOIN ANIMAL_OUTS USING(ANIMAL_ID)
WHERE SEX_UPON_OUTCOME IS NULL
ORDER BY A.DATETIME
LIMIT 3