-- 년, 월, 성별 별로 상품을 구매한 회원수를 집계
-- 결과는 년, 월, 성별을 기준으로 오름차순 정렬
-- 이때, 성별 정보가 없는 경우 결과에서 제외해주세요.
SELECT YEAR(sales_date) AS YEAR, MONTH(sales_date) AS MONTH, GENDER, COUNT(DISTINCT o.USER_ID) AS USERS
FROM USER_INFO u join ONLINE_SALE o on u.user_id = o.user_id
WHERE GENDER IS NOT NULL
GROUP BY YEAR(sales_date), MONTH(sales_date), GENDER
ORDER BY YEAR, MONTH, GENDER