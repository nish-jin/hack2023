import json

class mec_obj:
    def __init__(self, network):
        self.message_cache = dict()
        self.mec_on = False
        self.network = network

    def input_message(self, message):
        #TODO check json name is right
        self.message_cache[message['id']]
        if self.mec_on:
            self.generate_output()
    
    def generate_output(self):
        #TODO calc responses and use self.network.send_message()
        return 0
