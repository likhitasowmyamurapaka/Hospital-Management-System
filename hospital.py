import time
import os

patients = {}
patient_count = 1
consultation=0
receipt_count=101

def generate_pid():
    global patient_count
    pid = f"P{patient_count}"
    patient_count += 1
    return pid

def register_patient(name, age, gender,op_time):
    global consultation
    pid = generate_pid()
    patients[pid] = {
        "name": name,
        "age": age,
        "gender": gender,
        "bill_amount":0
    }
    if op_time>=9 and op_time<=12:
        consultation+=100
        time.sleep(1)
        print()
        print("OP Fee: ",consultation)
    elif op_time>12 and op_time<=18:
        consultation+=150
        time.sleep(1)
        print()
        print("OP Fee: ",consultation)
    else:
        time.sleep(1)
        print()
        print("After 6pm no appointments")
        return
    time.sleep(1)
    print()
    print(f"Patient {name} registered with Id {pid}")
    time.sleep(1)
    with open("patients.txt", "a") as file:
        file.write(f"{pid},{name},{age},{gender},{bill_amount}\n")
    return pid

def assign_doctor(pid):
    time.sleep(1)
    treatment = input("Enter the treatment 'heart/general/bones/brain' : ")
    if treatment == "heart":
        time.sleep(1)
        print(f"Doctor assigned for {pid} is Dr.Sharma - Cardiology (D101)")
    elif treatment == "general":
        time.sleep(1)
        print(f"Doctor assigned for {pid} is Dr.Vijay - General (D102)")
    elif treatment == "bones":
        time.sleep(1)
        print(f"Doctor assigned for {pid} is Dr.Smitha - Orthopedic (D103)")
    elif treatment == "brain":
        time.sleep(1)
        print(f"Doctor assigned for {pid} is Dr.Satya - Brain (D104)")
    else:
        time.sleep(1)
        print("Invalid treatment")
    return treatment

total_amount = 0
fee = 0
amount = 0
bill_amount = 0

def patient_admitted(pid):
    global total_amount
    room_amount = 0
    time.sleep(1)
    admitted = input("Is patient admitted? (yes/no): ")
    if admitted == "yes":
        time.sleep(1)
        room = input("Enter room type (general-ward/ICU/splroom): ")
        time.sleep(1)
        if room == "general-ward":
            days = int(input("How many days: "))
            room_amount = 2000
        elif room == "ICU":
            days = int(input("How many days: "))
            room_amount = 75000
        elif room == "splroom":
            days = int(input("How many days: "))
            room_amount = 5000
        else:
            time.sleep(1)
            print("No valid room allocated")
            return
        total_amount += room_amount * days
        time.sleep(1)
        print(f"Room charges added: {room_amount*days}")
        time.sleep(1)
    else:
        time.sleep(1)
        print("Patient not admitted")
        time.sleep(1)

def treatment_bill(treatment):
    global fee
    if treatment == "heart":
        fee += 5000
    elif treatment == "brain":
        fee += 4000
    elif treatment == "bones":
        fee += 2000
    elif treatment == "general":
        fee += 1000
    else:
        time.sleep(1)
        print("Invalid treatment")
        return
        time.sleep(1)
    print("Treatment is going on...")
    time.sleep(1)
    print(f"Treatment cost so far: {fee}")
    time.sleep(1)
    tests = input("Any test required? (x-ray/scan/none): ")
    time.sleep(1)
    if tests == "x-ray":
        fee += 3000
    elif tests == "scan":
        fee += 4000
    time.sleep(1)
    print()
    print(f"Total treatment cost: {fee}")

def medicines_purchased():
    global amount
    time.sleep(1)
    buy = input("Any medicines purchased? (yes/no): ")
    if buy == "yes":
        time.sleep(1)
        med = input("Enter medicine (cetirizine/dobutamine/paracetamol/vitamin-d): ")
        if med == "cetirizine":
            amount += 50
        elif med == "dobutamine":
            amount +=250
        elif med == "paracetamol":
            amount += 100
        elif med == "vitamin-d":
            amount += 400
        time.sleep(1)
        print(f"Medicines cost: {amount}")
    else:
        time.sleep(1)
        print("No medicines purchased")

def bill_generated(pid):
    global bill_amount
    bill_amount = total_amount + fee + amount
    time.sleep(1)
    print(f"Total bill for id {pid} is: {bill_amount}")
    patients[pid]["bill_amount"] = bill_amount
    folder = os.path.dirname(os.path.abspath(__file__))
    patient_file = os.path.join(folder, "patients.txt")

    with open(patient_file, "r") as f:
        lines = f.readlines() 
        
    with open(patient_file, "w") as f:
        for line in lines:
            parts = line.strip().split(",")
            if parts[0] == pid: 
                parts[-1] = str(bill_amount)
                f.write(",".join(parts) + "\n")
            else:
                f.write(line)

