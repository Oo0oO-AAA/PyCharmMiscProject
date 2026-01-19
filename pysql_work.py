import pymysql
def main():
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        db='company',
        charset='utf8'
    )
    cursor = conn.cursor()
    print("ok")
    try:
        create_table=f'''
            create table if not exists company.employees(
                id int primary key auto_increment,
                name varchar(100) not null,
                department varchar(100) not null,
                salary FLOAT         
            );
    '''
        cursor.execute(create_table)
    except Exception as e:
        print(e)


    try:
        insert_table=f'''
            insert into company.employees(name, department, salary)values (%s, %s, %s)
    '''
        data = [
            ('张三', '销售部', 8000),
            ('李四', '技术部', 1000),
            ('王五', '人事部', 7500),
            ('aaa', '人事部', 7500),
            ('bbb', '技术部', 1111),
            ('ccc', '人事部', 2222),
            ('ddd', '技术部', 3333)
        ]
        cursor.executemany(insert_table,data)
        print("插入多条数据：",data)
    except Exception as e:
        print(e)


    try:
        select_table=f'''
                select * from company.employees where department='技术部'
                
    '''
        cursor.execute(select_table)
        data=cursor.fetchall()
        for i in data:
            print(i)
    except Exception as e:
        print(e)


    try:
        update_table=f'''
            update company.employees set salary = 8500 where name = '张三'
    '''
        cursor.execute(update_table)
        print('张三工资更新成功')
    except Exception as e:
        print(e)


    try:
        delete_table=f'''
                delete from company.employees where name = '王五'
    '''
        cursor.execute(delete_table)
        print('已删除王五数据')
    except Exception as e:
        print(e)



    try:
        select_table=f'''select * from company.employees'''
        cursor.execute(select_table)
        data_end=cursor.fetchall()
        print('The end:')
        for i in data_end:
            print(i)
    except Exception as e:
        print(e)

    conn.commit()
    cursor.close()
    conn.close()
if __name__ == '__main__':
    main()