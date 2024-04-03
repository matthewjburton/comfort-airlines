TYPE=TRIGGERS
triggers='CREATE DEFINER=`admin`@`%` TRIGGER IF NOT EXISTS set_flight_angle\nBEFORE INSERT ON flights\nFOR EACH ROW\nBEGIN\n    IF NEW.angle_of_flight IS NULL THEN\n        SET @departure_lat = (SELECT latitude FROM airports WHERE airport_id = NEW.departure_airport_id);\n        SET @departure_lon = (SELECT longitude FROM airports WHERE airport_id = NEW.departure_airport_id);\n        SET @destination_lat = (SELECT latitude FROM airports WHERE airport_id = NEW.destination_airport_id);\n        SET @destination_lon = (SELECT longitude FROM airports WHERE airport_id = NEW.destination_airport_id);\n        SET @bearing_angle = DEGREES(ATAN2(SIN(RADIANS(@destination_lon - @departure_lon)) * COS(RADIANS(@destination_lat)), COS(RADIANS(@departure_lat)) * SIN(RADIANS(@destination_lat)) - SIN(RADIANS(@departure_lat)) * COS(RADIANS(@destination_lat)) * COS(RADIANS(@destination_lon - @departure_lon))));\n        \n        SET NEW.angle_of_flight = @bearing_angle;\n    END IF;\nEND'
sql_modes=1411383296
definers='admin@%'
client_cs_names='utf8mb3'
connection_cl_names='utf8mb3_general_ci'
db_cl_names='utf8mb4_general_ci'
created=1712156222172579
