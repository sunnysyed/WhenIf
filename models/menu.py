response.logo = A(IMG(_src=URL('PublishingImages/logoCDM.png', scheme='https', host='www.cdm.depaul.edu'), _style="width:130px;"), _href=URL('default','index'), _id="web2py-logo") 


response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = []
if auth.is_logged_in():
    response.menu = [ 
            (T('When If'),URL('default','index')==URL(),URL('default','index'),[]),
            (T('My Profile'),URL('default','myprofile')==URL(),URL('default','myprofile'),[]),
            (T('Search'),URL('default','search')==URL(),URL('default','search'),[]),
            (T('Courses'),URL('default','index')==URL(),A('Courses', _href="https://www.cdm.depaul.edu/academics/Pages/CourseCatalog.aspx", _target="_blank"),[]),
            (T('Degree Requirements'),URL('default','index')==URL(),A('Degree Requirements', _href="https://www.cdm.depaul.edu/academics/Pages/CourseCatalog.aspx", _target="_blank"),[]),
        ]
if auth.is_logged_in() and auth.has_membership("faculty"):
    response.menu.append((T('Students'),bool(request.controller == "default"), URL('default', 'students'), []))
