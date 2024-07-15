import mysql.connector

# 连接到 MySQL 数据库
def get_db_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="barcode_db"
    )
    return conn

# 根据扫码人查询数据
def get_records_by_user(user):
    conn = get_db_connection()
    cursor = conn.cursor()

    # 执行数据库查询
    cursor.execute("SELECT task, barcode, scan_time, user FROM scan_records WHERE user=%s", (user,))
    data = cursor.fetchall()

    # 关闭数据库连接
    cursor.close()
    conn.close()

    return data
