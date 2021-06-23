'''
This script performs a tap gesture on the element label specified if it is found.
This is useful for elements that appear conditionally or only some of the time.
Replace <your_label> below with the label name you gave your element in the test.ai GUI or template matching folder name.
'''

import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture_on_coord('tap', {'x': 775, 'y': 350})
