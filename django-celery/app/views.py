import json
import time

from django.http.response import JsonResponse
from django.shortcuts import render
from django_celery_results.models import TaskResult

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
        'elapsed_time': round(elapsed_time, 3)
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
        'elapsed_time': elapsed_time
    }

    return JsonResponse(data)


def show_async_job_result(request):
    """Show async job result"""
    task_id = request.GET.get('task_id', None)
    try:
        task = TaskResult.objects.get(task_id=task_id)
    except TaskResult.DoesNotExist:
        task = None
    
    if not task:
        return JsonResponse({})
    
    result_data = json.loads(task.result)
    data = {
        "result": result_data[0],
        "elapsed_time": result_data[1]
    }
    
    return JsonResponse(data)
