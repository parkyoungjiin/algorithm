SELECT a.AUTHOR_ID, a.AUTHOR_NAME, b.category, sum((b.price * s.sales)) as TOTAL_SALES
FROM BOOK b 
    JOIN BOOK_SALES s ON b.BOOK_ID = s.BOOK_ID 
    JOIN AUTHOR a ON b.AUTHOR_ID = a.AUTHOR_ID
WHERE s.SALES_DATE LIKE '2022-01%'
group by b.category, a.AUTHOR_ID
order by a.AUTHOR_ID, b.CATEGORY desc;