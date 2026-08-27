import funcoes

produtos_precos = {
    "Arroz 5kg": 25.90,
    "Feijão 1kg": 8.50,
    "Óleo de Soja 900ml": 6.99,
    "Açúcar 1kg": 4.50,
    "Café 500g": 18.00,
    "Sal 1kg": 3.20,
    "Macarrão 500g": 5.00,
    "Leite 1L": 4.80,
    "Manteiga 200g": 10.50,
    "Queijo Mussarela 1kg": 38.00,
    "Presunto 1kg": 28.00,
    "Pão de Forma": 7.50,
    "Ovos (Dúzia)": 9.90,
    "Peito de Frango 1kg": 16.50,
    "Carne Bovina 1kg": 35.00,
    "Tomate 1kg": 6.50,
    "Cebola 1kg": 5.20,
    "Batata 1kg": 5.80,
    "Maçã 1kg": 8.00,
    "Banana 1kg": 6.00,
    "Detergente": 2.20,
    "Sabão em Pó 1kg": 11.90,
    "Amaciante 2L": 14.00,
    "Papel Higiênico 4 un": 7.00,
    "Pasta de Dentes": 4.00,
    "Sabonete": 2.50,
    "Shampoo": 12.00,
    "Condicionador": 13.00,
    "Esponja de Aço": 2.00,
    "Água Sanitária 2L": 5.50
}

preco = []

for n in produtos_precos.values():
    preco.append(n)

funcoes.calcular_estatisticas(preco)
