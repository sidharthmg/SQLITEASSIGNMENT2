import sqlite3
conn=sqlite3.connect("EMPLOYEE.db")
cursor=conn.cursor()
cursor.execute("DROP TABLE IF EXISTS DEPARTMENTS")
query="""CREATE TABLE DEPARTMENTS (DEPARTMENT_ID INT,DEPARTMENT_NAME CHAR(20),FOREIGN KEY(DEPARTMENT_ID)
                REFERENCES EMPLOYEE (DEPARTMENT_ID))"""
conn.execute(query)
cursor.execute("INSERT INTO DEPARTMENTS(DEPARTMENT_ID,DEPARTMENT_NAME) VALUES (1,'HUMAN RESOURCE'),(2,'TECHNICAL'),"
               "(3,'TESTING'),(4,'QUALITY ASSURANCE'),(5,'FINANCE')")
f=True
while f:
    emp_id = int(input("Enter ID of department whose employee details have to be found:"))
    cursor.execute("SELECT DEPARTMENT_NAME FROM DEPARTMENTS WHERE DEPARTMENT_ID=?",(emp_id,))
    result = cursor.fetchone()
    print(f"\nEmployees Working in {result[0]} are:")
    cursor.execute("Select E.NAME,E.ID,E.SALARY,E.CITY,E.DEPARTMENT_ID,D.DEPARTMENT_NAME from EMPLOYEE E,Departments D "
                   "WHERE E.DEPARTMENT_ID=:id AND D.DEPARTMENT_ID=:id", {"id":emp_id})
    record = cursor.fetchall()
    for row in record:
        print("\nName:", row[0])
        print("ID:", row[1])
        print("Salary:", row[2])
        print("City:", row[3])
        print("Department:", row[4])
        print("Department:", result[0])
    d = input("Do you want to Continue Y or N:")
    if(d==Y):
        continue
    else:
        f=False
conn.commit()
conn.close()