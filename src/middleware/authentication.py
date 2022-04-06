from werkzeug import Response


# from config import config


class Authentication:
    def __init__(self, app):
        self.app = app
        # self.secret_key = config['apiKey']
        self.secret_key = '123abc'

    def __call__(self, start_request, start_response):
        '''
        Takes a incoming request to check for secret api key
        :param start_request:
        :param start_response:
        :return:
        '''
        try:
            secret_key = start_request.get("HTTP_X_API_KEY")
            if not secret_key or secret_key != self.secret_key:
                res = Response("Not Authorized", mimetype="text/plain", status=401)
                return res(start_request, start_response)

        except Exception as ex:
            res = Response("Not Authorized", mimetype="text/plain", status=401)
            return res(start_request, start_response)

        return self.app(start_request, start_response)
