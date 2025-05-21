while True:
    senha = input("Digite uma senha forte (mín. 8 caracteres e pelo menos 1 número) ou 'sair': ")

    if senha.lower() == 'sair':
        print("Encerrando...")
        break

    if len(senha) < 8:
        print("Senha muito curta. Deve ter no mínimo 8 caracteres.")
        continue

    if not any(char.isdigit() for char in senha):
        print("A senha deve conter pelo menos um número.")
        continue

    print("Senha forte cadastrada com sucesso!")
    break
