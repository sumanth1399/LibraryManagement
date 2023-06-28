# # import mysql
import mysql.connector as mysql

# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Sumodeepu@1999",
#     database="LibraryManagement",
# )


# def addbook():
#     bname = input("Enter book name: ")
#     bcode = input("Enter book code:")
#     total = input("Total books:")
#     sub = input("Enter subject:")
#     data = (bname, bcode, total, sub)
#     sql = "insert into books(bname,bcode,total,subject) values(%s,%s,%s,%s)"
#     c = mydb.cursor()
#     c.execute(sql, data)
#     mydb.commit()
#     print(".............")
#     print("Data entered successfully")
#     main()


# def issueb():
#     name = input("Enter name:")
#     rno = input("Enter rno:")
#     code = input("Enter book code:")
#     date = input("Enter date:")
#     sql = "insert into issue(name,regno,bcode,idate) values(%s,%s,%s,%s)"
#     data = (name, rno, code, date)
#     c = mydb.cursor()
#     c.execute(sql, data)
#     mydb.commit()
#     print("...............")
#     print("Book issued to :", name)
#     main()
#     bookup(code, -1)


# def submitb():
#     name = input("Enter name:")
#     regno = input("Enter rno:")
#     code = input("Enter book code:")
#     sdate = input("Enter date:")
#     sql = "insert into submit(name,regno,bcode,sdate) values(%s,%s,%s,%s)"
#     data = (name, regno, code, sdate)
#     c = mydb.cursor()
#     c.execute(sql, data)
#     mydb.commit()
#     print("...............")
#     print("Book submitted from :", name)
#     bookup(code, 1)


# def bookup(co, u):
#     sql = "select TOTAL from books where BCODE = %s"
#     data = (co,)
#     c = mydb.cursor()
#     c.execute(sql, data)
#     myresult = c.fetchone()
#     t = myresult[0] + u
#     sql = "update books set TOTAL = %s where BCODE = %s"
#     d = (t, co)
#     c.execute(sql, d)
#     mydb.commit()
#     main()


# def dbook():
#     ac = input("Enter book code:")
#     sql = "delete from books where BCODE = %s"
#     data = (ac,)
#     c = mydb.cursor()
#     c.execute(sql, data)
#     mydb.commit()
#     main()


# def dispbook():
#     sql = "select * from books"
#     c = mydb.cursor()
#     c.execute(sql)
#     myresult = c.fetchall()
#     for i in myresult:
#         print("Book name:", i[0])
#         print("Book code:", i[1])
#         print("Total:", i[2])
#         print("................")
#     main()


# def main():
#     print(
#         """............LIBRARY MANAGEMENT.............
#     1.Add book
#     2.Issue book
#     3.Submit book
#     4.Delete book
#     5.Display book
#     """
#     )
#     choice = input("Enter task no:")
#     print("............................")
#     if choice == "1":
#         addbook()
#     elif choice == "2":
#         issueb()
#     elif choice == "3":
#         submitb()
#     elif choice == "4":
#         dbook()
#     elif choice == "5":
#         dispbook()
#     else:
#         print("wrong choice")
#         main()


# def password():
#     import random

#     ps = random.randint(1000, 2000)
#     user = input("Enter Username: ")
#     print("Your password is:", ps)

#     verify = input("Enter password:")

#     if verify == str(ps):
#         main()
#     else:
#         verify != str(ps)
#         print("wrong password")
#         password()


# password()
db = mysql.connect(
    host="localhost",
    user="root",
    password="Sumodeepu@1999",
    database="LibraryManagement",
)
cursor = db.cursor(BufferError(True))


def student_session():
    while 1:
        print("1. Add Book")
        print("2. Show Books")

        user_option = input("Option : ")
        if user_option == "1":
            addbook()
        elif user_option == "2":
            showb()
        else:
            print("Wrong Option")


def addbook():
    bname = input("Enter book name: ")
    bcode = input("Enter book code:")
    total = input("Total books:")
    #     sub = input("Enter subject:")
    data = (bname, bcode, total)
    sql = "insert into addbook(bname,bcode,total) values(%s,%s,%s)"

    cursor.execute(sql, data)
    db.commit()
    print(".............")
    print("Added Book successfully")
    print(".............")


# def showb():
#     # sql = "select * from addbook"
#     # # def dispbook():
#     # #     sql = "select * from books"
#     # #     c = mydb.cursor()
#     # cursor.execute(sql)
#     # db.commit()
#     # bnames = cursor.fetchall()
#     # for i in :
#     #     print("Book name:", i[0])
#     sql = "SELECT \
#     users.id AS user, \
#     addbook.bname AS id \
#     FROM users \
#     INNER JOIN addbook ON users.username = addbook.id"

