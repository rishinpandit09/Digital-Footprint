import sys
import os
from scapy.all import sniff, IP, TCP, UDP
from app.models import db, TrafficLog
from app import create_app

# Determine the project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add the project root to sys.path
if project_root not in sys.path:
    sys.path.append(project_root)

# Create the Flask application context for database access
app = create_app()

def packet_callback(packet):
    """
    Callback function executed for each captured packet.
    It extracts IP and protocol data and stores it in the database.
    """
    if IP in packet:
        if TCP in packet:
            protocol_name = 'TCP'
        elif UDP in packet:
            protocol_name = 'UDP'
        else:
            protocol_name = 'Other'

        with app.app_context():
            new_log = TrafficLog(
                src_ip=packet[IP].src,
                dst_ip=packet[IP].dst,
                protocol=protocol_name,
                length=len(packet)
            )
            db.session.add(new_log)
            db.session.commit()

if __name__ == "__main__":
    print("Starting network traffic capture (may require sudo on Linux).")
    # You can customize the sniff interface or filter as needed:
    # For example: sniff(iface="eth0", prn=packet_callback, store=False)
    sniff(prn=packet_callback, store=False)
