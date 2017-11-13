# -*- coding: utf-8 -*-

db = DAL('sqlite://tasks.sqlite')

db.define_table('tasks', Field('seed'))