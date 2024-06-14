#saiprasad pujari
#Modify the Rectangle class to determine if a rectangle is tall (H > L) or short (H<L)
# define a class
class Rectangle:
    """ This is a class that reports on rectangles """
    def __init__(self, height, width):  # this init sets fields
        self.h = height
        self.w = width
    def isTallorShort(self):# checking if the rectangle is tall, short or neither tall or short
        if self.h > self.w:
            return "is tall"
        elif self.h < self.w:
            return "is short"
        else:
            return "neither tall or short"

        # main method
def main():
    # set fields for three rectangles
    rectangle1 = Rectangle(5, 10)
    rectangle2 = Rectangle(8, 1)
    rectangle3 = Rectangle(6, 6)
    print("Rectanble 1 is: ", rectangle1.isTallorShort())
    print("Rectangle 2 is: ", rectangle2.isTallorShort())
    print("Rectangle 3 is: ", rectangle3.isTallorShort())

# start process
if __name__ == "__main__":
    main()




