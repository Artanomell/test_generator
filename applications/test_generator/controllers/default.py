# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
import random
from gluon.contrib.pyfpdf import FPDF, HTMLMixin
import gluon.contrib.markdown as markdown

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    return redirect('test_generator/default/generate')
    # response.flash = T("Hello World")
    # return dict(message=T('Welcome to web2py!'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()

def generate():
    # if session.get('name', None):
    #     p = pdf.FPDF()
    #     p.add_page()
    #     p.set_font('Arial', '', 16)
    #     p.text(10,10,str(('asdasdsadsasdsddsaasd\nsdfsafsfsf')))
    #     response.headers['Content-Type'] = 'application/pdf'
    #     return p.output(dest='S')
    # else:
    form = FORM(
        H3(u'Строка для генерации задания'),
        INPUT(_name=u'name'),
        BUTTON(u'Отправить',_type=u'submit')
    )
    if form.process().accepted:
        SUB = TAG.sub
        rnd = random.Random(form.vars['name'])
        template = u'<li><p>%s<sub>%s</sub> -&gt; X<sub>%s</sub></p><li>'
        template2 = u'<li><p>%s<sub>%s</sub> -&gt; X<sub>%s</sub> -&gt; X<sub>%s</sub></p><li>'
        arr1 = (map(
            lambda a:LI(P(str(a[0]).replace('0o', '').replace('0b','').replace('0x','').capitalize(), SUB(a[1]), '-> X', SUB(a[2]))),
            (
            (rnd.randint(100, 1025), 10, 2),
            (bin(rnd.randint(30, 200)), 2, 10),
            (oct(rnd.randint(50, 300)), 8, 10),
            (rnd.randint(100, 512), 10, 8),
            (hex(rnd.randint(100, 2048)), 16, 10),
            (rnd.randint(100, 2048), 10, 16),
        )))

        arr2 = (map(
            lambda a: LI(P(str(a[0]).replace('0o', '').replace('0b', '').replace('0x', '').capitalize(), SUB(a[1]), ' -> X', SUB(a[2]), ' -> X', SUB(a[3]))),
            (
                (bin(rnd.randint(128, 4096)), 2, 16, 8),
                (hex(rnd.randint(128, 4096)), 16, 2, 8),
                (oct(rnd.randint(128, 4096)), 8, 16, 2)
            )))


        return dict(body=DIV(
            H3(u'Задание'),
            OL(arr1+arr2),
            A(BUTTON(u'Обновить'), _href='')
        ))
    elif form.errors:
        return dict(body=form)
    return dict(body=form)
