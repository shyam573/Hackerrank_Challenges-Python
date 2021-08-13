

class Student(Person):
    #   Class Constructor
    #   
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = [int(i) for i in scores]

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        val = sum(self.scores)/len(self.scores)
        if 90<=val<=100: return "O"
        elif 80<=val<90: return "E"
        elif 70<=val<80: return "A"
        elif 55<=val<70: return "P"
        elif 40<=val<55: return "D"
        else: return "T"
    
            

