class fiveG_Network:
    '''Simulates a 5g network for the cars and MEC to be placed into.'''

    def __init__(self):
        self.edge_list = dict()

    def ping(self, id, obj):
        '''Adds a given object to the 'connected devices' list.
        ID simulates an ip address.'''
        self.edge_list[id] = obj

    def broadcast(self, message):
        self.send_message('mec')

    def __publish_event(self, update):
        #some weird variable pushing thing with inheritance?
        return 0

    def send_message(self, message, dest_id):
        if dest_id in self.edge_list:
            (self.edge_list[dest_id]).input_message(message)
            return True #msg sent
        else:
            return False #msg destination missing