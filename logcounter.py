class LogCounter:
    def __init__(self, logs):
        self._logs = logs

    def count_error(self):
        return len([ log for log in self._logs if log.is_error() ])
