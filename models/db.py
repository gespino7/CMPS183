# -*- coding: utf-8 -*-

#DAL Constructor

db = DAL ('sqlite://storage.sqlite')

#Table Constructor -> method to define new tables.
db.define_table('vendor_info',Field('name','email','phone_num','business_name','address'))


print db
