# -*- coding: utf-8 -*-

#DAL Constructor

db = DAL ('sqlite://storage.sqlite')

#Table Constructor -> method to define new tables.
#Vendor contact info.
db.define_table('vendor',
                Field('name' ),
                Field('email'),
                Field('phone_num'),
                Field('business_name'),
                Field('address'),
                Field('date','datetime'),
                 format='%(business_name)s')

#User contact info.
db.define_table('user',
                Field('name' ),
                Field('email'),
                Field('phone_num'),
                Field('payment_info'),
                Field('date','datetime'),
                 format='%(name)s')




#Validations
db.vendor.business_name.requires = IS_NOT_IN_DB(db, db.vendor.business_name)
db.vendor.name.requires = IS_NOT_EMPTY()
db.vendor.email.requires = IS_EMAIL()
#Regex for phone numbers validation-> (123) 234-1234.
db.vendor.phone_num.requires = IS_MATCH('((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}',
                            error_message ='not a valid phone number.')
db.vendor.address.requires = IS_NOT_EMPTY()


db.user.name.requires = IS_NOT_IN_DB(db, db.user.name)
db.user.email.requires = IS_EMAIL()
db.user.phone_num.requires = IS_MATCH('((\(\d{3}\) ?)|(\d{3}-))?\d{3}-\d{4}',
                            error_message ='not a valid phone number.')
db.user.payment_info.requires = IS_NOT_EMPTY()







