from inventory_report.inventory.product import Product


def test_relatorio_produto():
    novo_prod = Product(
        1,
        'batata',
        'polenta',
        '2009-11-11',
        '2029-11-11',
        '12345600',
        'armazenar como batata'
        )
    assert novo_prod.id == 1
    assert novo_prod.data_de_fabricacao == '2009-11-11'
    assert novo_prod.data_de_validade == '2029-11-11'
    assert novo_prod.instrucoes_de_armazenamento == 'armazenar como batata'
    assert novo_prod.nome_da_empresa == 'polenta'
    assert novo_prod.nome_do_produto == 'batata'
    assert novo_prod.numero_de_serie == '12345600'
