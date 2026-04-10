from fastapi import status
from domain.exceptions.base import NotFoundException, AlreadyExistsException, UnauthorizedException, InvalidCredentialsException, NotHavePermissionException, DomainException, AlreadyDeletedException

class UserNotFoundException(NotFoundException):
    def __init__(self):
        super().__init__("User")

class UserAlreadyExistsException(AlreadyExistsException):
    def __init__(self):
        super().__init__("User")

class UserNotHavePermissionException(NotHavePermissionException):
    def __init__(self, message: str = "You don't have enough permissions"):
        super().__init__(message)

class UserUnauthorizedException(UnauthorizedException):
    def __init__(self, message: str = "Unauthorized access"):
        super().__init__(message)

class UserInvalidCredentialsException(InvalidCredentialsException):
    def __init__(self, message: str = "Invalid credentials"):
        super().__init__(message)

class UserNotActiveException(DomainException):
    def __init__(self, message: str = "User is not active"):
        super().__init__(message)

class UserAlreadyDeletedException(AlreadyDeletedException):
    def __init__(self):
        super().__init__("User")
