#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import pytest
import websvc

@pytest.fixture
def client():
    client = websvc.app.test_client()
    yield client

def test_home(client):
    """Check home page"""
    rv = client.get('/')
    assert b'bienvenido!' in rv.data 

def test_now(client):
    """Check home page"""
    rv = client.get('/now')
    receivednow = datetime.datetime.strptime(rv.data, "%Y-%m-%d %H:%M:%S.%f")
    expectednow = datetime.datetime.now()
    deltatime = abs(expectednow - receivednow)

    assert deltatime.total_seconds() < 1
