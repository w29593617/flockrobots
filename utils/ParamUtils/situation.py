import json
from utils.Basic.position import Position3D
from utils.Basic.velocity import Velocity3D


class SituationParam:
    """
    FlockSituation class contains basic params of a robot flock,
    including:

    - `flocksize`: the size of the robot flock/number of agents;

    - `initX/initY/initZ`: the initial positions of agents(robots) in the flock in 3 dimensions;

    - `simulationtime`: time length of the simulation;

    - `deltaT`: accuracy of the Euler method for solving the ODE;

    - `dangerradius`: radius of dangerous area between agents(robots);

    - `time2store`: time length to store;

    - `startofsteadystate`: Estimated tarting time of steady state. Averaging order params is only neccessary from here.

    """

    agentnumber: int
    simlength: int
    initpos: Position3D
    deltaT: float
    dangerradius: float
    length2store: float
    startofsteadystate: False

    def __init__(self, agentnumber=0, simlength=0, initpos=Position3D(),
                 deltaT=0.0, dangerradius=0.0, length2store=0.0, startofsteadystate=False):

        self.agentnumber = agentnumber
        self.simlength = simlength
        self.initpos = initpos
        self.deltaT = deltaT
        self.dangerradius = dangerradius
        self.length2store = length2store
        self.startofsteadystate = startofsteadystate

    def getdefault(self, filepath='default'):

        if filepath == 'default':
            filepath = 'config/params/situationparams_default.json'

        file_content = open(filepath)
        thejson = json.load(fp=file_content)

        jsonx = list(thejson['InitPosition'].values())[0]
        jsony = list(thejson['InitPosition'].values())[1]
        jsonz = list(thejson['InitPosition'].values())[2]

        newsituparam = SituationParam(agentnumber=thejson['AgentNumber'], simlength=thejson['SimulationLength'],
                                      initpos=Position3D(x=jsonx, y=jsony, z=jsonz), deltaT=thejson['deltaT'],
                                      dangerradius=thejson['DangerousRadius'], length2store=thejson['LengthToStore'],
                                      startofsteadystate=thejson['StartOfSteadyState'])

        return newsituparam
        pass

    '''
    def adjustsimlength(self, val):
        self.simlength = val

    def adjustlength2store(self, val):
        self.length2store = val
    '''
