import pyodbc
import pandas as pd

import requests
import json
from urllib import response

# Connection DB
direccion_servidor = 'libreria.c8jwd6wz5gva.us-east-1.rds.amazonaws.com'
nombre_bd = 'libreria'
nombre_usuario = 'admin'
password = 'admin2023*'
conn_str = ('DRIVER={SQL Server};SERVER=' +
                              direccion_servidor+';DATABASE='+nombre_bd+';UID='+nombre_usuario+';PWD=' + password)

# Connection API
ts=1
private_key = 'dd1da31a3335f53015282ec2f2d4afece46c6eb5'
public_key ='6e3cfc3811d936d54abec2bc8d8eeeea'
hashed ="d79e45ff312ea26ad105cbed25fafc8f"
#URLCharacters
urlCharacters = [f"https://gateway.marvel.com:443/v1/public/characters?ts={ts}&apikey={public_key}&hash={hashed}", 1]
#URLComics
urlComics = [f"https://gateway.marvel.com:443/v1/public/comics?ts={ts}&apikey={public_key}&hash={hashed}", 2]
Url = urlComics

response = requests.get(Url[0])

# Exec procedure
storedProcCharacters = "exec added_characters @name = ?, @description = ?, @modified = ?, @thumbnail = ?"
storedProcComics = "exec added_comics @digitalId = ?, @title = ?, @issueNumber = ?, @variantDescription = ?, @description = ?, @modified = ?, @isbn = ?, @upc = ?, @diamondCode = ?, @ean = ?, @issn = ?, @format = ? , @pageCount = ?, @textObjects = ?" 

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
if response.status_code==200:
    response_json =json.loads(response.text)
    
    for i in response_json["data"]["results"]:
         if Url[1]==1:
            nombre = i["name"]
            description = i["description"]
            modified = i["modified"]
            thumbnail = str(i["thumbnail"])

            cursor.execute(storedProcCharacters, nombre, description, modified, thumbnail)
         if Url[1]==2:
            digitalId = int(i["digitalId"])
            title = i["title"]
            issueNumber = str(i["issueNumber"])
            variantDescription = (i["variantDescription"])
            description = i["description"]
            modified = i["modified"]
            isbn = (i["isbn"])
            upc = i["upc"]
            diamondCode = i["diamondCode"]
            ean = (i["ean"])
            issn = i["issn"]
            format = i["format"]
            pageCount = int((i["pageCount"]))
            textObjects = str((i["textObjects"]))

            cursor.execute(storedProcComics, digitalId, title, issueNumber, variantDescription, description, modified, isbn, upc, diamondCode, ean, issn, format, pageCount, textObjects)

conn.commit()
conn.close()
cursor.close()
