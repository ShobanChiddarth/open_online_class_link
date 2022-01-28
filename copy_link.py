import definitions

if not definitions.LINK=='noclass':
    import pyperclip
    print(definitions.day)
    print(*definitions.time, sep=':')
    print(definitions.PERIOD)
    print('Copying :', definitions.LINK, sep='\n')
    pyperclip.copy(definitions.LINK)
    print('Succesfully Copied')
    input('Press enter to close') # to freeze the script to prevent it from closing
else:
    print('Break time / No class right now')
    input('Press enter to close')