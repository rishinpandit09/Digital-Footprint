from sqlalchemy.orm import Session
from app.models import TrafficLog

def categorize_traffic(db_session: Session):
    """
    Categorize traffic logs into broad categories based on the protocol field.
    This is a simplified example. In a real scenario, you'd use more complex logic
    (e.g., endpoints, domains, ports, etc.) to categorize network activity.
    """
    categories = {
        'Work-related': 0,
        'Streaming/Entertainment': 0,
        'Other': 0
    }

    all_logs = db_session.query(TrafficLog).all()
    for log in all_logs:
        if log.protocol == 'TCP':
            categories['Work-related'] += 1
        elif log.protocol == 'UDP':
            categories['Streaming/Entertainment'] += 1
        else:
            categories['Other'] += 1

    return categories

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