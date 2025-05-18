from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import subprocess


def editor(request):
    return render(request, 'editor.html')

@csrf_exempt
def run_code(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        user_input = request.POST.get('input', '')
        
        try:
            process = subprocess.Popen(
                ['python', '-c', code],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True
            )
            
            try:
                stdout, stderr = process.communicate(
                    input=user_input,
                    timeout=10
                )
                return JsonResponse({
                    'output': stdout,
                    'error': stderr
                })
            except subprocess.TimeoutExpired:
                process.kill()
                stdout, stderr = process.communicate()
                return JsonResponse({
                    'error': 'Execution timed out',
                    'output': stdout,
                    'error': stderr
                })
            
        except Exception as e:
            return JsonResponse({'error': str(e)})
    
    return JsonResponse({'error': 'Invalid request method'})