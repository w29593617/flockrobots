from utils.Basic.velocity import Velocity2D


class WindParam(Velocity2D):

    # TODO: why the wind has only a 2-dimensional velocity? What about 3D?

    def __init__(self, vx: float, vy: float):
        self.vx = vx
        self.vy = vy

    def func1(self):
        pass
