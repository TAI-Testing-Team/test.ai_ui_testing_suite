import logging
import time

def run(context):

    def wait_for_job_to_complete():
        context.verify(labels=["btn_screens"], label_count=1)

    context.wait(wait_for_job_to_complete, 40, sleep_in_between=10)    

