import os

class Config:
    """
    Configuration class for the Flask app and related components.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY', 'devkey')  # For session security
    # SQLite database file stored in the local directory
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///traffic_data.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Threshold and interval for activity monitoring (in seconds)
    ACTIVITY_THRESHOLD = 5     # Minimum number of requests in the interval
    CHECK_INTERVAL = 60        # Interval in seconds to check activity levels
