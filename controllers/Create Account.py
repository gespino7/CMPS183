user = raw_input('Create Username: ')
password = raw_input('Create Password: ')
store_user = user
store_pass = password

if user in store_user:
    print "That user already exists"
else
# add user and password to database
    store_user.append(user)
    store_pass.append(password)

while 1 == 1:
    userguess=""
    passwordguess=""
    key=""
    while (userguess != user) or (passwordguess != password):
        userguess = raw_input('User Name: ')
        passwordguess = raw_input('Password:')

    print "Welcome,",user, "!"
    print store_user
#    print store_pass
