mensagem_original = open('mensagem.txt', 'r')
mensagem_criptografada = open('cripto.txt', 'w')

for linha in mensagem_original.readlines():
    for letra in linha:
        if letra in 'aeiou':
            mensagem_criptografada.write('*')
        else:
            mensagem_criptografada.write(letra)

mensagem_original.close()
mensagem_criptografada.close()
