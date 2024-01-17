def leerDatos():
    import pymysql
    import datetime

    db = pymysql.connect(host='192.168.0.219', user='root', password='Braulio 55', db='AlmacendeTemperatura', charset='utf8')
    ahorita = datetime.datetime.now()
    sql = f"SELECT id, fecha, temperatura, humedad FROM Datos ORDER BY fecha desc limit 20;"
    cur = db.cursor()
    cur.execute(sql)
    resultado = cur.fetchall()
    db.commit()
    db.close()
    return resultado