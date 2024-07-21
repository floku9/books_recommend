from aiohttp.web_exceptions import HTTPUnauthorized, HTTPPaymentRequired, HTTPTooManyRequests


class HTTPExceptionsFactory:
    @classmethod
    def raise_exception(cls, status_code: int, reason: str):
        match status_code:
            case 401:
                raise HTTPUnauthorized(reason=reason)
            case 402:
                raise HTTPPaymentRequired(reason=reason)
            case 429:
                raise HTTPTooManyRequests(reason=reason)
            case _:
                raise Exception(reason)