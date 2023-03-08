def encode(password):
    new_pass = ''
    for elem in password[::]:
        if elem == '0':
            new_pass += '3'
        if elem == '1':
            new_pass += '4'
        if elem == '2':
            new_pass += '5'
        if elem == '3':
            new_pass += '6'
        if elem == '4':
            new_pass += '7'
        if elem == '5':
            new_pass += '8'
        if elem == '6':
            new_pass += '9'
        if elem == '7':
            new_pass += '0'
        if elem == '8':
            new_pass += '1'
        if elem == '9':
            new_pass += '2'
    return new_pass


print(encode('34624589'))