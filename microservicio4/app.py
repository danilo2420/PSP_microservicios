from flask import Flask, jsonify
import requests
import json

app4 = Flask(__name__)

@app4.route('/<int:municipioid>/<parametro1>/<parametro2>', methods=['GET'])
def get_combined(municipioid, parametro1, parametro2):
    urls = {
        "geo": f"http://geo_service:5000/{municipioid}/geo",
        "meteo": f"http://meteo_service:5001/{municipioid}/meteo",
        "demo": f"http://demo_service:5002/{municipioid}/demo"
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
    app4.run(host='0.0.0.0', port=5003)
