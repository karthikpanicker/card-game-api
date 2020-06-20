import json
import os
import sqlite3

from flask import Flask, redirect, request, url_for, render_template
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import requests

from cardgame.db import init_db_command
from cardgame.user import User

# Naive database setup
try:
    init_db_command()
except sqlite3.OperationalError:
    # Assume it's already been created
    pass



