from flask import Flask, jsonify
import requests

app2 = Flask(__name__) 

@app2.route('/<int:municipioid>/meteo', methods=['GET'])
def get_meteo(municipioid):
    try:
        meteo_url = f"https://www.el-tiempo.net/api/json/v2/provincias/18/municipios/{municipioid}"
        meteo_response = requests.get(meteo_url)

        if meteo_response.status_code == 200:
            data = meteo_response.json()

            # Devolver solo la información meteorológica
            weather_data = {
                "temperatura": data["temperatura_actual"],
                "temperatura_max": data["temperaturas"]["max"],
                "temperatura_min": data["temperaturas"]["min"],
                "humedad": data["humedad"],
                "viento": data["viento"],
                "precipitacion": data["precipitacion"],
                "lluvia": data["lluvia"]
            }
            return jsonify(weather_data), 200
        
    except e:
            return jsonify({"error": f"{e}"}), 500
    
if __name__ == '__main__':
    app2.run(port=5001)  
