import time
import logging

log = logging.getLogger(__name__)

def run(context):

    context.perform_gesture('tap', 'inp_description')
    context.perform_gesture('swipe_down','')
    context.get_all_elements()