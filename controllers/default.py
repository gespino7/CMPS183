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
    # grid = SQLFORM.smartgrid(db.invoice)
    # return dict(grid = grid)
    stores = db(db.vendor_).select().sort(lambda p: p.business_name)
    return dict(stores=stores)



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

@auth.requires_login()
def my_posts():
    invoices = db(db.invoice.seller_id == auth.user_id).select(orderby=db.invoice.date)
    items = db(db.item.seller_id == auth.user_id).select(orderby = db.item.item_name)
    if request.args(0):
        item = db.item[request.args(0)]
        form = SQLFORM(db.item,
                       item,
                       showid=False,
                       deletable=True,
                       submit_button="Update your post"
                       )
        if form.process(keepvalues=True).accepted:
            response.flash = 'comment accepted'
            redirect('/easycommerce/default/my_posts')
        elif form.errors:
            response.flash = 'please complete your post'
        else:
            response.flash = 'please finish your comment'
    else:
        form = SQLFORM(db.item,
                       showid=False,
                       submit_button="Create new post",

                       );
        if form.process(keepvalues=True).accepted:
            response.flash = 'comment accepted'
            redirect('/easycommerce/default/my_posts')
        elif form.errors:
            response.flash = 'please complete your post'
        else:
            response.flash = 'please finish your comment'
    return dict(form=form,items=items,invoices =invoices)

#Allow vendor to see page only when sing in.

def vendor():
    items = db(db.item.seller_id == auth.user_id).select(orderby = db.item.item_name)

    return dict(items=items)

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

def checkout():
    fields = ['first_name', 'last_name', 'card_number', 'security_code', 'exp_date']
    form = SQLFORM(db.cc, fields=fields)
    if form.process().accepted:
        response.flash = 'Your credit card is confirmed'
    elif form.errors:
        response.flash = 'please complete your changes'
    else:
        response.flash = 'Please edit form'
        # redirect(URL("index"))
    return dict(form=form)

def stores():
   stores = db(db.vendor_).select().sort(lambda p: p.business_name)
   return dict(stores=stores)

def shopping_cart_update():
    if request.vars['adding']:
        item = db.item[request.vars['adding']]
        db.shopping_cart.insert(item_name=item.title,
                               item_id=item.id,
                               price=item.price
                               )
        print("Added.")
        return
    if request.vars['remove']:

        item = db.item[request.vars['remove']]
        db(db.shopping_cart.item_id ==item.id ).delete()

        print("Removed")
        return

    item = db.item[request.vars['adding']]

    if item.amount > 0:
        newAmount = item.amount
        newAmount -=1
        item.update_record(amount=newAmount)

        return
    else:
        response.flash = 'Out of Stock'
    return request.vars


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


def shoppingcart():
    items = db(db.item.seller_id == auth.user_id).select(orderby = db.item.item_name)
    shopping_cart_items = db(db.shopping_cart.buyer_id == auth.user_id).select()
    return dict(items=items,shopping_cart_items=shopping_cart_items)

def vendor_info():
    form = SQLFORM(db.vendor_)
    if form.accepts(request.vars, session):
        response.flash = T('new record inserted')
        #add_member(vendor_group_id, user_id)  # defined buyer_group_id and user_id at bottom of db.py
        redirect(URL('vendor'))
    #else:
    #   response.flash = T('new record failed')
    return dict(form=form)

def buyer_info():
    form = SQLFORM(db.user_)
    if form.accepts(request.vars, session):
        response.flash = T('new record inserted')
        #auth.add_membership(buyer_group_id, user_id) # defined buyer_group_id and user_id at bottom of db.py
        #auth.settings.register_onaccept = add_buyer(buyer_group_id, user_id)
        #add_member(buyer_group_id, user_id)
        redirect(URL('buyer'))
        #add_buyer(buyer_group_id, user_id)
    #else:
    #    response.flash = T('new record failed')
    return dict(form=form)

def choose_type():
    return dict()