import pymysql

conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='db2')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)


def getone(sql,arg):
    cursor.execute(sql,arg)
    return cursor.fetchone()



def getList(sql):
    cursor.execute(sql)
    return cursor.fetchall()


def update(sql,arg):
    cursor.execute(sql,arg)
    conn.commit()


def insert(sql, arg):

    cursor.execute(sql, arg)
    conn.commit()
    # cursor.close()
    cursor.lastrowid
    # conn.close()
