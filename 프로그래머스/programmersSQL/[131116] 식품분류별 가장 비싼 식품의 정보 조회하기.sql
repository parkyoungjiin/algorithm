-- 식품분류별로 가격이 제일 비싼 식품의 분류, 가격, 이름을 조회
-- 식품분류가 '과자', '국', '김치', '식용유'인 경우만 출력
-- 결과는 식품 가격을 기준으로 내림차순 정렬
SELECT CATEGORY, MAX(PRICE) as MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE CATEGORY = '과자' or CATEGORY = '국' or CATEGORY ='김치' or CATEGORY ='식용유'
GROUP BY CATEGORY 
ORDER BY MAX_PRICE DESC

-- 위 코드를 했을 때 최대 가격은 나오지만, 최대 가격의 상품명 & 카테고리가 나오지 않음.

-- 수정 코드
SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT
WHERE PRICE IN (
            SELECT MAX(PRICE)
                FROM FOOD_PRODUCT
                    GROUP BY CATEGORY
                )
    AND CATEGORY IN ('과자', '국', '김치', '식용유')
GROUP BY CATEGORY
ORDER BY MAX_PRICE DESC

