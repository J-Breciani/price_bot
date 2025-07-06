from core.comparador import ComparadorPrecos

robo = ComparadorPrecos()
melhor_oportunidade = robo.melhor_preco("Smart TV")

if melhor_oportunidade:
    print(f"{melhor_oportunidade['loja']} - {melhor_oportunidade['titulo']} - R$ {melhor_oportunidade['preco']}")
    print(melhor_oportunidade['link'])
else:
    print("Produto não encontrado.")