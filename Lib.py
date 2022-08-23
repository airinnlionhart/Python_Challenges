class Factor:
    def __init__(self, number):
        self.number = number

    def return_factor_list(self):
        list_of_factors = []
        divisor = 2
        while divisor <= self.number:
            if self.number % divisor == 0:
                list_of_factors.append(divisor)
                self.number = self.number // divisor
            else:
                divisor += 1
        # removing duplicates by turning list into dictionary then back to a list
        return list(dict.fromkeys(list_of_factors))
