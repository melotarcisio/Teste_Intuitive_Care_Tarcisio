from tabula import read_pdf,convert_into
import pandas
import csv

#Salvando as tabelas
D_F = read_pdf('Componente_Organizacional.pdf',pages=79)
D_F2 = read_pdf('Componente_Organizacional.pdf',pages=[79,80,81,82,83,84])
D_F3 = read_pdf('Componente_Organizacional.pdf',pages=85)

def create_csv(file_content,file_name):
    new_file = open(file_name,'w')
    new_file.write(file_content)
    print('Arquivo criado com sucesso')

def repair_name(tbl):
    tbl = tbl.drop(0)
    tbl.columns = ['Código','Descrição da categoria']
    return tbl

def main():


    #Separando a primeira tabela
    df1 = pandas.DataFrame(D_F[0])
    #df1 = repair_name(df1)
    #df1 = df1.to_csv(sep=';',encoding='utf-8')

    #Separando a segunda tabela
    i = [None,None,None,None,None,None]
    i[0] = pandas.DataFrame(D_F2[1])
    i[0].columns = ['Código','Descrição da categoria']
    i[0] = i[0].drop(0)
    i[0].index=i[0].index-1
    j = 1
    df2 = i[0]
    while j<6:
        i[j] = pandas.DataFrame(D_F2[j+1])
        i[j].loc[-1] = i[j].columns
        i[j].columns = ['Código','Descrição da categoria']
        i[j].index = i[j].index + df2.shape[0] +1
        i[j] = i[j].sort_index()
        df2 = pandas.concat([df2,i[j]],axis=0)
        j = j+1
    df2 = df2.to_csv(sep=';',encoding='utf-8')  
    #print(j)

  
 
    create_csv(df2,'table2.csv')

    
    
    
    
    
    #compression_opts = dict(method='zip',archive_name='out.csv')
    #df1.to_csv('out.zip',sep=';',compression=compression_opts)

if __name__=='__main__':    
    main()