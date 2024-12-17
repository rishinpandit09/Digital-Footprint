import logging

from flask import Flask

from app.alerts import ActivityMonitor
from app.config import Config
from app.models import db
from app.routes import bp

def create_app():
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)
    # Load configuration from app.config.Config
    app.config.from_object(Config)

    # Initialize SQLAlchemy with the Flask app
    db.init_app(app)
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting Flask application...")
    with app.app_context():
        # Create database tables if they don't exist
        db.create_all()

    # Register blueprint for routes
    app.register_blueprint(bp)
    # Initialize and start the ActivityMonitor
    """
        Start the activity monitor once the app is running.
        This schedules periodic checks of the activity level.
        """
    threshold = 10  # Example threshold
    interval = 60  # Example interval in seconds
    monitor = ActivityMonitor(app, threshold, interval)
    monitor.start()
    logging.info("ActivityMonitor started.")

    return app
