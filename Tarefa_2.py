from tabula import read_pdf,convert_into
import pandas



df = read_pdf('Componente_Organizacional.pdf',pages=[79,80,81,82,83,84,85])
df = pandas.DataFrame(df)
#table1=df.to_csv(index=False,encoding="utf-8")  
#print(table1)


compression_opts = dict(method='zip',archive_name='out.csv')  
df.to_csv('out.zip',encoding="utf-8",index=False,compression=compression_opts)  