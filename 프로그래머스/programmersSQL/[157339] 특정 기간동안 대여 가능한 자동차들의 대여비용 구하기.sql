SELECT *
FROM (SELECT r.car_id, r.car_type, r.daily_fee
        FROM CAR_RENTAL_COMPANY_CAR r JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY h ON r.CAR_ID = h.CAR_ID
            WHERE h.start_date < '2022-11-01' and h.end_date < '2022-11-01' and (r.CAR_TYPE = "세단" or r.CAR_TYPE = "SUV")) as t 
        join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p ON t.car_type = p.car_type and p.duration_type Like '%30일 이상%'
