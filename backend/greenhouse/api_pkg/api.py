"""
api.py
- provides the API endpoints for consuming and producing 
  REST requests and responses
"""

from datetime import datetime, timedelta
from flask import Blueprint, jsonify, request, current_app
from greenhouse.consumers.weatherstatus import just_fetch_weatherdata

api = Blueprint('api', __name__)

@api.route('/get_current_weather/')
def get_current_weather():
    print("got here")
    response = just_fetch_weatherdata()
    return jsonify(response)