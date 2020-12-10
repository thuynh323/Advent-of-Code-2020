import re
class Bag:
    def __init__(self, rules, color):
        self.rules = rules
        self.color = color
        
    def parent(self):
        parent_bags = []
        for r in self.rules:
            if self.color in r:
                color_list = re.findall(r'^\S+\s\S+(?= bags contain [0-9])', r)[0]
                parent_bags.append(color_list)
        if self.color in parent_bags:
            parent_bags.remove(self.color)
        return parent_bags
        
    def child(self):
        child_color = []
        child_num = []
        for r in self.rules:
            if re.findall(r'^\S+\s\S+(?= bags contain [0-9])', r) == [self.color]:
                color_list = re.findall(r'(?<=[0-9] )\S+\s\S+', r)
                child_color.append(color_list)
                num_list = re.findall(r'\d+', r)
                child_num.append(num_list)
        child_color = [i for x in child_color for i in x]
        child_num = [x for x in child_num if x != []]
        child_num = [int(i) for x in child_num for i in x]
        child_bags = {}
        for k, v in zip(child_color, child_num):
            child_bags[k] = v
        return child_bags

def count_parents(rules, color):
    bags = Bag(rules, color).parent()
    containers = []
    for b in bags:
        containers.append(Bag(rules, b).parent())
        for bb in containers:
            for bbb in bb:
                containers.append(Bag(rules, bbb).parent())
    containers = [x for x in containers if x != []]
    containers = [i for x in containers for i in x]
    return len(set(containers)) + len(bags)
    
with open('day_07.txt') as f:
    lst = [x.strip('\n') for x in f.readlines()]
    print(f"Number of bags that can contain at least one shiny gold bag: {count_parents(lst, 'shiny gold')}")
