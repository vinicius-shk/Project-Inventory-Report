from simple_report import SimpleReport
from typing import List, Dict


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(my_list: List[Dict[str, str]]):
        superclass_ret = super(
            CompleteReport, CompleteReport
            ).generate(my_list)
        ordered_comp_prod_counter = dict()
        comp_quant = ''
        for item in my_list:
            if item["nome_da_empresa"] not in ordered_comp_prod_counter:
                ordered_comp_prod_counter[item["nome_da_empresa"]] = 1
            ordered_comp_prod_counter[item["nome_da_empresa"]] += 1
        items_list = ordered_comp_prod_counter.items()
        for key, value in items_list:
            comp_quant += f'{key}: {value}\n'
        return f'''{superclass_ret}
Produtos estocados por empresa:
{comp_quant}
        '''
