class TimeMap:

    def __init__(self):
        self.val = {} #{key, [(timestamp, value)]} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.val:
            self.val[key] = [(timestamp, value)]
        else:
            self.val[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.val:
            return ""
        else:
            retval = ""
            for ts, value in self.val[key]:
                if ts == timestamp:
                    return value
                elif ts < timestamp:
                    retval = value
        return retval