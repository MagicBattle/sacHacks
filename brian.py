# Yo whats going on guys and today we will be coding for Sac Hacks! Wow! OMG!

from flask import Flask, request, jsonify
import requests
import urllib.parse
import os
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://magicbattle.github.io"}})

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

def encode_url(url):
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    parsed = urllib.parse.urlsplit(url)
    encoded_path = urllib.parse.quote(parsed.path)
    encoded_query = urllib.parse.quote(parsed.query, safe="=&")
    encoded_fragment = urllib.parse.quote(parsed.fragment)
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, encoded_path, encoded_query, encoded_fragment))

def ask_gpt(website):
    prompt = f"""
    Analyze the carbon footprint of {website}. Consider:
    - Hosting (check if it's green using The Green Web Foundation).
    - Page size & bandwidth usage (estimated from common websites).
    - Data center efficiency.

    Provide a brief report on CO2 emissions and recommendations to reduce it.
    """

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert in environmental impact analysis."},
                {"role": "user", "content": prompt}
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error in GPT request: {str(e)}"

@app.after_request
def add_cors_headers(response):
    response.headers.add("Access-Control-Allow-Origin", "https://magicbattle.github.io")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type,Authorization")
    response.headers.add("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
    return response

@app.route('/check', methods=['GET'])
def check_website():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400 

    encoded_url = encode_url(url)
    gpt_analysis = ask_gpt(encoded_url)

    return jsonify({
        "url": encoded_url,
        "gpt_analysis": gpt_analysis
    })

print("Loaded API Key:", "SET" if OPENAI_API_KEY else "NOT SET")

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
