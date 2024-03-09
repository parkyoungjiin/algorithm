-- 보호소에서 중성화 수술을 거친 동물 정보
-- 보호소에 들어올 당시에는 중성화되지 않았지만, 보호소를 나갈 당시에는 중성화된 동물
SELECT i.ANIMAL_ID, i.ANIMAL_TYPE, i.NAME
    FROM ANIMAL_INS i JOIN ANIMAL_OUTS o ON i.ANIMAL_ID = o.ANIMAL_ID
        WHERE i.SEX_UPON_INTAKE LIKE 'Intact%' AND (o.SEX_UPON_OUTCOME LIKE 'Spayed%' OR o.SEX_UPON_OUTCOME LIKE 'Neutered%')
            ORDER BY i.ANIMAL_ID