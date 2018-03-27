usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole',
'InterpreterInterface', 'StartServer', 'bob']
username = input('Please enter your username: ')
allowed = False
for i in range(0, len(usernames)):
    if username == usernames[i]:
        allowed = True
        break

if allowed == True:
    print('Access granted')
else:
    print('Access denied')
