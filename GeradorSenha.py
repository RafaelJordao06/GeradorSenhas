import random, string
tamanhoSenha = int(input('Digite o tamanho da senha: '))
caracterSenha = string.ascii_letters + string.digits + string.punctuation
senha = []
for x in range(tamanhoSenha):
    senha.append(random.choice(caracterSenha))
print("".join(senha))