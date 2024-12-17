# Digital Footprint

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)

**Digital Footprint** is a Flask-based web application designed to capture, log, and visualize network traffic in real-time. Leveraging the power of Scapy for packet sniffing and Matplotlib for data visualization, this tool provides insightful summaries of your digital activities through dynamic pie charts. Whether you're monitoring your own network or analyzing traffic for educational purposes, Digital Footprint offers a comprehensive solution for network traffic analysis.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Accessing the Dashboard](#accessing-the-dashboard)
  - [Adding Traffic Logs](#adding-traffic-logs)
- [Project Structure](#project-structure)
- [Permissions and Security](#permissions-and-security)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Real-Time Traffic Capture:** Utilize Scapy to sniff and capture network packets directly from your machine.
- **Automated Logging:** Automatically log captured traffic details into a SQLite database using SQLAlchemy.
- **Dynamic Visualization:** Generate and update pie charts in real-time to represent categorized traffic data.
- **Cache Busting:** Ensure that the latest visualizations are always displayed without browser caching issues.
- **Background Processing:** Run traffic sniffing and monitoring as background threads without blocking the main Flask application.
- **Extensible Architecture:** Easily extendable for additional features like real-time notifications or more complex analytics.

## Prerequisites

Before setting up **Digital Footprint**, ensure you have the following installed on your system:

- **Python 3.8+**
- **pip** (Python package installer)
- **Git** (optional, for cloning the repository)
- **Administrator Privileges** (required for packet capturing)

