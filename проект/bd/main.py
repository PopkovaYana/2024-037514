from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import MySQLdb.cursors, re, hashlib

app = Flask(__name__)

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'qwer1234'
app.config['MYSQL_DB'] = 'pythonlogin'

mysql = MySQL(app)


@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return redirect(url_for('home'))
        else:
            msg = 'Неверны Имя пользователя/Пароль!'
    return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   
   return redirect(url_for('login'))

@app.route('/home')
def home():
    if 'loggedin' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/profile')
def profile():
    if 'loggedin' in session:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (session['id'],))
        account = cursor.fetchone()
        return render_template('profile.html', account=account)
    return redirect(url_for('login'))


from database import *
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles


Base.metadata.create_all(bind=engine)
 
app = FastAPI()
 

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return FileResponse("html/formForCompanyRegister.html")

@app.get("/index.html")
def root():
    return FileResponse("html/index.html")

@app.get("/form.html")
def root():
    return FileResponse("html/form.html")

@app.get("/home.html")
def root():
    return FileResponse("html/home.html")

@app.get("/home copy.html")
def root():
    return FileResponse("html/home copy.html")

@app.get("/api/users")
def get_people(db: Session = Depends(get_db)):
    filter='Заявкакомпании'
    return db.query(Person).all()
  
@app.get("/api/users/{id}")
def get_person(id, db: Session = Depends(get_db)):

    person = db.query(Person).filter(Person.id == id).first()

    if person==None:  
        return JSONResponse(status_code=404, content={ "message": "Пользователь не найден"})

    return person
  
  
@app.post("/api/users")
def create_person(data  = Body(), db: Session = Depends(get_db)):
    person = Person(name=data["name"], email=data["email"], number=data["number"], prog=data["prog"], comp=data["comp"], date=data["date"], coment=data["coment"])
    db.add(person)
    db.commit()
    db.refresh(person)
    return person
  
@app.put("/api/users")
def edit_person(data  = Body(), db: Session = Depends(get_db)):


    person = db.query(Person).filter(Person.id == data["id"]).first()

    if person == None: 
        return JSONResponse(status_code=404, content={ "message": "Пользователь не найден"})

    person.name = data["name"]
    person.email = data["email"]
    person.number = data["number"]
    person.prog = data["prog"]
    person.comp = data["comp"]
    person.date = data["date"]
    person.coment = data["coment"]
    db.commit()
    db.refresh(person)
    return person
  
  
@app.delete("/api/users/{id}")
def delete_person(id, db: Session = Depends(get_db)):

    person = db.query(Person).filter(Person.id == id).first()
   

    if person == None:
        return JSONResponse( status_code=404, content={ "message": "Пользователь не найден"})
   

    db.delete(person)  
    db.commit()     
    return person




@app.get("/home.html/api/users")
def get_people(db: Session = Depends(get_db)):
    filter='Заявкакомпании'
    return db.query(Person).filter(Person.comp != filter).all()

@app.get("/homeForAdmin.html/api/users")
def get_people(db: Session = Depends(get_db)):
    filter='Заявкакомпании'
    return db.query(Person).filter(Person.comp == filter).all()
  
@app.get("/homeForAdmin.html/api/users/{id}")
def get_person(id, db: Session = Depends(get_db)):

    person = db.query(Person).filter(Person.id == id).first()

    if person==None:  
        return JSONResponse(status_code=404, content={ "message": "Пользователь не найден"})

    return person
  
  
@app.post("/home copy.html/api/users")
def create_person(data  = Body(), db: Session = Depends(get_db)):
    person = Person(name=data["name"], email=data["email"], number=data["number"], prog=data["prog"], comp=data["comp"], date=data["date"], coment=data["coment"])
    db.add(person)
    db.commit()
    db.refresh(person)
    return person
  
@app.put("/home copy.html/api/users")
def edit_person(data  = Body(), db: Session = Depends(get_db)):
   

    person = db.query(Person).filter(Person.id == data["id"]).first()
    if person == None: 
        return JSONResponse(status_code=404, content={ "message": "Пользователь не найден"})

    person.name = data["name"]
    person.email = data["email"]
    person.number = data["number"]
    person.prog = data["prog"]
    person.comp = data["comp"]
    person.date = data["date"]
    person.coment = data["coment"]
    db.commit()
    db.refresh(person)
    return person
  
  
@app.delete("/home copy.html/api/users/{id}")
def delete_person(id, db: Session = Depends(get_db)):

    person = db.query(Person).filter(Person.id == id).first()
   

    if person == None:
        return JSONResponse( status_code=404, content={ "message": "Пользователь не найден"})
   

    db.delete(person)
    db.commit()
    return person