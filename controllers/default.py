# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# -------------------------------------------------------------------------
# This is a sample controller
# - index is the default action of any application
# - user is required for authentication and authorization
# - download is for downloading files uploaded in the db (does streaming)
# -------------------------------------------------------------------------
def index():
    # grid = SQLFORM.smartgrid(db.invoice)
    # return dict(grid = grid)
    modify(SQLFORM(db.auth_user))
    form = SQLFORM(db.auth_user)
    modify(form)
    #modify(form)
    if form.process().accepted:
        response.flash = 'your login is accepted'
        if (str(form.vars.User_Type) == "Vendor"):
            response.flash = 'the user is a VENDOR'
    return dict()

def test_page():
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
#@auth.requires_login()




def give_create_permission(form):
    group_id = auth.id_group('Vendors')
    auth.add_permission(group_id)

#auth.settings.register_onaccept = give_create_permission

#@auth.requires_membership('Buyers')
def buyer():
    grid = SQLFORM.smartgrid(db.vendor_)
    return dict(grid=grid)

#@auth.requires_membership('Vendors')
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

def choose_type():
    return dict()

def input_info():
    return dict()



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

"""def __add_user_membership(form):
    #group = db(db.auth_group.role == form.vars.User_Type).select().first()
    #group = vendor_group_id
    #user_id = form.vars.id
    #auth.add_membership(group, user_id)
    group_id = form.vars.group_name
    user_id = form.vars.id
    auth.add_membership(group_id, user_id)
"""

def fn(form):
    if (form.vars.User_Type == "Vendor"):
        auth.settings.login_next=URL('vendor')
        redirect(URL('vendor'))
    else:
        auth.settings.login_next=URL('buyer')

auth.settings.login_onaccept.append(lambda form: fn(form))

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

    #auth.settings.register_onaccept = add_membership(user_id)
    #auth.settings.register_onaccept = __add_user_membership
    # already existing code
    auth.settings.login_onaccept.append(lambda form: fn(form))
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)



