# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------


def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html
g
    if you need a simple wiki simply replace the two lines below with:
    return augitth.wiki()
    
    """

    grid = SQLFORM.smartgrid(db.invoice)
    return dict(grid=grid)

def customer_orders():
    return dict()
   
#Allow vendor to see page only when sing in.

def vendor():
    #grid = SQLFORM.smartgrid(db.vendor)
    vendors = db().select(db.vendor.ALL,
                           orderby=~db.vendor.business_name )
    return  dict(vendors = vendors)

def manager():
    vendors = db().select(db.vendor.ALL, orderby=db.vendor.business_name)
    return dict(vendors=vendors)


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
    also notice there is http://..../[app]/appadmin/manage_page.html/auth to allow administrator to manage_page.html users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)



