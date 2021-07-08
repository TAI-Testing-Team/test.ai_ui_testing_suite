
import logging
 
def run(context):
    context.verify(labels=["btn_label_batch_one"], label_count=0)
    context.verify(labels=["btn_label_batch_two"], label_count=0)
    context.verify(labels=["btn_batch_pink_one"], label_count=0)
    context.verify(labels=["btn_batch_pink_two"], label_count=0)
   