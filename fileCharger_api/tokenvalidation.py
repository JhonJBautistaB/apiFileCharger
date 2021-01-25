from functools import wraps
from json import loads

from fileCharger_api import models

def check_token(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
                
        token = request.headers['Authorization'].lstrip('Bearer')
        token = token.lstrip()
        
        # Validation if empy Token
        if not token:
            # Message Error
            response = loads({
                "status": "FORBIDDEN", "code": 403, "message": "YOU NEED TO LOGIN TO ENTER SYSTEM"})
            response.status_code = 403
            return response
        
        try:
            # Decode Token
            token_verify = jwt.decode(token, Config.SECRET_KEY)
            # Extract parameters
            email = token_verify['email']
            # Verify if email exist
            verify_user = models.Client.objects.get(email=email)
            # Validate that the email sent by token exists in DB
            if verify_user is None:
                response = loads({"status": "FORBIDDEN", "code": 403, "message": "YOUR TOKEN IS NOT VALID"})
                response.status_code = 403
                return response
        # Exception when token time expired
        except jwt.exceptions.ExpiredSignatureError:
            response = loads({"status": "FORBIDDEN", "code": 403, 'message': 'YOUR SESSION HAS EXPIRED, RESTART SESSION OR LOGIN'})
            response.status = 403
            return response
        # Exception when the token does not meet specificity
        except jwt.exceptions.InvalidSignatureError:
            response = loads({"status": "FORBIDDEN", "code": 403,'message': 'YOUR SESSION IS NOT VALID'})
            response.status_code = 403
            return response
        
        return func(*args, **kwargs)
    return wrapped