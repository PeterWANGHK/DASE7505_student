
import math

POINT_PLANNER=0; TRAJECTORY_PLANNER=1

PARABOLA=0; SIGMOID=1



class planner:
    def __init__(self, type_):

        self.type=type_

    
    def plan(self):
        
        if self.type==POINT_PLANNER:
            return self.point_planner()
        
        elif self.type==TRAJECTORY_PLANNER:
            return self.trajectory_planner()


    def point_planner(self):
        x=-1.0; y=-1.0; theta=0.0
        return x, y, theta


    def trajectory_planner(self):
        TRAJECTORY_TYPE=SIGMOID

        if TRAJECTORY_TYPE == PARABOLA:

            return [[ (x/10.0) ,(x/10.0)**2] for x in range(20,100)]

        else:
            return [[ (x/10.0) , 1/( 1 + math.exp(-(x/10)))] for x in range(20,100)]

