from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return str(self.value)
    
    
class Name(Field):
    def __init__(self, name):
        self.value = name
        
        
class Phone(Field):
    def __init__(self, phone):
        if self.validate(phone):
            self.value = phone
        else:
            raise ValueError("Invalid phone number format")

    def validate(self, phone):
        return len(phone) == 10 and phone.isdigit()

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return "Phone removed"

        return "Phone not found"

    def edit_phone(self, old_phone, new_phone):
        for p in self.phones:
            if p.value == old_phone:
                p.value = Phone(new_phone).value
                return "Phone updated"

        return "Phone not found"

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p.value

        return "Phone not found"

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, "Record not found")

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return "Record deleted"

        return "Record not found"