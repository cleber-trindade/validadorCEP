from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/cep/<cep>")
def buscar_cep(cep):
    if not cep.isdigit():
        return {"erro": "CEP inválido"}, 400

    resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    if resposta.status_code != 200 or 'erro' in resposta.json():
        return {"erro": "CEP não encontrado"}, 404

    return jsonify(resposta.json())

if __name__ == "__main__":
    app.run(debug=True)