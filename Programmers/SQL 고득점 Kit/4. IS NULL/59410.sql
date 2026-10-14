-- https://school.programmers.co.kr/learn/courses/30/lessons/59410
-- NULL 처리하기 (LV2)

SELECT
    ANIMAL_TYPE,
    NVL(NAME, 'No name') AS NAME,
    SEX_UPON_INTAKE
FROM
    ANIMAL_INS
ORDER BY
    ANIMAL_ID