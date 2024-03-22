from tinydb import TinyDB, where, Query
import datetime, time, requests

db = TinyDB("data.json", indent=4)
def check():
    # definition des variables
    url_site_1 = "http://" + input_url_site_1
    url_site_2 = "http://" + input_url_site_2
    status_site_1 = requests.get(url_site_1)
    status_site_2 = requests.get(url_site_2)
    list_request_not_200 = []
    
    temps = (datetime.datetime.now()).strftime('%H:%M:%S')

    db.upsert({"url": f"{url_site_1}", "status": f"{status_site_1.status_code}", "time_test": f"{temps}"}, where("url") == f"{url_site_1}")
    db.upsert({"url": f"{url_site_2}", "status": f"{status_site_2.status_code}", "time_test": f"{temps}"}, where("url") == f"{url_site_2}")

    User = Query()
    list_request_not_200 = db.get(User.status != 200)
    # print(list_request_not_200)
    record_1 = db.get(doc_id=1)
    if record_1:
        print("Record 1:")
        print(record_1)
    # list_request_not_200.append((str(request_not_200.get("url")) + str(request_not_200.get("status")) + str(request_not_200.get("time_test"))))
    

#     db.insert_multiple([
#     {"url": f"{url_site_1}", "status": f"{status_site_1}", "time_test": f"{temps.strftime('%H:%M:%S')}"},
#     {"url": f"{url_site_2}", "status": f"{status_site_2}", "time_test": f"{temps.strftime('%H:%M:%S')}"}
# ])
check()
# User = Query()
# log_site_1 = db.search(User.url == url_site_1)
# erreur_404 = db.get(User.status > 200)

# erreur_404 = db.search(where("status") > 200)
# # ajouter des éléments dans la db
# db.insert({"url": f"{url_site_1}", "status": 404})
# db.insert_multiple([
#     {"url": "youtube.com", "status": 200},
#     {"url": "lorys.fr", "status": 200},
#     {"url": "facebook.com", "status": 200}
    
# ])

# chercher des éléments dans la db



