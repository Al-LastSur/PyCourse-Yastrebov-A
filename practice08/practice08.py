import linecache

class Contact:
    def __init__(self, last_name, first_name, middle_name, phone_number):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_name = middle_name
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name} - {self.phone_number}"


class PhoneBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def export_to_txt(self, filename):
        with open(filename, 'w') as file:
            for contact in self.contacts:
                file.write(f"{contact.last_name},{contact.first_name},{contact.middle_name},{contact.phone_number}\n")

    def import_from_txt(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                contact = Contact(data[0], data[1], data[2], data[3])
                self.contacts.append(contact)

    def search_by_attribute(self, attribute):
        found_contacts = []
        for contact in self.contacts:
            if attribute.lower() in contact.last_name.lower() or attribute.lower() in contact.first_name.lower() or attribute.lower() in contact.middle_name.lower() or attribute.lower() in contact.phone_number.lower():
                found_contacts.append(contact)
        return found_contacts

    def copy_contact_from_file(self, source_filename, line_number):
        line = linecache.getline(source_filename, line_number)
        if line:
            data = line.strip().split(',')
            contact = Contact(data[0], data[1], data[2], data[3])
            self.contacts.append(contact)
            return True
        else:
            return False


def print_contacts(contacts):
    if contacts:
        for contact in contacts:
            print(contact)
    else:
        print("Контакты не найдены.")


def search_contact(phone_book):
    search_attribute = input("Введите характеристику для поиска контакта: ")
    found_contacts = phone_book.search_by_attribute(search_attribute)
    print("\nНайденные контакты:")
    print_contacts(found_contacts)


def copy_contact(phone_book):
    source_filename = input("Введите имя файла, из которого нужно скопировать контакт: ")
    line_number = int(input("Введите номер строки для копирования: "))
    if phone_book.copy_contact_from_file(source_filename, line_number):
        print("Контакт успешно скопирован.")
    else:
        print("Ошибка при копировании контакта. Проверьте правильность введенных данных.")


def main_menu(phone_book):
    while True:
        print("\nМеню:")
        print("1. Поиск по номеру")
        print("2. Поиск по имени")
        print("3. Поиск по фамилии")
        print("4. Внести данные в справочник")
        print("5. Скопировать контакт из файла")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            search_contact(phone_book)
        elif choice == '2':
            search_contact(phone_book)
        elif choice == '3':
            search_contact(phone_book)
        elif choice == '4':
            add_contact_from_terminal(phone_book)
        elif choice == '5':
            copy_contact(phone_book)
        elif choice == '6':
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите существующий пункт меню.")


def add_contact_from_terminal(phone_book):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    middle_name = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")

    contact = Contact(last_name, first_name, middle_name, phone_number)
    phone_book.add_contact(contact)
    print("Контакт успешно добавлен.")


def main():
    phone_book = PhoneBook()

    # Добавим несколько контактов для примера
    phone_book.add_contact(Contact("Иванов", "Иван", "Иванович", "1234567890"))
    phone_book.add_contact(Contact("Петров", "Петр", "Петрович", "9876543210"))

    # Экспортируем контакты в файл
    phone_book.export_to_txt("phone_book.txt")
    print("Контакты успешно экспортированы в файл 'phone_book.txt'")

    # Создадим новый телефонный справочник и импортируем данные из файла
    new_phone_book = PhoneBook()
    new_phone_book.import_from_txt("phone_book.txt")

    main_menu(new_phone_book)


if __name__ == "__main__":
    main()