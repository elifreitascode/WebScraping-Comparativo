from bs4 import BeautifulSoup
import win32com.client as win32
import requests

URL1 = 'https://produto.mercadolivre.com.br/MLB-2024353694-pc-gamer-facil-ryzen-7-5700g-vega-8-ssd-480gb-16gb-ddr4-500w-_JM#position=9&search_layout=grid&type=item&tracking_id=8bf89ebb-b21c-4915-96d3-2fbba6817e50'

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'}

site1 = requests.get(URL1, headers=headers)

soup = BeautifulSoup(site1.content, 'html.parser')

nome_produto1 = soup.find('h1', class_ = 'ui-pdp-title').get_text()

preço = soup.find('div', class_= 'ui-pdp-price__second-line').get_text().strip()

# ANTES DO PREÇO EM FORMA NUMÉRICA,TEM UMA ESCRITA INFORMANDO O PREÇO EM FORMA DE TEXTO,TEM QUE REMOVER ELA E DEIXAR APENAS O PREÇO EM FORMATO NUMÉRICO,USANDO A FUNÇAO STRIP PRA REMOVER

formato_preço = preço[12:18]

# TIRAR O PONTO,USANDO A FUNÇAO REPLACE

formato_preço = formato_preço.replace('.','')

# TRANSFORMAR EM UM NÚMERO REAL,POIS ELE ESTÁ COM UMA STRING

formato_preço=float(formato_preço)

 
# PEGAR O MESMO MODELO DE PRODUTO,NO SEGUNDO SITE
# REPETIR O PROCESSO

URL2 = 'https://www.kabum.com.br/produto/448296/pc-gamer-facil-computadores-amd-ryzen-5-5600g-16gb-ssd-480gb-linux-preto-21045'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'}

site2 = requests.get(URL2, headers=headers)

soup = BeautifulSoup(site2.content, 'html.parser')

nome_produto2 = soup.find('h1', class_= 'sc-89bddf0f-6 dDYTAu').get_text()

preço2 = soup.find('b',  class_='regularPrice').get_text().strip()

formato_preço2 = preço2 [3:8]

formato_preço2 = formato_preço2.replace('.','')

formato_preço2 = float(formato_preço2)


# PEGAR O MESMO MODELO DE PRODUTO NO TERCEIRO SITE
# REPETIR O PROCESSO (SE A QUANTIDADE DE SITES QUE EU QUERO PEGAR O PRODUTO,FOR MUITO GRANDE. USAR UM VETOR E UMA ESTRUTURA DE REPETIÇÃO)

URL3 = 'https://www.kabum.com.br/produto/441695/pc-gamer-eletronic-artssypc-plus-intel-6-nucleos-12-threads-8gb-ram-ddr4-geforce-gtx-1660-ti-6gb-ssd-480gb-fonte-500w-3gpl-006'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'}

site3 = requests.get(URL3, headers=headers)

soup = BeautifulSoup(site3.content, 'html.parser')

nome_produto3 = soup.find('h1', class_= 'sc-89bddf0f-6 dDYTAu').get_text()

preço3 = soup.find('b',  class_='regularPrice').get_text().strip()

formato_preço3 = preço3 [3:8]

formato_preço3 = formato_preço3.replace('.','')

formato_preço3 = float(formato_preço3)


def enviar_email1():
    # CRIAR A INTEGRAÇÃO COM O OUTLOOK (APP DE EMAIL QUE UTLIZO NO WINDOWS)
    outlook = win32.Dispatch('outlook.application')
    # CRIAR O EMAIL
    email= outlook.CreateItem(0)
    # INFORMAÇÕES DO EMAIL
    email.To = 'webscrapingproduto1@gmail.com'
    # ASSUNTO DO EMAIL
    email.Subject = 'PREÇO PC GAMER RYZEN 7'
    # CORPO DO EMAIL
    email.HTMLBody =f'''
    <p>Olá !</p> 
    
    <p>Seu produto:</p>
    <p>{nome_produto1}</p>
    
    <p>No site:</p>
    <p>{URL1}</p>
    <p>ESTÁ COM O VALOR QUE VOCÊ DESEJA !</p>

    <p>Abs,</p>
    <p>Elizeu Freitas</p>
    '''
    email.Send()
    print('EMAIL ENVIADO COM SUCESSO !')
def enviar_email2():
    # CRIAR A INTEGRAÇÃO COM O OUTLOOK (APP DE EMAIL QUE UTLIZO NO WINDOWS)
    outlook = win32.Dispatch('outlook.application')
    # CRIAR O EMAIL
    email= outlook.CreateItem(0)
    # INFORMAÇÕES DO EMAIL
    email.To = 'webscrapingproduto1@gmail.com'
    # ASSUNTO DO EMAIL
    email.Subject = 'PREÇO PC GAMER RYZEN 7'
    # CORPO DO EMAIL
    email.HTMLBody =f'''
    <p>Olá !</p> 
    
    <p>Seu produto:</p>
    <p>{nome_produto2}</p>
    
    <p>No site:</p>
    <p>{URL2}</p>
    <p>ESTÁ COM O VALOR QUE VOCÊ DESEJA !</p>

    <p>Abs,</p>
    <p>Elizeu Freitas</p>
    '''
    email.Send()
    print('EMAIL ENVIADO COM SUCESSO !')
def enviar_email3():
    # CRIAR A INTEGRAÇÃO COM O OUTLOOK (APP DE EMAIL QUE UTLIZO NO WINDOWS)
    outlook = win32.Dispatch('outlook.application')
    # CRIAR O EMAIL
    email= outlook.CreateItem(0)
    # INFORMAÇÕES DO EMAIL
    email.To = 'webscrapingproduto1@gmail.com'
    # ASSUNTO DO EMAIL
    email.Subject = 'PREÇO PC GAMER RYZEN 7'
    # CORPO DO EMAIL
    email.HTMLBody =f'''
    <p>Olá !</p> 
    
    <p>Seu produto:</p>
    <p>{nome_produto3}</p>
    
    <p>No site:</p>
    <p>{URL3}</p>
    <p>ESTÁ COM O VALOR QUE VOCÊ DESEJA !</p>

    <p>Abs,</p>
    <p>Elizeu Freitas</p>
    '''
    email.Send()
    print('EMAIL ENVIADO COM SUCESSO !')

valor_desejado = 3200

if formato_preço <= valor_desejado:
    enviar_email1()
elif formato_preço2 <= valor_desejado:
    enviar_email2()
elif formato_preço3 <= valor_desejado:
    enviar_email3()    

if formato_preço <= valor_desejado and formato_preço2 <= valor_desejado and formato_preço3 <= valor_desejado:
    enviar_email1()
    enviar_email2()
    enviar_email3()
elif formato_preço <= valor_desejado and formato_preço2 <= valor_desejado:
    enviar_email1()
    enviar_email2()
elif formato_preço <= valor_desejado and formato_preço3 <= valor_desejado:
    enviar_email1()
    enviar_email3()
elif formato_preço2 <= valor_desejado and formato_preço3<= valor_desejado:
    enviar_email2()
    enviar_email3()
 