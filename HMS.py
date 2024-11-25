# Node class for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Linked List implementation
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

# Doubly Linked List implementation
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

# Queue implementation
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

# Stack implementation
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

# Patient class
class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.medical_history = DoublyLinkedList()

# Doctor class
class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.assigned_patients = LinkedList()

# Appointment class
class Appointment:
    def __init__(self, patient, doctor, date, time):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time

# Billing Record class
class BillingRecord:
    def __init__(self, patient, amount, date):
        self.patient = patient
        self.amount = amount
        self.date = date

# Hospital Management System
class HospitalManagementSystem:
    def __init__(self):
        self.patient_records = LinkedList()
        self.doctor_records = LinkedList()
        self.appointment_queue = Queue()
        self.billing_history = Stack()
        self.inventory = []

    # Patient Management
    def add_patient(self, patient_id, name, age):
        new_patient = Patient(patient_id, name, age)
        self.patient_records.append(new_patient)
        print(f"Patient {name} added successfully.")

    def update_patient(self, patient_id, name=None, age=None):
        current = self.patient_records.head
        while current:
            if current.data.patient_id == patient_id:
                if name:
                    current.data.name = name
                if age:
                    current.data.age = age
                print(f"Patient {patient_id} updated successfully.")
                return
            current = current.next
        print(f"Patient {patient_id} not found.")

    def remove_patient(self, patient_id):
        self.patient_records.remove(patient_id)
        print(f"Patient {patient_id} removed successfully.")

    # Doctor Management
    def add_doctor(self, doctor_id, name, specialty):
        new_doctor = Doctor(doctor_id, name, specialty)
        self.doctor_records.append(new_doctor)
        print(f"Doctor {name} added successfully.")

    def update_doctor(self, doctor_id, name=None, specialty=None):
        current = self.doctor_records.head
        while current:
            if current.data.doctor_id == doctor_id:
                if name:
                    current.data.name = name
                if specialty:
                    current.data.specialty = specialty
                print(f"Doctor {doctor_id} updated successfully.")
                return
            current = current.next
        print(f"Doctor {doctor_id} not found.")

    def remove_doctor(self, doctor_id):
        self.doctor_records.remove(doctor_id)
        print(f"Doctor {doctor_id} removed successfully.")

    # Appointment Scheduling
    def schedule_appointment(self, patient_id, doctor_id, date, time):
        patient = self.find_patient(patient_id)
        doctor = self.find_doctor(doctor_id)
        if patient and doctor:
            new_appointment = Appointment(patient, doctor, date, time)
            self.appointment_queue.enqueue(new_appointment)
            print(f"Appointment scheduled for {patient.name} with {doctor.name} on {date} at {time}.")
        else:
            print("Patient or doctor not found.")

    # Billing and Payment Management
    def process_payment(self, patient_id, amount, date):
        patient = self.find_patient(patient_id)
        if patient:
            new_billing_record = BillingRecord(patient, amount, date)
            self.billing_history.push(new_billing_record)
            print(f"Payment of {amount} processed for {patient.name} on {date}.")
        else:
            print(f"Patient {patient_id} not found.")

    def undo_payment(self):
        if not self.billing_history.is_empty():
            undone_record = self.billing_history.pop()
            print(f"Payment of {undone_record.amount} for {undone_record.patient.name} on {undone_record.date} undone.")
        else:
            print("No payment records to undo.")

    # Inventory Management
    def add_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} added to inventory.")

    def remove_inventory(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{item} removed from inventory.")
        else:
            print(f"{item} not found in inventory.")

    # Helper functions
    def find_patient(self, patient_id):
        current = self.patient_records.head
        while current:
            if current.data.patient_id == patient_id:
                return current.data
            current = current.next
        return None

    def find_doctor(self, doctor_id):
        current = self.doctor_records.head
        while current:
            if current.data.doctor_id == doctor_id:
                return current.data
            current = current.next
        return None

# Automated console-based system
def main():
    hospital = HospitalManagementSystem()

    while True:
        print("\nHospital Management System")
        print("1. Add Patient")
        print("2. Update Patient")
        print("3. Remove Patient")
        print("4. Add Doctor")
        print("5. Update Doctor")
        print("6. Remove Doctor")
        print("7. Schedule Appointment")
        print("8. Process Payment")
        print("9. Undo Payment")
        print("10. Add Inventory")
        print("11. Remove Inventory")
        print("12. Exit")

        choice = input("Enter your choice (1-12): ")

        if choice == "1":
            patient_id = int(input("Enter Patient ID: "))
            name = input("Enter Patient Name: ")
            age = int(input("Enter Patient Age: "))
            hospital.add_patient(patient_id, name, age)

        elif choice == "2":
            patient_id = int(input("Enter Patient ID: "))
            name = input("Enter New Patient Name (leave blank to keep current): ")
            age = input("Enter New Patient Age (leave blank to keep current): ")
            hospital.update_patient(patient_id, name if name else None, int(age) if age else None)

        elif choice == "3":
            patient_id = int(input("Enter Patient ID: "))
            hospital.remove_patient(patient_id)

        elif choice == "4":
            doctor_id = int(input("Enter Doctor ID: "))
            name = input("Enter Doctor Name: ")
            specialty = input("Enter Doctor Specialty: ")
            hospital.add_doctor(doctor_id, name, specialty)

        elif choice == "5":
            doctor_id = int(input("Enter Doctor ID: "))
            name = input("Enter New Doctor Name (leave blank to keep current): ")
            specialty = input("Enter New Doctor Specialty (leave blank to keep current): ")
            hospital.update_doctor(doctor_id, name if name else None, specialty if specialty else None)

        elif choice == "6":
            doctor_id = int(input("Enter Doctor ID: "))
            hospital.remove_doctor(doctor_id)

        elif choice == "7":
            patient_id = int(input("Enter Patient ID: "))
            doctor_id = int(input("Enter Doctor ID: "))
            date = input("Enter Appointment Date (YYYY-MM-DD): ")
            time = input("Enter Appointment Time (HH:MM AM/PM): ")
            hospital.schedule_appointment(patient_id, doctor_id, date, time)

        elif choice == "8":
            patient_id = int(input("Enter Patient ID: "))
            amount = float(input("Enter Payment Amount: "))
            date = input("Enter Payment Date (YYYY-MM-DD): ")
            hospital.process_payment(patient_id, amount, date)

        elif choice == "9":
            hospital.undo_payment()

        elif choice == "10":
            item = input("Enter Item Name: ")
            hospital.add_inventory(item)

        elif choice == "11":
            item = input("Enter Item Name: ")
            hospital.remove_inventory(item)

        elif choice == "12":
            print("Exiting Hospital Management System...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()