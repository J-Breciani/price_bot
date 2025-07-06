import re
# função para formatar os valores dos preços

def formatar_texto( txt: str) -> float:
    # "R$ 2.999,00" -> 2999.00
    txt = re.sub(r"[^\d,]", "", txt).replace(",", ".") 
    return float(txt)