from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    nome = "João"
    return render_template("index.html", nome=nome)

@app.route('/mensagem', methods=["POST"])
def msg():
    mensagem = request.form["texto"]
    return f"{mensagem}"

if __name__ == "__main__":
    app.run(debug=True)