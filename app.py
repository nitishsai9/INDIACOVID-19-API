from flask import Flask
from flask import jsonify
import Indiacorona.py 
app = Flask(__name__)
@app.route('/, methods=['GET'])
def tot():
    return jsonify(Indiacorona.py .f)
@app.route('/stats', methods=['GET'])
def index():
    return jsonify(Indiacorona.py.d)
if __name__=="__main__":
    app.run(threaded=True, port=5000)
