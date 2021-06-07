import requests
from bs4 import BeautifulSoup

def get_page(page_name):
    return requests.get(page_name)

def download_file(url,file_name):
    new_file = open(file_name,'wb')
    response = get_page(url)
    new_file.write(response.content)
    print('Arquivo baixado com sucesso')

def main():
    page_name = 'http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar'
    page = get_page(page_name)
    soup = BeautifulSoup(page.text, 'html.parser')

    next_page=soup.find(class_='alert-link')
    next_page_link=next_page['href']
    next_page_link= 'http://www.ans.gov.br' + next_page_link
    print(next_page_link)

    page = get_page(next_page_link)
    soup = BeautifulSoup(page.text, 'html.parser')

    down_aux = soup.find_all('tr')
    down_link = None
    
    for tr in down_aux:
        if tr.find(text='Componente Organizacional') != None:
            a = tr.find('a')
            down_link = a['href']
            break
      
    down_link='http://www.ans.gov.br' + down_link

    download_file(down_link,'Componente_Organizacional.pdf')

        

if __name__=='__main__':    
    main()