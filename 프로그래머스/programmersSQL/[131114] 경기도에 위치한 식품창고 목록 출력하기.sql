-- 테이블에서 경기도에 위치한 창고의 ID, 이름, 주소, 냉동시설 여부를 조회하는 SQL문을 작성해주세요.
SELECT warehouse_id, warehouse_name, address, (CASE WHEN freezer_yn is null then 'N' else freezer_yn end) freezer_yn
FROM FOOD_WAREHOUSE
WHERE address LIKE '경기도%'
ORDER BY warehouse_id;