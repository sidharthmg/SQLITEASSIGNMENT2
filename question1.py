import sqlite3
conn=sqlite3.connect("employee.db")
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
query="""CREATE TABLE EMPLOYEE(NAME CHAR(20),ID INT NOT NULL PRIMARY KEY,SALARY INT,DEPARTMENT_ID INT)"""
conn.execute(query)
addcolumn="ALTER TABLE EMPLOYEE ADD COLUMN CITY CHAR (20)"
cursor.execute(addcolumn)
cursor.execute("INSERT INTO EMPLOYEE(NAME,ID,SALARY,DEPARTMENT_ID,CITY) VALUES ('LEO',1,40000,1,'PARIS'),('JAMES',2,35000,1,'DOHA'),"
               "('RIO',3,45000,2,'MADRID'),('MATHEW',4,50000,3,'TOKYO'),('ALEX',5,35000,3,'BERLIN')")
cursor.execute("SELECT NAME,ID,SALARY FROM EMPLOYEE")
record = cursor.fetchall()
for row in record:
        print("\nNAME:", row[0])
        print("ID:", row[1])
        print("SALARY:", row[2])
def emp_details(letter):
    cursor.execute("SELECT * FROM EMPLOYEE WHERE NAME LIKE 'letter%'")
    details = cursor.fetchall()
    if len(details) == 0:
        print("No employee whose name starts with {letter}")
    else:
        print("Employee details whose name starts with {letter} are:")
        for row in details:
            print("\nNAME:", row[0])
            print("ID:", row[1])
            print("SALARY:", row[2])
            print("DEPARTMENT_ID:", row[3])
            print("CITY:", row[4])

def emp_detailsid(id):
    cursor.execute("SELECT * FROM EMPLOYEE WHERE ID =?",(id,))
    detailsid = cursor.fetchall()
    print("Employee details whose name starts with {id} are:")
    for row in detailsid:
        print("\nNAME:", row[0])
        print("ID:", row[1])
        print("SALARY:", row[2])
        print("DEPARTMENT_ID:", row[3])
        print("CITY:", row[4])

def change_name(emp_id,emp_name):
    cursor.execute("SELECT NAME FROM EMPLOYEE WHERE ID =?",(emp_id,))
    result = cursor.fetchone()
    print("NAME OF EMPLOYEE BEFORE CHANGING:", result[0])
    cursor.execute("UPDATE EMPLOYEE SET NAME =:name WHERE ID =?", {"name": emp_name, "id": emp_id})
    print("NAME CHANGED")
    cursor.execute("SELECT NAME FROM EMPLOYEE WHERE ID =?", (emp_id,))
    result = cursor.fetchone()
    print("NAME OF EMPLOYEE AFTER CHANGING:", result[0])

f=True
while f:
    print("Enter 1 to print details of employees that start with a particular letter\n 2 to print details based on their ID"
          "\n 3 to change their name based on ID\n and 4 to EXIT\n")
    ch = int(input("Enter the number:"))
    if ch == 1:
        letter = input("Enter the letter:")
        emp_details(letter.capitalize())
    if ch ==2:
        id = int(input("Enter the ID:"))
        emp_detailsid(id)
    elif ch == 4:
        id = int(input("Enter the id of employee whose name has to be changed:"))
        name = input("Enter the name you want to give:")
        change_name(id, name)
    elif ch == 5:
        f= False
conn.commit()
conn.close()