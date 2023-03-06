from inventory_report.importer.importer import Importer
import xmltodict


class XmlImporter(Importer):
    @staticmethod
    def import_data(file):
        if '.xml' not in file:
            raise ValueError('Arquivo inválido')
        with open(file) as open_file:
            content = xmltodict.parse(open_file.read())["dataset"]["record"]
            return list(content)
