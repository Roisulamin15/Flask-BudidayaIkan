from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/Downloadaplikasi')
def Download_aplikasi():
    return render_template('Downloadaplikasi.html')

@app.route('/Tanyakansesuatu')
def tanyakan_sesuatu():
	return render_template('Tanyakansesuatu.html')

if __name__ == '__main__':
	app.run(debug=True)