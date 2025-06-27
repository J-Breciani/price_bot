from scraper_base import LojaScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class MagaluScraper(LojaScraper):
    
    def buscar_preco(self, produto:str) -> dict:
        self.driver.get('https://www.magazineluiza.com.br/')
        campo_busca = self.driver.find_element(By.XPATH, '//div[@id= "search-container"]')
        campo_busca.send_keys(produto, Keys.RETURN)
        time.sleep(2)
        
        try:
            titulo = self.driver.find_element(By.XPATH, '//h2[@data-testid="product-title"]')
            preco = self.driver.find_element(By.XPATH, '//p[@data-testid="price-value"]')
            link = self.driver.find_element(By.XPATH, '//h2[@data-testid="product-card-container"]')
            return {"loja": "Magalu", "titulo": titulo, "preco": preco, "link": link}
        except Exception as e:
            return {"loja": "Magalu", "erro": str(e)} 