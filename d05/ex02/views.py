from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

# Create your views here.

def init(request):
    response = sql_create_table()
    return HttpResponse(f"<p>{response}</p>")

def populate(request):
    response = sql_populate_table()
    return HttpResponse(f"<p>{response}</p>")

def display(request):
    movies = sql_fetch_movies()
    template = 'ex02/display.html'
    print(movies)
    return render(request, template, {'movies': movies})


def sql_create_table():
    sql_qry = """
    CREATE TABLE IF NOT EXISTS ex02_movies (
        title           VARCHAR(64) NOT NULL UNIQUE,
        episode_nb      INTEGER PRIMARY KEY,
        opening_crawl   TEXT,
        director        VARCHAR(32) NOT NULL,
        producer        VARCHAR(128) NOT NULL,
        release_date    DATE NOT NULL
    )
    """
    try:
        execute_query(sql_qry)
        return "OK"
    except psycopg2.Error as err:
        return str(err.pgerror)

def sql_populate_table():
    sql_qry = """
    INSERT INTO ex02_movies (title, episode_nb, director, producer, release_date) VALUES
        ('The Phantom Menace', 1 , 'George Lucas', 'Rick McCallum', '1999-05-19'),
        ('Attack of the Clones', 2, 'George Lucas', 'Rick McCallum', '2002-05-16'),
        ('Revenge of the Sith', 3, 'George Lucas', 'Rick McCallum', '2005-05-19'),
        ('A New Hope', 4, 'George Lucas', 'Gary Kurtz, Rick McCallum', '1977-05-25'),
        ('The Empire Strikes Back', 5, 'Irvin Kershner', 'Gary Kurtz, Rick McCallum', '1980-05-17'),
        ('Return of the Jedi', 6, 'Richard Marquand', 'Howard G. Kazanjian, George Lucas, Rick McCallum', '1983-05-25'),
        ('The Force Awakens', 7, 'J. J. Abrams', 'Kathleen Kennedy, J. J. Abrams, Bryan Burk', '2015-12-11');   
    """
    try:
        execute_query(sql_qry)
        return "OK"
    except psycopg2.Error as err:
        return str(err.pgerror)

def sql_fetch_movies():
    sql_qry = """
    SELECT * from ex02_movies;
    """

    try:
        return fetch_query(sql_qry)
    except psycopg2.Error:
        return None

def fetch_query(qry):
    conn = psycopg2.connect('dbname=django_tests user=postgres')
    cur = conn.cursor()
    cur.execute(qry)
    res = cur.fetchall()

    cur.close()
    conn.close()
    return res


def execute_query(qry):
    conn = psycopg2.connect('dbname=django_tests user=postgres')
    cur = conn.cursor()

    cur.execute(qry)

    conn.commit()
    cur.close()
    conn.close()

