from scraper_base import LojaScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class AmazonScraper(LojaScraper):
    
    def buscar_preco(self, produto: str) -> dict :
        self.driver.get("https://www.amazon.com.br/")
        campo_busca = self.driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]')
        campo_busca.send_keys(produto, Keys.RETURN)
        sleep(2)
        
        try:
            titulo = self.driver.find_element(By.XPATH, '//h2[@class="a-size-base-plus a-spacing-none a-color-base a-text-normal"]')
            preco = self.driver.find_element(By.XPATH, '//span[@class="a-price"]/span[@class="a-offscreen"]')
            link = self.driver.find_element(By.XPATH, '//a[@class="a-link-normal s-line-clamp-4 s-link-style a-text-normal"]')
            return {"loja": "Amazon", "titulo": titulo, "preço": preco, "link": link}
        except Exception as e:
            return {"loja": "Amazon", "erro": str(e)}