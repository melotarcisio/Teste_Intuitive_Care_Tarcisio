from tabula import read_pdf,convert_into
import pandas


#def new_file(file_name,file_content):
#    new_file = open(file_name,'wb')
#    #new_file.write(file_content.content)
#    print('Arquivo criado com sucesso')

df = read_pdf('Componente_Organizacional.pdf',pages=79)
df = pandas.DataFrame(df[0])
#table1=df.to_csv('out.zip',encoding="utf-8",compression=compression_opts)  
#new_file('Tabela1.csv',table1)
#print(table1)

compression_opts = dict(method='zip',archive_name='out.csv')  
df.to_csv('out.zip',encoding="utf-8",index=False,compression=compression_opts)  