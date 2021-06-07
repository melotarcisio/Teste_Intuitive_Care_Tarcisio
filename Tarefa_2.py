from tabula import read_pdf,convert_into
import pandas



df = read_pdf('Componente_Organizacional.pdf',pages=[79,80,81,82,83,84,85])
df1 = pandas.DataFrame(df[0])
df2 = pandas.DataFrame(df[1])
df3 = pandas.DataFrame(df[2])
#table1=df.to_csv(index=False,encoding="utf-8")  
print(df2)


compression_opts = dict(method='zip',archive_name='out.csv')
df1.to_csv('out.zip',sep=';',compression=compression_opts)
print(df1.to_csv(sep=';'))