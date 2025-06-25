#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, Response, Request
import json, sys, os, re, string, uuid, datetime, subprocess, tempfile, base64, urllib

app = Flask("websvc")

@app.route('/')
@app.route('/index')
@app.route('/index.htm')
@app.route('/index.html')
def home():
    return "Welcome to websvc!", 200


@app.route('/getdatetime')
@app.route('/now')
def now():
    return str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")), 200
