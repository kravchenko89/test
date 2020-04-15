import json
import time
from datetime import datetime


class SaveRequest(object):
    def __init__(self, response):
        self.response = response

    def __call__(self, request):
        request.start_time = time.time()
        response = self.response(request)
        time_full = (time.time() - request.start_time).__round__(3)

        with open('logs.json', mode='a', encoding='utf-8') as logs:
            json.dump({'info': [{'path': request.path,
                                 'execution_time': time_full,
                                 'data': str(datetime.now())}]},
                      logs,  ensure_ascii=True, indent=2)
            logs.write(',')

        return response
