from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json
import xmltodict


class Inventory:

    def csv_report(report, report_type):
        response = csv.DictReader(report)
        if report_type == 'simples':
            return SimpleReport.generate(list(response))
        return CompleteReport.generate(list(response))

    def json_report(report, report_type):
        content = json.load(report)
        if report_type == 'simples':
            return SimpleReport.generate(list(content))
        return CompleteReport.generate(list(content))

    def xml_report(report, report_type):
        xml_content = xmltodict.parse(report.read())["dataset"]["record"]
        if report_type == 'simples':
            return SimpleReport.generate(list(xml_content))
        return CompleteReport.generate(list(xml_content))

    @staticmethod
    def import_data(path: str, report_type: str):
        with open(path) as report:
            if '.csv' in path:
                return Inventory.csv_report(report, report_type)
            elif '.json' in path:
                return Inventory.json_report(report, report_type)
            return Inventory.xml_report(report, report_type)
