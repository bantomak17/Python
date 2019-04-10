class Duck():
    def __init__(self,input_name):
        self.hidden_name = input_name
    @property
    def plaza(self):
        print('inside the getter')
        return self.hidden_name
    @plaza.setter
    def plaza(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
