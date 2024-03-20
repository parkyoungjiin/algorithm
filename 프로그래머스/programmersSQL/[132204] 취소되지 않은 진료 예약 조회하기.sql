-- 2022년 4월 13일 취소되지 않은 흉부외과(CS) 진료 예약 내역을 조회하는 SQL문을 작성
-- 진료예약번호, 환자이름, 환자번호, 진료과코드, 의사이름, 진료예약일시 항목이 출력되도록 작성
-- 진료예약일시를 기준으로 오름차순 정렬해주세요
-- APNT_CNCL_YN (취소여부)
SELECT a.APNT_NO, b.PT_NAME, b.PT_NO, c.MCDP_CD, c.DR_NAME, a.APNT_YMD
    FROM (SELECT *
            FROM APPOINTMENT
                WHERE APNT_CNCL_YN = 'N' AND MCDP_CD = 'CS' AND APNT_YMD LIKE '%2022-04-13%') a
                JOIN PATIENT b ON a.PT_NO = b.PT_NO
                JOIN DOCTOR c ON a.MDDR_ID = c.DR_ID
        ORDER BY a.APNT_YMD
                