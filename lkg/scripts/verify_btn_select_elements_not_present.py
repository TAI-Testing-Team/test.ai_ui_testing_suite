
import logging
 
def run(context):
    context.verify(labels=["btn_select_visual_only"], label_count=0)
    context.verify(labels=["btn_select_skip_app_installation"], label_count=0)
    