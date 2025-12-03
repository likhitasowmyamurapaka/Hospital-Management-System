#registration
import itertools
import time
import os
patients={}
'''
doctors={
    "D101":"Dr.Sharma - Cardiology",
    "D102":"Dr.Vijay - General",
    "D103":"Dr.Smitha - Orthopedic",
    "D104":"Dr.Satya - Brain"
}
'''
patient_count=1
def generate_pid():
    global patient_count
    #patient_count=itertools.count(start=1,step=1)
    pid=f"P{patient_count}"
    patient_count+=1
    return pid

def register_patient(name,age,gender):
    pid=generate_pid()
    patients[pid]={
        "name":name,
        "age":age,
        "gender":gender
    }
    time.sleep(1)
    print(f"Patient {name} registered with Id {pid}")
    time.sleep(1)
    #print("File will be saved in:", os.getcwd())
    with open("patients.txt", "a") as f:
        f.write(f"{pid},{name},{age},{gender}\n")
    return pid

def assign_doctor(pid):
    if pid in patients:
        treatment=input("Enter the treatment 'heart/general/bones/brain' :")
        if treatment=="heart":
            time.sleep(1)
            print(f"Doctor assigned for {pid} is Dr.Sharma - Cardiology with id D101")
            time.sleep(1)
            print("Treatment is going on...")
        elif treatment=="general":
            time.sleep(1)
            print(f"Doctor assigned for {pid} is Dr.Vijay - General with id D102")
            time.sleep(1)
            print("Treatment is going on...")
        elif treatment=="bones":
            time.sleep(1)
            print(f"Doctor assigned for {pid} is Dr.Smitha - Orthopedic with id D103")
            time.sleep(1)
            print("Treatment is going on...")
        elif treatment=="brain":
            time.sleep(1)
            print(f"Doctor assigned for {pid} is Dr.Satya - Brain with id D104")
            time.sleep(1)
            print("Treatment is going on...")
        else:
            time.sleep(1)
            print("Invalid treatment")
    else:
        time.sleep(1)
        print("Invalid patient id")

total_amount=0
def patient_admitted(patient):
    room_amount=0
    global total_amount
    if pid in patients:
        if patient=="admitted":
            room=input("general-ward/ICU/splroom:")
            if room=="general-ward":
                per_day=int(input("How many days:"))
                room_amount+=2000
                total_amount+=room_amount*per_day
                time.sleep(1)
                print("The amount for admitted is:",total_amount)
            elif room=="ICU":
                per_day=int(input("How many days:"))
                room_amount+=3500
                total_amount+=room_amount*per_day
                time.sleep(1)
                print("The amount for admitted is:",total_amount)
            elif room=="splroom":
                per_day=int(input("How many days:"))
                room_amount+=5000
                total_amount+=room_amount*per_day
                time.sleep(1)
                print("The amount for admitted is:",total_amount)
            else:
                time.sleep(1)
                print("No room allocated")
        else:
            time.sleep(1)
            print("Patient not admitted")

consultation=500
fee=0
def treatment_bill(treatment):
    global consultation
    global fee
    if treatment=="heart":
        fee=consultation+5000
        time.sleep(1)
        print("The amount for treatment:",fee)
        tests=input("Enter the test 'x-ray/scan':")
        if tests=="x-ray":
            fee=consultation+8000
            time.sleep(1)
            print("The amount for treatment and tests is :",fee)
        elif tests=="scan":
            fee=consultation+9000
            time.sleep(1)
            print("The amount for treatment and tests is :",fee)
        else:
            time.sleep(1)
            print("No tests required/taken")
    elif treatment=="brain":
        fee=consultation+4000
        time.sleep(1)
        print("The amount for treatment:",fee)
        tests=input("Enter the test 'x-ray/scan':")
        if tests=="x-ray":
            fee=consultation+3000
            time.sleep(1)
            print("The amount for treatment and tests is :",fee)
        elif tests=="scan":
            fee=consultation+2000
            time.sleep(1)
            print("The amount for treatment and tests is :",fee)
        else:
            time.sleep(1)
            print("No tests required/taken")
    elif treatment=="bones":
        tests=input("Enter the test 'x-ray/scan':")
        fee=consultation+2000        
        print("The amount for treatment:",fee)
        if tests=="x-ray":
            fee=consultation+2000
            print(fee)
        elif tests=="scan":
            fee=consultation+1500
            print(fee)
        else:
            print("No tests required/taken")
    elif treatment=="general":
        fee=consultation+1000
        print("The amuunt for treatment:",fee)
        if tests=="x-ray":
            fee=consultation+2000
            print(fee)
        elif tests=="scan":
            fee=consultation+1500
            print(fee)
        else:
            print("No tests required/taken")
    else:
        print("No treatment taken")
       
