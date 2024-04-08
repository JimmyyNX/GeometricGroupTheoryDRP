def generate(characters, length):
    if length < 1:
        return []

    dp = [c for c in characters]

    for i in range(length - 1):
        dp = [character + sub_permutation for sub_permutation in dp for character in characters]

    return dp


class LampLight:
    street_state = set()
    position = int
    walked = str

    def __init__(self):
        self.street_state = set()
        self.position = 0
        self.walked = ""

    def walk(self, string):
        self.walked = string
        for action in string:
            if action == "a":
                if self.position in self.street_state:
                    self.street_state.remove(self.position)
                else:
                    self.street_state.add(self.position)
            if action == "f":
                self.position += 1
            if action == "b":
                self.position -= 1

    def reset(self):
        self.position = 0
        self.street_state = set()

    def distance(self):
        minimum = 0
        maximum = 0
        if self.street_state and min(self.street_state) <= 0:
            minimum = min(self.street_state)
        if self.street_state and max(self.street_state) >= 0:
            maximum = max(self.street_state)
        return min(2 * maximum - minimum + abs(minimum - self.position),
                   -2 * minimum + maximum + abs(maximum - self.position)) + len(self.street_state)

    def __eq__(self, other):
        if self.street_state == other.street_state and self.position == other.position:
            return True


k = 10

x = generate(["f", "b", "a", "n"], k)
# f should be interpreted as moving Right
# b should be interpreted as moving left
# a should be interpreted as toggling the light at the current position
# n should be interpreted as doing nothing
length_list = []
for todolist in x:
    Lamp = LampLight()
    Lamp.walk(todolist)
    for lamp in length_list:
        if Lamp.__eq__(lamp):
            break
    else:
        length_list.append(Lamp)
x = []
dead_list = []
print(len(length_list))
for Lamp2 in length_list:
    Lamp3 = LampLight()
    for j in ["f", "b", "a"]:
        Lamp3.street_state = Lamp2.street_state.copy()
        Lamp3.position = Lamp2.position
        Lamp3.walk(j)
        if Lamp3.distance() > Lamp2.distance():
            break
        Lamp3.reset()
    else:
        dead_list.append(Lamp2)

print(len(dead_list))
for i in dead_list:
    print(i.position)
    print(i.street_state)
