import click
from mongoengine import *
from flask.cli import with_appcontext
from flask import g

from repository.models import Cards, Users

cards = [
    {"name": "corazón", "type" : "organ", "color" : "red"},
    {"name": "corazón", "type" : "organ", "color" : "red"},
    {"name": "corazón", "type" : "organ", "color" : "red"},
    {"name": "corazón", "type" : "organ", "color" : "red"},
    {"name": "corazón", "type" : "organ", "color" : "red"},
 
    {"name" : "estómago", "type" : "organ", "color" : "green"},
    {"name" : "estómago", "type" : "organ", "color" : "green"},
    {"name" : "estómago", "type" : "organ", "color" : "green"},
    {"name" : "estómago", "type" : "organ", "color" : "green"},
    {"name" : "estómago", "type" : "organ", "color" : "green"},
    
    {"name" : "cerebro", "type" : "organ", "color" : "blue"},
    {"name" : "cerebro", "type" : "organ", "color" : "blue"},
    {"name" : "cerebro", "type" : "organ", "color" : "blue"},
    {"name" : "cerebro", "type" : "organ", "color" : "blue"},
    {"name" : "cerebro", "type" : "organ", "color" : "blue"},
    
    {"name" : "hueso", "type" : "organ", "color" : "yellow"},
    {"name" : "hueso", "type" : "organ", "color" : "yellow"},
    {"name" : "hueso", "type" : "organ", "color" : "yellow"},
    {"name" : "hueso", "type" : "organ", "color" : "yellow"},
    {"name" : "hueso", "type" : "organ", "color" : "yellow"},
    
    {"name" : "comodín", "type" : "organ", "color" : "multicolor"},
    
    {"name" : "virus de corazón", "type" : "virus", "color" : "red"},
    {"name" : "virus de corazón", "type" : "virus", "color" : "red"},
    {"name" : "virus de corazón", "type" : "virus", "color" : "red"},
    {"name" : "virus de corazón", "type" : "virus", "color" : "red"},
 
    {"name" : "virus de estómago", "type" : "virus", "color" : "green"},
    {"name" : "virus de estómago", "type" : "virus", "color" : "green"},
    {"name" : "virus de estómago", "type" : "virus", "color" : "green"},
    {"name" : "virus de estómago", "type" : "virus", "color" : "green"},
    
    {"name": "virus de cerebro", "type" : "virus", "color" : "blue"},
    {"name": "virus de cerebro", "type" : "virus", "color" : "blue"},
    {"name": "virus de cerebro", "type" : "virus", "color" : "blue"},
    {"name": "virus de cerebro", "type" : "virus", "color" : "blue"},
    
    {"name" : "virus de hueso", "type" : "virus", "color" : "yellow"},
    {"name" : "virus de hueso", "type" : "virus", "color" : "yellow"},
    {"name" : "virus de hueso", "type" : "virus", "color" : "yellow"},
    {"name" : "virus de hueso", "type" : "virus", "color" : "yellow"},
    
    {"name" : "virus comodín", "type" : "virus", "color" : "multicolor"},
    
    {"name" : "medicamento de corazón", "type" : "medicine", "color" : "red"},
    {"name" : "medicamento de corazón", "type" : "medicine", "color" : "red"},
    {"name" : "medicamento de corazón", "type" : "medicine", "color" : "red"},
    {"name" : "medicamento de corazón", "type" : "medicine", "color" : "red"},
    
    {"name" : "medicamento de estómago", "type" : "medicine", "color" : "green"},
    {"name" : "medicamento de estómago", "type" : "medicine", "color" : "green"},
    {"name" : "medicamento de estómago", "type" : "medicine", "color" : "green"},
    {"name" : "medicamento de estómago", "type" : "medicine", "color" : "green"},
    
    {"name" : "medicamento de cerebro", "type" : "medicine", "color" : "blue"},
    {"name" : "medicamento de cerebro", "type" : "medicine", "color" : "blue"},
    {"name" : "medicamento de cerebro", "type" : "medicine", "color" : "blue"},
    {"name" : "medicamento de cerebro", "type" : "medicine", "color" : "blue"},
    
    {"name" : "medicamento de hueso", "type" : "medicine", "color" : "yellow"},
    {"name" : "medicamento de hueso", "type" : "medicine", "color" : "yellow"},
    {"name" : "medicamento de hueso", "type" : "medicine", "color" : "yellow"},
    {"name" : "medicamento de hueso", "type" : "medicine", "color" : "yellow"},
    
    {"name" : "medicamento comodín", "type" : "medicine", "color" : "multicolor"},
    {"name" : "medicamento comodín", "type" : "medicine", "color" : "multicolor"},
    {"name" : "medicamento comodín", "type" : "medicine", "color" : "multicolor"},
    {"name" : "medicamento comodín", "type" : "medicine", "color" : "multicolor"},
    
    {"name" : "contagio", "type" : "medicine", "color" : "contagion"},
    {"name" : "contagio", "type" : "medicine", "color" : "contagion"},
    
    {"name" : "robo", "type" : "medicine", "color" : "stole"},
    {"name" : "robo", "type" : "medicine", "color" : "stole"},
    {"name" : "robo", "type" : "medicine", "color" : "stole"},
    
    {"name" : "intercambio", "type" : "medicine", "color" : "exchange"},
    {"name" : "intercambio", "type" : "medicine", "color" : "exchange"},
    {"name" : "intercambio", "type" : "medicine", "color" : "exchange"},
    
    {"name" : "guante de látex", "type" : "medicine", "color" : "discard"},
    
    {"name" : "cambio de cuerpo", "type" : "medicine", "color" : "body_change"}
]

def get_db(db_name, host_url):
    '''
    Se conecta a una base de datos y la devuelve al objeto grlobal g de Flask
    '''
    if "db" not in g:
        g.db = connect(
            db=db_name,
            host=host_url,
        )
        g.Cards = Cards
        g.Users = Users
    return g.db

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db(db_name, host_url):
    db = get_db(db_name, host_url)
    for card in cards:
        print(card)
        Cards(
            name=card["name"], type=card["type"], color=card["color"]
        ).save()

@click.command("init-db")
@click.argument('db', nargs=1)
@click.argument('host', nargs=-1)
@with_appcontext
def init_db_command(db, host):
    db_name = db
    host_url = host
    init_db(db_name, host_url)
    click.echo("Data Base initialized")


def init_app(app, db_name, host_url):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
