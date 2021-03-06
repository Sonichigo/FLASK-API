from flask import Flask, render_template, Request
from flask_mysqldb import MySQL
import yaml as yaml

app = Flask(__name__)
db=yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] =db['mysql_host']
app.config['MYSQL_USER'] =db['mysql_user']
app.config['MYSQL_PASSWORD'] =db['mysql_password']
app.config['MYSQL_DB'] =db['mysql_db']

mysql = MySQL(app)
@app.route('/', methods=['GET','POST' ])
def index():
    if Request.method=='POST':
        userDetails = Request.form
        name = userDetails['name']
        email = userDetails['email']
        cur =mysql.connection.cursor()
        cur.execute("INSERT INTO users(name,email) VALUES(%s,%s)",(name,email))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

    Name
    EMAIL
    NUMBER