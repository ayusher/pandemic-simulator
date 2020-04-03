import random

total_pop = 3000000
death_rate = .015
asym_rate = .2
tests_per_day = lambda x: min(1.1**x, 15000)
test_pos_rate = .05
incubation_time = 18
inc_uncm = 5
inc_uncp = 7
branch_factor = 2.2
tot_dead = 0
t_pos = 0

class Person:
        def __init__(self, d):
                self.branch = round(random.random()*2-random.random()*2+branch_factor)
                self.healed = d + incubation_time + random.randint(-inc_uncm, inc_uncp)
                self.infect_days = set([int(random.random()*(1+self.healed-d))+d, int(random.random()*(1+self.healed-d))+d])
                #self.infect_days = set([random.randint(d, self.healed), random.randint(d, self.healed)])
                self.tested = False
                if random.random()<death_rate: self.dead = random.randint(d, self.healed)
                else: self.dead = -1

        def run(self, d, p):
                if d in self.infect_days and self.branch>0:
                        self.branch -= 1
                        if random.randint(0, total_pop)<p: return 0
                        return 1
                return 0

        def heal(self, d, q):
                global tot_dead
                global t_pos

                if d >= self.healed:
                        if self.tested: t_pos -= 1
                        return 1
                if self.dead!=-1 and d>=self.dead:
                        tot_dead+=1
                        if self.tested: t_pos -= 1
                        return 1
                if random.random()>asym_rate and random.random()<tests_per_day(d)/(q-t_pos+.0001)*test_pos_rate:
                        self.infect_days = set()
                        self.tested = True
                        t_pos+=1
                return 0

day = 100
start_num = 250000
pop = {Person(day) for _ in range(start_num)}
tot_cases = start_num
li = []
li2 = []
day_dict = {}

while len(pop)>0:
        day_dict[day]=tot_cases
        li.append(tot_cases)
        li2.append(len(pop))
        new_sick = sum([a.run(day, tot_cases) for a in pop])
        pop = pop.union({Person(day) for _ in range(new_sick)})
        tot_cases = tot_cases + new_sick
        pop = {i for i in pop if i.heal(day, len(pop))==0}
        day += 1
        print("Day", day, "\tActive cases:", len(pop), "\tCases ever recorded:", tot_cases, "\tNewly sick:", new_sick, "Total dead:", tot_dead)

print("Total cases (cumulative) day by day:",li)
print("Active cases day by day:",li2)
