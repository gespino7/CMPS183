# -*- coding: utf-8 -*-
#DAL Constructor
db = DAL('sqlite://storage.sqlite')


from gluon.tools import Auth
auth = Auth(db)
auth.define_tables()

import datetime

#Vendor_ DB ------------------
db.define_table('vendor_',
                Field('name' ),
                Field('vendor_id', 'reference auth_user', default=auth.user_id),
                Field('email'),
                Field('phone_num'),
                Field('banner','upload',requires=IS_NOT_EMPTY()),
                Field('business_name'),
                Field('address'),
                Field('date','datetime',default=request.now),
                format='%(business_name)s')

#User_ DB ------------------
db.define_table('user_',
                Field('name' ),
                Field('user_id', 'reference auth_user', default=auth.user_id),
                Field('email'),
                Field('phone_num'),
                Field('payment_info'),
                Field('date','datetime',default=request.now),
                format='%(name)s')

#Item DB ------------------
db.define_table('item',
                Field('seller','reference auth_user', default=auth.user_id),
                Field('date_added','datetime',default=request.now),
                Field('item_name',requires=IS_NOT_EMPTY()),
                Field('description', requires=IS_NOT_EMPTY()),
                Field('image', 'upload'),
                Field('thumbnail', 'upload'),
                Field('price', 'double'),
                Field('status', 'boolean', default=False),
                Field('category', requires=IS_NOT_EMPTY()))

#Invoice DB ------------------
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

#Validations for Vendor ---------------------------
db.vendor_.business_name.requires = IS_NOT_IN_DB(db, db.vendor_.business_name)
db.vendor_.name.requires = IS_NOT_EMPTY()
db.vendor_.email.requires = IS_EMAIL()
#Regex for phone numbers validation-> (123) 234-1234.
db.vendor_.phone_num.requires = IS_MATCH('((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}',
                            error_message ='not a valid phone number.')
db.vendor_.address.requires = IS_NOT_EMPTY()
db.vendor_.vendor_id.writable = db.vendor_.vendor_id.readable = False
db.vendor_.date.writable = db.vendor_.date.readable = False

#Validations for User ---------------------------
db.user_.name.requires = IS_NOT_IN_DB(db, db.user_.name)
db.user_.email.requires = IS_EMAIL()
db.user_.phone_num.requires = IS_MATCH('((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}',
                            error_message ='not a valid phone number.')
db.user_.user_id.writable = db.user_.user_id.readable = False
db.user_.date.writable = db.user_.date.readable = False
db.user_.payment_info.requires = IS_NOT_EMPTY()

#Validations for Invoice ---------------------------
db.invoice.status.requires = IS_IN_SET(['pending','confirmed'])

#Validations for Credit Card ---------------------------
db.cc.first_name.requires = IS_NOT_EMPTY()
db.cc.last_name.requires = IS_NOT_EMPTY()
db.cc.card_number.requires = IS_MATCH('\d{4}\d{4}\d{4}\d{4}',
                           error_message ='not a valid card number.')
db.cc.security_code.requires = IS_MATCH('\d{3}',
                            error_message ='not a valid security code.')
db.cc.exp_date.requires = IS_MATCH('\d{2}/\d{2}',
                            error_message ='not a valid expiration date.')

#Validations for items ---------------------------
db.item.price.requires = IS_NOT_EMPTY(), IS_FLOAT_IN_RANGE(0, 999999999.0, dot='.',error_message='The price should be in the range $0..999,999,999')
db.item.date_added.requires = IS_NOT_EMPTY()
db.item.date_added.writable = False
db.item.seller.writable = False
db.item.thumbnail.writable = False
db.item.thumbnail.readable = False