SELECT b.category, sum(s.sales) as total_sales
FROM BOOK_SALES s JOIN BOOK b ON s.BOOK_ID  = b.BOOK_ID
WHERE LEFT(s.SALES_DATE,7) = '2022-01'
GROUP BY b.category
ORDER BY b.category;