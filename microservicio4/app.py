from flask import Flask, jsonify
import requests
import json

app4 = Flask(__name__)

@app4.route('/<int:municipioid>/<parametro1>/<parametro2>', methods=['GET'])
def get_combined(municipioid, parametro1, parametro2):
    urls = {
    "geo": f"http://127.0.0.1:5000/{municipioid}/geo",
    "meteo": f"http://127.0.0.1:5001/{municipioid}/meteo",
    "demo": f"http://127.0.0.1:5002/{municipioid}/demo"
    }

    response_data = {}

    for param in [parametro1, parametro2]:
        if param in urls:
            try:
                response = requests.get(urls[param])
                if response.status_code == 200:
                    response_data[param] = response.json()
                else:
                    response_data[param] = {"error": f"Estado {response.status_code}"}
            except requests.exceptions.RequestException as e:
                response_data[param] = {"error": str(e)}

    return jsonify(response_data)

if __name__ == '__main__':
    app4.run(port=5003)
