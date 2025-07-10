import re

# Lista de senhas fracas comuns
senhas_fracas = ["123456", "senha", "password", "admin", "qwerty", "123456789", "abc123"]

def verificar_forca(senha):
    pontuacao = 0

    # Verifica se a senha está na lista de senhas fracas
    if senha.lower() in senhas_fracas:
        return "Muito fraca (senha comum)"

    # Comprimento mínimo
    if len(senha) >= 8:
        pontuacao += 1

    # Letras maiúsculas e minúsculas
    if re.search(r'[A-Z]', senha) and re.search(r'[a-z]', senha):
        pontuacao += 1

    # Números
    if re.search(r'\d', senha):
        pontuacao += 1

    # Caracteres especiais
    if re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?~\\/-]', senha):
        pontuacao += 1

    # Classificação
    if pontuacao <= 1:
        return "Fraca"
    elif pontuacao == 2:
        return "Boa, mas pode melhorar"
    elif pontuacao == 3:
        return "Forte"
    else:
        return "Excelente"

# Teste simples
if __name__ == "__main__":
    senha = input("Digite sua senha: ")
    resultado = verificar_forca(senha)
    print(f"Resultado da análise: {resultado}")

if __name__ == "__main__":
    # Limpa o arquivo ao iniciar o programa
    with open("resultado_senhas.txt", "w") as f:
        f.write("Análise de Força de Senhas\n")
        f.write("==========================\n")

    while True:
        senha = input("Digite sua senha (ou 'sair' para encerrar): ")
        if senha.lower() == 'sair':
            break
        resultado = verificar_forca(senha)
        print(f"Resultado da análise: {resultado}\n")

          # 📝 Salva o resultado da senha analisada
        with open("resultado_senhas.txt", "a") as f:
            f.write(f"Senha: {senha} | Força: {resultado}\n")
