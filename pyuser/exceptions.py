class AuthException(Exception):
    
    def __init__(self, message):
        self.message = message


class EmailInUse(AuthException):

    def __init__(self, message):
        super().__init__(message)


class InvalidEmail(AuthException):
    
    def __init__(self, message):
        super().__init__(message)


class InvalidPassword(AuthException):

    def __init__(self, message):
        super().__init__(message)


class AccountLocked(AuthException):

    def __init__(self, message):
        super().__init__(message)