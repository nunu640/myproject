
from flask import Flask

app = Flask(__name__)

@app.route('/')
def ana_sehife():
    return """
    <!doctype html>
    <html lang="en">
    <head>
      <meta charest="utf-8">
      <title>Welcome to Terrace restaurant</title>
    </head>
    <body>
      <h1 style="color: red; font-size: 60px; font-family: 'Brush Script Mt', cursive;">
      
"""

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)