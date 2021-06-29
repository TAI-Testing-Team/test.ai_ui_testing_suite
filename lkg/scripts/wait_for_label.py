import logging
import time

def run(context):

    def wait_for_label():
        context.verify(labels=["btn_my_label"])
        context.perform_gesture('tap', 'btn_label_found')


    context.wait(wait_for_label, 5, sleep_in_between=5)    

