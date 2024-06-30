# Caixa-Eletronico-API

Essa API recebe um valor de saque desejado e retorna a quantidade de cédulas de cada valor necessárias para compor esse saque, utilizando a menor quantidade de cédulas possível. As cédulas consideradas são: 100, 50, 20, 10, 5 e 2.

## Requisitos

 Antes de começar a usar a API certifique que tenha instalado o Python e o Flask
- Python 3.12.4
- Flask 3.0.3

## Preparando para a instalação

1. Copia e cole o codigo na IDE ou clone o [repositório](https://docs.github.com/pt/repositories/creating-and-managing-repositories/cloning-a-repository).

2. Faça a criação de um ambiente virtual:
    ```sh
    py -m venv .venv # Windows
    venv\Scripts\activate  # No Windows

    python3 -m venv venv # MacOS/Linux
    source venv/bin/activate  # No macOS/Linux

    para desativar a venv use o comando "deactivate"
    ```
    caso precise de mais ajuda precise de mais ajuda use a [documentação oficial](https://packaging.python.org/pt-br/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments)

4. Instale ou atualize o pip e as dependências:
    ```sh
    # No Windows 
    py -m pip install --upgrade pip
    py -m pip --version

    # No MacOS/Linux
    python3 -m pip install --upgrade pip
    python3 -m pip --version

    Antes de instalar o flask use
    flask --version
    Se aparecer a saída abaixno no terminal você já tem o flask instalado
    Python 3.12.4
    Flask 3.0.3
    Werkzeug 3.0.3
    Se não aparecer digite o comando abaixo no terminal
    pip install Flask
    ```
    Caso esteja com duvidas ou não funcione por favor consulte a documentação oficial do [Flask](https://flask.palletsprojects.com/en/3.0.x/installation/)

## Como usar: 

1. inicialize o servidor Flask seguindo os passos abaixo no terminal:
    
   ```sh
    python app.py
    ```
    Caso prefira use a GUI da sua IDE para iniciar o servidor
    

3. Acesse a endpoint `/api/saque` para usar a API. Utilize uma ferramenta HTTP como o Postman ou curl para realizar a tarefa.

### No Windows, utilize o PowerShell com Curl. Substitua o valor inteiro dentro das chaves {}.

```sh
Invoke-WebRequest -Uri "http://localhost:5000/api/saque" -Method POST -ContentType "application/json" -Body '{"valor": 550}'

```
### Saída:
```sh
StatusCode        : 200                                                                                                                                                                                                     
StatusDescription : OK                                                                                                                                                                                                      
Content           : {                                                                                                                                                                                                       
                      "50": 1,
                      "100": 5
                    }

```

## Instalação e uso do Postman:
### No MacOS/Linux utilize o Postman

1.  Baixar e Instalar o Postman
Se você ainda não possui o Postman, acesse o [site](https://www.postman.com/) e faça o download da versão mais recente para o seu sistema operacional.
Siga as instruções de instalação para concluir o processo.

2. Crie uma nova requisição:

Clique no botão "New" e selecione "Request".
Dê um nome para sua requisição, por exemplo, "Teste de Saque".
Adicione a requisição a uma coleção ou crie uma nova coleção para organizá-la.
Configure a requisição:

Método: Selecione o método POST.
URL: Insira a URL http://localhost:5000/api/saque
Adicione os cabeçalhos:

Vá para a aba "Headers" e adicione um novo cabeçalho:
Key: Content-Type
Value: application/json
Adicione o corpo da requisição:

Vá para a aba "Body".
Selecione raw e depois escolha JSON (application/json) no menu dropdown à direita.
Insira o seguinte JSON como exemplo:
json
Copiar código
{
    "valor": 679
}
Envie a requisição:

Clique no botão "Send" para enviar a requisição.
Verifique a resposta:
Você deve ver uma resposta JSON similar a esta, que mostra a quantidade de cédulas necessárias para o saque:

```sh
{
    "2": 2,
    "5": 1,
    "20": 1,
    "50": 1,
    "100": 6
}

```
Para mais informações ou ajuda consulte a [documentação oficial](https://www.postman.com/api-documentation-tool/)


## quais foram os principais desafios

Os principais desafios que eu tive com o desafio foi a logica de saque para fazer de uma forma clara e facil de entender, por esse motivo escolhi usar a orientação a objeto na criação da API para facilitar a revisão do codigo e a requisão da endpoint onde tive que aprender o comando Invoke-WebRequest para realizar solicitações a API pelo terminal.
