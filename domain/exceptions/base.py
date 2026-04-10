from fastapi import status

class DomainException(Exception):
    def __init__(self, message: str, status_code: int = status.HTTP_400_BAD_REQUEST):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)

class NotFoundException(DomainException):
    def __init__(self, entity_name: str):
        super().__init__(f"{entity_name} not found", status.HTTP_404_NOT_FOUND)

class AlreadyExistsException(DomainException):
    def __init__(self, entity_name: str):
        super().__init__(f"{entity_name} already exists", status.HTTP_409_CONFLICT)

class AlreadyDeletedException(DomainException):
    def __init__(self, entity_name: str):
        super().__init__(f"{entity_name} already deleted", status.HTTP_400_BAD_REQUEST)



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
