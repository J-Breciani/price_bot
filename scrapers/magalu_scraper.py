from .scraper_base import LojaScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class MagaluScraper(LojaScraper):
    
    def buscar_preco(self, produto:str) -> dict:
        self.driver.get('https://www.magazineluiza.com.br/')
        self.driver.find_element(By.XPATH, '//input[@data-testid="input-search"]').send_keys(produto, Keys.RETURN)
        sleep(2)
        
        try:
            titulo = self.driver.find_element(By.XPATH, '//h2[@data-testid="product-title"]').text
            preco = self.driver.find_element(By.XPATH, '//p[@data-testid="price-value"]').text
            link_el = self.driver.find_element(By.XPATH, '//a[@data-testid="product-card-container"]')
            link = link_el.get_attribute("href")
            self.driver.close()
            return {"loja": "Magalu", "titulo": titulo, "preco": preco, "link": link}
        except Exception as e:
            self.driver.close()
            return {"loja": "Magalu", "erro": str(e)}

     
        