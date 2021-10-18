from flask import Flask, request, Response, jsonify
from elasticsearch import Elasticsearch
import json
import time

app = Flask(__name__)
es = Elasticsearch(['http://192.168.0.25:9200'])

@app.route('/get', methods=["GET"])
def getData():

    # Busca en Elastic solamente 10 documentos que tengan como index articles (http://192.168.0.6:9200/articles)
    data = es.search(index="articles", doc_type="_doc", size=10)
   # gol = data["hits"].decode('utf-8')
    # Abre o crea un archivos data.json y coloca los datos recibidos de data
    with open('data.json', encoding='utf-8', mode='w') as file:
        for hit in data['hits']['hits']:  
            data2=[
        {

            
            "_index": hit['_index'],
            "_id":  hit['_id'],
            "_source": {
                "category":  "\u00e1n" ,
                "title": "Pacto con Ir\u00e1n: el tribunal escuch\u00f3 otro nuevo pedido de nulidad de Cristina Kirchner y cambi\u00f3 el encuadre jur\u00eddico",
                "description": "El TOF 8 cit\u00f3 a las querellas para el mi\u00e9rcoles pr\u00f3ximo, pero bajo un art\u00edculo del C\u00f3digo Procesal distinto al que realiz\u00f3 la pol\u00e9mica audiencia preliminar. Los querellantes se preguntan si no es una \"trama jur\u00eddica\". ",
                "sourceUrl": "https://www.clarin.com/politica/pacto-iran-tribunal-escucho-nuevo-pedido-nulidad-cristina-kirchner-cambio-encuadre-juridico_0_MAXRyUeiC.html",
                "imageUrl": "https://images.clarin.com/2021/03/04/XrvGjYl0A_600x338__1.jpg",
                "publishedAt": "2021-08-25T19:41:13.000Z"
            }
        } 
        ]   
            json.dump(data, file, indent=4, ensure_ascii=False)
            print()

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
    new_data = es.index(index="articles", doc_type="_doc", id=8888, body=data)

    return Response(new_data['result'])


if __name__ == '__main__':
    app.run(debug=True)
