import json
import os


class JSONSaver:
    def __init__(self, filename):
        self.__filename = filename

        os.chdir(os.path.abspath(".."))
        folder_path = os.path.abspath("data")
        self.file_path = os.path.join(folder_path, filename)

    @property
    def file(self):
        return self.__filename

    @file.setter
    def file(self, name):
        self.__filename = name

    def add_vacancy(self, vacancy_data):
        with open(self.file_path, "w", encoding="utf-8") as file:
            json.dump(vacancy_data, file, indent=2, ensure_ascii=False)
        return self.file_path

    def get_vacancies(self):
        with open(self.file_path, 'r', encoding="utf-8") as file:
            return self.printjson(json.load(file))

    def remove_vacancy(self, vacancy_id, platform):
        with open(self.file_path, encoding="utf8") as file:
            data = json.load(file)
            if platform == "headhunter.ru":
                data['items'] = list(
                    filter(
                        lambda x: x.get('id') not in vacancy_id,
                        data.get('items', [])
                    )
                )
            elif platform == "superjob.ru":
                data['objects'] = list(
                    filter(
                        lambda x: x.get('id') not in vacancy_id,
                        data.get('objects', [])
                    )
                )
        with open(self.file_path, "w", encoding="utf8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)

    def printjson(self, data_dict):
        print(json.dumps(data_dict, indent=2, ensure_ascii=False))
