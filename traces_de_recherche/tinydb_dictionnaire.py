from tinydb import TinyDB, where, Query

db = TinyDB("data.json", indent=4)
url_site_1 = input("entrez l'url de votre site 👉: ")

# mettre à jour la db
db.update({"status": 404}, where("url") == "loryss.fr")
db.update({"roles": "pythonista"}, where("url") == "loryss.fr")
db.upsert({"url": "benoit.tv", "status": 200, "roles": "pythonista"}, where("url") == "benoit.t")



# ajouter des éléments dans la db
db.insert({"url": f"{url_site_1}", "status": 404})
db.insert_multiple([
    {"url": "youtube.com", "status": 200},
    {"url": "lorys.fr", "status": 200},
    {"url": "facebook.com", "status": 200}
    
])

# chercher des éléments dans la db
User = Query()
log_site_1 = db.search(User.url == url_site_1)
erreur_404 = db.get(User.status != 200)

erreur_404 = db.search(where("status") > 200)


