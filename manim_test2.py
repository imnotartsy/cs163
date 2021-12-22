from manimlib import *

class Naive(Scene):
    def construct(self):
        # ** Initialization and Scene Variables

         # Point Generation (parameters)
        numPoints = 20
        x_range_min = -6
        x_range_max = 6
        y_range_min = -4
        y_range_max = 4
        points = []

        pointsBetween = 0
        text, number = label = VGroup(
            Text(""),
            DecimalNumber(
                0,
                # show_ellipsis=True,
                num_decimal_places=0,
                # include_sign=True,
            )
        )
        label.to_corner(UR)
        # label.arrange(BOTTOM)
        self.add(label)
        number.add_updater(lambda m: m.set_value(pointsBetween))

        potentialMedian = Text("Potential Slab Found!")
        potentialMedian.to_edge(UP)

        slabSize = 1000 # "infinity" for the grid size
        slab = []







        # Grid Show
        grid = NumberPlane((-10, 10), (-5, 5))
        self.play(ShowCreation(grid))


        # Point Generation
        for i in range(numPoints):
            x = random.randint(x_range_min, x_range_max)
            y = random.randint(y_range_min, y_range_max)
            
            color = "%06x" % random.randint(0, 0xFFFFFF)
            print("" + str(i) + ": (", x, ",", y, ")", color)
            dot = Dot([x, y, 0]).set_color(color).scale(1)

            points.append(dot)
            # self.add(dot)
            # self.wait(.25)
            self.play(ShowCreation(dot))

        

        # For all unique triplets . . .
        for i in range(numPoints):
            for j in range(i+1, numPoints):


                # Generate first line
                p0 = points[i].get_center()
                p1 = points[j].get_center()

                line_0 = Line(p0, p1, color=WHITE)
                self.play(ShowCreation(line_0))


                # Generate parallel lines with other points
                for k in range(numPoints):
                    if (not k == i) and (not k == j):  
                        print(i, j, k)                  
                        p2 = points[k].get_center()

                        m = (p0[1] - p1[1]) / (p0[0] - p1[0])
                        b = p2[1] - p2[0] * m

                        x = 0 if p2[0] != 0 else 1
                        y = m*x + b
                        p3 = Dot([x, y, 0]).get_center()
                        line_1 = Line(p2, p3, color=RED)
                        self.play(ShowCreation(line_1))


                        # Count how many points are between the two generated lines
                        pointsBetween = 0
                        inBetween = []
                        for p in range(numPoints):
                            b2 = p0[1] - p0[0] * m
                            if (not p == i) and (not p == j) and (not p == k):
                                pTest = points[p].get_center()
                                print("Testing", pTest)
                                bTest = pTest[1] - pTest[0] * m


                                # If the test point is found to be within the lines; highlight in GREEN
                                if ((bTest > b) and (bTest < b2)) or ((bTest < b) and (bTest > b2)):
                                    pointsBetween += 1

                                    # Highlight dot that's in between
                                    dot = Dot(pTest).set_color(GREEN).scale(4)
                                    self.add(dot)
                                    inBetween.append(dot)


                        # Checks and announces potential median
                        if pointsBetween >= math.floor((numPoints + 1)/2 - 3):
                            print("POTENTIAL MEDIAN FOUND")
                            
                            # Calculate Slab distance
                            perp = -1/m
                            bPerp = p0[1] - p0[0] * perp
                            # perp * x + bPerp = y, is an equation perpendular to the line formed by p0 and p1
                            #    that goes through point p0
                
                            x = (bPerp - b)/(m+1/m)
                            y = (b + m*m*bPerp)/(m*m + 1)

                            pPerp = Dot([x, y, 0]).get_center()

                            # Show debugging output for potential median and slab size
                            line_2 = Line(p0, pPerp, color=YELLOW)
                            self.play(ShowCreation(line_2))

                            self.add((potentialMedian))
                            self.wait(2)
                            self.remove(potentialMedian)
                            self.remove(line_2)

                            # Slab distance
                            dist = pow(pow(abs(p0[0] - x), 2) + pow(abs(p0[1] - y), 2), 1/2)
                            if dist < slabSize:
                                slabSize = dist

                                slab = [[p0, p1], [p2, pPerp], slabSize, pointsBetween]


                        # Un-marks points marked as in between lines
                        for dot in inBetween:
                            self.remove(dot)



                        self.remove(line_1)
                self.remove(line_0)


        # Shows final slab and point count
        p0 = slab[0][0]
        p1 = slab[0][1]

        p2 = slab[1][0]
        pPerp = slab[1][1]

        pointsBetween = slab[3]

        line_3 = Line(p0, p1, color=PURPLE)
        self.play(ShowCreation(line_3))  
        line_4 = Line(p2, pPerp, color=PURPLE)
        self.play(ShowCreation(line_4))

        line_2 = Line(p0, pPerp, color=YELLOW)
        self.play(ShowCreation(line_2))      





        self.wait(2)