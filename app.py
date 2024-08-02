from flask import (
    Flask, 
    render_template, 
    request, 
    redirect, 
    url_for
)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from models.records import Student
import os

load_dotenv()

db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_database = os.getenv('DB_DATABASE')
database_url = f'postgresql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_database}'

engine = create_engine(database_url)
Session = sessionmaker(bind=engine)

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/show_all', methods=['POST'])
def show_all():
    try:
        with Session() as session:
            results = session.query(Student).limit(100).all()
    except Exception as e:
        print(f"Error occurred: {e}")
        results = []
    return render_template('results.html', results=results)


@app.route('/filter_by_name', methods=['POST'])
def filter_by_name():
    name = request.form.get('name', '')
    try:
        with Session() as session:
            results = session.query(Student).filter(Student.name.ilike(f'%{name}%')).limit(100).all()
    except Exception as e:
        print(f"Error occurred: {e}")
        results = []
    return render_template('results.html', results=results)


if __name__ == '__main__':
    app.run(debug=True)
