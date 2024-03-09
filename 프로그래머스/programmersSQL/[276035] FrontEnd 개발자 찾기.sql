-- DEVELOPERS 테이블에서 Front End 스킬을 가진 개발자의 정보를 조회
-- ID, 이메일, 이름, 성을 조회
-- 결과는 ID를 기준으로 오름차순 정렬

SELECT ID, EMAIL, FIRST_NAME, LAST_NAME
    FROM DEVELOPERS
        WHERE SKILL_CODE & (
            SELECT SUM(CODE) FROM SKILLCODES WHERE CATEGORY = 'Front End')
    ORDER BY ID