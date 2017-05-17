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

@auth.requires_login()
def search():
    return dict()
@auth.requires_login()
def result():
    return dict()

@auth.requires_login()
@auth.requires_membership("faculty")
def students():
    grid = SQLFORM.grid(db.auth_user)
    return locals()
def error():
    return dict()

def test():
    test = Mail()
    test.settings.server = 'email-smtp.us-west-2.amazonaws.com:587'
    test.settings.sender = 'sunnysyed93@gmail.com'
    test.settings.login = 'AKIAJMDHJPWDX3XJIQ5Q:BFT48Dz12fJECfPzUJ61xZDYgYuYVseBaGO+MwCl'
    test.settings.tls = True
    temp = test.send('sunnysyed93@gmail.com',
  'Message subject',
  'Plain text body of the message')
    return response.json(temp)
