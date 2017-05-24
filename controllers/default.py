# -*- coding: utf-8 -*-
### required - do no delete
def user():
    db.auth_user.faculty_Id.readable = db.auth_user.faculty_Id.writable = False 
    db.auth_user.start_date.readable = db.auth_user.start_date.writable = False
    db.auth_user.require_introduction_courses.readable = db.auth_user.require_introduction_courses.writable = False 
    form=auth()

    if request.args(0) == "register" and form.process().accepted:
        user_id = form.vars.id
    return dict(form = form)

def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    if auth.is_logged_in():
        history = db(db.history.student == auth.user.id).select()
        return dict(history=history)
    return dict()

@auth.requires_login()
def search():
    return dict()
@auth.requires_login()
def result():
    db.history.insert(student=auth.user,major=request.vars.degree, concentration=request.vars.concentration, quarter=request.vars.quarter, courses=int(request.vars.courses))
    taken = []
    courses = db(db.course_taken.student == auth.user.id).select()
    for course in courses:
        taken.append(course.course.course_name)
    seedData = seed.getSeedData()
    data = whatIf.whenIf(request.vars.degree, request.vars.concentration, request.vars.quarter, int(request.vars.courses), taken, seedData, auth.user.require_introduction_courses)
    return dict(data=data)

@auth.requires_login()
@auth.requires_membership("faculty")
def students():
    grid = SQLFORM.smartgrid(db.auth_user,
                        deletable=True,
                        editable=True,
                        details=True,
                        create=True,
                        user_signature=False, linked_tables=['course_taken'])
    return dict(grid=grid)
def error():
    return dict()

@auth.requires_login()
def myprofile():
    major = db(db.degree_concentration.id == auth.user.major_Id).select().first()
    faculty = db(db.auth_user.id == auth.user.faculty_Id).select().first()
    courses = db(db.course_taken.student == auth.user.id).select()
    return dict(user=auth.user, courses =courses, major=major, faculty=faculty)

@auth.requires_login()
@auth.requires_membership("admin")
def seedcourses():
    db.course.truncate()
    seedData = seed.getSeedData()
    for course in seedData['classes']:
        c = seedData['classes'][course]
        db.course.insert(course_name=course,course_full_name=c.name)
    return "Seed Complete"

@auth.requires_login()
@auth.requires_membership("admin")
def trunc_user():
    return db.auth_user.truncate()
