from datetime import datetime
from typing import Dict, List


class SimpleReport:
    @staticmethod
    def generate(my_list: List[Dict[str, str]]):
        format = '%Y-%m-%d'
        valid_exp_date_list = [
            item for item in my_list
            if datetime.strptime(item["data_de_validade"], format)
            > datetime.now()
            ]
        closer_exp = min(
            valid_exp_date_list, key=lambda x: x["data_de_validade"]
            )["data_de_validade"]
        oldest_manufact_date = min(
            my_list, key=lambda x: x["data_de_fabricacao"]
            )["data_de_fabricacao"]
        most_prods = max(
            new_list := [
                item["nome_da_empresa"] for item in my_list
            ], key=new_list.count
            )
        return (f'''Data de fabricação mais antiga: {oldest_manufact_date}
Data de validade mais próxima: {closer_exp}
Empresa com mais produtos: {most_prods}''')
