import subprocess
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ejecutar-playbook', methods=['GET'])
def ejecutar_playbook():
    playbook_path = '/app/playbook.yml' # Ruta dentro del contenedo, ajusta segun sea necesario
    try:
        #Ejecutar el playbook usando subprocess
        resultado= subprocess.run(['ansible-playbook', playbook_path], captura_output=True, text=True)
        output = resultado.stdout
        return jsonify({'status': 'sucess', 'output' : 'output'}), 200
    except Exception as e: 
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
        app.run(debug=True, hosts='0.0.0.0')

