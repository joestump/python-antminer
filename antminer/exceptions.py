from antminer.constants import RESPONSE_CODES


class APIException(Exception):
    def __init__(self, response, message=None):
        try:
            self.code = int(response['STATUS'][0]['Code'])
        except KeyError, IndexError:
            self.code = 0

        self.message = message
        self.response = response

    @property
    def reason(self):
        try:
            return RESPONSE_CODES[self.code]
        except KeyError:
            return 'UNKNOWN'

    def __repr__(self):
        return "{message} (#{code}: #{reason})".format(message=self.message,
            code=self.code, reason=self.reason)


class WarningResponse(APIException):
    pass


class ErrorResponse(APIException):
    pass

class FatalResponse(APIException):
    pass

class UnknownError(APIException):
    pass
