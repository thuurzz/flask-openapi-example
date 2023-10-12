from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)

app.config['SWAGGER'] = {
    'openapi': '3.0.2'
}

swagger = Swagger(app, template_file='openapi.yaml')

@app.route('/health', methods=['GET'])
def hello_world():
    """
    Verifica saúde da API
    ---
    tags:
        - Health
    security: []
    responses:
      200:
        description: API está saudável
      400:
        description: Houve um erro
    """
    return jsonify({"status": 'ok'})

if __name__ == "__main__":
    app.run(debug=True)
