import mysql.connector as sql
import stdiomask
conn=sql.connect(host='localhost',user='root',passwd='student')
if conn.is_connected():
    print('SUCCESSFULLY CONNECTED')
    c1=conn.cursor()
    c1.execute('create database if not exists ThumbayMedicalCenter')
    c1.execute('use ThumbayMedicalCenter')
    CH='yes'
    while CH.lower()=="yes":
        print()
        print()
        print("================================================================================")
        print()
        print("\t\t*_*_*_WELCOME TO THUMBAY MEDICAL CENTER_*_*_*")
        print("\t\t      ~ Your Health is in GOOD hands ~ ")
        print()
        print("================================================================================")
        print()
        print()
        print("\t\t\t\t1.LOGIN\n\n\t\t\t\t2.EXIT")
        print()
        print()
        print("================================================================================")
        print()
        choice1=int(input("ENTER YOUR CHOICE:"))
        print()
        if choice1==1:
            Ch='yes'
            while Ch.lower()=='yes':
                u1=input("ENTER USERNAME:")
                pwd1=stdiomask.getpass(prompt="ENTER PASSWORD:",mask="*")
                ch='yes'
                while ch.lower()=="yes":
                    if u1=='ADMIN'and pwd1=='123THUMBAY!@#':
                        print()
                        print('---WELCOME ADMIN---')
                        print()
                        print("==============================================================\
==================")
                        print()
                        print()
                        print("\t\t\t\t***MAIN MENU***\n\n\t\t\t\t1.Registeration\n\n\t\t\t\t\
2.Veiwing\n\n\t\t\t\t3.Updation")
                        print()
                        print()
                        print("================================================================\
================")
                        print()
                        choice=int(input("ENTER YOUR CHOICE:"))
                        if choice==1:
                            c1.execute('create table if not exists patient_details(p_id varchar(10)\
primary key not null,p_name char(20),p_age int(3),p_problems char(20),p_phoneno int(15))')
                            c1.execute('create table if not exists staff_details(st_id varchar(10)\
primary key not null,st_name char(20),st_age int(3),st_department char(20),st_phoneno int(15))')
                            c1.execute('create table if not exists doctor_details(d_id varchar(10)\
primary key not null,d_name char(20),d_age int(3),d_department char(20),d_phoneno int(15))')
                            c1.execute('create table if not exists nurse_details(n_id varchar(10)\
primary key not null,n_name char(20),n_age int(3),n_department char(20),n_phoneno int(15))')
                            ch1="yes"
                            print()
                            print("===============================================================\
=================")
                            print()
                            print()
                            print("\t\t\t\t***MENU I***\n\n\t\t\t1.Registering Patient Details\n\n\t\t\t\
2.Registering Doctor Details\n\n\t\t\t3.Registering Nurse Details\n\n\t\t\t\
4.Registering Non Medical Staff Details")
                            print()
                            print()
                            print("=================================================================\
===============")
                            print()
                            while ch1.lower()=="yes":
                                choice1=int(input("ENTER YOUR CHOICE:"))
                                if choice1==1:
                                    print("Patient ID:",end='')
                                    c1.execute('select max(p_id) from patient_details;')
                                    check=c1.fetchall()
                                    alph='P'
                                    for tup in check:
                                        for maxno in tup:
                                            if maxno==None:
                                                num=1
                                                p_id=alph+str(num)
                                            else:
                                                num=eval(maxno[-1])+1
                                                p_id=alph+str(num)
                                    print(p_id)
                                    p_name=input('Enter Patient Name:')
                                    p_age=int(input('Enter Age:'))
                                    p_problems=input('Enter the Problem/Disease:')
                                    p_phoneno=int(input('Enter Phone number:'))
                                    sql_insert="insert into patient_details(p_id,p_name,p_age,p_problems,p_phoneno)\
values(%s,%s,%s,%s,%s)"
                                    c1.execute(sql_insert,(p_id,p_name,p_age,p_problems,p_phoneno))
                                    print('====================SUCCESSFULLY REGISTERED====================')
                                    conn.commit()
                                elif choice1==2:
                                    print("Doctor ID:",end='')
                                    c1.execute('select max(d_id) from doctor_details;')
                                    check=c1.fetchall()
                                    alph='D'
                                    for tup in check:
                                        for maxno in tup:
                                            if maxno==None:
                                                num=1
                                                d_id=alph+str(num)
                                            else:
                                                num=eval(maxno[-1])+1
                                                d_id=alph+str(num)
                                    print(d_id)
                                    d_name=input('Enter Doctor Name:')
                                    d_age=int(input('Enter Age:'))
                                    d_department=input('Enter the Department:')
                                    d_phoneno=int(input('Enter Phone number:'))
                                    sql_insert="insert into doctor_details(d_id,d_name,d_age,d_department,d_phoneno)\
values(%s,%s,%s,%s,%s)"
                                    c1.execute(sql_insert,(d_id,d_name,d_age,d_department,d_phoneno))
                                    print('====================SUCCESSFULLY REGISTERED====================')
                                    conn.commit()
                                elif choice1==3:
                                    print("Nurse ID:",end='')
                                    c1.execute('select max(n_id) from nurse_details;')
                                    check=c1.fetchall()
                                    alph='N'
                                    for tup in check:
                                        for maxno in tup:
                                            if maxno==None:
                                                num=1
                                                n_id=alph+str(num)
                                            else:
                                                num=eval(maxno[-1])+1
                                                n_id=alph+str(num)
                                    print(n_id)
                                    n_name=input('Enter Nurse Name:')
                                    n_age=int(input('Enter Age:'))
                                    n_department=input('Enter the Department:')
                                    n_phoneno=int(input('Enter Phone number:'))
                                    sql_insert="insert into nurse_details(n_id,n_name,n_age,n_department,n_phoneno)\
values(%s,%s,%s,%s,%s)"
                                    c1.execute(sql_insert,(n_id,n_name,n_age,n_department,n_phoneno))
                                    print('====================SUCCESSFULLY REGISTERED====================')
                                    conn.commit()
                                elif choice1==4:
                                    print("Non Med Staff ID:",end='')
                                    c1.execute('select max(st_id) from staff_details;')
                                    check=c1.fetchall()
                                    alph='S'
                                    for tup in check:
                                        for maxno in tup:
                                            if maxno==None:
                                                num=1
                                                st_id=alph+str(num)
                                            else:
                                                num=eval(maxno[-1])+1
                                                st_id=alph+str(num)
                                    print(st_id)
                                    st_name=input('Enter Non Med Staff Name:')
                                    st_age=int(input('Enter Age:'))
                                    st_department=input('Enter type of job:')
                                    st_phoneno=int(input('Enter Phone number:'))
                                    sql_insert="insert into staff_details(st_id,st_name,st_age,st_department,st_phoneno)\
values(%s,%s,%s,%s,%s)"
                                    c1.execute(sql_insert,(st_id,st_name,st_age,st_department,st_phoneno))
                                    print('====================SUCCESSFULLY REGISTERED====================')
                                    conn.commit()
                                else:
                                    print("Invalid input. Please refer the menu to specify choices")
                                    print()
                                ch1=input("Do you want to continue registering?:[yes/no]")
                        elif choice==2:
                            ch2='yes'
                            print()
                            print("=========================================================\
=======================")
                            print()
                            print()
                            print("\t\t\t\t***MENU II***\n\n\t\t\t1.View all Patient Details\n\n\t\t\t\
2.View all Doctor Details\n\n\t\t\t3.View all Nurse Details\n\n\t\t\t4.View all Staff Details\n\n\t\t\t\
5.View specific Patient Details\n\n\t\t\t6.View specific Doctor Details\n\n\t\t\t\
7.View specific Nurse Details\n\n\t\t\t8.View specific Staff Details\n\n\t\t\t9.View all Departments\n\n\t\t\t\
10.View members of specific Department")
                            print()
                            print()
                            print("=========================================================\
=======================")
                            print()
                            while ch2.lower()=='yes':
                                choice2=int(input('ENTER YOUR CHOICE:'))
                                if choice2==1:
                                    c1.execute('select*from patient_details')
                                    r=c1.fetchall()
                                    if r==[]:
                                        print('\n! ! No records found ! !\n')
                                    else:
                                        print("PATIENT ID\t\tPATIENT NAME\t\tAGE\t\t\tPROBLEM\t\t\tCONTACT NO.")
                                        for i in r :
                                            for j in i:
                                                print(j,end='\t\t\t')
                                            print()
                                    conn.commit()
                                elif choice2==2:
                                    c1.execute("select*from doctor_details")
                                    s=c1.fetchall()
                                    if s==[]:
                                        print('\n! ! No records found ! !\n')
                                    else:
                                        print("DOCTOR ID\t\tDOCTOR NAME\t\t\tAGE\t\t\tDEPARTMENT\t\t\tCONTACT NO.")
                                        for i in s:
                                            for j in i:
                                                print(j,end='\t\t\t')
                                            print()
                                    conn.commit()
                                elif choice2==3:
                                    c1.execute("select*from nurse_details")
                                    t=c1.fetchall()
                                    if t==[]:
                                        print('\n! ! No records found ! !\n')
                                    else:
                                        print("NURSE ID\t\tNURSE NAME\t\t\tAGE\t\t\tDEPARTMENT\t\t\tCONTACT NO.")
                                        for i in t:
                                            for j in i:
                                                print(j,end='\t\t\t')
                                            print()
                                    conn.commit()
                                elif choice2==4:
                                    c1.execute("select*from staff_details")
                                    u=c1.fetchall()
                                    
                                    if u==[]:
                                        print('\n! ! No records found ! !\n')
                                    else:
                                        print("STAFF ID\t\tSTAFF NAME\t\t\tAGE\t\t\tDEPARTMENT\t\tCONTACT NO.")
                                        for i in u:
                                            for j in i:
                                                print(j,end='\t\t\t')
                                            print()
                                    conn.commit()
                                elif choice2==5:
                                    pid=input("Enter Patient ID:")
                                    c1.execute('select*from patient_details where p_id=%s',(pid,))
                                    v=c1.fetchall()
                                    if v==[]:
                                        print('\n! ! No records found ! !\n')
                                    else:
                                        print("PATIENT ID\t\tPATIENT NAME\t\tAGE\t\t\tPROBLEM\t\t\tCONTACT NO.")
                                        for i in v :
                                            for j in i:
                                                print(j,end='\t\t\t')
                                            print()
                                        conn.commit()
                                elif choice2==6:
                                    did=input("Enter Doctor ID:")
                                    c1.execute('select*from doctor_details where d_id=%s',(did,))
                                    w=c1.fetchall()
                                    if w==[]:
                                        print('\n! ! No records found ! !\n')
                                    else:
                                        print("DOCTOR ID\t\tDOCTOR NAME\t\t\tAGE\t\t\tDEPARTMENT\t\tCONTACT NO.")
                                        for i in w:
                                            for j in i:
                                                print(j,end='\t\t\t')
                                            print()
                                        conn.commit()
                                elif choice2==7:
                                    nid=input("Enter Nurse ID:")
                                    c1.execute('select*from nurse_details where n_id=%s',(nid,))
                                    x=c1.fetchall()
                                    if x==[]:
                                        print('\n! ! No records found ! !\n')





                                    else:
                                        print("NURSE ID\t\tNURSE NAME\t\t\tAGE\t\t\tDEPARTMENT\t\tCONTACT NO.")
                                        for i in x:
                                            for j in i:
                                                print(j,end='\t\t\t')
                                            print()
                                    conn.commit()
                                elif choice2==8:
                                    stid=input("Enter Staff ID:")
                                    c1.execute('select*from staff_details where st_id=%s',(stid,))
                                    y=c1.fetchall()
                                    if y==[]:
                                        print('\n! ! No records found ! !\n')
                                    else:
                                        print("STAFF ID\t\tSTAFF NAME\t\t\tAGE\t\t\tDEPARTMENT\t\tCONTACT NO.")
                                        for i in y:
                                            for j in i:
                                                print(j,end='\t\t\t')
                                            print()
                                        conn.commit()
                                elif choice2==9:
                                    c1.execute('select d.d_department,n.n_department from doctor_details d,\
nurse_details n')
                                    y=c1.fetchall()
                                    dpt=[]
                                    if y==[]:
                                        print('\n! ! No records found ! !\n')
                                    else:
                                        for i in y:
                                            for j in i:
                                                if j not in dpt:
                                                    dpt.append(j)
                                        print('DEPARTMENTS')
                                        for i in dpt:
                                            print(i)
                                elif choice2==10:
                                    dept=input('Enter the department:')
                                    c1.execute('select d_name from doctor_details where \
d_department=%s',(dept.upper(),))
                                    y=c1.fetchall()
                                    c1.execute('select n_name from nurse_details where \
n_department=%s',(dept.upper(),))
                                    z=c1.fetchall()
                                    if y==[]:
                                        print('\n! ! No records of doctors found ! !\n')

                                    else:
                                        list=[]
                                        print('DOCTORS')
                                        for i in y:
                                            if i[0] not in list:
                                                list.append(i[0])
                                                print(i[0])
                                    print()
                                    if z==[]:
                                        print('\n! ! No records of nurses found ! !\n')
                                    else:
                                        list=[]
                                        print('NURSES')
                                        for i in z:
                                            if i[0] not in list:
                                                list.append(i[0])
                                                print(i[0])
                                else:
                                    print("Invalid input. Please refer the menu to specify choices")
                                ch2=input("Do you want to continue veiwing?:[yes/no]")
                        elif choice==3:
                            ch3='yes'
                            while ch3.lower()=='yes':
                                print()
                                print("==================================================\
==============================")
                                print()
                                print()
                                print("\t\t\t\t***MENU III***\n\n\t\t\t1.Updating Patient Details\n\n\t\t\t\
2.Updating Doctor Details\n\n\t\t\t3.Updating Nurse Details\n\n\t\t\t4.Updating Non Medical Staff Details")
                                print()
                                print()
                                print("==================================================\
==============================")
                                print()
                                choice3=int(input('ENTER YOUR CHOICE:'))
                                if choice3==1:
                                    chP='yes'
                                    while chP.lower()=='yes':
                                        print()
                                        print("========================================================\
========================")
                                        print()
                                        print()
                                        print("\t\t\t\t***SUB - MENU***\n\n\t\t\tA:Updating Patient record\n\n\t\t\t\
B:Deleting Patient record")
                                        print()
                                        print()
                                        print("==========================================================\
======================")
                                        print()
                                        subchoice=input('ENTER YOUR CHOICE:')
                                        if subchoice.upper()=='A':
                                            print()
                                            print("========================================================\
========================")
                                            print()
                                            print()
                                            print("\t\t\t\t***SUB - MENU I***\n\n\t\t\t1.Patient Name\n\n\t\t\t\
2.Patient Age\n\n\t\t\t3.Patient Disease\n\n\t\t\t4.Patient Phone no")
                                            print()
                                            print()
                                            print("=============================================================\
===================")
                                            print()
                                            chA='yes'
                                            while chA.lower()=='yes':
                                                choiceA=int(input('ENTER YOUR CHOICE:'))
                                                if choiceA==1:
                                                    p_id=input('Enter ID  of Patient whose name is to be changed:')
                                                    c1.execute('SELECT p_name FROM patient_details WHERE p_id=%s',(p_id,))
                                                    t=c1.fetchall()
                                                    if t==[]:
                                                        print('\n! ! No  such record found ! !\n')
                                                    else:
                                                        for i in t:
                                                            for j in i:
                                                                print('Previous Name:',j)
                                                        p_name=input('Enter Updated Name of Patient:')
                                                        c1.execute('UPDATE patient_details SET p_name=%s \
WHERE p_id=%s',(p_name,p_id))
                                                        print('====================SUCCESSFULLY UPDATED\
====================')
                                                        c1.execute('select*from patient_details where p_id=%s',(p_id,))
                                                        v=c1.fetchall()
                                                        print("PATIENT ID\t\tPATIENT NAME\t\tAGE\t\t\tPROBLEM\t\t\t\
CONTACT NO.")
                                                        for i in v :
                                                            for j in i:
                                                                print(j,end='\t\t\t')
                                                            print()
                                                        conn.commit()
                                                elif choiceA==2:
                                                    p_id=input('Enter ID  of Patient whose age is to be changed:')
                                                    c1.execute('SELECT p_age FROM patient_details WHERE p_id=%s',(p_id,))
                                                    t=c1.fetchall()
                                                    if t==[]:
                                                        print('\n! ! No  such record found ! !\n')
                                                    else:
                                                        for i in t:
                                                            for j in i:
                                                                print('Previous Age:',j)
                                                        p_age=input('Enter Updtaed Age of Patient:')
                                                        c1.execute('UPDATE patient_details SET p_age=%s \
WHERE p_id=%s',(p_age,p_id))
                                                        print('====================SUCCESSFULLY UPDATED\
====================')
                                                        c1.execute('select*from patient_details where p_id=%s',(p_id,))
                                                        v=c1.fetchall()
                                                        print("PATIENT ID\t\tPATIENT NAME\t\tAGE\t\t\tPROBLEM\t\t\t\
CONTACT NO.")
                                                        for i in v :
                                                            for j in i:
                                                                print(j,end='\t\t\t')
                                                            print()
                                                        conn.commit()
                                                elif choiceA==3:
                                                    p_id=input('Enter ID  of Patient whose disease is to be changed:')
                                                    c1.execute('SELECT p_problems FROM patient_details \
WHERE p_id=%s',(p_id,))
                                                    t=c1.fetchall()
                                                    if t==[]:
                                                        print('\n! ! No  such record found ! !\n')
                                                    else:
                                                        for i in t:
                                                            for j in i:
                                                                print('Previous Disease:',j)
                                                        p_problems=input('Enter Updtaed Disease of Patient:')
                                                        c1.execute('UPDATE patient_details SET p_problems=%s \
WHERE p_id=%s',(p_problems,p_id))
                                                        print('====================SUCCESSFULLY UPDATED\
====================')
                                                        c1.execute('select*from patient_details where p_id=%s',(p_id,))
                                                        v=c1.fetchall()
                                                        print("PATIENT ID\t\tPATIENT NAME\t\tAGE\t\t\tPROBLEM\t\t\t\
CONTACT NO.")


                                                        for i in v :
                                                            for j in i:
                                                                print(j,end='\t\t\t')
                                                            print()
                                                        conn.commit()
                                                elif choiceA==4:
                                                    p_id=input('Enter ID  of Patient whose phone no. is to be changed:')
                                                    c1.execute('SELECT p_phoneno FROM patient_details \
WHERE p_id=%s',(p_id,))
                                                    t=c1.fetchall()
                                                    if t==[]:
                                                        print('\n! ! No  such record found ! !\n')
                                                    else:
                                                        for i in t:
                                                            for j in i:
                                                                print('Previous Phone no:',j)
                                                        p_phoneno=input('Enter Updtaed Phone no of Patient:')
                                                        c1.execute('UPDATE patient_details SET p_phoneno=%s \
WHERE p_id=%s',(p_phoneno,p_id))
                                                        print('====================SUCCESSFULLY UPDATED\
====================')
                                                        c1.execute('select*from patient_details where p_id=%s',(p_id,))
                                                        v=c1.fetchall()
                                                        print("PATIENT ID\t\tPATIENT NAME\t\tAGE\t\t\tPROBLEM\t\t\t\
CONTACT NO.")
                                                        for i in v :
                                                            for j in i:
                                                                print(j,end='\t\t\t')
                                                            print()
                                                        conn.commit()
                                                else:
                                                    print("Invalid input. Please refer the menu to specify choices")
                                                chA=input("Do you want to continue updating patient details?:[yes/no]")
                                        elif subchoice.upper()=='B':
                                            p_id=input('Enter ID  of Patient whose Record is to be deleted:')
                                            c1.execute('SELECT * FROM patient_details WHERE p_id=%s',(p_id,))
                                            t=c1.fetchall()
                                            if t==[]:
                                                print('\n! ! No  such record found ! !\n')
                                            else:
                                                sure=input('Are you sure you want to delete this record:[yes/no]')
                                                if sure.lower()=='yes':
                                                    c1.execute('DELETE FROM patient_details WHERE p_id=%s',(p_id,))
                                                    print('====================SUCCESSFULLY DELETED====================')
                                                else:
                                                    break
                                        else:
                                            print("Invalid input. Please refer the menu to specify choices")
                                        chP=input("Do you want to continue updating?:[yes/no]")
                                elif choice3==2:
                                    chD='yes'
                                    while chD.lower()=='yes':
                                        print()
                                        print("=========================================\
=======================================")
                                        print()
                                        print()
                                        print("\t\t\t\t***SUB - MENU***\n\n\t\t\tA:Updating Doctor record\n\n\t\t\t\
B:Deleting Doctor record")
                                        print()
                                        print()
                                        print("=========================================\
=======================================")
                                        print()
                                        subchoice=input('ENTER YOUR CHOICE:')
                                        if subchoice.upper()=='A':
                                            print()
                                            print("===============================================\
=================================")
                                            print()
                                            print()
                                            print("\t\t\t\t***SUB - MENU I***\n\n\t\t\t1.Doctor Name\n\n\t\t\t\
2.Doctor Age\n\n\t\t\t3.Doctor Department\n\n\t\t\t4.Doctor Phone no")
                                            print()
                                            print()
                                            print("=========================================\
=======================================")
                                            print()
                                            chA='yes'
                                            while chA.lower()=='yes':
                                                choiceA=int(input('ENTER YOUR CHOICE:'))
                                                if choiceA==1:
                                                    d_id=input('Enter ID  of Doctor whose name is to be changed:')
                                                    c1.execute('SELECT d_name FROM doctor_details WHERE d_id=%s',(d_id,))
                                                    t=c1.fetchall()
                                                    if t==[]:
                                                        print('\n! ! No  such record found ! !\n')
                                                    else:
                                                        for i in t:
                                                            for j in i:
                                                                print('Previous Name:',j)
                                                        d_name=input('Enter Updated Name of Doctor:')
                                                        c1.execute('UPDATE doctor_details SET d_name=%s \
WHERE d_id=%s',(d_name,d_id))
                                                        print('====================SUCCESSFULLY UPDATED\
====================')
                                                        c1.execute('select*from doctor_details where d_id=%s',(d_id,))
                                                        v=c1.fetchall()
                                                        print("DOCTOR ID\t\tDOCTOR NAME\t\t\tAGE\t\t\tDEPARTMENT\t\t\
CONTACT NO.")
                                                        for i in v :
                                                            for j in i:
                                                                print(j,end='\t\t\t')
                                                            print()
                                                        conn.commit()
                                                elif choiceA==2:
                                                    d_id=input('Enter ID  of Doctor whose age is to be changed:')
                                                    c1.execute('SELECT d_age FROM doctor_details WHERE d_id=%s',(d_id,))
                                                    t=c1.fetchall()
                                                    if t==[]:
                                                        print('\n! ! No  such record found ! !\n')
                                                    else:
                                                        for i in t:
                                                            for j in i:
                                                                print('Previous Age:',j)
                                                        d_age=input('Enter Updtaed Age of Doctor:')
                                                        c1.execute('UPDATE doctor_details SET d_age=%s \
WHERE d_id=%s',(d_age,d_id))
                                                        print('====================SUCCESSFULLY UPDATED\
====================')
                                                        c1.execute('select*from doctor_details where d_id=%s',(d_id,))
                                                        v=c1.fetchall()
                                                        print("DOCTOR ID\t\tDOCTOR NAME\t\t\tAGE\t\t\tDEPARTMENT\t\t\
CONTACT NO.")
                                                        for i in v :
                                                            for j in i:
                                                                print(j,end='\t\t\t')
                                                            print()
                                                        conn.commit()
                                                elif choiceA==3:
                                                    d_id=input('Enter ID  of Doctor whose department is to be changed:')
                                                    c1.execute('SELECT d_department FROM doctor_details \
WHERE d_id=%s',(d_id,))
                                                    t=c1.fetchall()
                                                    if t==[]:
                                                        print('\n! ! No  such record found ! !\n')


                                                    else:
                                                        for i in t:
                                                            for j in i:
                                                                print('Previous Department:',j)
                                                        d_department=input('Enter Updtaed Deparment of Doctor:')
                                                        c1.execute('UPDATE doctor_details SET d_department=%s \
WHERE d_id=%s',(d_department,d_id))
                                                        print('====================SUCCESSFULLY UPDATED\
====================')
                                                        c1.execute('select*from doctor_details where d_id=%s',(d_id,))
                                                        v=c1.fetchall()
                                                        print("DOCTOR ID\t\tDOCTOR NAME\t\t\tAGE\t\t\tDEPARTMENT\t\t\
CONTACT NO.")
                                                        for i in v :
                                                            for j in i:
                                                                print(j,end='\t\t\t')
                                                            print()
                                                        conn.commit()
                                                elif choiceA==4:
                                                    d_id=input('Enter ID  of Doctor whose phone no. is to be changed:')
                                                    c1.execute('SELECT d_phoneno FROM doctor_details \
WHERE d_id=%s',(d_id,))
                                                    t=c1.fetchall()
                                                    if t==[]:
                                                        print('\n! ! No  such record found ! !\n')
                                                    else:
                                                        for i in t:
                                                            for j in i:
                                                                print('Previous Phone no:',j)
                                                        d_phoneno=input('Enter Updtaed Phone no of Doctor:')
                                                        c1.execute('UPDATE doctor_details SET d_phoneno=%s \
WHERE d_id=%s',(d_phoneno,d_id))
                                                        print('====================SUCCESSFULLY UPDATED\
====================')
                                                        c1.execute('select*from doctor_details where d_id=%s',(d_id,))
                                                        v=c1.fetchall()
                                                        print("DOCTOR ID\t\tDOCTOR NAME\t\t\tAGE\t\t\tDEPARTMENT\t\t\
CONTACT NO.")
                                                        for i in v :
                                                            for j in i:
                                                                print(j,end='\t\t\t')
                                                            print()
                                                        conn.commit()
                                                else:
                                                    print("Invalid input. Please refer the menu to specify choices")
                                                chA=input("Do you want to continue updating Doctor details?:[yes/no]")
                                        elif subchoice.upper()=='B':
                                            d_id=input('Enter ID  of Doctor whose Record is to be deleted:')
                                            c1.execute('SELECT * FROM doctor_details WHERE d_id=%s',(d_id,))
                                            t=c1.fetchall()
                                            if t==[]:
                                                print('\n! ! No  such record found ! !\n')
                                            else:
                                                sure=input('Are you sure you want to delete this record:[yes/no]')
                                                if sure.lower()=='yes':
                                                    c1.execute('DELETE FROM doctor_details WHERE d_id=%s',(d_id,))
                                                    print('====================SUCCESSFULLY DELETED====================')
                                                else:
                                                    break
                                        else:
                                            print("Invalid input. Please refer the menu to specify choices")
                                        chD=input("Do you want to continue updating?:[yes/no]")
                                elif choice3==3:
                                    chN='yes'
                                    while chN.lower()=='yes':
                                        print()
                                        print("==================================================================\
==============")
                                        print()
                                        print()
                                        print("\t\t\t\t***SUB - MENU***\n\n\t\t\tA:Updating Nurse record\n\n\t\t\t\
B:Deleting Nurse record")
                                        print()
                                        print()
                                        print("==================================================\
==============================")
                                        print()
                                        subchoice=input('ENTER YOUR CHOICE:')
                                        if subchoice.upper()=='A':
                                            print()
                                            print("=================================================================\
===============")
                                            print()
                                            print()
                                            print("\t\t\t\t***SUB - MENU I***\n\n\t\t\t1.Nurse Name\n\n\t\t\t\
2.Nurse Age\n\n\t\t\t3.Nurse Department\n\n\t\t\t4.Nurse Phone no")
                                            print()
                                            print()
                                            print("==================================================\
==============================")
                                            print()
                                            chA='yes'
                                            while chA.lower()=='yes':
                                                choiceA=int(input('ENTER YOUR CHOICE:'))
                                                if choiceA==1:
                                                    n_id=input('Enter ID  of Nurse whose name is to be changed:')
                                                    c1.execute('SELECT n_name FROM nurse_details WHERE n_id=%s',(n_id,))
                                                    t=c1.fetchall()
                                                    if t==[]:
                                                        print('\n! ! No  such record found ! !\n')
                                                    else:
                                                        for i in t:
                                                            for j in i:
                                                                print('Previous Name:',j)
                                                        n_name=input('Enter Updated Name of Nurse:')
                                                        c1.execute('UPDATE nurse_details SET n_name=%s \
WHERE n_id=%s',(n_name,n_id))
                                                        print('====================SUCCESSFULLY UPDATED\
====================')
                                                        c1.execute('select*from nurse_details where n_id=%s',(n_id,))
                                                        v=c1.fetchall()
                                                        print("NURSE ID\t\tNURSE NAME\t\t\tAGE\t\t\tDEPARTMENT\t\t\
CONTACT NO.")
                                                        for i in v :
                                                            for j in i:
                                                                print(j,end='\t\t\t')
                                                            print()
                                                        conn.commit()
                                                elif choiceA==2:
                                                    n_id=input('Enter ID  of Nurse whose age is to be changed:')
                                                    c1.execute('SELECT n_age FROM nurse_details WHERE n_id=%s',(n_id,))
                                                    t=c1.fetchall()
                                                    if t==[]:
                                                        print('\n! ! No  such record found ! !\n')
                                                    else:
                                                        for i in t:
                                                            for j in i:
                                                                print('Previous Age:',j)
                                                        n_age=input('Enter Updtaed Age of Nurse:')
                                                        c1.execute('UPDATE nurse_details SET n_age=%s \
WHERE n_id=%s',(n_age,n_id))
                                                        print('====================SUCCESSFULLY UPDATED\
====================')
                                                        c1.execute('select*from nurse_details where n_id=%s',(n_id,))
                                                        v=c1.fetchall()
                                                        print("NURSE ID\t\tNURSE NAME\t\t\tAGE\t\t\tDEPARTMENT\t\t\
CONTACT NO.")

                                                        for i in v :
                                                            for j in i:
                                                                print(j,end='\t\t\t')
                                                            print()
                                                        conn.commit()
                                                elif choiceA==3:
                                                    n_id=input('Enter ID  of Nurse whose department is to be changed:')
                                                    c1.execute('SELECT n_department FROM nurse_details \
WHERE n_id=%s',(n_id,))
                                                    t=c1.fetchall()
                                                    if t==[]:
                                                        print('\n! ! No  such record found ! !\n')
                                                    else:
                                                        for i in t:
                                                            for j in i:
                                                                print('Previous Department:',j)
                                                        n_department=input('Enter Updtaed Deparment of Nurse:')
                                                        c1.execute('UPDATE nurse_details SET n_department=%s \
WHERE n_id=%s',(n_department,n_id))
                                                        print('====================SUCCESSFULLY UPDATED\
====================')
                                                        c1.execute('select*from nurse_details where n_id=%s',(n_id,))
                                                        v=c1.fetchall()
                                                        print("NURSE ID\t\tNURSE NAME\t\t\tAGE\t\t\tDEPARTMENT\t\t\
CONTACT NO.")
                                                        for i in v :
                                                            for j in i:
                                                                print(j,end='\t\t\t')
                                                            print()
                                                        conn.commit()
                                                elif choiceA==4:
                                                    n_id=input('Enter ID  of Nurse whose phone no. is to be changed:')
                                                    c1.execute('SELECT n_phoneno FROM nurse_details WHERE n_id=%s',(n_id,))
                                                    t=c1.fetchall()
                                                    if t==[]:
                                                        print('\n! ! No  such record found ! !\n')
                                                    else:
                                                        for i in t:
                                                            for j in i:
                                                                print('Previous Phone no:',j)
                                                        n_phoneno=input('Enter Updtaed Phone no of Nurse:')
                                                        c1.execute('UPDATE nurse_details SET n_phoneno=%s \
WHERE n_id=%s',(n_phoneno,n_id))
                                                        print('====================SUCCESSFULLY UPDATED\
====================')
                                                        c1.execute('select*from nurse_details where n_id=%s',(n_id,))
                                                        v=c1.fetchall()
                                                        print("NURSE ID\t\tNURSE NAME\t\t\tAGE\t\t\tDEPARTMENT\t\t\
CONTACT NO.")
                                                        for i in v :
                                                            for j in i:
                                                                print(j,end='\t\t\t')
                                                            print()
                                                        conn.commit()
                                                else:
                                                    print("Invalid input. Please refer the menu to specify choices")
                                                chA=input("Do you want to continue updating nurse details?:[yes/no]")
                                        elif subchoice.upper()=='B':
                                            n_id=input('Enter ID  of Nurse whose Record is to be deleted:')
                                            c1.execute('SELECT * FROM nurse_details WHERE n_id=%s',(n_id,))
                                            t=c1.fetchall()
                                            if t==[]:
                                                print('\n! ! No  such record found ! !\n')
                                            else:
                                                sure=input('Are you sure you want to delete this record:[yes/no]')
                                                if sure.lower()=='yes':
                                                    c1.execute('DELETE FROM nurse_details WHERE n_id=%s',(n_id,))
                                                    print('====================SUCCESSFULLY DELETED====================')
                                                else:
                                                    break
                                        else:
                                            print("Invalid input. Please refer the menu to specify choices")
                                        chN=input("Do you want to continue updating?:[yes/no]")
                                elif choice3==4:
                                    chS='yes'
                                    while chS.lower()=='yes':
                                        print()
                                        print("======================================================\
==========================")
                                        print()
                                        print()
                                        print("\t\t\t\t***SUB - MENU***\n\n\t\t\tA:Updating Staff record\n\n\t\t\t\
B:Deleting Staff record")
                                        print()
                                        print()
                                        print("===========================================================\
=====================")
                                        print()
                                        subchoice=input('ENTER YOUR CHOICE:')
                                        if subchoice.upper()=='A':
                                            print()

                                            print("=================================================================\
===============")
                                            print()
                                            print()
                                            print("\t\t\t\t***SUB - MENU I***\n\n\t\t\t1.Staff Name\n\n\t\t\t\
2.Staff Age\n\n\t\t\t3.Staff Department\n\n\t\t\t4.Staff Phone no")
                                            print()
                                            print()
                                            print("================================================================\
================")
                                            print()
                                            chA='yes'
                                            while chA.lower()=='yes':
                                                choiceA=int(input('ENTER YOUR CHOICE:'))
                                                if choiceA==1:
                                                    st_id=input('Enter ID  of Staff whose name is to be changed:')
                                                    c1.execute('SELECT st_name FROM staff_details WHERE st_id=%s',(st_id,))
                                                    t=c1.fetchall()
                                                    if t==[]:
                                                        print('\n! ! No  such record found ! !\n')
                                                    else:
                                                        for i in t:
                                                            for j in i:
                                                                print('Previous Name:',j)
                                                        st_name=input('Enter Updated Name of Staff:')
                                                        c1.execute('UPDATE staff_details SET st_name=%s \
WHERE st_id=%s',(st_name,st_id))
                                                        print('====================SUCCESSFULLY UPDATED\
====================')
                                                        c1.execute('select*from staff_details where st_id=%s',(st_id,))
                                                        v=c1.fetchall()
                                                        print("STAFF ID\t\tSTAFF NAME\t\t\tAGE\t\t\tDEPARTMENT\t\t\
CONTACT NO.")
                                                        for i in v :
                                                            for j in i:
                                                                print(j,end='\t\t\t')
                                                            print()
                                                        conn.commit()
                                                elif choiceA==2:
                                                    st_id=input('Enter ID  of Staff whose age is to be changed:')
                                                    c1.execute('SELECT st_age FROM staff_details WHERE st_id=%s',(st_id,))
                                                    t=c1.fetchall()
                                                    if t==[]:
                                                        print('\n! ! No  such record found ! !\n')


                                                    else:
                                                        for i in t:
                                                            for j in i:
                                                                print('Previous Age:',j)
                                                        st_age=input('Enter Updtaed Age of Staff:')
                                                        c1.execute('UPDATE staff_details SET st_age=%s \
WHERE st_id=%s',(st_age,st_id))
                                                        print('====================SUCCESSFULLY UPDATED\
====================')
                                                        c1.execute('select*from staff_details where st_id=%s',(st_id,))
                                                        v=c1.fetchall()
                                                        print("STAFF ID\t\tSTAFF NAME\t\t\tAGE\t\t\tDEPARTMENT\t\t\
CONTACT NO.")
                                                        for i in v :
                                                            for j in i:
                                                                print(j,end='\t\t\t')
                                                            print()
                                                        conn.commit()
                                                elif choiceA==3:
                                                    st_id=input('Enter ID  of Staff whose department is to be changed:')
                                                    c1.execute('SELECT st_department FROM staff_details \
WHERE st_id=%s',(st_id,))
                                                    t=c1.fetchall()
                                                    if t==[]:
                                                        print('\n! ! No  such record found ! !\n')
                                                    else:
                                                        for i in t:
                                                            for j in i:
                                                                print('Previous Department:',j)
                                                        st_department=input('Enter Updtaed Deparment of Staff:')
                                                        c1.execute('UPDATE staff_details SET st_department=%s \
WHERE st_id=%s',(st_department,st_id))
                                                        print('====================SUCCESSFULLY UPDATED\
====================')
                                                        c1.execute('select*from staff_details where st_id=%s',(st_id,))
                                                        v=c1.fetchall()
                                                        print("STAFF ID\t\tSTAFF NAME\t\t\tAGE\t\t\tDEPARTMENT\t\t\
CONTACT NO.")
                                                        for i in v :
                                                            for j in i:
                                                                print(j,end='\t\t\t')
                                                            print()
                                                        conn.commit()



                                                elif choiceA==4:
                                                    st_id=input('Enter ID  of Staff whose phone no. is to be changed:')
                                                    c1.execute('SELECT st_phoneno FROM staff_details \
WHERE st_id=%s',(st_id,))
                                                    t=c1.fetchall()
                                                    if t==[]:
                                                        print('\n! ! No  such record found ! !\n')
                                                    else:
                                                        for i in t:
                                                            for j in i:
                                                                print('Previous Phone no:',j)
                                                        st_phoneno=input('Enter Updtaed Phone no of Staff:')
                                                        c1.execute('UPDATE staff_details SET st_phoneno=%s \
WHERE st_id=%s',(st_phoneno,st_id))
                                                        print('====================SUCCESSFULLY UPDATED\
====================')
                                                        c1.execute('select*from staff_details where st_id=%s',(st_id,))
                                                        v=c1.fetchall()
                                                        print("STAFF ID\t\tSTAFF NAME\t\t\tAGE\t\t\tDEPARTMENT\t\t\
CONTACT NO.")
                                                        for i in v :
                                                            for j in i:
                                                                print(j,end='\t\t\t')
                                                            print()
                                                        conn.commit()
                                                else:
                                                    print("Invalid input. Please refer the menu to specify choices")
                                                chA=input("Do you want to continue updating staff details?:[yes/no]")
                                        elif subchoice.upper()=='B':
                                            st_id=input('Enter ID  of Staff whose Record is to be deleted:')
                                            c1.execute('SELECT * FROM staff_details WHERE st_id=%s',(st_id,))
                                            t=c1.fetchall()
                                            if t==[]:
                                                print('\n! ! No  such record found ! !\n')
                                            else:
                                                sure=input('Are you sure you want to delete this record:[yes/no]')
                                                if sure.lower()=='yes':
                                                    c1.execute('DELETE FROM staff_details WHERE st_id=%s',(st_id,))
                                                    print('====================SUCCESSFULLY DELETED====================')
                                                else:
                                                    break
                                        else:
                                            print("Invalid input. Please refer the menu to specify choices")
                                        chS=input("Do you want to continue updating?:[yes/no]")


                                else:
                                    print("Invalid input. Please refer the menu to specify choices")
                                ch3=input("Do you want to continue with main menu of updation/deletion?:[yes/no]")
                        else:
                            print("Invalid input. Please refer the menu to specify choices")
                        print("==========YOU HAVE RETURNED TO MAIN PAGE==========")
                        ch=input("Do you want to continue to main menu?:[yes/no]")
                    else:
                        print('USERNAME OR PASSWORD APPEARS TO BE INCORRECT!!')
                        break
                Ch=input("Do you want to login again?:[yes/no]")
        elif choice1==2:
            break
        else:
            print("Invalid input. Please refer the menu to specify choices")
        CH=input("Do you want to start all over again ?:[yes/no]")
    print()
    print("! ! (^_^) Thank You for visitng THUMBAY MEDICAL CENTER(^_^) ! !")
    print("! ! \t\t~ Your Health is in GOOD hands ~\t    ! !")
    print()
    conn.close()
else:
    print('! ! ERROR IN CONNECTION ! !')