def payment_status():
    global bill_amount, receipt_count
    time.sleep(1)
    pay_method = input("Enter the payment method 'UPI/cash': ")
    time.sleep(1)
    pay = int(input("Enter the amount you want to pay: "))
    remaining = bill_amount - pay
    
    if pay_method=="cash":
        if pay == bill_amount:
            time.sleep(1)
            print("Total bill cleared")
            time.sleep(1)
            receipt_no=generate_receipt()
            print(f"Receipt: {receipt_no} issued for id {pid}")
            bill_amount=0
        elif pay>bill_amount:
            change=pay-bill_amount
            time.sleep(1)
            print("Your change is:",change)
            bill_amount=0
        else:
            bill_amount=remaining
            time.sleep(1)
            print(f"Bill is pending, remaining amount: {bill_amount}")

    elif pay_method=="UPI":
        if pay == bill_amount:
            time.sleep(1)
            print("Total bill cleared")
            time.sleep(1)
            receipt_no=generate_receipt()
            print(f"Receipt: {receipt_no} issued for id {pid}")
        elif pay>bill_amount:
            change=pay-bill_amount
            time.sleep(1)
            print("Your change in cash:",change)
            bill_amount=0
        else:
            bill_amount=remaining
            time.sleep(1)
            print(f"Bill is pending, remaining amount: {bill_amount}")

def registered_data():
    if not patients:
        print("No patients registered yet.")
        return
    print("\n--- Registered Patients ---")
    for key, value in patients.items():
        print(f"ID: {pid}, Name: {value['name']}, Age: {value['age']}, Gender: {value['gender']}, Total bill: {value['bill_amount']}")
    print("------------------------------\n")    
    
def patients_data():
    folder = os.path.dirname(os.path.abspath(__file__))
    patient_file = os.path.join(folder, "patients.txt")

    with open(patient_file, "r") as file:
        lines = file.readlines()
        if not lines:
            print("No patients registered yet.")
            return
        print("\n--- Registered Patients ---")
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 5:
                pid, name, age, gender, bill_amount = parts
            elif len(parts) == 4:
                pid, name, age, gender = parts
                bill_amount = "0"
            else:
                continue
            print(f"ID: {pid}, Name: {name}, Age: {age}, Gender: {gender}, Bill: {bill_amount}")
        print("----------------------------\n")


def load_patient_count():
    global patient_count

    with open("patients.txt", "r") as file:
        lines = file.readlines()
        if lines:
            last_line = lines[-1].strip()
            last_id = last_line.split(",")[0]
            if last_id.startswith("P") and last_id[1:].isdigit():
                patient_count = int(last_id[1:]) + 1

load_patient_count()

def generate_receipt():
    global receipt_count
    receipt_no=f"R{receipt_count}"
    receipt_count+=1
    return receipt_no

while True:
    print("\n==== Hospital System ====")
    print("1. Registration")
    print("2. Registered")
    print("3. Patients Data")
    print("4. Registered Data")
    print("5. Exit")
    print()

    main_choice = int(input("Enter your choice: "))
    print()

    if main_choice == 1:
        while True:
            patient_name = input("Enter patient name: ")
            time.sleep(1)
            age = int(input("Enter patient age: "))
            time.sleep(1)
            gender = input("Enter patient gender 'male/female': ")
            time.sleep(1)
            op_time=int(input("Enter the time that patient entered:"))
            time.sleep(1)
            pid = register_patient(patient_name, age, gender,op_time)
            print()
            time.sleep(1)
            more = input("Do you want to register another patient? (yes/no): ").lower()
            print()
            time.sleep(1)
            if more != "yes":
                break
            time.sleep(1)
            
    elif main_choice == 2:
        time.sleep(1)
        pid = input("Enter patient id: ")
        if pid in patients:
            treatment = assign_doctor(pid)
            print()
            patient_admitted(pid)
            print()
            treatment_bill(treatment)
            print()
            medicines_purchased()
            print()
            bill_generated(pid)
            print()
            payment_status()
            print()
        else:
            print("Invalid patient id!")

    elif main_choice == 3:
        patients_data()

    elif main_choice==4:
        registered_data()        

    elif main_choice == 5:
        print("Exiting.... Stay Healthy!")
        break
    
    else:
        print("Invalid choice!")
