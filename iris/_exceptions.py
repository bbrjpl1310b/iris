class IrisApiException(Exception):
    pass


class FailedRequestException(IrisApiException):
    pass


class HttpUnsuccessfullStatusException(IrisApiException):
    pass


class ExpiredTokenException(IrisApiException):
    pass


class WrongPINException(IrisApiException):
    pass


class WrongTokenException(IrisApiException):
    pass


class UsedTokenException(IrisApiException):
    pass


class InvalidHeaderException(IrisApiException):
    pass


class MissingHeaderException(IrisApiException):
    pass


class InvalidBodyModelException(IrisApiException):
    pass


class InvalidSignatureException(IrisApiException):
    pass


class CertificateNotFoundException(IrisApiException):
    pass


class EntityNotFoundException(IrisApiException):
    pass


class ConstraintViolationException(IrisApiException):
    pass


class InvalidParameterValueException(IrisApiException):
    pass


class MissingUnitSymbolException(IrisApiException):
    pass


class InternalServerErrorException(IrisApiException):
    pass


class ResponseInvalidContentTypeException(IrisApiException):
    pass
