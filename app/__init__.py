from flask import Flask
from flask_cors import CORS
from flask import jsonify, request
from flask_pymongo import ObjectId, PyMongo

app = Flask(__name__)
CORS(app)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/nutrilike'
mongo = PyMongo(app)
db = mongo.db

@app.route('/proteins', methods=['GET'])
def protein():

    products = []
    for doc in db.protein.find():
        products.append({
            "_id" : str(ObjectId(doc['_id'])),
            "name": doc['name'],
            "measurement": doc['measurement'],
            "quantity": doc['quantity'],
            "calories": doc['calories']
        })

    return jsonify(products)

@app.route('/protein/<id>', methods=['GET'])
def getProtein(id):

    doc = db.protein.find_one({ "_id": ObjectId(id) })
    product = {
        "_id" : str(ObjectId(doc['_id'])),
        "name": doc['name'],
        "measurement": doc['measurement'],
        "quantity": doc['quantity'],
        "calories": doc['calories']
    } 

    return jsonify(product)

@app.route('/protein', methods=['POST'])
def postProtein():

    id = db.protein.insert_one({
        "name": request.json['name'],
        "measurement": request.json['measurement'],
        "quantity": request.json['quantity'],
        "calories": request.json['calories']
    })
    name = str(request.json['name'])
    response = {
        "_id": str(id.inserted_id),
        "msg": f'producto {name} agregado exitosamente'
        } 

    return jsonify(response)

@app.route('/protein/<id>', methods=['DELETE'])
def deleteProtein(id):

    db.protein.delete_one({ "_id": ObjectId(id) })
    response = {
        "msg": "Product deleted"
    }
    return jsonify(response)

@app.route('/protein/<id>', methods=['PUT'])
def updateProtein(id):

    db.protein.update_one({ "_id": ObjectId(id) }, { '$set': {
        "name": request.json['name'],
        "measurement": request.json['measurement'],
        "quantity": request.json['quantity'],
        "calories": request.json['calories']
    }})
    response = {
        "msg": "product updated"
    }

    return jsonify(response)

@app.route('/lipids', methods=['GET'])
def lipids():

    products = []
    for doc in db.lipid.find():
        products.append({
            "_id" : str(ObjectId(doc['_id'])),
            "name": doc['name'],
            "measurement": doc['measurement'],
            "quantity": doc['quantity'],
            "calories": doc['calories']
        })

    return jsonify(products)

@app.route('/lipid/<id>', methods=['GET'])
def getLipid(id):

    doc = db.lipid.find_one({ "_id": ObjectId(id) })
    product = {
        "_id" : str(ObjectId(doc['_id'])),
        "name": doc['name'],
        "measurement": doc['measurement'],
        "quantity": doc['quantity'],
        "calories": doc['calories']
    } 

    return jsonify(product)

@app.route('/lipid', methods=['POST'])
def postLipid():

    id = db.lipid.insert_one({
        "name": request.json['name'],
        "measurement": request.json['measurement'],
        "quantity": request.json['quantity'],
        "calories": request.json['calories']
    })
    name = str(request.json['name'])
    response = {
        "_id": str(id.inserted_id),
        "msg": f'producto {name} agregado exitosamente'
        } 

    return jsonify(response)

@app.route('/lipid/<id>', methods=['DELETE'])
def deleteLipid(id):

    db.lipid.delete_one({ "_id": ObjectId(id) })
    response = {
        "msg": "Product deleted"
    }
    return jsonify(response)

@app.route('/lipid/<id>', methods=['PUT'])
def updateLipid(id):

    db.lipid.update_one({ "_id": ObjectId(id) }, { '$set': {
        "name": request.json['name'],
        "measurement": request.json['measurement'],
        "quantity": request.json['quantity'],
        "calories": request.json['calories']
    }})
    response = {
        "msg": "product updated"
    }

    return jsonify(response)

@app.route('/complexs', methods=['GET'])
def complex():

    products = []
    for doc in db.complex.find():
        products.append({
            "_id" : str(ObjectId(doc['_id'])),
            "name": doc['name'],
            "measurement": doc['measurement'],
            "quantity": doc['quantity'],
            "calories": doc['calories']
        })

    return jsonify(products)

@app.route('/complex/<id>', methods=['GET'])
def getComplex(id):

    doc = db.complex.find_one({ "_id": ObjectId(id) })
    product = {
        "_id" : str(ObjectId(doc['_id'])),
        "name": doc['name'],
        "measurement": doc['measurement'],
        "quantity": doc['quantity'],
        "calories": doc['calories']
    } 

    return jsonify(product)

