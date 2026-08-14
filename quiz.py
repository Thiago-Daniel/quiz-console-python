# Exercício - sistema de perguntas e respostas

letras = ['A' , 'B', 'C', 'D']

perguntas = [
    {
        'Pergunta': 'Quanto eh 2 + 2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto eh 5 * 5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto eh 10 / 2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
    {
        'Pergunta': 'Quanto eh 11 * 11?',
        'Opções': ['120', '125', '110', '121'],
        'Resposta': '121',
    },
]

acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'] + '\n')

    for indice, opcao in enumerate(pergunta['Opções']):
        print(f'{letras[indice]}) {opcao}')

    resposta = input('Qual sua resposta?').upper()

    indice_escolhido = letras.index(resposta)

    opcao_escolhida = pergunta['Opções'][indice_escolhido]

    if opcao_escolhida == pergunta['Resposta']:
        print('Sua resposta está correta! ✅')
        acertos += 1
    else:
        print('Resposta errada! ❌')
print('Você acertou: ', acertos, 'de', len(perguntas))