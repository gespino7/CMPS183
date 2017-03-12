# from gluon.tools import Mail
#
# @auth.requires_login()
# mail = auth.settings.mailer
#
# #emails will not be sent but will logged to console instead
# #mail.settings.server = 'logging'
# mail.settings.server = 'gae'
# mail.settings.sender = 'you@example.com'
# mail.settings.login = auth.user_id':'auth.user_password
#
# #SMTP server does not require authentication
# #mail.settings.login = None
#
# #don't want to use TLS
# mail.settings.tls = False
#
# mail.send(to=[auth.user.email],
#           subject='Order Confirmation',
#           reply_to='you@example.com',
#           message='The order has been placed.')
#
