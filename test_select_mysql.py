import pymysql

def main():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='123456',
        db='test2',
        charset='utf8'
    )
    cursor = conn.cursor()
    print("连接成功")
#     select_sql = f'''
#         select  age, gender
#         from test2.student
#         group by  age ,gender
#         order by age desc ,gender ;
#
# '''
#     cursor.execute(select_sql)
#
#     #data = cursor.fetchall()
#     #data = cursor.fetchone()
#     data = cursor.fetchmany(3)
#
#
#     print(data)

#删除
    dele_sql = f''' delete from test2.student where age < 18'''
    cursor.execute(dele_sql)


    conn.commit()
    print('受影响的行数:',{cursor.rowcount})
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()