import  numpy as np
class FuzzyGasController:
    """
    # emtiazi todo
    write all the fuzzify,inference,defuzzify method in this class
    """

    def __init__(self):
        self.close =  0
        self.moderate = 0
        self.far = 0
        self.high = 0
        self.low = 0
        self.medium = 0

    def fuzzify(self,center):
        if 0 <= center <= 50:
            self.close= -0.02 * center + 1
        if 40 <= center <= 100:
            if center<= 50:
                self.moderate = 1/10 * center -4
            else:
                self.moderate = -1/50 * center + 2
        if 90<= center<= 200:
            self.far = 1/110 * center - 9/11
        if center>= 200 :
            self.far = 1

    def inference(self):
        self.low = self.close
        self.medium = self.moderate
        self.high = self.far


    def maxRotate(self, speed):
        max_rotate = 0
        if 0 <= speed <=10:
            if speed <= 5:
                max_rotate = max(min(speed/5,self.low),max_rotate)
            else:
                max_rotate = max(min((-speed/5) + 2,self.low),max_rotate)

        if 0 <= speed <= 30:
            if speed <= 15:
                max_rotate = max(min(speed / 15, self.medium), max_rotate)
            else:
                max_rotate = max(min((-speed / 15) + 2, self.medium), max_rotate)
        if 25 <= speed <= 90:
            if speed <= 30:
                max_rotate = max(min((speed / 5)  - 5, self.high), max_rotate)
            else:
                max_rotate = max(min((-speed / 60) + 3/2, self.high), max_rotate)
        return max_rotate

    def defuzzify(self):
        soorat = 0.0
        makhraj = 0.0
        X = np.linspace(0, 90, 900)
        delta = X[1] - X[0]

        for i in X:
            max_rotate = self.maxRotate(i)
            soorat += max_rotate * i * delta
            makhraj += max_rotate * delta

        center = 0.0
        if makhraj != 0:
            center = 1.0 * float(soorat) / float(makhraj)

        return center

    def decide(self, center_dist):
        """
        main method for doin all the phases and returning the final answer for gas
        """
        self.fuzzify(center_dist)
        self.inference()

        return self.defuzzify()