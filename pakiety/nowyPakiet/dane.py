import time

def pobierz_date():
    data= time.gmtime()
    print(data.tm_year,'-',data.tm_mon,'-',data.tm_mday, 'nowa data')