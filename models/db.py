# -*- coding: utf-8 -*-


#DAL Constructor


db = DAL ('sqlite://storage.sqlite',migrate = False)

import datetime
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

##############
db.define_table('comment',
                Field('user_id', 'reference auth_user', default=auth.user_id),
                Field('rate'),
                Field('post_content', 'text'),
                Field('created_on', 'datetime', default=datetime.datetime.utcnow())
                )


db.comment.user_id.readable = db.comment.user_id.writable = False

db.comment.post_content.requires = IS_NOT_EMPTY()

db.comment.rate.requires =  IS_IN_SET([0,1,2,3,4,5])

db.comment.created_on.writable = False


##############

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
