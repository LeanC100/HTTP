from flask import Flask, request, Response, jsonify
from elasticsearch import Elasticsearch
import json
import time

app = Flask(__name__)
es = Elasticsearch(['http://192.168.0.6:9200'])


@app.route('/get', methods=["GET"])
def getData():

    # Busca en Elastic solamente 10 documentos que tengan como index articles (http://192.168.0.6:9200/articles)
    data = es.search(index="articles", doc_type="_doc", size=10)
    # Abre o crea un archivos data.json y coloca los datos recibidos de data
    with open('data.json', 'w') as file:
        json.dump(data["hits"], file, indent=4)

    return data


@app.route('/post', methods=["POST"])
def postData():

    # Coloca los datos recibidos
    data = {
        "category": request.json['category'],
        "title": request.json['title'],
        "description": request.json['description'],
        "sourceUrl": request.json['sourceUrl'],
        "imageUrl": request.json['imageUrl'],
        "publishedAt": request.json['publishedAt'],
    }

    # inserta el nuevo articulo en Elastic
    new_data = es.index(index="articles", doc_type="_doc", id=9999, body=data)

    return Response(new_data['result'])


if __name__ == '__main__':
    app.run(debug=True)
