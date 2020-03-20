# ClickhouseKafka

Just do a docker-compose up to get it started.

# To Run Clickhouse Server

docker exec -it <container_id_for_clickhouse_server> bash

# To Run Clickhouse Client

docker exec -it <container_id_for_clickhouse_server> clickhouse-client mn

You can run the queries in here.

# Connect to Client

docker run -it --rm --network="intranet" --link clickhouse-server:clickhouse-server yandex/clickhouse-client --host clickhouse-server
