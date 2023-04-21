import sqlite3
conn = sqlite3.connect('users')
cursor = conn.cursor()
cursor.execute("drop table users")
cursor.execute("""create table if not exists users(
id integer primary key,
name text,
email text)""")
conn.commit()

def insert_value(id, name, email):
        conn = sqlite3.connect('users')
        cursor = conn.cursor()
        cursor.execute("""insert into users  (id, name, email) values (:id,:name,:email) """,
                       {"id": id, "name": name, "email": email})
        conn.commit()

def select_func():
        cursor = conn.cursor()
        cursor.execute("""select * from users""")
        print(cursor.fetchall())

def select_user(id):
        cursor = conn.cursor()
        cursor.execute("""select * from users where id=:id""", {"id": id})
        print(cursor.fetchall())

def select_user2(id, name):
        cursor = conn.cursor()
        cursor.execute("""select * from users where id=:id and name=:name """, {"id": id, "name": name})
        print(cursor.fetchall())

def delete_user(id):
        cursor = conn.cursor()
        cursor.execute("""delete from users where id=:id""", {"id": id})
        print(cursor.fetchall())
        conn.commit()

def main():
        # insert_value(1, 'Глеба', 'dfgdfgd@mail.ru')
        # insert_value(2, 'Леха', 'hbfdqhwbd@mail.ru')
        # insert_value(3, 'Кирилл', 'gwthwtch@mail.ru')
        # insert_value(4, 'Глеб', 'cyjtryhrt@mail.ru')
        # insert_value(5, 'Максим', 'dzsqwdz@mail.ru')
        # insert_value(6, 'Виктория', 'gfxtrg@mail.ru')
        # insert_value(7, 'Дарья', 'brtbtcb@mail.ru')
        # insert_value(8, 'Юлия', 'xergreth@mail.ru')
        # insert_value(9, 'Мария', 'bvtyjrtyx@mail.ru')
        # insert_value(10, 'Ксения', 'xrthxrth@mail.ru')
        # insert_value(11, 'Валерия', 'jvutvjtyrhc@mail.ru')
        # insert_value(12, 'Наташа', 'qweqzfew@mail.ru')
        # insert_value(13, 'Анатолий', 'qweqweqwe@mail.ru')
        # insert_value(14, 'Денис', 'qweret@mail.ru')
        # insert_value(15, 'Евгений', 'qwerty@mail.ru')
        # insert_value(16, 'Снежана', '123@mail.ru')
        # insert_value(17, 'Юлия', 'gggggvvvv@mail.ru')
        # insert_value(18, 'София', 'hyhyuhyh@mail.ru')
        # insert_value(19, 'Дмитрий', 'vdfvcxv@mail.ru')
        # insert_value(20, 'Виктор', 'qzdrwzertf12323333@mail.ru')


        # Поиск всех пользывателей
        select_func()
        insert_value(20, 'Виктор', 'qzdrwzertf12323333@mail.ru')
        insert_value(19, 'Дмитрий', 'vdfvcxv@mail.ru')
         #Поиск по id
        select_user(19)
        # Удаление по id
        delete_user(1)
        # Поиск по id и имени
        select_user2(3, 'Кирилл')
        select_func()

main()
conn.close()