is_connection_open = False
is_login = True

if(not is_connection_open & is_login):
    print("you are connected")
else:
    print("you do not connected")

if is_login | is_connection_open:
    print('something it is doing')