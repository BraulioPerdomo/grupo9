def GrabarTemperaturaYHumedad(temperatura, humedad):
    import pymysql
    import datetime

    db = pymysql.connect(host='192.168.0.219', user='root', password='Braulio 55', db='AlmacendeTemperatura', charset='utf8')
    ahorita = datetime.datetime.now()
    sql = f"INSERT INTO Datos (fecha, temperatura, humedad) VALUES ('{ahorita}', {temperatura}, {humedad});"
    cur = db.cursor()
    cur.execute(sql)
    db.commit()
    db.close()