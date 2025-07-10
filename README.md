
# 🔐 Verificador de Força de Senha

Este é um projeto simples em Python que analisa a força de senhas digitadas pelo usuário, com o objetivo de demonstrar boas práticas em segurança digital, lógica de programação e uso de expressões regulares.

---

## 🎯 Objetivo

Criar um verificador de senhas que identifique se uma senha é:
- Muito fraca (por estar em listas comuns ou ser previsível)
- Fraca
- Boa, mas pode melhorar
- Forte
- Excelente

Além disso, o sistema salva os resultados em um arquivo `.txt` para análise posterior.

---

## 🛠️ Funcionalidades

- Análise de:
  - Comprimento da senha
  - Presença de letras maiúsculas e minúsculas
  - Números
  - Caracteres especiais
  - Palavras/senhas fracas comuns

- Salva os resultados da análise em um arquivo de texto:

resultado_senhas.txt

## 📚 Tecnologias utilizadas

- Python 3.x
- Biblioteca `re` (regex)

---

## 🚀 Como executar

1. Clone este repositório ou baixe os arquivos.
2. Execute o script no terminal:

```bash
python verificador_forca_senha.py

💡 Exemplos de saída
Digite sua senha (ou 'sair' para encerrar): senha123
Resultado da análise: Fraca

Digite sua senha (ou 'sair' para encerrar): Bea!2025
Resultado da análise: Excelente

📁 Estrutura do projeto

verificador_senha/
│
├── verificador_forca_senha.py      # Código principal
├── resultado_senhas.txt            # Resultado das análises (gerado automaticamente)
└── README.md                       # Este arquivo

✅ Aprendizados
Estrutura de decisão lógica

Regex e validação de strings

Pensamento crítico aplicado à segurança

Prática de automação simples com Python

Uso de arquivos .txt para salvar logs

📌 Observações
Este projeto é apenas educacional e serve como base para estudos em segurança cibernética.
Você pode expandi-lo com uma interface gráfica, banco de dados ou integração com API.


## ✨ Autora

Beatriz Pereira Acrizio  
[GitHub](https://github.com/ACRIZIO0507) | [LinkedIn](https://www.linkedin.com/in/bea-acrizio07)

