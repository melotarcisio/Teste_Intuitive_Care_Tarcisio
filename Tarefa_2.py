from tabula import read_pdf,convert_into
import pandas
import csv

def create_csv(file_content,file_name):
    new_file = open(file_name,'w')
    #file_content = csv.writer(file_contet)
    new_file.write(file_content)
    print('Arquivo criado com sucesso')

#Salvando as tabelas
df = read_pdf('Componente_Organizacional.pdf',pages=[79,80,81,82,83,84,85])
#Separando a primeira tabela
df1 = pandas.DataFrame(df[0])
df1 = df1.to_csv(sep=';',encoding='utf-8')
#Separando a segunda tabela
df2 = pandas.DataFrame(df[1])

df3 = pandas.DataFrame(df[2])
#table1=df.to_csv(index=False,encoding="utf-8")  
#print(df2)
create_csv(df1,'table1.csv')

compression_opts = dict(method='zip',archive_name='out.csv')
#df1.to_csv('out.zip',sep=';',compression=compression_opts)
print(df1)