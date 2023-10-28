import json

class mac:
    def __init__(self):
        message_cache = set()
        #TODO make environment class for simulation?

    def input_message(self, message):
        #TODO make car message datatype
        #TODO convert json to message class
        #TODO if set has message with same id, replace - otherwise append
        self.message_cache.append(message)

