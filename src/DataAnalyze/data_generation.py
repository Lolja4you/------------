import random
def data_test_gen(t=10):return (
            int((350*(t+random.randint(1,10)))**(1/2)),
            int((5000*(random.randint(1,50)))**(1/2)),
            int((15000*(random.randint(1,50)))**(1/2)),
            int((9000*(random.randint(1,50)))**(1/2)),
            int((12000*(random.randint(1,50)))**(1/2)),
            int((20000*(random.randint(1,50)))**(1/2)),
            int((40000*(random.randint(1,50)))**(1/2)),
            # round((350*(t+random.randint(1,10)))**(1/2), 3),
            # round((5000*(random.randint(1,50)))**(1/2), 3),
            # round((15000*(random.randint(1,50)))**(1/2), 3),
            # round((9000*(random.randint(1,50)))**(1/2), 3),
            # round((12000*(random.randint(1,50)))**(1/2), 3),
            # round((20000*(random.randint(1,50)))**(1/2), 3),
            # round((40000*(random.randint(1,50)))**(1/2), 3),
        )