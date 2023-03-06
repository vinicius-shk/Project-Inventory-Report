from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


class Inventory:

    def csv_report(file, report_type):
        response = CsvImporter.import_data(file)
        if report_type == 'simples':
            return SimpleReport.generate(response)
        return CompleteReport.generate(response)

    def json_report(file, report_type):
        content = JsonImporter.import_data(file)
        if report_type == 'simples':
            return SimpleReport.generate(content)
        return CompleteReport.generate(content)

    def xml_report(file, report_type):
        xml_content = XmlImporter.import_data(file)
        if report_type == 'simples':
            return SimpleReport.generate(xml_content)
        return CompleteReport.generate(xml_content)

    @staticmethod
    def import_data(path: str, report_type: str):
        if '.csv' in path:
            return Inventory.csv_report(path, report_type)
        elif '.json' in path:
            return Inventory.json_report(path, report_type)
        return Inventory.xml_report(path, report_type)
