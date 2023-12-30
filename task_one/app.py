from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', strict_slashes=False, methods=['GET'])
def first_app():
    """A minimal api endpoint that returns my basic info"""
    
    return jsonify({
         "gender": "Male",
         "github_url": "https://github.com/dominic-source",
         "name": "Morba Chinonso"
    })
    
    

if __name__ == '__main__':
    app.run(port=5000, host='127.0.0.1')