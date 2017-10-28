from antminer.constants import RESPONSE_CODES


class APIException(Exception):
    def __init__(self, response, message=None):
        try:
            self.code = int(response['STATUS'][0]['STATUS']['Code'])
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


class WarningResponse(Exception):
    pass


class ErrorResponse(Exception):
    pass

class FatalResponse(Exception):
    pass

class UnknownError(Exception):
    def __init__(self, response):
        self.response = response
