# -*- coding: utf-8 -*-
### required - do no delete
def user():
    db.auth_user.faculty_Id.readable = db.auth_user.faculty_Id.writable = False 
    db.auth_user.start_date.readable = db.auth_user.start_date.writable = False 

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
    seedData = seed.getSeedData()
    data = whatIf.whatIf(request.vars.degree, "Computer Science", request.vars.quarter, int(request.vars.courses), [], seedData)
    return dict(data=data, seedData=seedData)

@auth.requires_login()
@auth.requires_membership("faculty")
def students():
    grid = SQLFORM.grid(db.auth_user)
    return locals()
def error():
    return dict()

@auth.requires_login()
def myprofile():
    major = db(db.degree_concentration.id == auth.user.major_Id).select().first()
    courses = db(db.course_taken.student == auth.user.id).select()
    return dict(user=auth.user, courses =courses, major=major)
