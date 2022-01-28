nome = str(input('Qaul seu Nome? '))
if nome == 'Jefferson':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem polular no Brasil.')
else:
    print('Seu nome é bem normal !')
print('tenha um bom dia, {}'.format(nome))