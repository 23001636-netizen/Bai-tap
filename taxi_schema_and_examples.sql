-- DDL: create database and table
CREATE DATABASE IF NOT EXISTS test1;
USE test1;

CREATE TABLE IF NOT EXISTS taxi_trips (
    vendor_id VARCHAR(10),
    pickup_datetime DATETIME,
    dropoff_datetime DATETIME,
    passenger_count INT,
    trip_distance FLOAT,
    payment_type VARCHAR(20),
    fare_amount FLOAT,
    tip_amount FLOAT,
    total_amount FLOAT
);

-- DML examples
-- Insert one row
INSERT INTO taxi_trips (vendor_id, pickup_datetime, dropoff_datetime, passenger_count, trip_distance, payment_type, fare_amount, tip_amount, total_amount)
VALUES ('V1','2019-01-01 00:03:00','2019-01-01 00:13:00',1,2.5,'Credit card',10.5,2.0,12.5);

-- Bulk insert (multiple values)
INSERT INTO taxi_trips (vendor_id, pickup_datetime, dropoff_datetime, passenger_count, trip_distance, payment_type, fare_amount, tip_amount, total_amount)
VALUES
('V2','2019-01-01 00:05:00','2019-01-01 00:20:00',2,5.0,'Cash',15.0,0,15.0),
('V3','2019-01-01 00:10:00','2019-01-01 00:25:00',1,3.2,'Credit card',12.0,1.5,13.5);

-- CRUD examples
-- Read
SELECT vendor_id, pickup_datetime, dropoff_datetime FROM taxi_trips WHERE passenger_count >= 2 LIMIT 10;
-- Update
UPDATE taxi_trips SET tip_amount = tip_amount * 1.1 WHERE payment_type = 'Credit card' AND pickup_datetime >= '2019-01-01';
-- Delete
DELETE FROM taxi_trips WHERE fare_amount = 0;

-- Load data example (server-side file)
-- LOAD DATA INFILE '/path/on/server/train_part1.csv' INTO TABLE taxi_trips FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES (text);