amount=0
def medicines_purchased(medicines):
    if medicines=="purchased":
        medicine=input("paracetomol/antibiotics:")
        global amount
        if medicine=="paracetomol":
            amount+=100
            print(amount)
        elif medicine=="antibiotics":
            amount+=350
            print(amount)
        else:
            print("No medicines purchased")
    else:
        print("No medicines needed")

bill_amount=0
def bill_generated(pid):
    #nonlocal fee
    #nonlocal total_amount
    global bill_amount
    if pid in patients:
        bill_amount=total_amount+consultation+fee+amount
        print(bill_amount)
    else:
        print("Invalid patient id")
    
def payment_status(pay_method):
    global bill_amount
    pay=int(input("Enter the amount you want to pay:"))
    bill_amount=bill_amount-pay
    if pay_method=="cash":
        if bill_amount==0:
            print("Total bill cleared")
            receipt_issue=itertools.count(start=101,step=1)
            print("Receipt:" "R"+str(next(receipt_issue)))
        else:
            print("Bill is pending")            
    elif pay_method=="UPI":
        if bill_amount==0:
            print("Total bill cleared")
            receipt_issue=itertools.count(start=101,step=1)
            print("Receipt:" "R"+str(next(receipt_issue)))
        else:
            print("Bill is pending,The amount to be paid is:",bill_amount)
    elif pay_method=="card":
        if bill_amount==0:
            print("Total bill cleared")
            receipt_issue=itertools.count(start=101,step=1)
            print("Receipt:" "R"+str(next(receipt_issue)))
        else:
            print("Bill is pending,The amount to be paid is",bill_amount)
    else:
        print("Zero amount is paid/Select valid payment method")       
        
while True:
    print()
    print("---- Hospital Management ----")
    print("1.Register patient")
    print("2.Assign doctor")
    print("3.Patient admitted")
    print("4.Treatment Bill")
    print("5.Medicines purchased")
    print("6.Bill generated")
    print("7.Payment status")
    print("8. Patients data")
    print()
    
    choice=int(input("Enter the choice number:"))

    if choice==1:
        #pid=input("Enter pid no:")
        #patient_register=input("Enter patient details:-")
        patient_name=input("Enter the patient name:")
        age=int(input("Enter the patient age:"))
        gender=input("Enter the patient gender 'male/female':")
        #time.sleep(1)
        #print("Assigning a doctor for consultation/treatment")
        #time.sleep(1)
        pid=register_patient(patient_name,age,gender)
        time.sleep(1)

    if choice==2:
        pid=input("Enter pid no:")
        assign_doctor(pid)
        time.sleep(1)

    if choice==3:
        patient=input("Position of patient 'admitted':")
        patient_admitted(patient)
    
    if choice==4:
        treatment=input("Enter the treatment 'heart/brain/bones/general':")
        treatment_bill(treatment)

    if choice==5:
        medicines=input("purchased/not:")
        medicines_purchased(medicines)

    if choice==6:
        pid=input("Enter patient id no:")
        bill_generated(pid)

    if choice==7:
        pay_method=input("Enter the payment method 'UPI/cash/card':")
        payment_status(pay_method)

    if choice==8:
        patients_data()