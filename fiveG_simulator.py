class fiveG_Network:
    '''Simulates a 5g network for the cars and MEC to be placed into.'''

    def __init__(self):
        self.edge_list = dict()

    def ping(self, id, obj):
        '''Adds a given object to the 'connected devices' list.
        ID simulates an ip address.'''
        self.edge_list[id] = obj

    def broadcast(self, message):
        '''Called when an object is broadcasting a general 
        message for the mec to recieve.'''
        self.send_message(message, 'mec')

    def send_message(self, message, dest_id):
        '''Called when an object is sending a message to a 
        specific recipient over the network. In the real world,
        the dest_id would be an IP or other sort of address.'''
        if dest_id in self.edge_list:
            (self.edge_list[dest_id]).input_message(message)
            return True #msg sent
        else:
            return False #msg destination missing