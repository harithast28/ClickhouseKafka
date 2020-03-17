ATTACH MATERIALIZED VIEW filters_consumer TO default.filters_stats
(
    `userId` UInt64, 
    `name` String, 
    `value` String
) AS
SELECT *
FROM default.filters
