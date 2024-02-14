TYPE=TRIGGERS
triggers='CREATE DEFINER=`admin`@`%` TRIGGER IF NOT EXISTS calculate_total_gates\nBEFORE INSERT ON airports\nFOR EACH ROW\nBEGIN\n    DECLARE gates INT;\n    \n    \n    SET gates = LEAST(ROUND(NEW.metro_population / 1000000), IF(NEW.is_hub, 11, 5));\n    \n    \n    SET NEW.total_gates = gates;\nEND'
sql_modes=1411383296
definers='admin@%'
client_cs_names='utf8mb3'
connection_cl_names='utf8mb3_general_ci'
db_cl_names='utf8mb4_general_ci'
created=1707872669859261
