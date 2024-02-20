SELECT MCDP_CD AS '진료과코드', count(*) AS '5월예약건수'
FROM APPOINTMENT
WHERE DATE_FORMAT(APNT_YMD, '%Y-%m') = '2022-05'
GROUP BY MCDP_CD
-- 별칭으로 지정한 경우 GROUP BY, ORDER BY, HAVING절에서 사용할 경우는 작은 따옴표는 붙이지 말아야 함.
-- 문자를 ORDER BY 하겠다는 의미이기 때문임.
ORDER BY 5월예약건수, 진료과코드



