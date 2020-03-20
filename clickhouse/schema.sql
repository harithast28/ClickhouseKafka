CREATE TABLE IF NOT EXISTS filters (
  userId UInt64,
  name String,
  value String
) ENGINE = Kafka SETTINGS
            kafka_broker_list = 'kafka:9092',
            kafka_topic_list = 'jsontopic',
            kafka_group_name = 'statistics',
            kafka_format = 'JSONEachRow',
            kafka_num_consumers = 2


CREATE TABLE IF NOT EXISTS filters_stats (
  userId Nullable(UInt32),
  name String,
  value String
) ENGINE = MergeTree()
ORDER BY timestamp

CREATE MATERIALIZED VIEW IF NOT EXISTS filters_consumer TO filters_stats
  AS SELECT * FROM filters;
