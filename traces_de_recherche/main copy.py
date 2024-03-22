from flask import Flask, request, render_template, flash
import requests, datetime, time, threading
from tinydb import TinyDB, where, Query


# fonction flask
app = Flask(__name__)
app.secret_key = "test"

# création du fichier json
db = TinyDB(r"C:\Users\lorys\pypif\flaskstage\pinglog\logs.json", indent=4)
# db = TinyDB("/pinglog/logs.json", indent=4)

# création des variables des formulaires html
url_site_1 = "http://facebook.com"
url_site_2 = "http://youtube.com"


# accueil
@app.route('/')
def index():
    return render_template("index.html")

def check():
    # définition des url
    global input_url_site_1, input_url_site_2, url_site_1, url_site_2
    # url_site_1 = "http://" + input_url_site_1
    # url_site_2 = "http://" + input_url_site_2

    
    
    # definition des variables
    status_site_1 = requests.get(url_site_1)
    status_site_2 = requests.get(url_site_2)
    global list_request_not_200
    list_request_not_200 = []
    global record_1
    global record_2

    temps = (datetime.datetime.now()).strftime('%H:%M:%S')

    # ajout des différentes valeurs et clés des sites rentrés par l'utilisateur
    db.upsert({"url": f"{url_site_1}", "status": f"{status_site_1.status_code}", "time_test": f"{temps}"}, where("url") == f"{url_site_1}")
    db.upsert({"url": f"{url_site_2}", "status": f"{status_site_2.status_code}", "time_test": f"{temps}"}, where("url") == f"{url_site_2}")

    #check statut sites et ajout à "ne fonctionne renvoie pas le statut 200"
    User = Query()
    list_request_not_200 = db.get(User.status != 200)
    record_1 = db.get(doc_id=1)
    record_2 = db.get(doc_id=2)
    
# mise en place de l'appel de la fonction check() en background toutes les x secondes
def schedule_task():
    while True:
        check()
        time.sleep(3)
        


scheduler_thread = threading.Thread(target=schedule_task)
scheduler_thread.daemon = True
scheduler_thread.start()

# page resultat
@app.route('/resultat', methods=['GET', 'POST'])
def resultat():
    logs = []
    if list_request_not_200:
        for url in list_request_not_200:
            log = db.search(Query().url == url)
            if log:
                logs.append(log[0])
    return render_template("resultat.html", logs=logs)



# # page resultat
# @app.route('/resultat', methods=['GET', 'POST'])
# def resultat():
#     if f"{url_site_1}" in list_request_not_200:
#         flash("le site 1 ne renvoie pas la requete 200 👉:" + str(request.form["record_1"] ))
#     else:
#         flash(f"le site {url_site_1} est ok")
#     if f"{url_site_1}" in list_request_not_200:
#         flash("le site 2 ne renvoie pas la requete 200 👉:" + str(request.form["record_2"] ))
#     else:
#         flash(f"le site {url_site_2} est ok")
#     return render_template("index.html", list_request_not_200 = list_request_not_200)






# pas de doublons de app.run
if __name__=="__main__":
    app.run(host="0.0.0.0", port= 9999, debug=True)