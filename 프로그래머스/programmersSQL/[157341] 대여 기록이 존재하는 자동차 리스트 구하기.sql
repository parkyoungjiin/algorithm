--  테이블에서 자동차 종류가 '세단'인 자동차들 중 10월에 대여를 시작한 기록이 있는 자동차 ID 리스트를 출력
-- 자동차 ID 리스트는 중복이 없어야 하며, 자동차 ID를 기준으로 내림차순 정렬해주세요
SELECT DISTINCT a.CAR_ID
    FROM CAR_RENTAL_COMPANY_CAR a JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY b ON a.CAR_ID = b.CAR_ID
        WHERE a.CAR_TYPE = '세단' AND b.START_DATE >= '2022-10-01'
            ORDER BY a.CAR_ID DESC