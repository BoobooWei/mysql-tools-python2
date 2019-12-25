# MySQL参数检测报告

如果不提供主机登陆和数据库只读权限 ，那么，请客户在数据库中执行如下操作：

* 执行 `mysql -uxxx -pxxx -e "show global status;" > mysql_global_status.sql` 将结果保存至`mysql_global_status.sql`文件
* 执行 `mysql -uxxx -pxxx -e "show global variables;” > mysql_global_variables.sql`  将结果保存至`mysql_global_variables.sql`文件
* 将`mysql_global_status.sql` 和 `mysql_global_variables.sql` 发送给我们

在获取到mysql_global_status.sql和mysql_global_variables.sql后，通过python脚本在我们本地进行数据库性能诊断。