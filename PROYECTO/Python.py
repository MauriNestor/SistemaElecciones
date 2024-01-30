from flask import Flask, render_template

app = Flask(__name__)


candidatos = [
    {"nombre": "Candidato1", "partido": "UTP", "image_path": "candidato1.jpg"},
    {"nombre": "Candidato2", "partido": "UDD", "image_path": "candidato2.jpg"},
    {"nombre": "Candidato3", "partido": "OPS", "image_path": "candidato3.jpg"},
    {"nombre": "Candidato4", "partido": "XYZ", "image_path": "candidato4.jpg"},
    {"nombre": "Candidato5", "partido": "ABC", "image_path": "candidato5.jpg"},
    
]

resultados = [100, 80, 60, 40, 30]  # Agrega los resultados a cada candidato

@app.route('/')
def index():
    return render_template('tu_archivo_html.html', candidatos=candidatos, resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)
