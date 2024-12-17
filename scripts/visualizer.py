import logging
import os
import sys

import matplotlib.pyplot as plt
from app import create_app
from app.models import db
from app.utils import categorize_traffic

# Determine the project root directory
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
# Add the project root to sys.path
if project_root not in sys.path:
    sys.path.append(project_root)
# Create the Flask application context for database access
app = create_app()

def create_pie_chart(data, output_file):
    """
    Creates a pie chart image of the traffic categories.
    """
    labels = list(data.keys())
    sizes = list(data.values())

    if sum(sizes) == 0:
        logger.warning("No data to visualize.")
        return

    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title("Digital Footprint Collage")
    plt.savefig(output_file)
    plt.close()
    logger.info(f"Visualization saved to {output_file}")

if __name__ == "__main__":
    with app.app_context():
        logger.info("Categorizing traffic data...")
        data = categorize_traffic(db.session)  # Pass db.session here
        logger.info(f"Traffic data categorized: {data}")
        create_pie_chart(data, 'app/static/footprint_collage.png')