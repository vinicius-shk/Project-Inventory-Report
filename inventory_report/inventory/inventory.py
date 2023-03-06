# from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv


class Inventory:
    @staticmethod
    def import_data(path: str, report_type: str):
        with open(path) as report:
            response = csv.DictReader(report)
            if report_type == 'simples':
                return SimpleReport.generate(list(response))
            elif report_type == 'completo':
                return CompleteReport.generate(list(response))
            else:
                raise ValueError
