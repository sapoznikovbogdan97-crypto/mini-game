import random

class  Researcher:
    def __init__(self, id, group, experience = 1):
        self.id = id
        self.group = group
        self.experience = experience
        arctic_team  = []
        ocean_team = []


    def upgrade(self):
        self.experience += 1
        print("уровень иледователя увеличен на 1")

class Robot():
    def __init__(self, id, group):
        self.id = id
        self.group = ["Arctic", "Ocean"]
        self.random_group = random.choice(self.group)
    def follow(self, researcher):
        self.researcher = researcher
        print("робот", self.id, "следует за исследователем", self.researcher.id)
        print(self.random_group)

if __name__ == '__main__':
    researcher1 = Researcher(1010, "Arctic")
    researcher2 = Researcher(1011, "Ocean")
    robot1 = Robot(1101, group=random.choice(["Arctic", "Ocean"]))
    robot1.follow(researcher1 or researcher2)
    robot2 = Robot(1111, group=random.choice(["Arctic", "Ocean"]))
    robot2.follow(researcher1 or researcher2)