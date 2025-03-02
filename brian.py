# Yo whats going on guys and today we will be coding for Sac Hacks! Wow! OMG!
# EPIC 
# W
import requests
import urllib.parse

print("Hello World!") 

def encode_url(url):
    '''If url inputted doesnt have http in front or whatever'''
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url

    parsed = urllib.parse.urlsplit(url)

    encoded_path = urllib.parse.quote(parsed.path)

    encoded_query = urllib.parse.quote(parsed.query, safe="=&")
    encoded_fragment = urllib.parse.quote(parsed.fragment)

    encoded_url = urllib.parse.urlunsplit((parsed.scheme,
                                            parsed.netloc,
                                            encoded_path,
                                            encoded_query,
                                            encoded_fragment))
    return encoded_url





url = "https://www.roblox.com/home" # REPLACE WITH DESIRED URL

encoded_url = encode_url(url) # If user doesnt give http in front itll add it as well as go thru other stuff. API only works with "URL Encoded" urls

response = requests.get(f"https://api.websitecarbon.com/site?url={encoded_url}")

print(response.text)

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
