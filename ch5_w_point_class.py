import sys



def main():
    
    def area(r):
        return 3.14159 * r**2
    
    def distance(p1, p2):
        '''Function to find distance between two points using Pythagorean method'''
        # subtract to find difference in x and y values
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        
       # square the difference between x and y values 
        dx2 = dx**2
        dy2 = dy**2
        
        # distance between two points Pythagorean Style
        dist = (dx2 + dy2)**0.5
        
        return dist

    def area2(xc,yc,xp,yp):
        return area(distance(xc,yc,xp,yp))

    area2(1,2,4,6)





if __name__ == "__main__":
    main()
