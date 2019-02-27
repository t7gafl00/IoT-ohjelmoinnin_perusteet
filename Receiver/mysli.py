# -*- coding: utf-8 -*-
# Author: Florian Gabelle

import mysql.connector
import datetime

#Connect to database
db = mysql.connector.connect(
    host = "mysli.oamk.fi",
    user = "t7gafl00",
    passwd = "cfCcr3hr4c3CgyNZ",
    database = "opisk_t7gafl00"
    )

#Writes sensor values to database
def to_db(value1, value2, value3, value4):
    cursor = db.cursor()
    sql = "INSERT INTO iot (date, temperature, pressure, humidity, luminance) VALUES(now(), %s, %s, %s, %s)"
    val = (value1, value2, value3, value4)

    try:
        # Execute SQL command
        cursor.execute(sql, val)
        # Commit your changes in the database
        db.commit()
    
    except:
        # Rollback in case there is any error
        db.rollback()
        
    print(cursor.rowcount, "record inserted.", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S:%f"))