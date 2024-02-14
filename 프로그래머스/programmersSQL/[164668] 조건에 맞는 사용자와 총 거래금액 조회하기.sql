-- JOIN, GROUP BY만 적용한 코드

SELECT USER_ID, NICKNAME, sum(PRICE) AS TOTAL_SALES
FROM USED_GOODS_BOARD b
JOIN USED_GOODS_USER u ON WRITER_ID = USER_ID
WHERE STATUS = "DONE"
GROUP BY USER_ID
HAVING TOTAL_SALES >= 700000
ORDER BY TOTAL_SALES ASC


-- 서브쿼리 코드
SELECT u.USER_ID, u.NICKNAME, b.PRICE AS TOTAL_SALES
FROM (
    select writer_id, sum(price) as price from used_goods_board
    where status="done"
            group by writer_id having price>=700000) b 
JOIN used_goods_user u ON b.writer_id = u.user_id
ORDER BY TOTAL_SALES ASC