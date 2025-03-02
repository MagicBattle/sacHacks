# Yo whats going on guys and today we will be coding for Sac Hacks! Wow! OMG!
from flask import Flask, request, jsonify
import requests
import urllib.parse
from flask_cors import CORS

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

API_TOKEN = "ci1egxw2v.clixa5qci0000e7og427vx8lrf9ecf2a6.2141e66cad2dbea8"

def encode_url(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    parsed = urllib.parse.urlsplit(url)
    encoded_path = urllib.parse.quote(parsed.path)
    encoded_query = urllib.parse.quote(parsed.query, safe="=&")
    encoded_fragment = urllib.parse.quote(parsed.fragment)

    encoded_url = urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, encoded_path, encoded_query, encoded_fragment))
    return encoded_url

@app.route('/check', methods=['GET'])
def check_website():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400 
    
    encoded_url = encode_url(url)
    headers = {
        "x-api-token": API_TOKEN,
        "accept": "application/json"
    }

    api_url = f"https://ecoping.earth/api/website?url={encoded_url}"

    try:
        response = requests.get(api_url, headers=headers)

        if response.status_code == 200:
            return jsonify(response.json()), 200
        elif response.status_code == 404:
            return jsonify({"error": "Website not found in Ecoping database"}), 404
        elif response.status_code == 401:
            return jsonify({"error": "Invalid API token"}), 401
        else:
            return jsonify({"error": f"API request failed with status {response.status_code}"}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Request error: {str(e)}"}), 500 
    
if __name__ == '__main__':
    app.run(debug=True)


# url = "https://www.roblox.com/home" # REPLACE WITH DESIRED URL

# encoded_url = encode_url(url) # If user doesnt give http in front itll add it as well as go thru other stuff. API only works with "URL Encoded" urls

# response = requests.get(f"https://api.websitecarbon.com/site?url={encoded_url}")

# print(response.text)

### EXAMPLE OF RESPONSE.TEXT:
'''
{
  "url": "https://www.google.com/",
  "green": true, # HERE IT WILL BE TRUE, FALSE, OR UNKNOWN. 
  "bytes": 987799,
  "cleanerThan": 0.77,
  "rating": "B",
  "statistics": {
    "adjustedBytes": 745788.245,
    "energy": 0.0005626012370456011,
    "co2": {
      "grid": {
        "grams": 0.24866974677415568,
        "litres": 0.13831011315578537
      },
      "renewable": {
        "grams": 0.21558879403587433,
        "litres": 0.11991048724275329
      }
    }
  },
  "timestamp": 1740873753
}
'''
