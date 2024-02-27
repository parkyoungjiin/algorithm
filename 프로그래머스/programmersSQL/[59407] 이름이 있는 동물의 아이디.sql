-- 이름이 있는 채로 들어온 동물의 ID를 조회하는 SQL 문을 작성
--  단, ID는 오름차순 정렬되어야 합니다.
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL