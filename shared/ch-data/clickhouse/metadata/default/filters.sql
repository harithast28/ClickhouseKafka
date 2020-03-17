ATTACH TABLE filters
(
    `userId` UInt64, 
    `name` String, 
    `value` String
)
ENGINE = Kafka
SETTINGS kafka_broker_list = 'localhost:9092', kafka_topic_list = 'jsontopic', kafka_group_name = 'statistics', kafka_format = 'JSONEachRow', kafka_num_consumers = 2
