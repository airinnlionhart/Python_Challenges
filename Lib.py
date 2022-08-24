import logging
import time


# Logging
def log_message(start, message):
    elapsed = str(round(time.time() - start, 2))
    message = message
    return "elapsed: " + elapsed + " " + message


def log_error(message):
    logging.basicConfig(format='%(levelname)s: %(asctime)s %(message)s', level=logging.error(message))


def log_info(message):
    logging.basicConfig(filename='app.log', format='%(levelname)s: %(asctime)s %(message)s',
                        level=logging.INFO)
    logging.info(message)


class Factor:
    # Class for finding Factor of numbers
    def __init__(self, number):
        self.number = number
        self.start = time.time()

        if isinstance(self.number, int):
            self.number = number
        else:
            log_error(log_message(self.start, "error was expecting an int and got " + str(self.number)))
            exit(1)

    def return_factor_list(self):
        list_of_factors = []
        divisor = 2
        while divisor <= self.number:
            if self.number % divisor == 0:
                list_of_factors.append(divisor)
                self.number = self.number // divisor
            else:
                divisor += 1
        log_info(log_message(self.start, "returned a list of factors"))
        # removing duplicates by turning list into dictionary then back to a list
        return list(dict.fromkeys(list_of_factors))


class IsPalindrome:
    def __init__(self, word):
        self.word = word
        self.start = time.time()

    def check(self):
        try:
            if str(self.word).lower().replace(" ", '') == str(self.word).replace(" ", '').lower()[::-1]:
                log_info(log_message(self.start, "returned a boolean"))
                return True
            else:
                log_info(log_message(self.start, "returned false " + str(self.word).replace(" ", '').lower()[::-1]))
                return False
        except Exception as e:
            log_error(log_message(self.start, str(e)))
