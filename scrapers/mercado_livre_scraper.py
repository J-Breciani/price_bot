from .scraper_base import LojaScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class MercadoLivreScraper(LojaScraper):
    
    def buscar_preco(self, produto:str) -> dict:
        self.driver.get("https://www.mercadolivre.com.br/")
        self.driver.find_element(By.XPATH, '//input[@id="cb1-edit"]').send_keys(produto, Keys.RETURN)
        sleep(2)
        
        try:
            titulo_el = self.driver.find_element(By.XPATH, '(//a[@class="poly-component__title"])[1]')
            titulo = titulo_el.text
            link = titulo_el.get_attribute("href")
            preco = self.driver.find_element(By.XPATH,  '(//span[@class="andes-money-amount__fraction"])[1]').text
            self.driver.close()
            
            return {"loja": "Mercado Livre","titulo": titulo, "preco": preco, "link": link }
        except Exception as e:
            self.driver.close()
            return {"loja": "Magalu", "erro": str(e)}
            