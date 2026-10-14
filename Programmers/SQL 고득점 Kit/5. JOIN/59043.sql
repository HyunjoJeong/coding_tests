-- https://school.programmers.co.kr/learn/courses/30/lessons/59043
-- 있었는데요 없었습니다 (Lv3)

SELECT
    I.ANIMAL_ID AS ANIMAl_ID,
    I.NAME AS NAME
FROM
    ANIMAL_INS I
    JOIN ANIMAL_OUTS O
        ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE
    O.DATETIME < I.DATETIME
ORDER BY
    I.DATETIME