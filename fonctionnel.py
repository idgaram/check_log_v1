from flask import Flask, request, render_template, jsonify
import requests, datetime, json
from tinydb import TinyDB, where, Query


# fonction flask
app = Flask(__name__)
app.secret_key = "test"


# définition des variables
temps = (datetime.datetime.now()).strftime('%H:%M:%S')
url_site_1 = "http://example.com"
url_site_2 = "http://example.org"


# création du fichier json
# pour pc
# db = TinyDB(r"C:\Users\lorys\pypif\flaskstage\pinglog\logs.json", indent=4)

# pour docker
db = TinyDB("logs.json", indent=4)



# accueil
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url_site_1 = "http://" + request.form["url_site_1"]
        url_site_2 = "http://" + request.form["url_site_2"]
        status_site_1 = requests.get(url_site_1)
        status_site_2 = requests.get(url_site_2)
        db.upsert({"url": f"{url_site_1}", "status": f"{status_site_1.status_code}", "time_test": f"{temps}"}, where("url") == f"{url_site_1}")
        db.upsert({"url": f"{url_site_2}", "status": f"{status_site_2.status_code}", "time_test": f"{temps}"}, where("url") == f"{url_site_2}")
        return render_template("test_v3.html", url_site_1=url_site_1 , url_site_2=url_site_2)
    return render_template('index_v1.html')

@app.route('/logs')
def get_logs():
    with open("logs.json", 'r') as f:
        logs = json.load(f)
    return jsonify(logs)


# pas de doublons de app.run
if __name__=="__main__":
    app.run(host="0.0.0.0", port= 9999, debug=True)