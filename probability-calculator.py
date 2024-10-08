import copy
import random

class Hat:
    def __init__(self, **args):
        self.contents = [color for color, count in args.items() for _ in range(count)]

    def draw(self,num_balls):
        if num_balls >= len(self.contents):
            selections = copy.copy(self.contents)
            self.contents.clear()
            return selections

        selections = []
        for _ in range(num_balls):
            choice = random.choice(self.contents)
            selections.append(choice)
            self.contents.remove(choice)
        return selections


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success = 0
    for _ in range(num_experiments):
        selections = copy.deepcopy(hat).draw(num_balls_drawn)
        is_success = all(selections.count(ball) >= count for ball, count in expected_balls.items())
        if is_success:
            success += 1
    
    print(success/num_experiments)
    return success / num_experiments


hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
