import time
import logging

log = logging.getLogger(__name__)

def run(context):

    driver = context.get_driver()
    context.perform_gesture('tap', 'ddm_all_users')
    driver.session.execute_command('ClickCommand', [{'type': 'css', 'value': '#results-options > div:nth-child(2) > form > div:nth-child(1) > div > select > option:nth-child(2)'}])
    context.get_all_elements()



#results-options > div:nth-child(2) > form > div:nth-child(1) > div > select > option:nth-child(2)