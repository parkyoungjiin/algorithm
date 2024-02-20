-- 틀린 코드
-- select Month(rental.start_date) as month, rental.car_id, rental.records
--    from (
--         SELECT car_id, count(*) as records, start_date
--         FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
--         WHERE start_date between '2022-08-01' and '2022-10-31'
--         group by car_id
--    ) as rental
--    where rental.records >= 5
--    order by month, car_id desc

-- 정답 코드
select Month(rental.start_date) as month, rental.car_id, rental.records
from (
        SELECT car_id, count(*) as records, start_date
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE start_date between '2022-08-01' and '2022-10-31' and records >= 5
        group by car_id, month(start_date)
    ) as rental
order by month, car_id desc