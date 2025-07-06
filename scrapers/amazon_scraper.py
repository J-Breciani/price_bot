from .scraper_base import LojaScraper
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class AmazonScraper(LojaScraper):
    
    def buscar_preco(self, produto: str) -> dict :
        self.driver.get("https://www.amazon.com.br/")
        self.driver.find_element(By.XPATH, '//input[@id="twotabsearchtextbox"]').send_keys(produto, Keys.RETURN)
        sleep(2)
        
        try:
            titulo = self.driver.find_element(By.XPATH, '//h2[@class="a-size-base-plus a-spacing-none a-color-base a-text-normal"]').text
            preco = self.driver.find_element(By.XPATH, '//div[@data-component-type="s-search-result"][1]//span[@class="a-offscreen"]').text
            link_el = self.driver.find_element(By.XPATH, '//div[@data-component-type="s-search-result"][1]//h2/a/span')
            link = link_el.get_attribute("href")
            self.driver.close()
            return {"loja": "Amazon", "titulo": titulo, "preco": preco, "link": link}
        except Exception as e:
            self.driver.close()
            return {"loja": "Amazon", "erro": str(e)}