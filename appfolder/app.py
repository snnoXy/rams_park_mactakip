from flask import Flask, jsonify
from utils import get_match_response, create_mail
from config import mailList

app = Flask(__name__)
app.config["DEBUG"] = False


@app.route("/", methods=["GET"])
def home():
    return """<h1>Merhaba</h1>
        <p>Rams Park Maç takip sistemine hoşgeldiniz.\n .../get_matches adresine istek atarak maç durumunun mail ile iletilmesini sağlayabilirsiniz.</p>"""


@app.route("/get_matches", methods=["GET"])
def get_matches():
    create_mail(mailList, matchResponse)
    return jsonify(matchResponse.matchState), 200


if __name__ == "__main__":
    matchResponse = get_match_response()
    app.run()
