from tabula import read_pdf
import pandas
import zipfile
import os

#Salvando as tabelas
D_F = read_pdf('Tarefa_1/Componente_Organizacional.pdf',pages=[79,80,81,82,83,84,85])


def create_csv(file_content,file_name):
    new_file = open(file_name,'w')
    new_file.write(file_content)
    print('Arquivo criado com sucesso')
    new_file.close()

def repair_table(df):
    df.columns = ['Código;Descrição da categoria']
    df = df.drop(0)
    for linha in range(df.shape[0]):
        df.iat[linha,0]=df.iat[linha,0].replace(' ', ';',1)
    df = df.sort_index()
    return df

def table_concatenate(df):
    dfs = [None,None,None,None,None,None]
    dfs[0] = pandas.DataFrame(df[1])
    dfs[0].columns = ['Código','Descrição da categoria']
    dfs[0] = dfs[0].drop(0)
    dfs[0].index=dfs[0].index-1
    df2 = dfs[0]
    for pagina  in range(1,6):
        dfs[pagina] = pandas.DataFrame(df[pagina+1])
        dfs[pagina].loc[-1] = dfs[pagina].columns
        dfs[pagina].columns = ['Código','Descrição da categoria']
        dfs[pagina].index = dfs[pagina].index + df2.shape[0] +1
        dfs[pagina] = dfs[pagina].sort_index()
        df2 = pandas.concat([df2,dfs[pagina]],axis=0)
    return df2  

def zip_files(zip_name,files_,):
    zf=zipfile.ZipFile('Tarefa_2/' + zip_name,'w')
    for file_name in files_:
        zf.write(file_name)
        os.remove(file_name)
    zf.close()


def main():
    files = ['table1.csv','table2.csv','table3.csv']

    #Primeira tabela
    df1 = pandas.DataFrame(D_F[0])
    df1 = repair_table(df1)         #Resolvendo o problema de leitura da tabela
    df1 = df1.to_csv(encoding='utf-8',index=False)
    create_csv(df1,'table1.csv')

    #Segunda tabela
    df2 = table_concatenate(D_F)        #Para concatenar a tabela que se estende por várias páginas no pdf
    df2 = df2.to_csv(sep=';',encoding='utf-8',index=False)
    create_csv(df2,'table2.csv')


    #Terceira tabela
    df3 = pandas.DataFrame(D_F[7])
    df3 = repair_table(df3)        #Resolvendo o problema de leitura da tabela
    df3 = df3.to_csv(encoding='utf-8',index=False)
    create_csv(df3,'table3.csv')

    #Compactando arquivos
    zip_files('Teste_Intuitive_Care_Tarcisio.zip',files)


if __name__=='__main__':    
    main()