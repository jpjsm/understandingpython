#!/usr/bin/env python
# -*- coding: utf-8 -*-

# See following article to understand the logic behind
# https://jakubturek.com/functional-reactive-programming-in-python/

import requests
import funcy
import rx

def re_request(method, url, **kwargs):
    def subscribe(observer):
        response = requests.request(method, url, **kwargs)

        try:
            response.raise_for_status()
            observer.on_next(response)
            observer.on_completed()
        except requests.HTTPError as e:
            observer.on_error(e)

        return lambda: None # It is a shortcut for generating an empty Disposable object.

    return rx.Observable.create(subscribe)

def rx_json(method, url, **kwargs):
  return rx_request(method, url, **kwargs) \
    .map(lambda r: r.json())
