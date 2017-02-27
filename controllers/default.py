# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
import os

def serve_file():
    filename = request.args(0)
    path = os.path.join(request.folder, 'private', 'file_subfolder', filename)
    return response.stream(path)

def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """
    categories = get_categories()
    listings = get_listings()
    num_listings = len(listings)
    return dict(categories=categories,listings=listings,num_listings=num_listings)

def get_listings():
    return db(db.listing).select().sort(lambda p: p.date_added, reverse=True)

def get_categories():
    return db(db.listing).select().sort(lambda p: p.category, reverse=True)

@auth.requires_login()
def add():
    listing = db.post[request.args(0)]
    type = db.post[request.args(0)]
    form = SQLFORM(db.listing, listing, type,
                   showid=False,
                   deletable=True)
    if form.process().accepted:
        response.flash = 'Listing Accepted'
    return dict(form=form)

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
