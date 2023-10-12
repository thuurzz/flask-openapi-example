# API de Clientes

Bem-vindo ao repositório da API de Clientes! Este projeto é uma aplicação web desenvolvida usando Python, Flask, SQLAlchemy, Flask-RESTful, Flasgger e autenticação JWT. É destinado a fornecer um sistema robusto e eficiente para gerenciar clientes.

## Começando

### Pré-requisitos

- Python 3.7 ou superior
- Pip (gerenciador de pacotes Python)
- Virtualenv (opcional, mas recomendado)

### Instalação

1. Clone o repositório

   ```shell
   git clone https://github.com/thuurzz/flask-openapi-example
   ```

2. Navegue até o diretório do projeto

   ```shell
   cd flask-openapi-example
   ```

3. Crie um ambiente virtual (opcional)

   ```shell
   python -m venv maquininha
   ```

4. Ative o ambiente virtual

   - No Linux/Mac:
     ```shell
     source maquininha/bin/activate
     ```
   - No Windows:
     ```shell
     maquininha\Scripts\activate
     ```

5. Instale as dependências

   ```shell
   pip install -r requirements.txt
   ```

6. Inicie a aplicação
   ```shell
   python main.py
   ```

## Documentação da API

A documentação da API, incluindo os endpoints disponíveis, parâmetros e exemplos de respostas, está disponível em `/apidocs` quando a aplicação está em execução.

## Contrato OpenAPI

O contrato OpenAPI que define a especificação da API está disponível no arquivo `openapi.yaml` na raiz do projeto. Ele segue a especificação OpenAPI 3.0.2 e define os endpoints, parâmetros, respostas e esquemas de segurança da API.

## Licença

Este projeto está licenciado sob os termos da licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

&copy; 2023 Arthur Vinícius. Todos os direitos reservados.
