import requests
from bs4 import BeautifulSoup

PAGE_NAME = 'http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar'

#Função para baixar conteúdo da página
def get_page(page_url):
    return requests.get(page_url)

#Função para baixar arquivo
def download_file(url,file_name):
    new_file = open('Tarefa_1/'+file_name,'wb')
    response = get_page(url)
    new_file.write(response.content)
    print('Arquivo baixado com sucesso')

def main():
    #Baixando o html da página
    page = get_page(PAGE_NAME)
    soup = BeautifulSoup(page.text, 'html.parser')

    #Encontrando o link para a próxima página
    next_page=soup.find(class_='alert-link')
    next_page_link=next_page['href']
    next_page_link= 'http://www.ans.gov.br' + next_page_link

    #Baixando a próxima página
    page = get_page(next_page_link)
    soup = BeautifulSoup(page.text, 'html.parser')

    #Encontrando a tabela com os links para o download
    down_aux = soup.find_all('tr')
    down_link = None
    for tr in down_aux: #Encontrando o link correto para download
        if tr.find(text='Componente Organizacional') != None:
            a = tr.find('a')
            down_link = a['href']
            break

    #Completando link  
    down_link='http://www.ans.gov.br' + down_link

    #Baixando arquivo
    download_file(down_link,'Componente_Organizacional.pdf')

 
if __name__=='__main__':    
    main()