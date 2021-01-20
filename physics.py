class Velocity:
    def __init__(self, velocity=None, displacement=None, time=None, units=None):
        self.units = units
        if isinstance(velocity, int) or isinstance(velocity, float):
            self.velocity = velocity

        if (isinstance(displacement, float) or isinstance(displacement, int)) \
                and \
                (isinstance(time, float) or isinstance(displacement, int)):
            self.displacement = displacement
            self.time = time

    def velocity(self):
        try:
            return self.displacement / self.time

        except ValueError:
            try:
                if self.units is None:
                    return str(self.velocity) + "units"

                else:
                    return str(self.velocity) + self.units

            except ValueError:
                return None


class Gravity:
    def __init__(self, r, m2, m1=None):
        self.earth_mass = 5.972 * (10 ** 24)
        self.earth_radius = 6378 * 1000
        self.G = 6.67430 * (10 ** -11)
        self.r = r
        self.m1 = m1
        self.m2 = m2

    # m1 and m2 should be in kg's and r should be in metres
    def general_force(self):
        return -self.G * ((self.m1 * self.m2) / (self.r ** 2))

    def general_acceleration(self):
        return -self.general_force() / self.m2

    # r should be in metres while m2 should be in kgs
    def g_force(self):
        self.r += self.earth_radius
        self.m1 = self.earth_mass
        return self.general_force()

    def g_acceleration(self):
        return self.g_force() / self.m2


vi = Velocity(19.6, units="m/s")
