from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import redirect
import time
from django.contrib.auth import authenticate, login, logout

class LogOutMiddleware(MiddlewareMixin):

    def process_request(self, request):
        if request.user.is_authenticated:
            if request.session['last_request']:
                counter = time.time() - request.session['last_request']
                if counter > 60:
                    del request.session['last_request'] 
                    logout(request)  
            request.session['last_request'] = time.time()
        else:
            return
