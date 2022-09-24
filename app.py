from flask import Flask, render_template, request,redirect,url_for, flash,session

from forms import LoginForm, RegistrationForm
from flask_mysqldb import MySQL
import MySQLdb.cursors


app = Flask(__name__)

app.config['SECRET_KEY'] = '75391'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Siddu@2407'
app.config['MYSQL_DB'] = 'sdp'

db = MySQL(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/aboutus')
def about():
    return render_template("aboutus.html")

@app.route('/profile')
def profile():
    return render_template("profile.html")

@app.route('/ticket')
def ticket():
    return render_template("ticket.html")

@app.route('/booking')
def booking():
    return render_template("booking.html")

@app.route('/checkout')
def checkout():
    return render_template("checkout.html")

@app.route('/cancel')
def cancel():
    return render_template("cancel.html")

@app.route('/login/',methods=['GET','POST'])
def login():
    form = LoginForm(request.form)
    if form.validate() and request.method == 'POST':
        username = request.form.get('username')
        password = request.form['password']
        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM REGISTER WHERE username=%s and password = %s', (username,password,))
        account = cursor.fetchone()
        if account:
            session['loged_in'] = True
            session['user'] = username
            return redirect(url_for('index'))
        else:
            flash('Invalid Credentials! Username or Password incorrect')

    return render_template('login.html', form = form)

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm(request.form)
    if form.validate() and request.method == 'POST':
        username = request.form.get('username')
        password = request.form['password']
        email = request.form.get('email')
        phoneno = request.form.get('phoneno')
        address = request.form.get('address')

        cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM REGISTER WHERE username=%s',(username,))
        account = cursor.fetchone()
        if not account:
            cursor.execute('INSERT INTO REGISTER VALUES(NULL,%s,%s,%s,%s,%s)',
                           (username,password,email,phoneno,address,))
            db.connection.commit()
            return redirect(url_for('login'))
        else:
            flash('User already Existed!, Try another username')

    return render_template('register.html', form = form)

@app.route('/logout')
def logout():
    session.pop('loged_in',None)
    session.pop('user',None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)