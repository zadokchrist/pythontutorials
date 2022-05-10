prevcommand=''
while  True:
    command = input('> ').lower()

    if command== 'help':
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)
    elif command=='start' and prevcommand !='start':
        prevcommand='start'
        print('Car started... Ready to go')
    elif command=='start' and prevcommand=='start':
        print('Car already started...')
    elif command=='stop' and prevcommand != 'stop':
        prevcommand='stop'
        print('Car stopped...')
    elif command=='stop' and prevcommand == 'stop':
        print('Car already stopped...')
    elif command=='quit':
        break
    else:
        print("I don't understand your command")