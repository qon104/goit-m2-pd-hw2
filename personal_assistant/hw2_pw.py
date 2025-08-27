# Абстрактный класс view
from abc import ABC, abstractmethod

class View(ABC):
    @abstractmethod
    def display(self, data):
        pass

# Конкретная реализация view для консоли
class ConsoleView(View):
    def display(self, data):
        print(data)

# Класс записи контакта
class Record:
    def __init__(self, name, phones=None, birthday=None):
        self.name = name                  # Name
        self.phones = phones or []        # list
        self.birthday = birthday          # Birthday

    def add_phone(self, p):
        self.phones.append(p)

    def remove_phone(self, p):
        if p in self.phones:
            self.phones.remove(p)

    def edit_phone(self, old, new):
        for i, ph in enumerate(self.phones):
            if ph == old:
                self.phones[i] = new

    def add_birthday(self, b):
        self.birthday = b

# Класс адресной книги
class AdressBook:
    def __init__(self):
        self.records = {}  # dict

    def add_record(self, record: Record):
        self.records[record.name] = record

    def find(self, name):
        return self.records.get(name)

    def delete(self, name):
        if name in self.records:
            del self.records[name]

    def get_upcoming_birthdays(self, days):
        # заглушка, возвращает список имен с днями рождения в пределах days
        return [r.name for r in self.records.values() if r.birthday]

# Обработчик команд
class CommandHandler:
    def __init__(self, ab: AdressBook, view: View):
        self.address_book = ab
        self.view = view

    def execute(self, cmd):
        # Простая заглушка
        print(f"Executing command: {cmd}")
