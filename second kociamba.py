 import kociemba

    # def solve(self):
        
    #     order = input("Enter the Rubik's cube orientation: ") #"".join(qb.current_face for qb in self.cube)
    #     print(order)
    #     for i in ["U", "R", "L", "D", "B", "F"]:
    #         correct = (i,"=",order.count(i))
    #         #print(correct)
    #         self.all9.append(correct)
    #     print(self.all9)
    #     return kociemba.solve(order)
    
def solve(self):
    while self.all9 != "[('U', '=', 9), ('R', '=', 9), ('L', '=', 9), ('D', '=', 9), ('B', '=', 9), ('F', '=', 9)]":
        order = input("Enter the Rubik's cube orientation: ") #"".join(qb.current_face for qb in self.cube)
        if order == "UUUUUUUUURRRRRRRRRLLLLLLLLLDDDDDDDDDBBBBBBBBBFFFFFFFFF":
            fin =  "Finished"
            return fin 
        print(order[0:3])
        print(order[3:6])
        print(order[6:9])
        print(order[])
        for i in ["U", "R", "L", "D", "B", "F"]:
            correct = (i,"=",order.count(i))
            self.all9.append(correct)

    return kociemba.solve(order)

    


   