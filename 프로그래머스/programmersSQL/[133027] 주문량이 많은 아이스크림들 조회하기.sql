-- 7월 아이스크림 총 주문량 + 상반기의 아이스크림 총 주문량 큰 순서대로 상위 3개맛 조회
select t.flavor
    from (SELECT (sum(f.TOTAL_ORDER) + sum(j.TOTAL_ORDER)) AS TOTAL, f.FLAVOR
        FROM FIRST_HALF f 
        JOIN JULY j ON f.FLAVOR = j.FLAVOR
        GROUP BY f.FLAVOR
        ORDER BY TOTAL DESC) as t
    limit 3;



        




