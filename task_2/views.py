from django.http import JsonResponse


def calculate(request):
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        operation = request.POST.get('operation')

        if not num1 or not num2 or not operation:
            return JsonResponse({'error': 'Invalid parameters'})

        num1 = int(num1)
        num2 = int(num2)

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2
        else:
            return JsonResponse({'error': 'Invalid operation'})

        return JsonResponse({'result': result})

    return JsonResponse({'error': 'Invalid request method'})
