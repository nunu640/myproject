
from flask import Flask

app = Flask(__name__)

@app.route('/')
def ana_sehife():
    return """
    <h2 style="color:red;">Salam Favorite Premium market səhifəsinə xoş gəlmisiniz!</h2>
    <p style="font-size:18px; color:black;">
    Bu saytda siz Favorite Premium Market haqqında geniş məlumat əldə edəcəksiniz.
    Səhifəmizdə marketin müştərilərə olan xidmətləri, geniş növdə məhsullarımız 
    haqqında məlumatlar öz əksini tapmaqdadır.
    </p>

    <!-- Burada market sekli var -->
    <img src="https://lh3.googleusercontent.com/p/AF1QipOoBcbHutl52Iqv1hDlxIH5plp7e4p8xjPgxXfV=s680-w680-h510-rw"
         alt="Favorite Market sekli" width="400">
    
    <br><br>


    <a href="/rengler">Kataloqa kecid edin</a> 
    """

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
