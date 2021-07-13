''' This script creates a unique name each time the test runs by adding a date and time stamp to the end of the existing text that is entered'''

import logging
import os
import time
from datetime import datetime

log = logging.getLogger(__name__)


# Generate a datetime string to use as a unique prefix or suffix
timestamp = datetime.now().strftime("%m/%d/%Y-%H:%M:%S")

# Generate the complete unique name and store it in a variable
os.environ[("unique_name")] = "Test Run " + timestamp

# Verify the above code
os.environ.get("unique_name")

def run(context):
    context.perform_gesture('text_entry', 'inp_run_name', grep=os.environ.get("unique_name"))