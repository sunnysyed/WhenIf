# -*- coding: utf-8 -*-
### required - do no delete
def user():
    form=auth()
#    if request.args(0) == "register" and request.post_vars.first_name and request.post_vars.last_name:
#        request.post_vars.username = request.post_vars.first_name + request.post_vars.last_name
        
    if request.args(0) == "register" and form.process().accepted:
        user_id = form.vars.id
    return dict(form = form)
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    return dict()

def search():
    return dict()

def result():
    return dict()

def error():
    return dict()
