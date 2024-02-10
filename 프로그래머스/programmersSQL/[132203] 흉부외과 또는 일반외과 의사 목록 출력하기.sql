-- 코드를 입력하세요
SELECT dr_name, dr_id, mcdp_cd, date_format(hire_ymd, '%Y-%m-%d')
FROM doctor
where mcdp_cd = 'CS' or mcdp_cd = 'GS'
ORDER BY hire_ymd desc, dr_name asc