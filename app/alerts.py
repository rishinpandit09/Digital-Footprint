# app/alerts.py
import threading
import time
from app.models import db, TrafficLog
from datetime import datetime, timedelta

class ActivityMonitor:
    """
    Monitors activity levels in defined intervals. If the count of logged packets
    is below the threshold, it prints an alert message.
    """

    def __init__(self, app, threshold, interval):
        """
        Initializes the ActivityMonitor.

        :param app: The Flask application instance.
        :param threshold: The minimum number of activities required to avoid an alert.
        :param interval: The time interval (in seconds) between activity checks.
        """
        self.app = app
        self.threshold = threshold
        self.interval = interval
        self.timer = None
        self.running = False

    def start(self):
        """
        Starts the activity monitoring.
        """
        self.running = True
        self._schedule()

    def stop(self):
        """
        Stops the activity monitoring.
        """
        self.running = False
        if self.timer:
            self.timer.cancel()

    def _check_activity(self):
        """
        Checks the recent activity and prints an alert if necessary.
        """
        with self.app.app_context():
            # Calculate the cutoff time for the last interval
            cutoff = datetime.utcnow() - timedelta(seconds=self.interval)
            recent_activity = db.session.query(TrafficLog).filter(TrafficLog.timestamp >= cutoff).count()

            if recent_activity < self.threshold:
                print("ALERT: Low activity detected! Consider pausing surfing.")
            else:
                print("Activity level normal.")

        self._schedule()

    def _schedule(self):
        """
        Schedules the next activity check.
        """
        if self.running:
            # Schedule the next check after `interval` seconds
            self.timer = threading.Timer(self.interval, self._check_activity)
            self.timer.start()
