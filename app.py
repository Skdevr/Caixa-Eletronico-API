from flask import Flask, request, jsonify

class CaixaEletronico:
    def __init__(self):
        self.CEDULAS = [100, 50, 20, 10, 5, 2]

    def sacar(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            return jsonify({'erro': 'Valor de saque inválido, por favor insira um número inteiro positivo.'}), 400

        cedulas = {}
        for cedula in self.CEDULAS:
            qtd_cedulas = valor // cedula
            if qtd_cedulas > 0:
                cedulas[cedula] = qtd_cedulas
                valor -= qtd_cedulas * cedula

        if valor > 0:
            return jsonify({'erro': 'Não é possível sacar este valor com as cédulas disponíveis.'}), 400

        return jsonify(cedulas)

app = Flask(__name__)
caixa = CaixaEletronico()

@app.route('/api/saque', methods=['POST'])
def sacar_api():
    if request.content_type != 'application/json':
        return jsonify({'erro': 'Tipo de conteúdo não suportado, por favor envie os dados no formato JSON.'}), 415
    
    data = request.get_json()
    valor = data.get('valor')

    return caixa.sacar(valor)

if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)