#     cursor.execute(sql)
#     users = cursor.fetchall()

#     for x in users:
#         print(x)


# #     myresult = c.fetchall()
# #     for i in myresult:
# #         print("Book name:", i[0])
# #         print("Book code:", i[1])
# #         print("Total:", i[2])
# #         print("................")
# #     main()


def admin_session():
    while 1:
        print("")
        print("Welcome to admin panel")
        print("1. Register New Student")
        print("2. Register New Teacher")
        print("3. delete Existing Stuednt")
        print("4. delete Existing Teacher")
        print("5. Update Student Details")
        print("6. Update Teacher Details")
        print("7. Logout")

        user_option = input(str("Option : "))
        if user_option == "1":
            print("Student registration ")
            username = input("Enter Name : ")
            password = input("Enter Password : ")
            query_vals = (username, password)
            cursor.execute(
                "INSERT INTO users (username, password, privilege) VALUES (%s,%s, 'Student')",
                query_vals,
            )
            db.commit()
            print(username + " Registered Successfully")

        elif user_option == "2":
            print("Teacher regisration ")
            username = input("Enter Name : ")
            password = input("Enter Password : ")
            query_vals = (username, password)
            cursor.execute(
                "INSERT INTO users (username, password, privilege) VALUES (%s,%s, 'Teacher')",
                query_vals,
            )
            db.commit()
            print(username + " Registered Successfully")

        elif user_option == "3":
            print("Delete Existing student")
            username = input("Enter Name : ")
            query_vals = (username, "Student")
            cursor.execute(
                "DELETE FROM users WHERE username = %s AND privilege = %s",
                query_vals,
            )
            db.commit()
            if cursor.rowcount < 1:
                print("No student Found with this name")
            else:
                print(username + " Deleted Successfully")

        elif user_option == "4":
            print("Delete Existing Teacher")
            username = input("Enter Name : ")
            query_vals = (username, "Teacher")
            cursor.execute(
                "DELETE FROM users WHERE username = %s AND privilege = %s",
                query_vals,
            )
            db.commit()
            if cursor.rowcount < 1:
                print("No Teacher Found with this name")
            else:
                print(username + " Deleted Successfully")

        elif user_option == "5":
            print("Update Student Details")
            username = input("Enter Name : ")
            new_username = input("Enter New User Name: ")
            new_password = input("Enter New Password: ")
            query_vals = (new_username, new_password, username, "Student")
            cursor.execute(
                "UPDATE users SET username = %s, password = %s WHERE username = %s AND privilege = %s",
                query_vals,
            )
            db.commit()
            print(username + " Registered Successfully")
            print(cursor.rowcount, "record(s) affected")
            print("Student Details Updated")

        elif user_option == "6":
            print("Update Teacher Details")
            username = input("Enter Name : ")
            new_username = input("Enter New User Name: ")
            new_password = input("Enter New Password: ")
            query_vals = (new_username, new_password, username, "Teacher")
            cursor.execute(
                "UPDATE users SET username = %s, password = %s WHERE username = %s AND privilege = %s",
                query_vals,
            )
            db.commit()
            print(username + " Registered Successfully")
            print(cursor.rowcount, "record(s) affected")
            print("Teacher Details Updated")

        elif user_option == "7":
            print("Logged Out Successfully")
            break
        else:
            print("Wrong Option Selected")


def admin():
    print(20 * "-", "Admin Login", 20 * "-")
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username == "admin":
        if password == "password":
            admin_session()
        else:
            print("wrong password")
    else:
        print("Login details Invalid")


def student():
    print(20 * "-", "Student Login", 20 * "-")
    username = input("Enter username: ")
    password = input("Enter password: ")
    query_vals = (username, password, "Student")
    cursor.execute(
        "SELECT * FROM users WHERE username = %s AND password = %s AND privilege = %s",
        query_vals,
    )
    user = cursor.fetchone()
    if user:
        if user[2] == password and user[1] == username:
            print("Login Successful")
            student_session()
        else:
            print("Login Failed loo")
    else:
        print("Login Failed")


def main():
    while 1:
        print(print(20 * "-", "Welcome to Library", 20 * "-"))
        print("")
        print("1. Login as Student")
        print("2. Login as Teacher")
        print("3. Login as Admin")

        user_option = input(str("Option : "))
        if user_option == "1":
            student()
            print(20 * "-", "Student Login", 20 * "-")
        elif user_option == "2":
            print(20 * "-", "Teacher Login", 20 * "-")
        elif user_option == "3":
            admin()
        else:
            print("Wrong Option")


main()
