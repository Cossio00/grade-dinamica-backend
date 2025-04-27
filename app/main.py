from flask import request, jsonify, send_from_directory
import pdfplumber
from app.disciplina import Disciplina
import os

def configure_routes(app):
    @app.route("/")
    def index():
        return send_from_directory(app.static_folder, 'index.html')

    @app.route("/upload", methods=["POST"])
    def processar_pdf():
        if 'file' not in request.files:
            return jsonify({"erro": "Nenhum arquivo enviado"}), 400

        file = request.files['file']
        disciplinas = []

        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    for row in table:
                        if row and row[-1] == 'AP':
                            codigo, nome = row[1].split(" - ")
                            if len(row) > 10:
                                disciplina = Disciplina(codigo, nome, row[7], row[-1], 0)
                            else:
                                disciplina = Disciplina(codigo, nome, row[2], row[-1], 0)
                            disciplinas.append(disciplina)

        for d in disciplinas:
            if "(E)" in d.getNome():
                d.setTipo(1)
            elif "(F)" in d.getNome():
                d.setTipo(2)

        return jsonify([d.to_dict() for d in disciplinas])
