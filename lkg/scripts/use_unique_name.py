'''
This script uses a variable set by another script in a different test. 
This script uses the generated variable (in this case: a unique test run name) to enter the unique name into an input field.  
'''

import logging
import os
import time
from datetime import datetime

log = logging.getLogger(__name__)

def run(context):
	context.perform_gesture('text_entry_no_submit', 'inp_run_name', grep=os.environ.get("unique_name"))


def element_exists(context, label):
    labels_per_elem = context.find_elements_with_label(label)
    return labels_per_elem and len(labels_per_elem.keys()) > 0	
