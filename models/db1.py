# -*- coding: utf-8 -*-

db.define_table('degree_concentration',
                Field('major_degree',requires = IS_NOT_EMPTY()),
                Field('concentration',requires = IS_NOT_EMPTY()),
                Field('link',requires = IS_NOT_EMPTY())
                )

db.define_table('course',
                Field('course_name',requires = IS_NOT_EMPTY()),
                Field('course_full_name',requires = IS_NOT_EMPTY()),
                Field('major_degree',db.degree_concentration),
                Field('conc',db.degree_concentration),
                Field('unit',type = 'integer',requires = IS_NOT_EMPTY()),
                Field('description',type = 'text',requires = IS_NOT_EMPTY()),
                Field('intoductory',type = 'boolean',requires = IS_NOT_EMPTY()),
                Field('inClassOnly',type = 'boolean',requires = IS_NOT_EMPTY()),
                Field('onlineOnly',type = 'boolean',requires = IS_NOT_EMPTY()),
                Field('priority',type = 'integer',requires = IS_NOT_EMPTY())
                )

db.define_table('preqs',
                Field('course',db.course),
                Field('preqs',db.course)
                )

db.define_table('course_taken',
                Field('student',db.auth_user),
                Field('course',db.course)
                )

db.define_table('term',
                Field('course',db.course),
                Field('term',requires = IS_NOT_EMPTY())
                )
