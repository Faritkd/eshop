from django.http import HttpRequest


def get_client_ip(request: HttpRequest):
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        user_ip = request.META['HTTP_X_FORWARDED_FOR'].split(',')[0]
    else:
        user_ip = request.META.get('REMOTE_ADDR')
    return user_ip
