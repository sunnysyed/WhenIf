# -*- coding: utf-8 -*-

# -------------------------------------------------------------------------
# This scaffolding model makes your app work on Google App Engine too
# File is released under public domain and you can use without limitations
# -------------------------------------------------------------------------

if request.global_settings.web2py_version < "2.14.1":
    raise HTTP(500, "Requires web2py 2.13.3 or newer")

# -------------------------------------------------------------------------
# if SSL/HTTPS is properly configured and you want all HTTP requests to
# be redirected to HTTPS, uncomment the line below:
# -------------------------------------------------------------------------
request.requires_https()

# -------------------------------------------------------------------------
# app configuration made easy. Look inside private/appconfig.ini
# -------------------------------------------------------------------------
from gluon.contrib.appconfig import AppConfig
from gluon.tools import Mail
from gluon.tools import Recaptcha



# -------------------------------------------------------------------------
# once in production, remove reload=True to gain full speed
# -------------------------------------------------------------------------
myconf = AppConfig(reload=True)

if not request.env.web2py_runtime_gae:
    # ---------------------------------------------------------------------
    # if NOT running on Google App Engine use SQLite or other DB
    # ---------------------------------------------------------------------
    db = DAL(myconf.get('db.uri'),
             pool_size=myconf.get('db.pool_size'),
             migrate_enabled=True,
             check_reserved=['all'])
else:
    # ---------------------------------------------------------------------
    # connect to Google BigTable (optional 'google:datastore://namespace')
    # ---------------------------------------------------------------------
    db = DAL('google:datastore+ndb')
    # ---------------------------------------------------------------------
    # store sessions and tickets there
    # ---------------------------------------------------------------------
    session.connect(request, response, db=db)
    # ---------------------------------------------------------------------
    # or store session in Memcache, Redis, etc.
    # from gluon.contrib.memdb import MEMDB
    # from google.appengine.api.memcache import Client
    # session.connect(request, response, db = MEMDB(Client()))
    # ---------------------------------------------------------------------

# -------------------------------------------------------------------------
# by default give a view/generic.extension to all actions from localhost
# none otherwise. a pattern can be 'controller/function.extension'
# -------------------------------------------------------------------------
response.generic_patterns = ['*'] if request.is_local else []
# -------------------------------------------------------------------------
# choose a style for forms
# -------------------------------------------------------------------------
response.formstyle = myconf.get('forms.formstyle')  # or 'bootstrap3_stacked' or 'bootstrap2' or other
response.form_label_separator = myconf.get('forms.separator') or ''

# -------------------------------------------------------------------------
# (optional) optimize handling of static files
# -------------------------------------------------------------------------
# response.optimize_css = 'concat,minify,inline'
# response.optimize_js = 'concat,minify,inline'

# -------------------------------------------------------------------------
# (optional) static assets folder versioning
# -------------------------------------------------------------------------
# response.static_version = '0.0.0'

# -------------------------------------------------------------------------
# Here is sample code if you need for
# - email capabilities
# - authentication (registration, login, logout, ... )
# - authorization (role based authorization)
# - services (xml, csv, json, xmlrpc, jsonrpc, amf, rss)
# - old style crud actions
# (more options discussed in gluon/tools.py)
# -------------------------------------------------------------------------

from gluon.tools import Auth, Service, PluginManager

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db, host_names=myconf.get('host.names'))
service = Service()
plugins = PluginManager()

db.define_table('degree_concentration',
                Field('major_degree',requires = IS_NOT_EMPTY()),
                Field('concentration',requires = IS_NOT_EMPTY()),
                Field('link',requires = IS_NOT_EMPTY())
                )

## after auth = Auth(db)
auth.settings.extra_fields['auth_user']= [
  Field('address', 'string'),
  Field('phone', 'string'),
  Field('date_of_birth', 'datetime'),
  Field('sex', 'string', requires=IS_IN_SET(['Male', 'Female'])),
  Field('faculty_Id', 'integer'),
  Field('start_date', 'datetime'),
  Field('require_introduction_courses', 'boolean', default=False),
  Field('major_Id', 'reference degree_concentration',
      label = T('Major'),
      notnull = True,
      required = True,
      requires = IS_IN_DB(db, db.degree_concentration.id, '%(major_degree)s - %(concentration)s') )
]

# -------------------------------------------------------------------------
# create all tables needed by auth if not custom tables
# -------------------------------------------------------------------------
auth.define_tables(username=False, signature=False)

#auth_table=auth.settings.table_user
#auth_table.username.requires = IS_NOT_IN_DB(db, auth_table.username)

# -------------------------------------------------------------------------
# configure email
# -------------------------------------------------------------------------
mail = auth.settings.mailer
mail.settings.server = 'email-smtp.us-west-2.amazonaws.com:25'
mail.settings.sender = 'sunnysyed93@gmail.com'
mail.settings.login = 'AKIAICHBNDVEZJHTFPQA:Aujg0dUgumrs0r8qvpKpIxAQOEnZJZYbmfdarK+dMxpD'
mail.settings.tls = True


# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True
auth.settings.register_verify_password=False

#auth.settings.captcha = Recaptcha(request,
#    '6Le_JSIUAAAAADYiIaES37K7GdMjaYaCXcNLBLvb', '6Le_JSIUAAAAANU41ZeUVmRqsYu2HK_DgZHvx8l6')

#auth.settings.verify_email_onaccept = lambda form: mail.send(to='sunnysyed93@gmail.com',subject='New Student Registration',message=repr(form.vars))



# -------------------------------------------------------------------------
# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.
#
# More API examples for controllers:
#
# >>> db.mytable.insert(myfield='value')
# >>> rows = db(db.mytable.myfield == 'value').select(db.mytable.ALL)
# >>> for row in rows: print row.id, row.myfield
# -------------------------------------------------------------------------

# -------------------------------------------------------------------------
# after defining tables, uncomment below to enable auditing
# -------------------------------------------------------------------------
# auth.enable_record_versioning(db)




def user_bar():
    
    action = '/user'
    if auth.user:
        return '''<li class="dropdown" data-w2pmenulevel="l0"><a class="dropdown-toggle" data-toggle="dropdown" href="#" rel="nofollow">Welcome ''' + auth.user.first_name +'''</a><ul class="dropdown-menu"><li><a href="/user/profile?_next=/" rel="nofollow"><i class="icon icon-user glyphicon glyphicon-user"></i> Profile</a></li><li><a href="/user/change_password?_next=/" rel="nofollow"><i class="icon icon-lock glyphicon glyphicon-lock"></i> Password</a></li><li class="divider"></li><li><a href="/user/logout?_next=/" rel="nofollow"><i class="icon icon-off glyphicon glyphicon-off"></i> Log Out</a></li></ul></li>'''
    else:
        return '''<li class="dropdown" data-w2pmenulevel="l0"><a class="dropdown-toggle" data-toggle="dropdown" href="#" rel="nofollow">Log In</a><ul class="dropdown-menu"><li><a href="/user/register?_next=/" rel="nofollow"><i class="icon icon-user glyphicon glyphicon glyphicon-education"></i> Apply</a></li><li><a href="/user/request_reset_password?_next=/" rel="nofollow"><i class="icon icon-lock glyphicon glyphicon-lock"></i> Lost password?</a></li><li class="divider"></li><li><a href="/user/login?_next=/" rel="nofollow"><i class="icon icon-off glyphicon glyphicon-user"></i> Log In</a></li></ul></li>'''
