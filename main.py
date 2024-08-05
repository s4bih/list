from flask import Flask,render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    apel = "apel"
    pisang = "pisang"
    anggur = "anggur"
    chitato = "chitato"
    lays = "lays"
    qtela = "qtela"
    return render_template('lisr.html', apel = apel, pisang = pisang, anggur = anggur, chitato = chitato, lays = lays, qtela = qtela)


if __name__ == '__main__':
    app.run(debug   = True)