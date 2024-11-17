CREATE DATABASE IF NOT EXISTS db;

CREATE TABLE IF NOT EXISTS db.assigned_orders
(
    assign_order_id UUID,
    order_id Integer,
    executer_id Integer,
    coin_coeff Float,
    coin_bonus_amount Float,
    final_coin_amount Float,
    route_information String,
    assign_time DateTime('Europe/Moscow'),
    acquire_time DateTime('Europe/Moscow')
)
ENGINE = MergeTree()
PRIMARY KEY (assign_order_id);
