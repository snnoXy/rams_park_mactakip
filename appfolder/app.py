from flask import Flask, jsonify
from utils import get_match_response, create_mail
from config import mailList

app = Flask(__name__)
app.config["DEBUG"] = False


@app.route("/", methods=["GET"])
def home():
    return """<h1>RAMS Park Maç Takip Sistemi</h1>
        <p>Merhaba, Rams Park Maç takip sistemine hoşgeldiniz. .../get_matches adresine istek atarak maç durumunun mail ile iletilmesini sağlayabilirsiniz.</p>
    <h3> Maç durumunu mail ile iletmek için </h4>
            <form action="http://127.0.0.1:5000/get_matches">
                    <input type="submit" value="Mail yolla"/>
            </form>
        <p> Not: Eğer bir maç yoksa mail atılmayacaktır."""


@app.route("/get_matches", methods=["GET"])
def get_matches():
    create_mail(mailList, matchResponse)
    return jsonify("There is a match" if matchResponse.matchState == 1 else "No match"), 200


if __name__ == "__main__":
    matchResponse = get_match_response()
    app.run()
