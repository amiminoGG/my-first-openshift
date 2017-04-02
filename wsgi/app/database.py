from app import app
from flask_pymongo import PyMongo
from flask import jsonify, render_template
import os

app.config['MONGO_DBNAME'] = os.environ['OPENSHIFT_APP_NAME']
app.config['MONGO_URI'] = os.environ['OPENSHIFT_MONGODB_DB_URL'] + os.environ['OPENSHIFT_APP_NAME']

mongo = PyMongo(app)

@app.route('/database_all', methods=['GET'])
def get_all_database_info():
    collection = mongo.db.London_Visitors
    document = collection.find_one()
    output = []
    output.append({attr:value for attr, value in document.iteritems() if attr!=u'_id'})
    return render_template("database.html", show_text1 = mongo.db.collection_names(), show_text2 = dir(mongo.db), show_text3 = dir(mongo.db.London), show_text4 = output)

@app.route('/database/collections', methods=['GET'])
def get_all_databases():
    return jsonify({'result': mongo.db.collection_names()})

@app.route('/database/methods', methods=['GET'])
def get_db_methods_and_attributes():
    return jsonify({'All methods and attributes on a flask mongodb object' : dir(mongo.db)})

@app.route('/database/London/methods', methods=['GET'])
def get_collection_methods_and_attributes():
    return jsonify({'All methods and attributes on a flask mongodn collection object' : dir(mongo.db.London)})

@app.route('/database/London/sample', methods=['GET'])
def get_sample_document():
    collection = mongo.db.London_Visitors
    document = collection.find_one()
    output = []
    output.append({attr:value for attr, value in document.iteritems() if attr!=u'_id'})
    return jsonify({'sample record' : output})
