import time

from django.http.response import JsonResponse
from django.shortcuts import render

from app.tasks import run_modeling_job

# Create your views here.

def index(request, *args, **kwargs):
    context = {}
    return render(request, "index.html", context=context)


def sync_run_modeling_job(request):
    """Long computing task"""
    # Run computing
    result, elapsed_time = run_modeling_job()

    # Return response
    data = {
        'result': result,
        'elasped_time': round(elapsed_time, 3)
    }
    return JsonResponse(data)


def async_run_modeling_job(request):
    """Asynchronous long computing task"""
    # Run computing asynchronously
    t0 = time.time()
    async_result = run_modeling_job.delay()
    elapsed_time = round(time.time() - t0, 3)
    
    # Return response
    data = {
        'result': async_result.id,
        'elasped_time': elapsed_time
    }

    return JsonResponse(data)
