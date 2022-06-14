import time

class Pythonisms:
    '''
    Pythonisms practicing the dunder methods
    '''
    def __init__(self, collection):
        self.collection = collection

    def __str__(self):
        string ="The current items in the collection are as follows:"
        for item in self.collection:
            string += f" {item}"
        return string

    def __sum__(self):
        

    def sum_collection(self):
        start_time = time.time()
        if not self.collection:
            print(f'This process was completed in {time.time() - start_time} seconds')
            return 'There is no collection to add!'