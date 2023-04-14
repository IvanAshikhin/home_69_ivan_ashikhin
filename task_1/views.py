import json

from django.http import JsonResponse, HttpResponseBadRequest


def get_numbers(data):
    try:
        a = int(data.get('A'))
        b = int(data.get('B'))
    except (ValueError, TypeError):
        return None
    return a, b


def check_numbers(numbers):
    if None in numbers:
        return HttpResponseBadRequest('Invalid or missing numbers')
    return None


def add(request):
    data = json.loads(request.body)
    numbers = get_numbers(data)
    error = check_numbers(numbers)
    if error:
        return error
    result = numbers[0] + numbers[1]
    return JsonResponse({'answer': result})


def subtract(request):
    data = json.loads(request.body)
    numbers = get_numbers(data)
    error = check_numbers(numbers)
    if error:
        return error
    result = numbers[0] - numbers[1]
    return JsonResponse({'answer': result})


def multiply(request):
    data = json.loads(request.body)
    numbers = get_numbers(data)
    error = check_numbers(numbers)
    if error:
        return error
    result = numbers[0] * numbers[1]
    return JsonResponse({'answer': result})


def divide(request):
    data = json.loads(request.body)
    numbers = get_numbers(data)
    error = check_numbers(numbers)
    if error:
        return error
    if numbers[1] == 0:
        return HttpResponseBadRequest('Cannot divide by zero')
    result = numbers[0] / numbers[1]
    return JsonResponse({'answer': result})

