# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
<<<<<<< HEAD
import os

def serve_file():
    filename = request.args(0)
    path = os.path.join(request.folder, 'private', 'file_subfolder', filename)
    return response.stream(path)

=======
>>>>>>> 616f496c885a067b39c9d58cf56aa94ac018971c
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html
g
    if you need a simple wiki simply replace the two lines below with:
    return augitth.wiki()

    """
<<<<<<< HEAD
    categories = get_categories()
    listings = get_listings()
    num_listings = len(listings)
    return dict(categories=categories,listings=listings,num_listings=num_listings)

def get_listings():
    return db(db.listing).select().sort(lambda p: p.date_added, reverse=True)
=======
    # grid = SQLFORM.smartgrid(db.invoice)
    # return dict(grid = grid)
    return dict()

@auth.requires_login()
def customer_orders():
    if request.vars['status'] and request.vars['status']!="all":
        invoices = db((db.invoice.seller_id == auth.user_id) & (db.invoice.status == request.vars['status'])).select(
            orderby=db.invoice.date)
        print ("hello" + request.vars['status'])
    else:
        invoices = db(db.invoice.seller_id == auth.user_id).select(orderby=db.invoice.date)
        print ("no status")
    return dict(invoices=invoices)



#Allow vendor to see page only when sing in.
@auth.requires_login()
def vendor():
    grid = SQLFORM.smartgrid(db.invoice)
    return  dict(grid = grid)


@auth.requires_login()
def manager():
    invoices = db(db.invoice.seller_id == auth.user_id).select(orderby=db.invoice.date)
    return dict(invoices=invoices)

@auth.requires_login()
def status_update():
    if request.vars['status']:
        return
    invoice = db.invoice[request.vars['order_id']]
    if invoice.status == 'pending':
        invoice.update_record(status = "confirmed")
    else:
        invoice.update_record(status = "pending")
    return invoice.status

def card():
    fields = ['first_name',  'last_name', 'card_number','security_code', 'exp_date']
    form = SQLFORM(db.cc, fields=fields)
    if form.process().accepted:
        response.flash = 'Your credit card is confirmed'

    else:
        response.flash = 'please fill out your credit card information'
      # redirect(URL("index"))
    return dict(form=form)



>>>>>>> 616f496c885a067b39c9d58cf56aa94ac018971c

def get_categories():
    return db(db.listing).select().sort(lambda p: p.category, reverse=True)

def item():
    listing = db.listing[request.args(0)]
    listings = db(db.listing).select()
    return dict(listing=listing,listings=listings)

def map():
    return dict()

@auth.requires_login()
def add():
    listing = db.listing[request.args(0)]
    type = db.listing[request.args(0)]
    form = SQLFORM(db.listing, listing, type,
                   showid=False)
    if form.process().accepted:
        response.flash = 'Listing Accepted'
    return dict(form=form)

def maptest():
    return dict()

@auth.requires_login()
def add_vendor():
    vendor_info = db.vendor_info[request.args(0)]
    form = SQLFORM(db.vendor_info, vendor_info,
                   showid=False)
    if form.process().accepted:
        response.flash = 'Vendor Added'
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



