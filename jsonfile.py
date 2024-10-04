import json

class DisplayJson:

    @staticmethod
    def save_to_json(data, filename):
        try:  # Обработка встроенной ошибки
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4)
            print(f"Все книги успешно сохранены в JSON-файл {filename}")
        except IOError as e:
            print(f"Ошибка записи в JSON-файл: {str(e)}")

    @staticmethod
    def load_from_json(filename):
        try:  # Обработка встроенной ошибки
            with open(filename, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {
                "fairy_tales": [], "dramas": [], "fantasys": [], "techno_fantasys": [],
                "dark_fantasys": [], "science_fictions": [], "historicals": [], "travellings": []
            }

    # Добавляем книги
    @staticmethod
    def add_fairy_tale(data, fairy_tale):
        data['fairy_tales'].append(fairy_tale.to_dict())

    @staticmethod
    def add_drama(data, drama):
        data['dramas'].append(drama.to_dict())

    @staticmethod
    def add_fantasy(data, fantasy):
        data['fantasys'].append(fantasy.to_dict())

    @staticmethod
    def add_techno_fantasy(data, techno_fantasy):
        data['techno_fantasys'].append(techno_fantasy.to_dict())

    @staticmethod
    def add_dark_fantasy(data, dark_fantasy):
        data['dark_fantasys'].append(dark_fantasy.to_dict())

    @staticmethod
    def add_science_fiction(data, science_fiction):
        data['science_fictions'].append(science_fiction.to_dict())

    @staticmethod
    def add_historical(data, historical):
        data['historicals'].append(historical.to_dict())

    @staticmethod
    def add_travelling(data, travelling):
        data['travellings'].append(travelling.to_dict())
