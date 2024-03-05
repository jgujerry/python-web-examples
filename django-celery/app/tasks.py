import random
import time
from celery import shared_task


@shared_task(name="run_modeling_job")
def run_modeling_job():
    """Computing task running a long time"""
    t0 = time.time()
    time.sleep(10 * random.random())
    result = random.randint(1000, 10000)
    elapsed_time = time.time() - t0

    return result, elapsed_time
