TYPE=VIEW
query=select `performance_schema`.`global_status`.`VARIABLE_NAME` AS `variable_name`,`performance_schema`.`global_status`.`VARIABLE_VALUE` AS `variable_value` from `performance_schema`.`global_status` where `performance_schema`.`global_status`.`VARIABLE_NAME` like \'perf%lost\' and `performance_schema`.`global_status`.`VARIABLE_VALUE` > 0
md5=c734b24ae48c36b59fc217e2407acb24
updatable=1
algorithm=1
definer_user=mariadb.sys
definer_host=localhost
suid=0
with_check_option=0
<<<<<<< HEAD
timestamp=0001711388851485959
=======
timestamp=0001711496638725739
>>>>>>> 0223c7e (Added add_airport(), view_airport(),)
create-version=2
source=SELECT variable_name, variable_value\n  FROM performance_schema.global_status\n WHERE variable_name LIKE \'perf%lost\'\n   AND variable_value > 0;
client_cs_name=utf8mb3
connection_cl_name=utf8mb3_general_ci
view_body_utf8=select `performance_schema`.`global_status`.`VARIABLE_NAME` AS `variable_name`,`performance_schema`.`global_status`.`VARIABLE_VALUE` AS `variable_value` from `performance_schema`.`global_status` where `performance_schema`.`global_status`.`VARIABLE_NAME` like \'perf%lost\' and `performance_schema`.`global_status`.`VARIABLE_VALUE` > 0
mariadb-version=110202
