class LogCounter:
    def __init__(self, logs):
        self._logs = logs

    def count_error(self):
        return len([ log for log in self._logs if log.is_error() ])

    def group_by_user(self):
        result = {}
        for log in self._logs:
            user = log.user or 'guest'
            result.setdefault(user, [])
            result[user].append(log)
        return result
