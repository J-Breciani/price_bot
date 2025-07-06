from .scraper_base import LojaScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class CasasBahiaScraper(LojaScraper):
    
    def buscar_preco(self, produto:str) -> dict:
        self.driver.get("https://www.casasbahia.com.br/")
        self.driver.find_element(By.XPATH, '//input[@id="search-input"]').send_keys(produto, Keys.RETURN)
        sleep(2)
        
        try:
            titulo_el = self.driver.find_element(By.XPATH, '//div[@class="product-card__details-wrapper"][1]//h3[@class="product-card__title"]/a')
            titulo = titulo_el.text
            link = titulo_el.get_attribute("href")
            preco = self.driver.find_element(By.XPATH,  '(//strong[@class="sales-price"])[1]').text
            self.driver.close()
            
            return {"loja": "Casas Bahia","titulo": titulo, "preco": preco, "link": link }
        except Exception as e:
            self.driver.close()
            return {"loja": "Magalu", "erro": str(e)}
            