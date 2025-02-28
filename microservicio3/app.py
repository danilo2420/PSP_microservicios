from flask import Flask, jsonify
import json

app3 = Flask(__name__)

with open("demo.json", "r", encoding="utf-8") as file:
    demo_data = json.load(file)

@app3.route('/<int:municipioid>/demo', methods=['GET'])
def get_demo(municipioid):
    if municipioid == demo_data["municipioid"]:
        return jsonify(demo_data), 200  # Devuelve 200 OK explícitamente
    else:
        return jsonify({"error": "Municipio no encontrado"}), 404  # Devuelve 404 si no coincide

if __name__ == '__main__':
    app3.run(port=5002)