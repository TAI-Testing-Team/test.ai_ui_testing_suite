import time
import logging

log = logging.getLogger(__name__)

def run(context):

    context.perform_gesture('tap', 'btn_label_tab_live')
    context.get_all_elements()
    context.perform_gesture('text entry','inp_label_name', 'tab_live')
    context.get_all_elements()