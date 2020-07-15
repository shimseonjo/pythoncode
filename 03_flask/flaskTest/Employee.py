class Employee():
    def __init__(self,firstName,lastName):
        self.firstName = firstName
        self.lastName = lastName

    def toJSON(self):
        return {"emp": {'firstName': self.firstName,
                              'lastName': self.lastName}}
