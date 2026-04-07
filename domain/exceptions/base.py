from fastapi import status

class DomainException(Exception):
    def __init__(self, message: str):
        self.message = message
        self.status_code = status.HTTP_400_BAD_REQUEST
        super().__init__(self.message)

class NotFoundException(DomainException):
    def __init__(self, entity_name: str):
        self.status_code = status.HTTP_404_NOT_FOUND
        super().__init__(f"{entity_name} not found")

class AlreadyExistsException(DomainException):
    def __init__(self, entity_name: str):
        self.status_code = status.HTTP_409_CONFLICT
        super().__init__(f"{entity_name} already exists")



class UnauthorizedException(DomainException):
    def __init__(self, message: str = "Unauthorized access"):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        super().__init__(message)


class InvalidCredentialsException(DomainException):
    def __init__(self, message: str = "Invalid credentials"):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        super().__init__(message)

class NotHavePermissionException(DomainException):
    def __init__(self, message: str = "You don't have enough permissions"):
        self.status_code = status.HTTP_403_FORBIDDEN
        super().__init__(message)
