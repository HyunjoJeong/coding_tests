-- https://school.programmers.co.kr/learn/courses/30/lessons/293261
-- 물고기 종류 별 대어 찾기 (Lv3)

-- 1) 정석 풀이?
SELECT
    F.ID,
    N.FISH_NAME,
    F.LENGTH
FROM
    FISH_INFO F
    JOIN FISH_NAME_INFO N
        ON F.FISH_TYPE = N.FISH_TYPE
WHERE
    (F.FISH_TYPE, F.LENGTH) IN (
        SELECT
            FISH_TYPE,
            MAX(LENGTH)
        FROM
            FISH_INFO
        GROUP BY
            FISH_TYPE
    )
ORDER BY
    F.ID

-- 2) 성능 개선판?
SELECT
    F.ID,
    N.FISH_NAME,
    F.LENGTH
FROM
    FISH_INFO F
    JOIN FISH_NAME_INFO N
        ON F.FISH_TYPE = N.FISH_TYPE
    JOIN (
        SELECT
            FISH_TYPE,
            MAX(LENGTH) AS MAX_LENGTH
        FROM
            FISH_INFO
        GROUP BY
            FISH_TYPE
    ) MAX_FISH
        ON F.FISH_TYPE = MAX_FISH.FISH_TYPE
        AND F.LENGTH = MAX_FISH.MAX_LENGTH
ORDER BY
    F.ID