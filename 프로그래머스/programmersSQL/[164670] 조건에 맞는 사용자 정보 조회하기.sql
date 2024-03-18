-- USED_GOODS_BOARD와 USED_GOODS_USER 테이블에서 
-- 중고 거래 게시물을 3건 이상 등록한 사용자의 사용자 ID, 닉네임, 전체주소, 전화번호를 조회하는 SQL문을 작성
-- 전체 주소는 시, 도로명 주소, 상세 주소가 함께 출력되도록 해주시고, 전화번호의 경우 xxx-xxxx-xxxx 같은 형태로 하이픈 문자열(-)을 삽입하여 출력
-- 회원 ID 내림차순 정렬
SELECT b.USER_ID, b.NICKNAME, CONCAT(CITY,' ', STREET_ADDRESS1,' ',STREET_ADDRESS2) AS '전체주소', 
    CONCAT(SUBSTR(TLNO,1,3),'-',SUBSTR(TLNO,4,4),'-',SUBSTR(TLNO,8,4)) AS '전화번호'
    FROM USED_GOODS_BOARD a JOIN USED_GOODS_USER b ON a.WRITER_ID = b.USER_ID
            GROUP BY a.WRITER_ID HAVING COUNT(*) >= 3
                ORDER BY b.USER_ID DESC