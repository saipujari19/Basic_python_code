#saiprasad pujari
#Research and solve to find the diagonal of a rectangle
import math
# defining a class
class Rectangle:
    """ This is a class that reports on rectangles """
    def __init__(self, height, width):  # this init sets fields
        self.h = height
        self.w = width
    def diagonal(self): #   finding diagonal
        return math.sqrt(self.h ** 2 + self.w ** 2)
# main method
def main():
    # set fields for three shapes
    rectangle1 = Rectangle(1, 12)
    rectanble2 = Rectangle(4, 3)
    rectangle3 = Rectangle(-5, 6)
    #checking diagonals
    print(f"Rectangle 1 diagonal is: {rectangle1.diagonal():.2f}")
    print(f"rectangle 2 diagonal is: {rectanble2.diagonal():.2f}")
    print(f"Rectangle 3 diagonal is: {rectangle3.diagonal():.2f}")
# start process
if __name__ == "__main__":
    main()

