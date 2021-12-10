from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
   return 'Hola Mundo soy Alejandro un gusto saludarte !'

@app.route('/<name>')
def hola_nombre(name):
   return 'Hola Mundo soy Alejandro un gusto saludarte %s!' % name

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)