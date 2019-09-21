import pymysql

# 连接MySQL数据库

connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='root',
                             db='test', charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

try:

    # 通过cursor创建游标

    cursor = connection.cursor()

    # 创建sql 语句

    sql = "select * from student"

    # 执行sql语句

    cursor.execute(sql)

    # 获取所有记录列表

    results = cursor.fetchall() 
    # print(results) 
    for data in results:      
        # 打印结果      
        print(data)

except Exception:
    print("查询失败")

# 关闭游标连接cursor.close()# 关闭数据库连接connection.close()
