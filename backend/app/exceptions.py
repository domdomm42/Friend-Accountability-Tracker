class InvalidInputException(Exception):
    def __init__(self, message: str):
        self.message = message
        self.code = 400

    def __str__(self):
        return f"Friendo - Code: {self.code}, Message: {self.message}"


class NotUniqueException(Exception):
    def __init__(self, message: str):
        self.message = message
        self.code = 409

    def __str__(self):
        return f"Friendo - Code: {self.code}, Message: {self.message}"


class InvalidRequestException(Exception):
    def __init__(self, message: str):
        self.message = message
        self.code = 400

    def __str__(self):
        return f"Friendo - Code: {self.code}, Message: {self.message}"


class InsuficientFundsException(Exception):
    def __init__(self, message: str):
        self.message = message
        self.code = 402

    def __str__(self):
        return f"Friendo - Code: {self.code}, Message: {self.message}"


class ForbiddenAccessException(Exception):
    def __init__(self, message: str):
        self.message = message
        self.code = 403

    def __str__(self):
        return f"Friendo - Code: {self.code}, Message: {self.message}"


class ForbiddenActionException(Exception):
    def __init__(self, message: str):
        self.message = message
        self.code = 403

    def __str__(self):
        return f"Friendo - Code: {self.code}, Message: {self.message}"


class BadGatewayException(Exception):
    def __init__(self, message: str = "Unable to connect to the database. Please try again later."):
        self.message = message
        self.code = 502

    def __str__(self):
        return f"Friendo - Code: {self.code}, Message: {self.message}"


class NotFoundException(Exception):
    def __init__(self, message: str):
        self.message = message
        self.code = 400

    def __str__(self):
        return f"Friendo - Code: {self.code}, Message: {self.message}"


class InternalServerError(Exception):
    def __init__(self, message: str):
        self.message = message
        self.code = 500

    def __str__(self):
        return f"Friendo - Code: {self.code}, Message: {self.message}"