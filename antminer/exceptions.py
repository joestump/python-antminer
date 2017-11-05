from antminer.constants import RESPONSE_CODES


def raise_exception(response, message=None):
    try:
        raise STATUS_CODE_TO_EXCEPTION[response['STATUS'][0]['STATUS']](response, message)
    except KeyError, IndexError:
        raise UnknownError(response)


class APIException(Exception):
    def __init__(self, response, message=None):
        try:
            self.code = int(response['STATUS'][0]['Code'])
        except:
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


# Maps the basic warning codes returned from the API to
# our Exceoption classes.
STATUS_CODE_TO_EXCEPTION = {
    'W': WarningResponse,
    'E': ErrorResponse,
    'F': FatalResponse
}



