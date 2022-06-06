import datetime
from collections import UserDict
from datetime import date, timedelta


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name] = record

    def search_by_records(self, value):
        return value in self.data.values()

    def iterator(self):
        return self


class Record:
    def __init__(self, name, phone_number="", birthday=""):
        self.phone_number = phone_number
        self.name = name
        self.phones = []
        self.birthday = birthday

    def add_phone_number(self, phone_number):
        self.phones.append(phone_number)
        return self.phones

    def delete_phone_number(self, phone_number):
        self.phones.remove(phone_number)

    def edit_phone_number(self, old_number, new_number):
        for index, phone in enumerate(self.phones):
            if str(phone) == str(old_number):
                self.phones[index] = new_number
                break

    def days_to_birthday(self):
        if not self.birthday:
            return
        now = datetime.date.today()
        if (self.birthday.value.replace(year=now.year) - now).days > 0:
            return (self.birthday.value.replace(year=now.year) - now).days
        return (self.birthday.value.replace(year=now.year + 1) - now).days


class Field:
    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        print(new_value)


class Name(Field):
    def __init__(self, name):
        self.value = name


x = Name("Vasya")
print(x)


class Phone(Field):
    def __init__(self, phone_number):
        self.value = phone_number


y = Phone("0937236707")
print(y)


class Birthday(Field):
    def __init__(self, birthday):
        self.value = birthday


b = Birthday("29-02-2000")
print(b)


def main():
    pass


if __name__ == '__main__':
    main()

ab = AddressBook()

name1 = Name('Bill')
print(name1)
phone1 = Phone('123456')
print(phone1)
rec = Record(name1, phone1)
print(rec)
birthday1 = Record("29.02.2000")
print(birthday1)

ab.add_record(rec)
print(ab)

phone2 = Phone('09876')
rec.edit_phone_number(phone1, phone2)
print(rec)

name2 = Name("Jill")
rec2 = Record(name2)
ab.add_record(rec2)
print(ab)

# class Iterable:
#     MAX_VALUE = 10
#
#     def __init__(self):
#         self.current_value = 0
#
#     def __next__(self):
#         if self.current_value < self.MAX_VALUE:
#             self.current_value += 1
#             return self.current_value
#         raise StopIteration
#
#
# class CustomIterator:
#     def __iter__(self):
#         return Iterable()
#
#
# c = CustomIterator()
# for i in c:
#     print(i)
