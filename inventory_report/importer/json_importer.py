from inventory_report.importer.importer import Importer
import json


class JsonImporter(Importer):
    @staticmethod
    def import_data(file):
        if '.json' not in file:
            raise ValueError('Arquivo inválido')
        with open(file) as open_file:
            content = json.load(open_file)
            return list(content)
