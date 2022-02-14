# This is robot controllers project
from abc import abstractmethod


class Controller:
    """
    Class with abstract methods.
    That's mean this class cannot be called, but inheritors can.
    """
    def __init__(self, name="robot"):
        self.name = name

    """Return short information about the controller"""
    def toString(self):
        return str(self.name) + "."

    """The main function which return control action"""
    @abstractmethod
    def run(self):
        pass


class Relay(Controller.Controller):
    def __init__(self, name="Robot's Relay controller"):
        super(Relay, self, name).__init__()

    def run(self, error):
        """
        Relay has not any coefficient.
        Result must be between -100 and 100.
        """
        return -100 if (error < 0) else 100


class P(Controller.Controller):
    """ P controller """
    def __init__(self, coefficientP=0, name="Robot's PI-controller"):
        self.kP = coefficientP
        super(PID, self, name).__init__()

    def toString(self):
        return self.name + " with P-coefficient: " + str(self.kP) + "."

    def run(self, error):
        """ Result must be between -100 and 100 """
        return max(self.kP * error) if (error < 0) else min(self.Kp * error)


class PI(Controller.Controller):
    """ PI controller """
    def __init__(self, coefficientP=0, coefficientI=0, name="Robot's PI-controller"):
        self.kP = coefficientP
        self.kI = coefficientI
        super(PID, self, name).__init__()

    def toString(self):
        return self.name + " with coefficients: P and I: " + str(self.kP) + " " + str(self.kI) + "."

    def run(self, error):
        """ Result must be between -100 and 100 """
        ...


class PID(Controller.Controller):
    """ PI controller """
    def __init__(self, coefficientP=0, coefficientI=0, coefficientD=0, name="Robot's PI-controller"):
        self.kP = coefficientP
        self.kI = coefficientI
        self.kD = coefficientD
        super(PID, self, name).__init__()

    def toString(self):
        return self.name + " with coefficients: P, I, D: " + str(self.kP) + " " + str(self.kI) + " " + str(self.kD)+"."

    def run(self, error):
        """ Result must be between -100 and 100 """
        ...

