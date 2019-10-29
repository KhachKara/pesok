import camelot

#source = 'Tele2-Details-2019-09-79773895866.pdf'
#table = camelot.raed_pdf(source)
#print(table.df)
source = 'Tele2-Details-2019-09-79773895866.pdf'

print(camelot.read_pdf(source).df)