import sys
import http.server
import socketserver
from flask import Flask, json, request
from flask_cors import CORS
import requests
sys.path.append('..')
import utils.dbProvider as dbp
from controllers.block import Block
from controllers.blockModel import BlockModel
import werkzeug
from http.server import BaseHTTPRequestHandler
from urllib import parse

argv = sys.argv
database = dbp.DBProvider()
api_trace = "https://gentle-coast-69723.herokuapp.com/api/apps/a0d8b0dd5a0556e788da64cb4c559586/traces/"
dev_app_id = "a0d8b0dd5a0556e788da64cb4c559586"
prod_app_id = "11f3aee68e09d3d6a5600bcfa8bc2229"


api = Flask(__name__)
CORS(api)
@api.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400
@api.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, werkzeug.exceptions.HTTPException):
        return e
@api.route('/api/block_models/', methods=['GET'])
def get_blocks_models():
    r = requests.get('https://dry-brushlands-69779.herokuapp.com/api/feature_flags/')
    content = request.get_json()
    if bool(r.json()['restful_response']):
        return json.dumps({"block_models":database.get_blocks_names()})
    else:
        return json.dumps(database.get_blocks_names())

@api.route('/api/block_models/<block_model_name>/', methods=['POST'])
def load_blocks_of_model(block_model_name):
    content = request.get_json()
    column_raw = content['columns']
    columns_names = column_raw.split(" ")
    data = content['data']
    attributes_types = content['attributes_types'].split()
    mass_attribute = content['mass_attribute']
    collection = database.select_collection(block_model_name)
    block_model = BlockModel(block_model_name)
    database.load_blocks(data,block_model_name,columns_names, attributes_types, mass_attribute)
    trace_json = {
        "trace": {
            "span_id": database.create_span_id(),
            "event_name": "block_model_loaded",
            "event_data": block_model_name,
        }
    }
    requests.post(api_trace, json=trace_json)
    return json.dumps(content)

@api.route('/api/block_models/<block_model_name>/blocks/', methods=['GET', 'POST'])
def get_blocks_of_model(block_model_name):
    print(request.method)
    if request.method == 'GET':
        block_model = BlockModel(block_model_name).get_blocks(database)
        r = requests.get('https://dry-brushlands-69779.herokuapp.com/api/feature_flags/')
        content = request.get_json()
        trace_json = {
            "trace": {
                "span_id": database.get_span_id(),
                "event_name": "blocks_requested",
                "event_data": block_model_name,
            }
        }
        requests.post(api_trace, json=trace_json)
        if bool(r.json()['restful_response']):
            return json.dumps({"block_model":{"blocks":block_model}})
        else:
            return json.dumps(block_model)
 
    
@api.route('/api/block_models/<block_model_name>/blocks/<index>', methods=['GET'])
def get_block_info(block_model_name,index):
    if request.method == 'GET':
        collection = database.select_collection(block_model_name)
        block_by_index = BlockModel(block_model_name).find_block_by_index(index, collection)
        r = requests.get('https://dry-brushlands-69779.herokuapp.com/api/feature_flags/')
        content = request.get_json()
        block = block_by_index.info_json(block_model_name, database)
        trace_json = {
            "trace": {
                "span_id": database.get_span_id(),
                "event_name": "blocks_info_requested",
                "event_data": block["x"] + "," + 
                block["y"] + "," +  block["z"],
            }
        }
        requests.post(api_trace, json=trace_json)
        if bool(r.json()['restful_response']):
            return json.dumps({"block":block})
        else:
            return json.dumps(block)
    

@api.route('/api/block_models/<block_model_name>/reblock/', methods=['POST'])
def reblock_model(block_model_name):
    content = request.get_json()
    reblock_x = int(content['reblock_x'])
    reblock_y = int(content['reblock_y'])
    reblock_z = int(content['reblock_z'])
    attributes_types = content['attributes_types'].split()
    collection = database.select_collection(block_model_name)
    mass_attribute = content['mass_attribute']
    block_model = BlockModel(block_model_name)
    reblock_model_collection = block_model.reblock(collection, reblock_x, reblock_y, reblock_z, attributes_types, mass_attribute)
    reblock_collection = reblock_model_collection.find({})
    return_json = []
    for block in reblock_collection:
        return_json.append(block)
    trace_json = {
            "trace": {
                "span_id": database.get_span_id(),
                "event_name": "blocks_requested",
                "event_data": block_model_name + "_reblock",
            }
        }
    requests.post(api_trace, json=trace_json)
    return json.dumps({"status": "reblocked"})

