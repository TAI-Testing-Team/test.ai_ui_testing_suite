import time
import logging

log = logging.getLogger(__name__)

def run(context):

    driver = context.get_driver()
    context.perform_gesture('tap', 'ddm_select_interaction')
    driver.session.execute_command('ClickCommand', [{'type': 'css', 'value': '#teststep1 > div > div:nth-child(5) > div > div > div.options.collapse.show > div:nth-child(9)'}])
    context.get_all_elements()


    # Successful try to hit an easy button. This taps the Screens tab. 

    #driver.session.execute_command('ClickCommand', [{'type': 'css', 'value':'.css-wu1i9m'}])


    #teststep0 > div > div.clear-top > div > div > div.options.collapse.show > div:nth-child(8)
    #teststep0 > div > div.clear-top > div > div > div.options.collapse.show > div:nth-child(8) > div > span > span
    #teststep0 > div > div.clear-top > div > div > div.options.collapse.show > div:nth-child(1) > div > span
    #teststep0 > div > div.clear-top > div
    #teststep0 > div > div.clear-top > div > div
    #context.perform_gesture('tap', 'ddm_select_interaction')
    #context.perform_gesture('tap', 'ttl_swipe_up')
    #context.perform.gesture('swipe up', '')