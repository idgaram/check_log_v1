from flask import Flask, request, render_template
import requests, datetime, time, json, threading








# fonction flask
app = Flask(__name__)
app.secret_key = "test"

# création du fichier json
chemin = "/pinglog/logs.json"
with open(chemin, "w", encoding='utf-8') as f:
    json.dump("", f)



# importation et création de la liste du json
def check():
    sites = ["https://www.loryss.fr/", "https://youtube.com"]
    temps = datetime.datetime.now()


    #check statut sites et ajout à fonctionne /ne fonctionne pas 
    ok = []
    neg = []
    for site in sites:
        statut = requests.get(site)
        if statut.status_code == 200:
            ok.append(site)
        else:
            neg.append(site)
            neg.append(statut)
    
    # création / modification du fichier json
    with open(chemin, "r", encoding='utf-8') as f:
        contenu = json.load(f)
    
    with open(chemin, "w", encoding='utf-8') as f:
        json.dump(f"{contenu} {temps.strftime('%H:%M:%S')} {neg}  ", f, indent=4)
    

def schedule_task():
    while True:
        check()
        time.sleep(3)
        

# mise en place de l'appel de la fonction check() en background toutes les x secondes
scheduler_thread = threading.Thread(target=schedule_task)
scheduler_thread.daemon = True
scheduler_thread.start()

# accueil
@app.route('/', methods=['GET', 'POST'])
def index():
    with open(chemin, "r", encoding='utf-8') as f:
        contenu = json.load(f)
    return render_template("index.html", contenu=contenu)




# pas de doublons de app.run
if __name__=="__main__":
    app.run(host="0.0.0.0", port= 9999, debug=True)