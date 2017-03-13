from gluon.tools import Mail
mail = auth.settings.mailer
mail.settings.server = 'logging'
mail.settings.login = None

customerOrder = True


if customerOrder == True:
    mail.settings.sender = "gespino7@ucsc.edu"
    headers = {'Return-Path': 'abaskar@ucsc.edu'}
    message = response.render('orderapproved.html', "Order approved")
    mail.send(to=['abaskar@ucsc.edu'],
          subject='Order Confirmation',
          message=message)
    n = 10*60
    while n > 0:
        minute = n / 60
        print (minute + "minutes")
        n = n - 1
        if n == 0:
            mail.send(to=['abaskar@ucsc.edu'],
                  subject='Order Complete',
                  message= 'Order is ready for pickup!')
if customerOrder == False:
    mail.settings.sender = "gespino7@ucsc.edu"
    headers = {'Return-Path': 'abaskar@ucsc.edu'}
    message = response.render('ordernotapproved.html', "Order not approved")
    mail.send(to=['abaskar@ucsc.edu'],
          subject = 'Order Declined',
          message = message)



#from gluon.contrib.sms_utils import SMSCODES, sms_email
#email = sms_email('vendor.number','vendor.phoneprovider')
#mail.send (to=user.email, subject='Order Confirmation', message='Order confirmed.')