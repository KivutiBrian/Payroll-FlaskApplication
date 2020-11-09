
class Payroll:

    # private
    personal_relief = 2400

    def __init__(self, basic_salary, benefits):
        self.basic_salary = basic_salary
        self.benefits = benefits

    def calculate_gross_salary(self):
        """
        Gross salary is the salary that you get after adding all the benefits and allowances
        before the deduction of income tax and other deductions such as bonus, overtime
        """
        return self.basic_salary + self.benefits

    
