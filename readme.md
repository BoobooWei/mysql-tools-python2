# MySQL参数检测报告

**当前支持的数据库版本为 5.5 5.6 5.7**

如果不提供主机登陆和数据库只读权限 ，那么，请客户在数据库中执行如下操作：

* 执行 `mysql -uxxx -pxxx -e "show global status;" > mysql_global_status.sql` 将结果保存至`mysql_global_status.sql`文件
* 执行 `mysql -uxxx -pxxx -e "show global variables;” > mysql_global_variables.sql`  将结果保存至`mysql_global_variables.sql`文件
* 将`mysql_global_status.sql` 和 `mysql_global_variables.sql` 从服务器传送到本地，并覆盖当前目录中的文件，注意文件名不要写错了。

在获取到`mysql_global_status.sql`和`mysql_global_variables.sql`后，通过python脚本在本地进行数据库性能诊断。


```bash
# 前提已经按照上面的帮助获取到数据库的全局参数配置和全局状态值，并将文件覆盖当前目录中的 *.sql 文件。
# mysql -uxxx -pxxx -e "show global status;" > mysql_global_status.sql
# mysql -uxxx -pxxx -e "show global variables;” > mysql_global_variables.sql

# 运行后，在report目录中会生成相应的报告
(venv) 02:40 PM :mysql-tools-python2 booboowei$ python get_mysql_tuning.py --VariablesFile mysql_global_variables.sql --StatusFile mysql_global_status.sql
MySQL 参数报告生成成功，请访问 report 目录查看。
```

