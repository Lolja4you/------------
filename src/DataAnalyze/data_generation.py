import random
def data_test_gen(t=10, option=4):
            if option == 0: return(
                t+random.randint(1,10),
                t+random.randint(1,50),
                t+random.randint(1,50),
                t+random.randint(1,50),
                t+random.randint(1,50),
                t+random.randint(1,50),
                t+random.randint(1,50),
            )
            elif option == 1: return(
                int((350*(t+random.randint(1,10)))**(1/2)),
                int((random.randint(1,50))**(1/2)),
                int((random.randint(1,50))**(1/2)),
                int((random.randint(1,50))**(1/2)),
                int((random.randint(1,50))**(1/2)),
                int((random.randint(1,50))**(1/2)),
                int((random.randint(1,50))**(1/2)),
            )
            elif option == 2: return(
                t+random.randint(1,10),
                t+random.randint(1,5),
                t+random.randint(1,5),
                t+random.randint(1,5),
                t+random.randint(1,5),
                t+random.randint(1,5),
                t+random.randint(1,5),
            )
            elif option == 3: return(
                t+5,
                t+5,
                t+5,
                t+5,
                t+5,
                t+5,
                t+5,
            )
            elif option == 4: return(
                round((350*(t+random.randint(1,10)))**(1/2), 3),
                t+random.randint(1,10),
                t+random.randint(1,20),
                t+random.randint(1,30),
                t+random.randint(1,40),
                t+random.randint(1,50),
                t+random.randint(1,60),
            )
            else: return(
                round((350*(t+random.randint(1,10)))**(1/2), 3),
                round((5000*(random.randint(1,50)))**(1/2), 3),
                round((15000*(random.randint(1,50)))**(1/2), 3),
                round((9000*(random.randint(1,50)))**(1/2), 3),
                round((12000*(random.randint(1,50)))**(1/2), 3),
                round((20000*(random.randint(1,50)))**(1/2), 3),
                round((40000*(random.randint(1,50)))**(1/2), 3),
            )
        