import sqlite3


if __name__ == '__main__':
    # 创建 / 加载硬盘数据库链接
    conn = sqlite3.connect('test.db')

    # 内存数据库
    # conn = sqlite3.connect(':memory:')

    #创建一个游标 cursor
    cur = conn.cursor()

    # 建表的sql语句
    sql_text_1 = '''CREATE TABLE scores
            (姓名 TEXT,
                班级 TEXT,
                性别 TEXT,
                语文 NUMBER,
                数学 NUMBER,
                英语 NUMBER);'''
    # 执行sql语句
    cur.execute(sql_text_1)

    # 插入数据
    # 插入单条数据
    sql_text_2 = "INSERT INTO scores VALUES('A', '一班', '男', 96, 94, 98)"
    cur.execute(sql_text_2)

    # 插入多条数据
    data = [('B', '一班', '女', 78, 87, 85),
        ('C', '一班', '男', 98, 84, 90),
        ]
    cur.executemany('INSERT INTO scores VALUES (?,?,?,?,?,?)', data)

    # 手动 commit 改动
    conn.commit()

    # 查询数据
    # 查询数学成绩大于90分的学生
    sql_text_3 = "SELECT * FROM scores WHERE 数学>90"
    cur.execute(sql_text_3)

    # 获取查询结果
    cur.fetchall()

    # 关闭游标
    cur.close()

    # 关闭连接
    conn.close()

    pass