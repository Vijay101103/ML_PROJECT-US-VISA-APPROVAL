import logging
import os
from datetime import datetime

# Function to get the project root directory (assuming this script is run from the project root)
def get_project_root():
    return os.path.dirname(os.path.abspath(__file__))

# Generate log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the log directory path
log_dir = 'logs'

# Construct the full logs path using the project root directory
logs_path = os.path.join(get_project_root(), log_dir)

# Ensure that the log directory exists
os.makedirs(logs_path, exist_ok=True)

# Full path to the log file
log_file_path = os.path.join(logs_path, LOG_FILE)

# Configure logging to write to the file
logging.basicConfig(
    filename=log_file_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

# Example logging
logging.info("Logging setup is complete.")
