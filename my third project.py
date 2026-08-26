student=[]
subject=set()

while True:

    print('''1. ADD STUDENT
         2. DISPLAY ALL STUDENT
         3. DELET STUDENT
         4. UPDATE STUDENT
         5. DISPLAY SUBJECT OFFERED
         6. EXIT ''')
    choice=int(input("enter any choice"))

    if(choice==1):

        sid1=input("enter student id")
        name=input("enter name")
        age=int(input("enter student age"))
        dob=input("enter student birth date")
        sub1=input("enter student subject(comma seprated)")
        subj=[sub.strip() for sub in sub1.split(",")]
        subject.update(subj)

        grade=input("enter student grade")
        std_info1=(sid1,dob)

        print("")
        print("Student added succesfully")
        print("")

        st_record={"Identity":std_info1,
               "NAME":name,
               "AGE":age,
               "GRADE":grade,
               "DOB":dob,
               "SUBJECT":subj}

        student.append(st_record)

    elif(choice==2):

        print("---DISPLAY STUDENT---")

        if not student:
            print("no record found")

        else:
            for s in student:
                sid,dob=s["Identity"]

                print(f'''
                student id={sid}
                stdent name={s['NAME']}
                date of birth={dob}
                age={s['AGE']}
                grade={s['GRADE']}
                subject={",".join(s['SUBJECT'])}''')

    elif(choice==3):

        sid=input("enter student id for delet")

        found=False

        for i,s in enumerate(student):
            if(s['Identity'][0]==sid):
                del student[i]
                found=True
                print("student deleted succesfully")
                break

        if not found:
            print("student not found")

    elif(choice==4):

        sid=input("enter student id for update")

        found=False

        for s in student:

            if(s['Identity'][0]==sid):

                c1=int(input('''
            1.UPDATE AGE
            2.UPDATE SUBJECT
            '''))

                if(c1==1):
                    age=int(input("enter new age"))
                    s["AGE"]=age
                    print("age updated succesfully")

                elif(c1==2):
                    nsub=input("enter student subject(comma seprated)")
                    sub_list=[sub3.strip() for sub3 in nsub.split(",")]
                    s['SUBJECT']=sub_list
                    subject.update(sub_list)
                    print("subject updated succesfully")

                else:
                    print("invalid choice")

                found=True
                break

        if not found:
            print("student not found")

    elif(choice==5):

        print("subject")

        for sub2 in subject:
            print(sub2)

    elif(choice==6):

        print("thank you for using this")
        break

    else:
        print("invalid choice")