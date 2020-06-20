from django.shortcuts import render
from django.http import HttpResponse
import psycopg2

# Create your views here.

def init(request):
    response = sql_create_table()
    return HttpResponse(f"<p>{response}</p>")


def sql_create_table():
    sql_qry = """
    CREATE TABLE IF NOT EXISTS ex00_movies (
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


def execute_query(qry):
    conn = psycopg2.connect('dbname=django_tests user=postgres')
    cur = conn.cursor()

    cur.execute(qry)

    conn.commit()
    cur.close()
    conn.close()

