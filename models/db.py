# -*- coding: utf-8 -*-


#DAL Constructor


db = DAL ('sqlite://storage.sqlite')


from gluon.tools import Auth
auth = Auth(db)
auth.define_tables()
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
import datetime
db.define_table('listing',
                Field('seller','reference auth_user', default=auth.user_id),
                Field('date_added', 'datetime', default=datetime.datetime.utcnow(), requires=IS_DATE()),
                Field('item_name',requires=IS_NOT_EMPTY()),
                Field('description', requires=IS_NOT_EMPTY()),
                Field('image', 'upload'),
                Field('price', 'double'),
                Field('status', 'boolean', default=False),
                Field('category', requires=IS_NOT_EMPTY()),
                format='%(subject)s')

#Date format %m-%d-%Y %I:%M%P
db.listing.price.requires = IS_NOT_EMPTY(), IS_FLOAT_IN_RANGE(0, 999999999.0, dot='.',error_message='The price should be in the range $0..999,999,999')
db.listing.date_added.requires = IS_NOT_EMPTY()
db.listing.date_added.writable = False
db.listing.seller.writable = False
db.listing._plural = " "

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









