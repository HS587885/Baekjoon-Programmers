SELECT B.BOOK_ID, A.AUTHOR_NAME, SUBSTR(B.PUBLISHED_DATE, 1, 10) AS PUBLISHED_DATE
FROM BOOK B JOIN AUTHOR A ON A.AUTHOR_ID = B.AUTHOR_ID
WHERE B.CATEGORY = '경제'
ORDER BY PUBLISHED_DATE;
