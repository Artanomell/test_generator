### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_queue',
    Field('f_name', type='string',
          label=T('Name')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('t_queue_archive',db.t_queue,Field('current_record','reference t_queue',readable=False,writable=False))
