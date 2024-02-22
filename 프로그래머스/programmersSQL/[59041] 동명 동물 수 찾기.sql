-- 동물 보호소에 들어온 동물 이름 중 두 번 이상 쓰인 이름
-- 해당 이름이 쓰인 횟수를 조회
-- 결과는 이름이 없는 동물은 집계에서 제외하며, 결과는 이름 순으로 조회

SELECT name, count(*)
FROM ANIMAL_INS
WHERE name is not null
GROUP BY NAME HAVING COUNT(*) >= 2
order by name 