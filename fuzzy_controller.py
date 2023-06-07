import  numpy as np
class FuzzyController:
    """
    #todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        self.close_L = self.close_R = 0
        self.moderate_L = self.moderate_R = 0
        self.far_L = self.far_R = 0
        self.high_right = 0
        self.low_right = 0
        self.nothing = 0
        self.low_left = 0
        self.high_left = 0


    def fuzzify(self, left_dist, right_dist):
        if 0 <= left_dist <= 50:
            self.close_L = -0.02 * left_dist + 1
        if 0 <= right_dist <= 50:
            self.close_R = -0.02 * right_dist + 1
        if 35 <= left_dist <= 65:
            if left_dist <= 50:
                self.moderate_L = 1 / 15 * left_dist - 7 / 3
            else:
                self.moderate_L = -1 / 15 * left_dist + 13 / 3
        if 35 <= right_dist <= 65:
            if right_dist <= 50:
                self.moderate_R = 1 / 15 * left_dist + 7 / 3
            else:
                self.moderate_R = -1 / 15 * left_dist + 13 / 3
        if 50 <= left_dist <= 100:
            self.far_L = 0.02 * left_dist - 1
        if 50 <= right_dist <= 100:
            self.far_R = 0.02 * right_dist - 1
    def inference(self):
        self.low_right = min(self.close_L, self.moderate_R)
        self.high_right = min(self.close_L, self.far_R)
        self.low_left = min(self.moderate_L, self.close_R)
        self.high_left = min(self.far_L, self.close_R)
        self.nothing = min(self.moderate_L, self.moderate_R)

    def maxRotate(self,rotate):
        max_rotate = 0
        if -50 <= rotate <= -5:
            if rotate <= -20:
                max_rotate = max(min(1 / 30 * rotate + 5 / 3,self.high_right),max_rotate)
            else:
                max_rotate = max(min(-1 / 15 * rotate - 1 / 3,self.high_right),max_rotate)
        if -20 <= rotate <= 0:
            if rotate <= -10:
                max_rotate = max(min(1 / 10 * rotate + 2,self.low_right),max_rotate)
            else:
                max_rotate = max(min(-1 / 10 * rotate,self.low_right),max_rotate)
        if -10 <= rotate <= 10:
            if rotate <= 0:
                max_rotate = max(min(1 / 10 * rotate + 1,self.nothing),max_rotate)
            else:
                max_rotate = max(min(-1 / 10 * rotate + 1,self.nothing),max_rotate)
        if 0 <= rotate <= 20:
            if rotate <= 10:
                max_rotate = max(min(1 / 10 * rotate,self.low_left),max_rotate)
            else:
                max_rotate = max(min(-1 / 10 * rotate + 2,self.low_left),max_rotate)
        if 5 <= rotate <= 50:
            if rotate <= 20:
                max_rotate = max(min(1 / 15 * rotate - 1 / 3,self.high_left),max_rotate)
            else:
                max_rotate = max(min(-1 / 30 * rotate + 5 / 3,self.high_left),max_rotate)
        return max_rotate


    def defuzzify(self):
        soorat = 0.0
        makhraj = 0.0
        X = np.linspace(-50,50,1000)
        delta = X[1] - X[0]

        for i in X:
            max_rotate = self.maxRotate(i)
            soorat += max_rotate * i * delta
            makhraj += max_rotate *  delta

        center = 0.0
        if makhraj != 0 :
            center = 1.0 * float(soorat)/float(makhraj)

        return center




    def decide(self, left_dist, right_dist):
        """
        main method for doin all the phases and returning the final answer for rotation
        """
        self.fuzzify(left_dist, right_dist)
        self.inference()
        return self.defuzzify()
