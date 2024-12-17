from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class TrafficLog(db.Model):
    __tablename__ = 'traffic_logs'

    id = db.Column(db.Integer, primary_key=True)
    src_ip = db.Column(db.String(45), nullable=False)
    dst_ip = db.Column(db.String(45), nullable=False)
    protocol = db.Column(db.String(10), nullable=False)
    length = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<TrafficLog {self.src_ip} -> {self.dst_ip} [{self.protocol}]>"