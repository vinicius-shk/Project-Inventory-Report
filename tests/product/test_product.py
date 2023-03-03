from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        1,
        'Produto X',
        'Empresa X',
        '2009-06-12',
        '2012-06-12',
        '123456789012',
        'em temperatura ambiente ao abrigo de luz'
        )
    assert isinstance(new_product, Product)
    assert new_product.id == 1
    assert new_product.nome_do_produto == 'Produto X'
    assert new_product.nome_da_empresa == 'Empresa X'
    assert new_product.data_de_fabricacao == '2009-06-12'
    assert new_product.data_de_validade == '2012-06-12'
    assert new_product.numero_de_serie == '123456789012'
    assert (
        new_product.instrucoes_de_armazenamento ==
        'em temperatura ambiente ao abrigo de luz'
        )
