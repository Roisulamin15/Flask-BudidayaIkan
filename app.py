from flask import Flask, render_template, request, redirect, url_for, session
import pymysql

app = Flask(__name__)
app.secret_key = 'ikan'  # Kunci rahasia untuk session
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ikan'

# Halaman Utama
@app.route("/")
def index():
    return render_template("index.html")

# Halaman Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Membuat koneksi ke database menggunakan PyMySQL
        connection = pymysql.connect(
            host=app.config['MYSQL_HOST'],
            user=app.config['MYSQL_USER'],
            password=app.config['MYSQL_PASSWORD'],
            database=app.config['MYSQL_DB'],
            cursorclass=pymysql.cursors.DictCursor
        )

        try:
            with connection.cursor() as cursor:
                # Query untuk mengambil data user dari database berdasarkan username dan password
                cursor.execute("SELECT * FROM admin WHERE username = %s AND password = %s", (username, password))
                user = cursor.fetchone()

                if user:
                    session['logged_in'] = True  # Tandai user sebagai sudah login
                    return redirect(url_for('edit_dokumentasi'))
                else:
                    return 'Login failed, please check your username and password'

        except Exception as e:
            return f"An error occurred: {e}"
        finally:
            connection.close()  # Pastikan koneksi ditutup

    return render_template('admin/login.html')  # Pastikan path benar

# Halaman Edit Dokumentasi
@app.route('/editdokumentasi', methods=['GET', 'POST'])
def edit_dokumentasi():
    if 'logged_in' not in session:
        return redirect(url_for('login'))  # Arahkan ke login jika belum login

    return render_template('admin/edit_dokumentasi.html')

if __name__ == '__main__':
    app.run(debug=True)
