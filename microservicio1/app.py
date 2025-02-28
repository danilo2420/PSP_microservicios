from flask import Flask, jsonify
import json

app1 = Flask(__name__)

# Cargar datos desde el archivo JSON
with open("municipio.json", "r", encoding="utf-8") as file:
    municipio_data = json.load(file)

@app1.route('/<int:municipioid>/geo', methods=['GET'])
def get_geo(municipioid):
    if municipioid == municipio_data["municipioid"]:
        return jsonify(municipio_data), 200  # Devuelve 200 OK explícitamente
    else:
        return jsonify({"error": "Municipio no encontrado"}), 404  # Devuelve 404 si no coincide

if __name__ == '__main__':
    app1.run(port=5000)