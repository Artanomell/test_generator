# -*- coding: utf-8 -*-
db = DAL('sqlite://jobs.sqlite')

db.define_table('studens', Field('name'), )
db.define_table('jobs', Field('name'), Field('task'))