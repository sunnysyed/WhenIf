# -*- coding: utf-8 -*-

db.define_table('course',
                Field('course_name',requires = IS_NOT_EMPTY()),
                Field('course_full_name',requires = IS_NOT_EMPTY()),
                Field('description',type = 'text'),
                Field('intoductory',type = 'boolean', default=False),
                Field('inClassOnly',type = 'boolean', default=False),
                Field('onlineOnly',type = 'boolean', default=False),
                )

db.define_table('course_taken',
                Field('student',db.auth_user),
                Field('course', 'reference course',
                      label = T('Course'),
                      notnull = True,
                      required = True,
                      requires = IS_IN_DB(db, db.course.id, '%(course_name)s - %(course_full_name)s'))
                )

db.define_table('history',
                Field('student','reference auth_user'),
                Field('major',type='text'),
                Field('concentration',type='text'),
                Field('quarter',type='text'),
                Field('courses', type='integer')
                )
