#This script is to be used to find out the methods of any particular object by running a DIR. 

import logging 
import time 
import pprint

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    #pprint.pprint(dir(driver))
    #pprint.pprint(dir(context))
    element = context.find_element('mnu_select_app')
    context.perform_gesture('text_entry', 'inp_search', '')

    print('============================= output print ==================================')
    print(element)
    print(driver)
    print(context)
    #print(dir(context))
    print('================================ end print ==================================')