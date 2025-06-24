from flask import Flask, request, jsonify, Response
import json

def load_jsonfile(filename):
    '''
    Returns an object from a JSON file
    '''
    with open(filename, 'r') as infile:
        return json.load(infile)

main = Flask("static-mappings")

@main.route("/", methods=['GET'])
def home():
    staticmappings = load_jsonfile("/Users/jjofre/projects/understandingpython/rnt-static_mappings.json")
    return Response(json.dumps(staticmappings), mimetype = 'application/json'), 200
