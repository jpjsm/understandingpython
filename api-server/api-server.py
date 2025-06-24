#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, render_template, Response, Request
import json, sys, os, re, string, uuid, datetime, subprocess, tempfile, uuid

class ParseArguments(object):
    @staticmethod
    def parseargs(requestargs, required, optional=[], ignoreunkownarguments=True):
        '''
        Extracts from requests args the expected parameters.
        All input parameters are converted to lowercase. This codes asumes
        an english alphabet for the parameters.
        If any parameter is missing, throw an exception.
        If unkown parameters are received throw an exception, 
        unless ignoreunknownarguments is True.

        Parameters:
        requestargs, a dictionary with <argument-name,argument-value> key-value pair.
                    Usually, request.args.to_dict()

        required, the names of the required parameters, as a list.

        optional, the names of the optional parameters, as a list.

        ignoreunkownarguments, If True, any argument received not in in the list of 
                            parameters will be ignored.
                            If False, an InvalidUsage('Unknown request.', status_code=400, argname)
                            exception will be raised.
        '''
        # validate arguments
        if required is None:
            return {'message':'Missing arguments.', 'status':'400', 'argname':'required'}, 400

        if requestargs is None:
            return {'message':'Missing arguments.', 'status':'400', 'argname':'requestargs'}, 400

        if optional is None:
            optional = []

        # normalize casing for argument comparison      
        musthave=dict([(p.upper().lower(), None) for p in required])
        mayhave=dict([(p.upper().lower(), None) for p in optional])


        for argname in requestargs:
            argnamelower = argname.upper().lower()
            if argnamelower in musthave:
                musthave[argnamelower] = requestargs[argname]
            elif argnamelower in mayhave:
                mayhave[argnamelower] = requestargs[argname]
            else:
                if not ignoreunkownarguments:
                    return {'message':'Unknown request.', 'status':'400', 'argname':argname}, 400
        
        # find all key-value pairs where value is None
        missingarguments = [x for x in musthave if musthave[x] is None]

        if missingarguments:
            return {'message':'Missing arguments.', 'status':'400', 'argname':missingarguments}, 400

        return dict(musthave, **mayhave), 200


class MyResponse(Response):
    timeformat = "%Y-%m-%d %H:%M:%S.%f"
    # default_mimetype = 'application/json'

class InvalidUsage(Exception):
    '''
    Simple exception class
    The basic idea is to introduce a new exception 
    that can take a proper human readable message, 
    a status code for the error and some optional 
    payload to give more context for the error.
    
    excerpt from 'http://flask.pocoo.org/docs/1.0/patterns/apierrors/'
    '''

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        else:
            self.status_code = 400
        self.payload = payload

    def to_dict(self):
        rv = { }
        rv["ErrorDetail"] = self.payload 
        rv['Error'] = self.message
        rv['status'] = self.status_code
        return rv

#
## Bring the service up
#
UPLOAD_FOLDER = '/tmp/api-server-uploads'

app = Flask("get-date")
app.response_class = MyResponse
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    '''
    Registering an Error Handler

    A view can now raise that exception with an error message. 
    Additionally some extra payload can be provided as a dictionary 
    through the payload parameter.
    '''
    response = jsonify(error.to_dict())
    return response, int(error.status_code)

@app.route("/")
@app.route("/index")
@app.route("/index.htm")
@app.route("/index.html")
def home():
    jsonresults = {
            "Title": "get-date-api",
            "overview": "The get date and time rest API demo"
        }
    return jsonify(jsonresults), 200

@app.route("/GetDate", methods=['GET'])
@app.route("/getdate", methods=['GET'])
def getdate():
    '''
    Returns the current date and time.

    '''
    currentdatetime = datetime.datetime.now().strftime(MyResponse.timeformat)
    return jsonify(currentdatetime), int(200)

# @app.route('/upload')
# def upload_file():
#    return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        source = f.filename
        destination = os.path.join('/tmp', os.path.basename(source))
        f.save(destination)
        return "Original file '{0}' uploaded successfully to '{1}'".format(source, destination)
    else:
        return '''
            <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="UTF-8">
                    <title>API-Server File Upload</title>
                </head>
                <body>
                    <form action = "http://172.24.240.99/uploader" method = "POST" enctype = "multipart/form-data">
                        <input type = "file" name = "file" />
                        <input type = "submit"/>
                    </form>
                </body>
            </html>
        '''

	
@app.route('/AddPassthrough', methods = ['GET', 'POST'])
def AddPassthrough():
    if request.method == 'POST':
        tmpname = str(uuid.uuid4())
        certlocations = []

        for cert in ['servername', 'clientcert', 'servercert', 'servercertkey', 'destination']:
            f = request.files[cert]
            source = f.filename
            location = os.path.join('/tmp', tmpname + '-' + cert + os.path.splitext(source)[1])
            f.save(location)
            certlocations.append(location)

        return "Certs {0} uploaded !".format(certlocations)
    else:
        return '''
            <!DOCTYPE html>
            <html>
                <head>
                    <meta charset="UTF-8">
                    <title>AddPassthrough</title>
                </head>
                <body>
                    <form action = "http://172.24.240.99/AddPassthrough" method = "POST" enctype = "multipart/form-data">
                        Server Name: <input type = "file" name = "servername" /><br>
                        Client Cert Location: <input type = "file" name = "clientcert" /><br>
                        Server Cert Location: <input type = "file" name = "servercert" /><br>
                        Server Key Location: <input type = "file" name = "servercertkey" /><br>
                        Destination: <input type = "file" name = "destination" /><br>
                        <input type = "submit"/>
                    </form>
                </body>
            </html>
        '''        