from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url_site_1 = request.form['url_site_1']
        url_site_2 = request.form['url_site_2']
        return render_template('resultat_v1.html', url_site_1=url_site_1, url_site_2=url_site_2)
    return render_template('index_v1.html')

if __name__ == '__main__':
    app.run(debug=True)
