from playerclass import Player
from teamclass import Team
from flask import Flask, render_template, g, request, session, url_for, redirect
import sqlite3
import requests

app = Flask(__name__)
app.config["SECRET_KEY"] = "BA35!"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/wiki/<string:subject>")
def wiki(subject):
    session["subject"] = subject
    return render_template("wiki.html", subject=subject)

@app.route("/user/<string:team>", methods=["GET", "POST"])
def teampage(team):
    session["team"] = team
    return render_template("teampage.html", teampage=teampage)