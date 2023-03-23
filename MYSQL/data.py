import pymysql

usr = 'root'
pwd = 'Aaa89823'
db = 'books'

connection = pymysql.connect(
    host='localhost', port=3306, user=usr, password=pwd, database=db)
cursor = connection.cursor()
# 測試連線
sql = 'SELECT VERSION()'
cursor.execute(sql)
data = cursor.fetchone()
print("Database version : %s" % data)

connection = pymysql.connect(
    host='localhost', port=3306, user=usr, password=pwd, database=db)
cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS books")

try:
    with connection.cursor() as cursor:
        # 建立 SQL 語句
        sql = """CREATE TABLE `******` (
                `name` char(20) NOT NULL,
                `author` char(20),
                `year` int(10),
                `review` varchar (3000)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""

        # 執行 SQL 語句
        cursor.execute(sql)
    # 提交變更
    connection.commit()
finally:
    # 關閉連接
    connection.close()
