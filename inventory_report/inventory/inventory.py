from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json 


class Inventory:
    @staticmethod
    def import_data(path: str, report_type: str):
        with open(path) as report:
            if '.csv' in path:
                response = csv.DictReader(report)
                if report_type == 'simples':
                    return SimpleReport.generate(list(response))
                return CompleteReport.generate(list(response))
            elif '.json' in path:
                content = json.load(report)
                if report_type == 'simples':
                    return SimpleReport.generate(list(content))
                return CompleteReport.generate(list(content))
