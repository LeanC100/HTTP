from flask import Flask,request,Response, jsonify
from elasticsearch import Elasticsearch
import json
import time

app= Flask(__name__)
es = Elasticsearch(['http://192.168.0.6:9200'])

@app.route('/get', methods=["GET"])
def getData():

    # Busca en Elastic solamente 10 documentos que tengan como index articles (http://192.168.0.6:9200/articles)
    data = es.search(index="articles", doc_type="_doc", size=10)
    # Abre o crea un archivos data.json y coloca los datos recibidos de data
    with open('data.json', 'w') as file:
        json.dump(data["hits"], file, indent=4)
        
    return data


if __name__ == '__main__':
    app.run(debug=True)
