from jsonfile import DisplayJson
from xmlfile import DisplayXml
from menu import Fairy_tale, Drama, Fantasy, Techno_fantasy, Dark_fantasy, Science_fiction, Historical, Travelling

# Функция для валидации и обработки ввода цены
def get_price(prompt):
    while True:
        try:
            price = int(input(prompt))
            if price <= 0:
                raise ValueError
            return price
        except ValueError:
            print("Пожалуйста, введите положительное число.")

# Функция для вывода данных
def print_data(data, file_format):
    if file_format == 'json':
        print("\nДанные из JSON:")
    elif file_format == 'xml':
        print("\nДанные из XML:")

    # Вывод сказок
    print("\nСказки:")
    for fairy_tale in data['fairy_tales']:
        print(f"Название: {fairy_tale['title']}, Цена: {fairy_tale['price']} руб., Добро: {fairy_tale['good']}., Зло: {fairy_tale['evil']}")

    # Вывод пьес
    print("\nПьесы:")
    for drama in data['dramas']:
        print(f"Название: {drama['title']}, Цена: {drama['price']} руб., Место: {drama['place']} мл.")

    # Вывод фэнтези
    print("\nФэнтези:")
    for fantasy in data['fantasys']:
        print(f"Название: {fantasy['title']}, Цена: {fantasy['price']} руб., мир: {fantasy['world']}")

    # Вывод техно-фэнтези
    print("\nТехно-фэнтези:")
    for techno_fantasy in data['techno_fantasys']:
        print(f"Название: {techno_fantasy['title']}, Цена: {techno_fantasy['price']} руб., Технологии: {techno_fantasy['technologies']}")

    # Вывод тёмного фэнтези
    print("\nТёмное фэнтези:")
    for dark_fantasy in data['dark_fantasys']:
        print(f"Название: {dark_fantasy['title']}, Цена: {dark_fantasy['price']} руб., Некрополис: {dark_fantasy['necropolis']}")

    # Вывод научной фантастики
    print("\nНаучная фантастика:")
    for science_fiction in data['science_fictions']:
        print(f"Название: {science_fiction['title']}, Цена: {science_fiction['price']} руб., Объект: {science_fiction['object']}")

    # Вывод исторических произведений
    print("\nИсторические произведения:")
    for historical in data['historicals']:
        print(f"Название: {historical['title']}, Цена: {historical['price']} руб., Дата: {historical['date']}")

    # Вывод путешествий
    print("\nПутешествия:")
    for travelling in data['travellings']:
        print(f"Название: {travelling['title']}, Цена: {travelling['price']} руб., Место путешествия: {travelling['travel_place']}")

# Основная функция программы
def main():
    # Загружаем данные из JSON и XML файлов
    data_from_json = DisplayJson.load_from_json("menu.json")
    data_from_xml = DisplayXml.load_from_xml("menu.xml")

    while True:
        choice = input("\nВыберите действие:\n"
                       "1. Добавить сказку\n"
                       "2. Добавить драму\n"
                       "3. Добавить фэнтези\n"
                       "4. Добавить техно-фэнтези\n"
                       "5. Добавить тёмное фэнтези\n"
                       "6. Добавить научную фантастику\n"
                       "7. Добавить историческое произведение\n"
                       "8. Добавить путешествие\n"
                       "9. Сохранить в JSON\n"
                       "10. Сохранить в XML\n"
                       "11. Читать из JSON\n"
                       "12. Читать из XML\n"
                       "13. Выход\n")

        if choice == '1':
            title = input("Введите название сказки: ")
            price = get_price("Введите цену: ")
            good = input("Введите доброго героя: ")
            evil = input("Введите злого героя: ")
            fairy_tale = Fairy_tale(title, price, good, evil)
            DisplayJson.add_fairy_tale(data_from_json, fairy_tale)
            DisplayXml.add_fairy_tale(data_from_xml, fairy_tale)
        elif choice == '2':
            title = input("Введите название драмы: ")
            price = get_price("Введите цену: ")
            place = input("Введите место: ")
            drama = Drama(title, price, place)
            DisplayJson.add_drama(data_from_json, drama)
            DisplayXml.add_drama(data_from_xml, drama)
        elif choice == '3':
            title = input("Введите название фэнтези: ")
            price = get_price("Введите цену: ")
            world = input("Введите название мира: ")
            fantasy = Fantasy(title, price, world)
            DisplayJson.add_fantasy(data_from_json, fantasy)
            DisplayXml.add_fantasy(data_from_xml, fantasy)
        elif choice == '4':
            title = input("Введите название техно-фэнтези: ")
            price = get_price("Введите цену: ")
            technologies = input("Введите технологии: ")
            techno_fantasy = Techno_fantasy(title, price, technologies)
            DisplayJson.add_techno_fantasy(data_from_json, techno_fantasy)
            DisplayXml.add_techno_fantasy(data_from_xml, techno_fantasy)
        elif choice == '5':
            title = input("Введите название тёмного фэнтези: ")
            price = get_price("Введите цену: ")
            necropolis = input("Введите столицу нежити: ")
            dark_fantasy = Dark_fantasy(title, price, necropolis)
            DisplayJson.add_dark_fantasy(data_from_json, dark_fantasy)
            DisplayXml.add_dark_fantasy(data_from_xml, dark_fantasy)
        elif choice == '6':
            title = input("Введите название научной фантастики: ")
            price = get_price("Введите цену: ")
            obj = input("Введите тему обсуждения: ")
            science_fiction = Science_fiction(title, price, obj)
            DisplayJson.add_science_fiction(data_from_json, science_fiction)
            DisplayXml.add_science_fiction(data_from_xml, science_fiction)
        elif choice == '7':
            title = input("Введите название исторического произведения: ")
            price = get_price("Введите цену: ")
            date = input("Введите дату события: ")
            historical = Historical(title, price, date)
            DisplayJson.add_historical(data_from_json, historical)
            DisplayXml.add_historical(data_from_xml, historical)
        elif choice == '8':
            title = input("Введите название путешествия: ")
            price = get_price("Введите цену: ")
            travel_place = input("Место путешествия: ")
            travelling = Travelling(title, price, travel_place)
            DisplayJson.add_travelling(data_from_json, travelling)
            DisplayXml.add_travelling(data_from_xml, travelling)
        elif choice == '9':
            DisplayJson.save_to_json(data_from_json, "menu.json")
            print(f"Данные сохранены в menu.json")
        elif choice == '10':
            DisplayXml.save_to_xml(data_from_xml, "menu.xml")
            print(f"Данные сохранены в menu.xml")
        elif choice == '11':
            print_data(data_from_json, 'json')
        elif choice == '12':
            print_data(data_from_xml, 'xml')
        elif choice == '13':
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите действие снова.")

if __name__ == "__main__":
    main()