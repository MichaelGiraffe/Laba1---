import xml.etree.ElementTree as ET


class DisplayXml:

    # Добавление отступов для красивого вывода (pretty-print)
    @staticmethod
    def indent(elem, level=0):
        i = "\n" + level * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for subelem in elem:
                DisplayXml.indent(subelem, level + 1)
            if not subelem.tail or not subelem.tail.strip():
                subelem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    # Сохранение данных в XML-файл
    @staticmethod
    def save_to_xml(data, filename):
        root = ET.Element('books')

        # Fairy tales
        fairy_tales = ET.SubElement(root, 'fairy_tales')
        for fairy_tale in data['fairy_tales']:
            fairy_tale_element = ET.SubElement(fairy_tales, 'fairy_tale')
            for key, value in fairy_tale.items():
                child = ET.SubElement(fairy_tale_element, key)
                child.text = str(value)

        # Dramas
        dramas = ET.SubElement(root, 'dramas')
        for drama in data['dramas']:
            drama_element = ET.SubElement(dramas, 'drama')
            for key, value in drama.items():
                child = ET.SubElement(drama_element, key)
                child.text = str(value)

        # Fantasys
        fantasys = ET.SubElement(root, 'fantasys')
        for fantasy in data['fantasys']:
            fantasy_element = ET.SubElement(fantasys, 'fantasy')
            for key, value in fantasy.items():
                child = ET.SubElement(fantasy_element, key)
                child.text = str(value)

        # Techno-fantasys
        techno_fantasys = ET.SubElement(root, 'techno_fantasys')
        for techno_fantasy in data['techno_fantasys']:
            techno_fantasy_element = ET.SubElement(techno_fantasys, 'techno_fantasy')
            for key, value in techno_fantasy.items():
                child = ET.SubElement(techno_fantasy_element, key)
                child.text = str(value)

        # Dark fantasys
        dark_fantasys = ET.SubElement(root, 'dark_fantasys')
        for dark_fantasy in data['dark_fantasys']:
            dark_fantasy_element = ET.SubElement(dark_fantasys, 'dark_fantasy')
            for key, value in dark_fantasy.items():
                child = ET.SubElement(dark_fantasy_element, key)
                child.text = str(value)

        # Science fiction
        science_fictions = ET.SubElement(root, 'science_fictions')
        for science_fiction in data['science_fictions']:
            science_fiction_element = ET.SubElement(science_fictions, 'science_fiction')
            for key, value in science_fiction.items():
                child = ET.SubElement(science_fiction_element, key)
                child.text = str(value)

        # Historicals
        historicals = ET.SubElement(root, 'historicals')
        for historical in data['historicals']:
            historical_element = ET.SubElement(historicals, 'historical')
            for key, value in historical.items():
                child = ET.SubElement(historical_element, key)
                child.text = str(value)

        # Travellings
        travellings = ET.SubElement(root, 'travellings')
        for travelling in data['travellings']:
            travelling_element = ET.SubElement(travellings, 'travelling')
            for key, value in travelling.items():
                child = ET.SubElement(travelling_element, key)
                child.text = str(value)

        DisplayXml.indent(root)

        try:
            tree = ET.ElementTree(root)
            tree.write(filename, encoding='utf-8', xml_declaration=True)
            print(f"Данные успешно сохранены в файл '{filename}'")
        except IOError as e:
            print(f"Ошибка при записи в XML-файл: {str(e)}")

    # Загрузка данных из XML-файла
    @staticmethod
    def load_from_xml(filename):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
        except FileNotFoundError:
            return {
                "fairy_tales": [], "dramas": [], "fantasys": [], "techno_fantasys": [],
                "dark_fantasys": [], "science_fictions": [], "historicals": [], "travellings": []
            }

        data = {
            "fairy_tales": [], "dramas": [], "fantasys": [], "techno_fantasys": [],
            "dark_fantasys": [], "science_fictions": [], "historicals": [], "travellings": []
        }

        # Загрузка данных
        fairy_tales = root.find('fairy_tales')
        if fairy_tales is not None:
            for fairy_tale in fairy_tales:
                fairy_tale_data = {}
                for child in fairy_tale:
                    fairy_tale_data[child.tag] = child.text
                data['fairy_tales'].append(fairy_tale_data)

        dramas = root.find('dramas')
        if dramas is not None:
            for drama in dramas:
                drama_data = {}
                for child in drama:
                    drama_data[child.tag] = child.text
                data['dramas'].append(drama_data)

        fantasys = root.find('fantasys')
        if fantasys is not None:
            for fantasy in fantasys:
                fantasy_data = {}
                for child in fantasy:
                    fantasy_data[child.tag] = child.text
                data['fantasys'].append(fantasy_data)

        techno_fantasys = root.find('techno_fantasys')
        if techno_fantasys is not None:
            for techno_fantasy in techno_fantasys:
                techno_fantasy_data = {}
                for child in techno_fantasy:
                    techno_fantasy_data[child.tag] = child.text
                data['techno_fantasys'].append(techno_fantasy_data)

        dark_fantasys = root.find('dark_fantasys')
        if dark_fantasys is not None:
            for dark_fantasy in dark_fantasys:
                dark_fantasy_data = {}
                for child in dark_fantasy:
                    dark_fantasy_data[child.tag] = child.text
                data['dark_fantasys'].append(dark_fantasy_data)

        science_fictions = root.find('science_fictions')
        if science_fictions is not None:
            for science_fiction in science_fictions:
                science_fiction_data = {}
                for child in science_fiction:
                    science_fiction_data[child.tag] = child.text
                data['science_fictions'].append(science_fiction_data)

        historicals = root.find('historicals')
        if historicals is not None:
            for historical in historicals:
                historical_data = {}
                for child in historical:
                    historical_data[child.tag] = child.text
                data['historicals'].append(historical_data)

        travellings = root.find('travellings')
        if travellings is not None:
            for travelling in travellings:
                travelling_data = {}
                for child in travelling:
                    travelling_data[child.tag] = child.text
                data['travellings'].append(travelling_data)

        return data

    # Добавление новой книги в категорию
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
