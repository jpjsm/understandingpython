class Celsius:
    """
    Using property decorator
    - this explains the basics of property decorator
    """

    def __init__(self, temperature=0):
        self.temperature = temperature

    # Let's define getter and setter for temperature
    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible")
        self._temperature = value

    # Let's make AsFahrenheit a read-only property
    @property
    def AsFahrenheit(self):
        return (self.temperature * 1.8) + 32


if __name__ == "__main__":
    human = Celsius(37)
    print(human.temperature)
    try:
        human.temperature = -300
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")

    print(human.AsFahrenheit)
    try:
        human.AsFahrenheit = 98.6
    except BaseException as err:
        print(f"Unexpected {err=}, {type(err)=}")
