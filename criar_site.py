def criarSite():
    consoleMenu = '[t] - título\n' \
                  '[d] - divider\n' \
                  '[c] - parágrafo\n' \
                  '[s] - salvar alterações e sair\n'
    print(consoleMenu)
    x = ''
    with open('site.html', 'w') as arq:
        while x != 's':
            x = input('Digite a opção: ')

            if x == 't':
                op = input('digite o título do site: ')
                arq.write(f'<h1>{op}</h1>')
            elif x == 'd':
                try:
                    arq.write('<hr>')
                    print('divider adicionado :)')
                except:
                    print('não consegui adicionar o divider :(')
            elif x == 'c':
                op = input('digite o conteudo do parágrafo: ')
                arq.write(f"<p>{op}</p>")
                print('paragrafo adicionado :)')

criarSite()
