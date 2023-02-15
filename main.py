print("***************SURAJKUND INTERNATIONAL SCHOOL MANAGEMENT***************")

# creating database
import mysql.connector as sql
mydb = sql.connect(host='localhost', user='your_user', passwd='your_pass', database='school_management')
mycursor = mydb.cursor()
mycursor.execute("create database if not exists school_management")
mycursor.execute("use school_management")


# creating tables
mycursor.execute("create table if not exists students(name varchar(50) not null primary key , class varchar(20) not null, roll_no integer not null, gender char(1) not null)")
mycursor.execute("create table if not exists staff(name varchar(50) not null primary key , gender char(1) not null, subject varchar(30) not null, salary integer not null)")
mydb.commit()
while(True):

    print("1.LOGIN")
    print("2.EXIT")
    choice = int(input("ENTER YOUR CHOICE:"))
    if choice == 1:
        u1 = input("Enter username:")
        pwd1 = input("Enter the password:")
        while u1 == 'sql' and pwd1 == 'school':
            print('connected!')
            print("1. Enter data for new student")
            print("2. Enter data for new staff")
            print("3. Search student data")
            print("4. Search staff data")
            print("5. Remove student record")
            print("6. Remove staff record")
            print("7. All students details")
            print("8. All staff details")
            print("9. Exit")

            ch = int(input("Enter your choice:"))

# code for entering a new student record
            if (ch==1):
                print("All information prompted are mandatory to be filled")
                name = input("Enter student name:")
                classs = input("Enter student class:")
                roll_no = int(input("Enter student roll number:"))
                gender = input("Enter student gender (M/F):")
                mycursor.execute("insert into students values('"+name+"', '"+classs+"', '"+str(roll_no)+"', '"+gender+"')")
                mydb.commit()
                print("Student record have been saved successfully!")

# code for entering a new staff record
            elif (ch==2):
                print("All information prompted are mandatory to be filled")
                name = input("Enter staff name:")
                gender = input("Enter staff gender (M/F):")
                subject = input("Enter staff subject or department:")
                salary = int(input("Enter staff salary:"))
                mycursor.execute("insert into staff values('"+name+"', '"+gender+"', '"+subject+"', '"+str(salary)+"')")
                mydb.commit()
                print("Staff record have been saved successfully!")

# code for displaying students data
            elif (ch==3):
                roll_no = input("Enter student roll number:")
                mycursor.execute("select * from students where roll_no = '"+roll_no+"'")
                for i in mycursor:
                    name, classs, roll_no, gender = i
                    print(f'Name:- {name}')
                    print(f'Class:- {classs}')
                    print(f'Roll Number:- {roll_no}')
                    print(f'Gender:- {gender}')

# code for displaying staff data
            elif (ch==4):
                name = input("Enter staff name:")
                mycursor.execute("select * from staff where name = '" + name + "'")
                for i in mycursor:
                    name, gender, subject, salary = i
                    print(f'Name:- {name}')
                    print(f'Gender:- {gender}')
                    print(f'Subject:- {subject}')
                    print(f'Salary:- {salary}')

# code for deleting student data
            elif (ch==5):
                r_no = str(input("Enter roll number:"))
                mycursor.execute("delete from students where roll_no = '"+r_no+"'")
                mydb.commit()
                print("Student record is successfully deleted.")

# code for deleting staff data
            elif (ch==6):
                name = str(input("Enter staff name:"))
                mycursor.execute("delete from staff where name = '"+name+"'")
                mydb.commit()
                print("Staff record is successfully deleted.")

# code for all students details
            elif (ch==7):
                sql_w = ("select * from students")
                mycursor.execute(sql_w)
                r = mycursor.fetchall()
                for i in r:
                    print(i)

# code for all staff details
            elif (ch==8):
                sql_x = ("select * from staff")
                mycursor.execute(sql_x)
                r = mycursor.fetchall()
                for i in r:
                    print(i)

# code to exit
            elif (ch==9):
                break

    elif choice == 2:
        exit()

    else:
        print('wrong username or password')