@api.route('/api/block_models/<block_model_name>/prec/', methods=['POST'])
def load_prec(block_model_name):
    content = request.get_json()
    prec_list = content['prec_list']
    database.load_prec(prec_list, block_model_name)
    trace_json = {
            "trace": {
                "span_id": database.get_span_id(),
                "event_name": "block_model_precedences_loaded",
                "event_data": block_model_name + "_prec",
            }
        }
    requests.post(api_trace, json=trace_json)
    return json.dumps({"status": "loaded_prec"})

@api.route('/api/block_models/<block_model_name>/blocks/<index>/extract/', methods=['POST'])
def delete_prec(block_model_name, index):
    content = request.get_json()
    block_model = BlockModel(block_model_name)
    deleted = block_model.delete_block_prec(index)
    collection = database.select_collection(block_model_name)
    block_by_index = BlockModel(block_model_name).find_block_by_index(index, collection)
    block = block_by_index.info_json(block_model_name, database)
    trace_json = {
            "trace": {
                "span_id": database.get_span_id(),
                "event_name": "block_extracted",
                "event_data": block["x"] + "," + 
                block["y"] + "," +  block["z"],
            }
        }
    requests.post(api_trace, json=trace_json)
    return json.dumps({"blocks": deleted})


if __name__ == '__main__':
    api.run(host='0.0.0.0')





if __name__ == "__main__":
    #Load blocks from a file giving the path into database
    if argv[1] == "-lf":
        block_model_name = argv[3]
        print("Insert the column names in the order of the file separated by one space")
        column_raw = input()
        columns_names = column_raw.split(" ")       
        path = argv[2]                              
        collection = database.select_collection(block_model_name)
        block_model = BlockModel(block_model_name)
        database.load_blocks(path,block_model_name,columns_names)
    #Number of mine blocks
    elif argv[2] == "num_blocks":
        block_model_name = argv[1]
        block_model = BlockModel(block_model_name)
        collection = database.select_collection(block_model_name)
        result = block_model.blocks_count(collection)
        print(result)
    #Mass value of block
    elif len(argv) > 5 and argv[5] == "mass":
        mass_name = input("Enter the name of mass column: ")
        weight_name = input("[1]KG \n[2]TONS\n")
        block_model_name = argv[1]
        coordinate_x = argv[2]
        coordinate_y = argv[3]
        coordinate_z = argv[4]
        block_model = BlockModel(block_model_name)
        db = database.select_collection(block_model_name)
        block = block_model.find_block(coordinate_x,coordinate_y,coordinate_z, db)
        if block:
            result = block.block_mass(mass_name, weight_name)
            print(result)
        else:
            print("Block not found")
    #reblock
    elif argv[2] =="reblock":
        block_model_name = argv[1]
        reblock_x = int(argv[3])
        reblock_y = int(argv[4])
        reblock_z = int(argv[5])
        collection = database.select_collection(block_model_name)
        block_model = BlockModel(block_model_name)
        print("Insert the attributes types printed bellow separeted by space")
        print("Types:\n\tCategorical: cat\n\tProportional: prop\n\tContinue: con")
        print(' '.join(map(str, block_model.reblock_model_attributes(collection))))

        attributes_types = input('').split()
        mass_attribute = input('Insert the name of mass attribute\n')
        reblock_model_collection = block_model.reblock(collection, reblock_x, reblock_y, reblock_z, attributes_types, mass_attribute)
        reblock_collection = reblock_model_collection.find({})
        for block in reblock_collection:
            print(block)

    #grade
    elif len(argv) > 6 and argv[6] == "grade":
        mineral_type_value = input('Mineral weight value came in: \n[1] Percent\n[2] Tons\n[3] KG\n')
        mass_name = input("Enter the name of mass column: ")
        weight_name = input("[1]KG \n[2]TONS\n")
        block_model_name = argv[1]
        coordinate_x = argv[2]
        coordinate_y = argv[3]
        coordinate_z = argv[4]
        mineral_name = argv[5]
        block_model = BlockModel(block_model_name)
        collection = database.select_collection(block_model_name)
        block = block_model.find_block(coordinate_x,coordinate_y,coordinate_z, collection)
        result = block.block_grade(mineral_name,mass_name, weight_name, mineral_type_value)
        print(result)
    #attribute
    elif len(argv) == 6:
        block_model_name = argv[1]
        coordinate_x = argv[2]
        coordinate_y = argv[3]
        coordinate_z = argv[4]
        collection = database.select_collection(block_model_name)
        block_model = BlockModel(block_model_name)
        block = block_model.find_block(coordinate_x,coordinate_y,coordinate_z, collection)
        if argv[5] not in block.to_json().keys():
            print("Invalid attribute")
        else:
            print(block.block_attribute(argv[5]))
    