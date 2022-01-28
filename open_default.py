import definitions

if not definitions.LINK=='noclass':
    import webbrowser
    print(definitions.day)
    print(*definitions.time, sep=':')
    print(definitions.PERIOD)
    print('Opening :', definitions.LINK, sep='\n')
    webbrowser.open(definitions.LINK)
    print('Succesfully Opened')
    input('Press enter to close') # to freeze the script to prevent it from closing
else:
    print('Break time / No class right now')
    input('Press enter to close')