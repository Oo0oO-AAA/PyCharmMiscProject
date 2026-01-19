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
    print('游标连接成功')

#创建新表
    creat_table =f'''
            create table if not exists test2.student(
                id int primary key auto_increment comment '自增主键',
                name varchar(20) not null comment '姓名',
                age int not null comment '年龄',
                gender varchar(20) not null comment'性别：男/女'
            );
'''
    cursor.execute(creat_table)

#插入语句
    insert_sql = f'''
        insert into student  (name, age, gender) values (%s, %s, %s)
    '''

    #单条插入
    # data_few = ('aaa',111, '男')
    # cursor.execute(insert_sql,data_few)
    # print("插入成功",{data_few})

    #多条插入
    data = [
        ('aaa',111, '男'),
        ('bbb',222, '女'),
        ('ccc',333, '男')
    ]
    cursor.executemany(insert_sql,data)
    print(f'多条语句插入成功,{data}')

    #添加5个成员
    # for i in range(5):
    #     data05 = ('aaa',i,'男')
    #     cursor.execute(insert_sql, data05)
    # print('add success')

    cursor.execute('select *  from student where age > 18  order by id')
    #查看所有数据
    res_all = cursor.fetchall()
    for i in res_all:
        print(i)

    #查看单条数据
    # res_one = cursor.fetchone()
    # print('one:',res_one)
    #查看多条数据
    # res_many = cursor.fetchmany(3)
    # print('many:',res_many)

    conn.commit()
    cursor.close()
    conn.close()

    print('The end')

if __name__ == '__main__':
    main()