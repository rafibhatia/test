for attempt in range(3): 
    name = input('What is your name? ')
    
    if name == 'eli':
        print('Hi, ' + name)
        break 
    else:
        print('Sorry, locked out. Please try again.')
        
else:
    print('Too many attempts, program locked.')
