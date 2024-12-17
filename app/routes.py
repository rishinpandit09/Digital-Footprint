from flask import Blueprint, render_template, jsonify
from app.utils import categorize_traffic
from app.models import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    """
    Serves the main page, which shows a simple summary of the categorized traffic data.
    """
    traffic_data = categorize_traffic(db.session)
    return render_template('index.html', traffic_data=traffic_data)

@bp.route('/api/traffic_summary')
def traffic_summary():
    """
    Returns the categorized traffic summary as JSON.
    Useful for frontend updates or integrations.
    """
    traffic_data = categorize_traffic(db.session)
    return jsonify(traffic_data)
