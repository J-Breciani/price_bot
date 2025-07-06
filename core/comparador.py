from scrapers.magalu_scraper import MagaluScraper
#from scrapers.amazon_scraper import AmazonScraper
from scrapers.mercado_livre_scraper import MercadoLivreScraper
from utils import formatacao

class ComparadorPrecos:
    def __init__(self):
        self.scrapers = [MagaluScraper(headless=False), MercadoLivreScraper(headless=False)]
        
    def melhor_preco(self, produto:str):
        resultados = {}
        menor_preço = 100000
        for scraper in self.scrapers:
            dicionario = scraper.buscar_preco(produto)
            preco_do_produto = formatacao.formatar_texto(dicionario["preco"])
            if preco_do_produto < menor_preço:
                menor_preço = preco_do_produto
                resultados = dict(loja= dicionario["loja"],titulo=dicionario["titulo"], preco=dicionario["preco"],link=dicionario["link"] )
        return resultados
            
            