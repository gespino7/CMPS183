# -*- coding: utf-8 -*-


#DAL Constructor


db = DAL ('sqlite://storage.sqlite',migrate = False)


from gluon.tools import Auth
auth = Auth(db)
categories = (["Buyer", "Vendor"])
auth.settings.extra_fields['auth_user'] = [Field('User_Type', requires=IS_IN_SET(categories))]
#auth.settings.register_onaccept = __add_user_membership
#auth.add_group('Vendors', 'description1')
#auth.add_group('Buyers', 'description2')


def fn(form):
    if (form.vars.User_Type == "Vendor"):
        #auth.settings.login_next=URL('vendor')
        redirect(URL('vendor'))
    else:
        auth.settings.login_next=URL('buyer')

auth.settings.login_onaccept.append(lambda form: fn(form))


def modify(form):
    auth.settings.login_onaccept.append(fn(form))


def give_create_permission(form):
    group_id = auth.id_group('Vendors')
    auth.add_permission(group_id)

#auth.settings.register_onaccept = give_create_permission

def conditional_login(user_type):
    if (user_type == "vendor"):
        auth.settings.login_next = URL('vendor')
    else:
        auth.settings.login_next = URL('index')


auth.settings.login_next = URL('choose_type')
auth.settings.register_next = URL('input_info')



#Table Constructor -> method to define new tables.
#Vendor_ contact info.
db.define_table('vendor_',
                Field('name' ),
                Field('email'),
                Field('phone_num'),
                Field('business_name'),
                Field('address'),
                Field('date','datetime'),
                 format='%(business_name)s')


db.define_table('user_',
                Field('name' ),
                Field('email'),
                Field('phone_num'),
                Field('payment_info'),
                Field('date','datetime'),
                 format='%(name)s')



db.define_table('item',
                Field('title'),
                Field('description','text'),
                Field('image','upload'),
                Field('price','double'),
                Field('amount','integer')
                )

db.define_table('invoice',
                Field('seller_id'),
                Field('customer_id'),
                Field('item_id'),
                Field('amount'),
                Field('date','datetime',default=request.now),
                Field('status',default = 'pending')
                )

db.define_table('invoice_',
                Field('seller'),
                Field('customer'),
                Field('amount'),
                Field('date','datetime',default=request.now),
                Field('invoice'),
                Field('status'))

db.define_table('cc',
                Field('first_name'),
                Field('last_name'),
                Field('card_number'),
                Field('security_code'),
                Field('exp_date'))


#User_ contact info.


#Validations
db.vendor_.business_name.requires = IS_NOT_IN_DB(db, db.vendor_.business_name)
db.vendor_.name.requires = IS_NOT_EMPTY()
db.vendor_.email.requires = IS_EMAIL()
#Regex for phone numbers validation-> (123) 234-1234.
db.vendor_.phone_num.requires = IS_MATCH('((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}',
                            error_message ='not a valid phone number.')
db.vendor_.address.requires = IS_NOT_EMPTY()


db.user_.name.requires = IS_NOT_IN_DB(db, db.user_.name)
db.user_.email.requires = IS_EMAIL()
db.user_.phone_num.requires = IS_MATCH('((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}',
                            error_message ='not a valid phone number.')

db.user_.payment_info.requires = IS_NOT_EMPTY()
db.invoice.status.requires = IS_IN_SET(['pending','confirmed'])


db.user_.payment_info.requires = IS_NOT_EMPTY()
###############credit card
db.cc.first_name.requires = IS_NOT_EMPTY()
db.cc.last_name.requires = IS_NOT_EMPTY()
db.cc.card_number.requires = IS_MATCH('\d{4}\d{4}\d{4}\d{4}',
                           error_message ='not a valid card number.')
db.cc.security_code.requires = IS_MATCH('\d{3}',
                            error_message ='not a valid security code.')
db.cc.exp_date.requires = IS_MATCH('\d{2}/\d{2}',
                            error_message ='not a valid expiration date.')
#user_name=False

db.user_.payment_info.requires = IS_NOT_EMPTY()



#auth.settings.extra_fields['auth_user']= [Field('phone')]

auth.settings.extra_fields['auth_user_']= [Field('phone')]
auth.define_tables(username=False,signature=False,migrate =False)

#auth.settings.login_onaccept.append(fn(auth_user))


vendor_group_id = auth.add_group('Vendors')
buyer_group_id = auth.add_group('Buyers')

user_id = auth.user_id

def add_member(group_ident, user_ident):
    auth.add_membership(group_ident, user_ident)


def add_membership(user_ident):
    if (user_ident.User_Type == "Vendor"):
        auth.add_membership(vendor_group_id, user_ident)
    else:
        auth.add_membership(buyer_group_id, user_ident)


#auth.settings.register_onaccept = __add_user_membership

