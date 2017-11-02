response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('На главную'),False,'/'),
(T('Список очередей'),URL('default','index')==URL(),URL('default','index'),[]),
# (T('Queue'),URL('default','queue_manage')==URL(),URL('default','queue_manage'),[]),
]
