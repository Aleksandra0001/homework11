import datetime
from collections import UserDict
import re

PHONE_REGEX = re.compile(r"^\+?(\d{2})?\(?(0\d{2})\)?(\d{7}$)")


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name] = record

    def search_by_records(self, value):
        return value in self.data.values()

    def iterator(self, n):
        if len(self.data) < n:
            raise Exception(
                f'Amount of records in <Address Book> is less then <n> = {n} you have entered')
        else:
            data_list = list(self.data.items())
            while data_list:
                result = '\n'.join(
                    [f'Contact <{el[0]}> has following contacts {el[1]}' for el in data_list[:n]])
                yield result
                data_list = data_list[n:]


class Record:
    def __init__(self, name, phone_number=None, birthday=None):
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
    def __init__(self, value):
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


class Phone(Field):
    def __init__(self, phone_number):
        self.value = valid_phone(phone_number)


def valid_phone(phone_number):
    if bool(re.match(PHONE_REGEX, phone_number)):
        return phone_number
    else:
        return str(f"Phone number {phone_number} is not valid")


class Birthday(Field):
    def __init__(self, birthday):
        self.value = birthday


def main():
    pass


if __name__ == '__main__':
    main()

