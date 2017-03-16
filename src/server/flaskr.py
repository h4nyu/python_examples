#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sqlite3
from flask import Flask
from flask import request
from flask import session
from flask import g
from flask import redirect
from flask import url_for
from flask import abort
from flask import render_template
from flask import flash


app = Flask(__name__)  # create the application instance

app.config.from_object(__name__)  # load config from this file, flaskr.py

app.config.update(
    dict(
        SECRET_KEY='development key',
        USERNAME='admin',
        PASSWORD='defualt'
    )
)
app.config.from_envvar('FLASKR_SETTINGS')
