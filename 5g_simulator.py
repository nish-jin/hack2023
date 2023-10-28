class fiveG_Network:
    '''Simulates a 5g network for the cars and MEC to be placed into.'''

    def __init__(self, mec_obj):
        self.mec = mec_obj
        self.obu_list = dict()

    def brodcast(self, message):
        self.mec.input_message(message)
        #TODO make mec input

    def publish_event(self, update):
        for car in self.obu_list:
            car.input_update(update)
            #TODO make car input update