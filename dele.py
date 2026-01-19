import pymysql
def main():
    conn = pymysql.connect(
        host='localhost',
    port=3306,
    user='root',
    password='123456',
    db='del',
    charset='utf8'
    )
    cursor = conn.cursor()
    print("ok")
    try:
        create_table = f'''
        create table if not exists del.employees(
        id int primary key auto_increment,
        name varchar(100),
        department varchar(100),
        salary float
        );
'''
        cursor.execute(create_table)
        print("表格创建成功")
    except Exception as e:
        print(e)

    try:
        insert_employees=f'''
    insert into del.employees(name, department, salary) values (%s, %s, %s);
    '''
        data = [
            ('张三','销售部',8000),
            ('李四','技术部',1000),
            ('王五','人事部',7500),
            ('aaa','人事部',7500),
            ('bbb','技术部',1111),
            ('ccc','人事部',2222),
            ('ddd','技术部',3333)

        ]
        cursor.executemany(insert_employees,data)
        print("表格插入成功", data)
    except Exception as e:
        print(e)

    try:
        select_employees=f'''
    select * from del.employees where department='技术部';
    '''
        cursor.execute(select_employees)
        vis = cursor.fetchall()
        print('技术部：')
        for row in vis:
            print(row)
    except Exception as e:
        print(e)

    try:
        update_employees=f'''
    update del.employees  set salary='8500' where name = '张三' 
    '''
        cursor.execute(update_employees)
        print('张三工资更新成功')
    except Exception as e:
        print(e)


    try:
        delete_table=f'''
    delete from del.employees where name = '王五'
    '''
        cursor.execute(delete_table)
        print('王五数据删除成功')
    except Exception as e:
        print(e)




    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    main()


print('测试')