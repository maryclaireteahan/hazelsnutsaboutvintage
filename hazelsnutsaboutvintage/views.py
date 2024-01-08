from django.shortcuts import render


def handler404(request, exception):
    '''
        This function shows a customized 404 error page
    '''
    return render(request, '404.html', status=404)