@app.route('/complex', methods=['POST'])
def postComplex():

    id = db.complex.insert_one({
        "name": request.json['name'],
        "measurement": request.json['measurement'],
        "quantity": request.json['quantity'],
        "calories": request.json['calories']
    })
    name = str(request.json['name'])
    response = {
        "_id": str(id.inserted_id),
        "msg": f'producto {name} agregado exitosamente'
        } 

    return jsonify(response)

@app.route('/complex/<id>', methods=['DELETE'])
def deleteComplex(id):

    db.complex.delete_one({ "_id": ObjectId(id) })
    response = {
        "msg": "Product deleted"
    }
    return jsonify(response)

@app.route('/complex/<id>', methods=['PUT'])
def updateComplex(id):

    db.complex.update_one({ "_id": ObjectId(id) }, { '$set': {
        "name": request.json['name'],
        "measurement": request.json['measurement'],
        "quantity": request.json['quantity'],
        "calories": request.json['calories']
    }})
    response = {
        "msg": "product updated"
    }

    return jsonify(response)

@app.route('/simples', methods=['GET'])
def simple():

    products = []
    for doc in db.simple.find():
        products.append({
            "_id" : str(ObjectId(doc['_id'])),
            "name": doc['name'],
            "measurement": doc['measurement'],
            "quantity": doc['quantity'],
            "calories": doc['calories']
        })

    return jsonify(products)

@app.route('/simple/<id>', methods=['GET'])
def getSimple(id):

    doc = db.simple.find_one({ "_id": ObjectId(id) })
    product = {
        "_id" : str(ObjectId(doc['_id'])),
        "name": doc['name'],
        "measurement": doc['measurement'],
        "quantity": doc['quantity'],
        "calories": doc['calories']
    } 

    return jsonify(product)

@app.route('/simple', methods=['POST'])
def postSimple():

    id = db.simple.insert_one({
        "name": request.json['name'],
        "measurement": request.json['measurement'],
        "quantity": request.json['quantity'],
        "calories": request.json['calories']
    })
    name = str(request.json['name'])
    response = {
        "_id": str(id.inserted_id),
        "msg": f'producto {name} agregado exitosamente'
        } 

    return jsonify(response)

@app.route('/simple/<id>', methods=['DELETE'])
def deleteSimple(id):

    db.simple.delete_one({ "_id": ObjectId(id) })
    response = {
        "msg": "Product deleted"
    }
    return jsonify(response)

@app.route('/simple/<id>', methods=['PUT'])
def updateSimple(id):

    db.simple.update_one({ "_id": ObjectId(id) }, { '$set': {
        "name": request.json['name'],
        "measurement": request.json['measurement'],
        "quantity": request.json['quantity'],
        "calories": request.json['calories']
    }})
    response = {
        "msg": "product updated"
    }

    return jsonify(response)

@app.route('/stringy', methods=['GET'])
def fribrous():

    products = []
    for doc in db.fibrous.find():
        products.append({
            "_id" : str(ObjectId(doc['_id'])),
            "name": doc['name'],
            "measurement": doc['measurement'],
            "quantity": doc['quantity'],
            "calories": doc['calories']
        })

    return jsonify(products)

@app.route('/fibrous/<id>', methods=['GET'])
def getFibrous(id):

    doc = db.fibrous.find_one({ "_id": ObjectId(id) })
    product = {
        "_id" : str(ObjectId(doc['_id'])),
        "name": doc['name'],
        "measurement": doc['measurement'],
        "quantity": doc['quantity'],
        "calories": doc['calories']
    } 

    return jsonify(product)

@app.route('/fibrous', methods=['POST'])
def postFibrous():

    id = db.fibrous.insert_one({
        "name": request.json['name'],
        "measurement": request.json['measurement'],
        "quantity": request.json['quantity'],
        "calories": request.json['calories']
    })
    name = str(request.json['name'])
    response = {
        "_id": str(id.inserted_id),
        "msg": f'producto {name} agregado exitosamente'
        } 

    return jsonify(response)

@app.route('/fibrous/<id>', methods=['DELETE'])
def deleteFibrous(id):

    db.fibrous.delete_one({ "_id": ObjectId(id) })
    response = {
        "msg": "Product deleted"
    }
    return jsonify(response)

@app.route('/fibrous/<id>', methods=['PUT'])
def updateFibrous(id):

    db.fibrous.update_one({ "_id": ObjectId(id) }, { '$set': {
        "name": request.json['name'],
        "measurement": request.json['measurement'],
        "quantity": request.json['quantity'],
        "calories": request.json['calories']
    }})
    response = {
        "msg": "product updated"
    }

    return jsonify(response)