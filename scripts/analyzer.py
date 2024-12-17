from app.models import db
from app.utils import categorize_traffic
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Simple analyzer that prints a summary of the categorized traffic
    with app.app_context():
        summary = categorize_traffic(db)
        print("Traffic Summary:", summary)
