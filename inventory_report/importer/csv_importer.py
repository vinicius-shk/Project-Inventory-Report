from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @staticmethod
    def import_data(file):
        if '.csv' not in file:
            raise ValueError('Arquivo inválido')
        with open(file) as open_file:
            content = csv.DictReader(open_file)
            return list(content)
