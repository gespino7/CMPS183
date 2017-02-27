# db connection
db = DAL('sqlite://storage.sqlite')

# import Access Control (authentication and authorization) module Auth
from gluon.tools import Auth

# host names must be a list of allowed host names (glob syntax allowed)
auth = Auth(db)


# -------------------------------------------------------------------------
# create all tables needed by auth if not custom tables
# -------------------------------------------------------------------------
auth.define_tables(username=False,signature=False,migrate =False)


# -------------------------------------------------------------------------
# configure auth policy
# -------------------------------------------------------------------------
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

#---------------------------------------------------------
# Table for post data
#---------------------------------------------------------

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