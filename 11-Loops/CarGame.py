#Car Game
command = ""
is_carStarted = False
while True:
    command = input().lower()
    if command == 'help':
        print('''start - to start the car
stop - to stop the car
quit - to exit''')
    elif command == 'start':
        if is_carStarted:
            print('Car already Started!!!')
        else:
            print('Car Started...')
            is_carStarted = True
    elif command == 'stop':
        if is_carStarted:
            print('Car stopped.')
            is_carStarted = False
        else:
            print('Car is already stopped!!!')
    elif command == 'quit':
        break;
    else:
        print("I don't understand that...")
