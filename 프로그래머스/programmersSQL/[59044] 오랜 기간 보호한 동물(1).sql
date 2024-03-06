-- 아직 입양을 못 간 동물 중
-- 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회
-- 결과는 보호 시작일 순으로 조회
SELECT i.NAME, i.DATETIME
    FROM ANIMAL_INS i LEFT JOIN ANIMAL_OUTS o ON i.ANIMAL_ID = o.ANIMAL_ID
        WHERE o.ANIMAL_ID IS NULL
            ORDER BY i.DATETIME
                LIMIT 3;