import json
import requests

def postData():
    '''
        print("Categoria:")
        category = str(input())
        print("titulo")
        title = str(input())
        print("descripcion")
        description = str(input())
        print("Enlace del articulo")
        sourceUrl = str(input())
        print("Enlace de la imagen")
        imageUrl = str(input())
        print("Horario de publicacion")
        publishedAt = str(input())

        data = {
            "category": category,
            "title": title,
            "description": description,
            "sourceUrl": sourceUrl,
            "imageUrl": imageUrl,
            "publishedAt": publishedAt
        }
    '''

    # datos del nuevo articulo
    date = {
        "category": "Política",
        "title": "Pacto con Irán: el tribunal escuchó otro nuevo pedido de nulidad de Cristina Kirchner y cambió el encuadre jurídico",
        "description": "El TOF 8 citó a las querellas para el miércoles próximo, pero bajo un artículo del Código Procesal distinto al que realizó la polémica audiencia preliminar. Los querellantes se preguntan si no es una \"trama jurídica\". ",
        "sourceUrl": "https://www.clarin.com/politica/pacto-iran-tribunal-escucho-nuevo-pedido-nulidad-cristina-kirchner-cambio-encuadre-juridico_0_MAXRyUeiC.html",
        "imageUrl": "https://images.clarin.com/2021/03/04/XrvGjYl0A_600x338__1.jpg",
        "publishedAt": "2021-08-25T19:41:13.000Z"
    }

    # se envian los datos al server flask
    result = requests.post('http://192.168.0.6:5000/post', json= date)

 
    print(result.text)    



if __name__ == '__main__':
    postData()
