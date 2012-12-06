CURYEAR = 2012
ELITE_SELECTION = 3
MUTATION_RATE = 0.05
SEED_RADIUS = 50

def room_parse(n):
     if n is 1:
         return (2, 1)
     if n is 2:
         return (1, 1)
     if n is 3:
         return (3, 1)
     if n is 4:
         return (2, 2)
     if n is 5:
         return (1, 2)
     if n is 6:
         return (3, 2)

def normalize(record):
    # name - shouldn't be important, but might as well
    record[1] = abs(hash(record[1]))

    if record[4] == "KNS": record [4] = 1
    if record[4] == "2QNS": record [4] = 2
    if record[4] == "SUNS": record [4] = 3
    if record[4] == "KS": record [4] = 4
    if record[4] == "2QS": record [4] = 5
    if record[4] == "SUS": record [4] = 6

    if record[5] == "y": record [5] = 1
    if record[5] == "n": record [5] = 0

    if record[6] == "y": record [6] = 1
    if record[6] == "n": record [6] = 0

    if record[8] == "NA": record [8] = 2012

    if record[9] == "Regular": record [9] = 1
    if record[9] == "Value": record [9] = 2
    if record[9] == "Peak": record [9] = 3


    if record[11] == "-": record [11] = 10
    if record[12] == "-": record [12] = 10
    if record[13] == "-": record [13] = 20

    # need to parse "to": out of 14 and subtract larger number from smaller number
    record[14] = int(record[14].split(' to ')[1])-int(record[14].split(' to ')[0]) if ' to ' in record[14] else int(record[14])

    if record[17] == "AK": record [17] = 1
    if record[17] == "EP": record [17] = 2
    if record[17] == "HS": record [17] = 3
    if record[17] == "MK": record [17] = 4

    # Reservation Made
    if record[18] == "Jan": record [18] = 10
    if record[18] == "Feb": record [18] = 9
    if record[18] == "Mar": record [18] = 8
    if record[18] == "Apr": record [18] = 7
    if record[18] == "May": record [18] = 6
    if record[18] == "Jun": record [18] = 5
    if record[18] == "Jul": record [18] = 4
    if record[18] == "Aug": record [18] = 3
    if record[18] == "Sep": record [18] = 2    
    if record[18] == "Oct": record [18] = 1


    # Income
    if record[19] == "NR":
        record [19] = 0
    elif record[19] == "The 1 percent":
        record [19] = 999
    else:
        record[19] = int(record[19].replace('k', '')) # Remove the thousands' - they're unnecessary

    # Race
    if record[20] == "African American": record [20] = 1.2
    if record[20] == "Asian": record [20] = .8
    if record[20] == "Hispanic": record [20] = 1
    if record[20] == "NR": record [20] = 1
    if record[20] == "Other": record [20] = 1
    if record[20] == "White": record [20] = 1.1

    if record[21] == "AL": record [21] = 2
    if record[21] == "Europe": record [21] = 20
    if record[21] == "FL": record [21] = 1
    if record[21] == "GA": record [21] = 2
    if record[21] == "IN": record [21] = 3
    if record[21] == "MA": record [21] = 5
    if record[21] == "MD": record [21] = 3.5
    if record[21] == "MS": record [21] = 4
    if record[21] == "NC": record [21] = 3
    if record[21] == "NH": record [21] = 4
    if record[21] == "NY": record [21] = 5
    if record[21] == "OH": record [21] = 4
    if record[21] == "PA": record [21] = 3.5
    if record[21] == "RI": record [21] = 4
    if record[21] == "SC": record [21] = 3
    if record[21] == "TN": record [21] = 3
    if record[21] == "TX": record [21] = 2
    if record[21] == "VA": record [21] = 3
    if record[21] == "VT": record [21] = 4
    if record[21] == "WV": record [21] = 3

    if record[22] == "n": record [22] = 0
    if record[22] == "y (birthday)": record [22] = 1
    if record[22] == "y (graduation)": record [22] = 2
    if record[22] == "y (wedding/anniversary)": record [22] = 3

    if record[23] == "n": record [23] = 0
    if record[23] == "y (nuts)": record [23] = 3
    if record[23] == "y (animals)": record [23] = 2
    if record[23] == "y (environmental)": record [23] = 1

    if record[24] == "Courtyard": record [24] = 2
    if record[24] == "No Pref": record [24] = 0
    if record[24] == "Standard": record [24] = 1
    if record[24] == "Woods": record [24] = 3

    if record[26] == "EE": record [26] = 3
    if record[26] == "EL": record [26] = 2
    if record[26] == "LL": record [26] = 1

    if record[27] == "P": record [27] = 1
    if record[27] == "W": record [27] = 2

    if record[28] == "y": record [28] = 1
    if record[28] == "n": record [28] = 0

    #Group Res (Linked res in parens) I dont know how to handle this. slot 29

    if 'y' in record[29]: record [29] = 1
    else: record [29] = 0

    if 'y' in record[30]: record [30] = 1
    elif 'n' in record[30]: record [30] = 0

    if record[31] == "Frequently": record [31] = 3
    if record[31] == "Occasionally": record [31] = 2
    if record[31] == "Rarely": record [31] = 1
    if record[31] == "Never": record [31] = 0

    if record[32] == "Donald": record [32] = 1
    if record[32] == "Goofy": record [32] = 2
    if record[32] == "Hook": record [32] = 3
    if record[32] == "Iago": record [32] = 4
    if record[32] == "Jafar": record [32] = 5
    if record[32] == "Launchpad": record [32] = 6
    if record[32] == "Mickey": record [32] = 7
    if record[32] == "Pete": record [32] = 8
    if record[32] == "Scar": record [32] = 9
    if record[32] == "Ursula": record [32] = 10

    if record[33] == "QS": record [33] = 1
    if record[33] == "Snack": record [33] = 2
    if record[33] == "TS": record [33] = 3

    if record[34] == "NA": record [34] = 0
    if record[34] == "AirTran": record [34] = 1
    if record[34] == "American": record [34] = 2
    if record[34] == "Avianca": record [34] = 3
    if record[34] == "Delta": record [34] = 4
    if record[34] == "JetBlue": record [34] = 5
    if record[34] == "Southwest": record [34] = 6
    if record[34] == "United": record [34] = 7
    if record[34] == "US Air": record [34] = 8

    if record[37] == "Frequently": record [37] = 3
    if record[37] == "Occasionally": record [37] = 2
    if record[37] == "Rarely": record [37] = 1
    if record[37] == "Never": record [37] = 0

    if record[38] == "Frequently": record [38] = 3
    if record[38] == "Occasionally": record [38] = 2
    if record[38] == "Rarely": record [38] = 1
    if record[38] == "Never": record [38] = 0
     
    if record[39] == "Far": record [39] = 1
    if record[39] == "Near": record [39] = 1
    if record[39] == "None": record [39] = 0

    if record[40] == "Both": record [40] = 3
    if record[40] == "Crib": record [40] = 2
    if record[40] == "Rail": record [40] = 1
    if record[40] == "None": record [40] = 0

    if record[41] == "y": record [41] = 1
    if record[41] == "n": record [41] = 0

    if record[42] == "Frequently": record [42] = 3
    if record[42] == "Occasionally": record [42] = 2
    if record[42] == "Rarely": record [42] = 1

    if record[43] == "Big Thunder Mountain": record [43] = 1
    if record[43] == "Buzz Lightyear's Space Ranger Spin": record [43] = 2
    if record[43] == "Dumbo the Flying Elephant": record [43] = 3
    if record[43] == "Flights of Wonder": record [43] = 4
    if record[43] == "Haunted Mansion": record [43] = 5
    if record[43] == "It's Tough to be a Bug!": record [43] = 6
    if record[43] == "Journey into Imagination": record [43] = 7
    if record[43] == "Jungle Cruise": record [43] = 8
    if record[43] == "Kali River Rapids": record [43] = 9
    if record[43] == "Kilimanjaro Safaris": record [43] = 10
    if record[43] == "Living with the Land": record [43] = 11
    if record[43] == "Mad Tea Party": record [43] = 12
    if record[43] == "Maelstrom": record [43] = 13
    if record[43] == "Muppet*Vision 3D": record [43] = 14
    if record[43] == "Nap Time with Ben Franklin and Mark Twain": record [43] = 15
    if record[43] == "Primeval Whirl": record [43] = 16
    if record[43] == "Soarin'": record [43] = 17
    if record[43] == "Space Mountain": record [43] = 18
    if record[43] == "Spaceship Earth": record [43] = 19
    if record[43] == "Splash Mountain": record [43] = 20
    if record[43] == "Star Tours: The Adventure Continues": record [43] = 21
    if record[43] == "Toy Story Mania": record [43] = 22
    if record[43] == "Voyage of the Little Mermaid": record [43] = 23
    if record[43] == "Walt Disney's Enchanted Tiki Room": record [43] = 24
    if record[43] == "Walt Disney's Carousel of Progress": record [43] = 25

    if record[44] == "y": record [44] = 0
    if record[44] == "n": record [44] = 1

    if record[45] == "y": record [45] = 0
    if record[45] == "n": record [45] = 1

    if record[46] == "n": record [46] = 0
    if record[46] == "y (hearing impaired)": record [46] = 1
    if record[46] == "y (sight impaired)": record [46] = 2
    if record[46] == "y (wheelchair)": record [46] = 3

    if record[47] == "n": record [47] = 0
    if record[47] == "y": record [47] = 1

    if record[48] == "NA": record [48] = 0 
    if record[48] == "2QNSCV": record [48] = 1
    if record[48] == "2QNSSV": record [48] = 2
    if record[48] == "2QNSWV": record [48] = 3
    if record[48] == "2QSCV": record [48] = 4
    if record[48] == "2QSSV": record [48] = 5
    if record[48] == "2QSWV": record [48] = 6
    if record[48] == "KNSCV": record [48] = 7
    if record[48] == "KNSSV": record [48] = 8
    if record[48] == "KNSWV": record [48] = 9
    if record[48] == "KSCV": record [48] = 10
    if record[48] == "KSSV": record [48] = 11
    if record[48] == "KSWV": record [48] = 12
    if record[48] == "SUNSCV": record [48] = 13
    if record[48] == "SUNSSV": record [48] = 14
    if record[48] == "SUNSWV": record [48] = 15
    if record[48] == "SUSCV": record [48] = 16
    if record[48] == "SUSSV": record [48] = 17
    if record[48] == "SUSWV": record [48] = 18

    def tryintparse(n):
        try:
            return int(n)
        except:
            return n

    return map(tryintparse, record)

reservation_data = list()
rooms = dict()
import csv
with open('ReservationInformation.csv', 'rU') as f:
    for l in csv.reader(f):
        reservation_data.append(l)
with open('rooms.csv', 'rU') as f:
    for l in csv.reader(f):
        rooms[int(l[0])] = map(int,l[1:])

reservation_data = map(normalize, reservation_data[1:])
res_trans = [[row[i] for row in reservation_data] for i in range(len(reservation_data[0]))]

## Transformations
# remember to find average number of complaints
# Years since last visit
res_trans[8] = map(lambda y: 2012 - y, res_trans[8])
# Your name doesn't matter.
res_trans[1] = map(lambda y: 0, res_trans[1])
# Frequent Attraction
res_trans[43] = map(lambda y: 0, res_trans[43])
# Favorite Character
res_trans[32] = map(lambda y: 0, res_trans[32])


# Normalize certain values by z-score
def z_transform(dt):
    n = len(dt)+1
    mean = float(sum(dt))/n
    stdv = (sum(map(lambda x: (x - mean)**2, dt))/(n-1))**(1.0/2)
    return map(lambda x: (x - mean) / stdv, dt)

# complaints
res_trans[10] = map(lambda p: 1/p, z_transform(res_trans[10]))
# make this inverse so lower scores earn higher points
# avg park day?


reservation_data = [[row[i] for row in res_trans] for i in range(len(res_trans[0]))]
for r in reservation_data:
    #print r
    pass

# idea: have priority_function *actually be a function*.
# This would allow for more complicated, but better mating.
def generate_queue(priority_function, data):
    """Takes in a priority function as a list of coefficients for a polynomial function
    and returns a priority queue of reservation numbers"""
    q = list()
    for reservation in data:
        s = sum([f*d for (f,d) in zip(priority_function, reservation[2:])])
        # This goes through each pair of multipliers and data points
        # and adds the result to the sum
        
        q.append((reservation[0], s))
    
    # Sort the list of reservation_number-priority tuples and return the list of reservation numbers
    return map(lambda n: n[0], sorted(q, key=lambda t: t[1]))

def assign(queue):
    global reservation_data
    global rooms
    """"Takes a list of reservation numbers
    and assigns them rooms on a first come, first serve basis."""
    assignment = list()
    def getRoom(rm):
        """gets an appropriate room for a room preference"""
        # {ID: [Room type, S/NS, View, Pool, Elevator]}
        import copy
        current = copy.deepcopy(rooms)
        if rm[-1]:
            current = dict((k, v) for k, v in current.iteritems() if k < 2000)
        import random
        for i in range(len(rm) - 1):
            prev = copy.deepcopy(current)
            current = dict((k, v) for k, v in current.iteritems() if v[i] == rm[i])
            if len(current) == 0:
                current = prev
        # make sure there are no repeats - 
        return min(current.keys())
        
    for res in queue:
        # {ID: [Room type, S/NS, View, Pool, Elevator]}
        res -= 1
        rt = room_parse(reservation_data[res][4])[0]
        ns = room_parse(reservation_data[res][4])[1]
        kids = reservation_data[res][3] > 1
        pref = [rt, ns,
                    reservation_data[res][24], # veiw pref
                    reservation_data[res][42], # pool
                    2 if reservation_data[res][39] is 'Near' else 1 if reservation_data[res][39] is 'Far' else 0, #elevator pref
                    kids]
        p = getRoom(pref)
        assignment.append((res + 1, p))
    return assignment

def mutate(l):
    r = l[:]
    for i in range(len(r)):
        r[i] = r[i]*random.uniform(-MUTATION_RATE*r[i], MUTATION_RATE*r[i])
    return r

def mate(l1, l2):
    ret = list()
    l = len(l1)
    for i in range(l):
        if(random.uniform(0,1) < .5):
            ret.append(l1[i])
        else:
            ret.append(l2[i])
    return children(ret, 20) + children(l1, 10) + children(l2, 10) + [l1] + [l2]

def children(lst, num):
    return [mutate(lst) for i in range(num)]

import random
funcs = [0]*len(reservation_data[0])
funcs1 = map(lambda a: random.randrange(-2,2), funcs)
funcs2 = map(lambda a: random.randrange(-2,2), funcs)
for f in (funcs1,funcs2, mate(funcs1,funcs2)):
    #print f
    pass
q1 = generate_queue(funcs1, reservation_data)
q2 = generate_queue(funcs2, reservation_data)

import subprocess
def runsh(s, iter=100):
    return int(subprocess.check_output(["java", "-jar", "sim.jar", "-q", s, str(iter)]))

def fitness(assignment):
    """Takes a list of room-reservation tuples and returns a fitness"""
        
    # write the file
    with open('./specimen.csv', 'w') as f:
        real_assignments = assignment
        for (room, res) in real_assignments:
            f.write('{},{}\n'.format(room,res))
        
    #run the simulator
    return int(runsh('specimen.csv'))

def elite(population):
    """ returns the elite members of the population """
    global reservation_data
    
    fitnesslevels = list()
    for specimen in population:
        q = generate_queue(specimen, reservation_data)
        assignment = assign(q)
        myfit = fitness(assignment)
        fitnesslevels.append((myfit, assignment, specimen))
        print myfit,
    print "Done."
    r = sorted(fitnesslevels, key=lambda pair: pair[0])
    with open('./best.csv', 'w') as f:
        for (room, res) in r[0][1]:
            f.write('{},{}\n'.format(room, res))

    return r[:ELITE_SELECTION]

def iterate(population):
    import itertools
    t = elite(population)
    el = itertools.combinations(t[:3], 2)
    ret = list()
    for comb in el:
        ret += mate(comb[0][2], comb[1][2])
    return ret

def getfit(s):
    return int(runsh('best.csv'))

import random
population = [map(lambda p: random.uniform(-SEED_RADIUS, SEED_RADIUS), [0]*49) for i in range(50)]
generation = 0
while(True):
    generation += 1
    population = iterate(population)
    bestfit = int(runsh('best.csv', 1000))
    goatfit = int(runsh('GOAT.csv', 1000))
    print('GOAT {} (G {}) (P {}) (B {})'.format(goatfit, generation, len(population), bestfit))
    if bestfit < goatfit:
        import os
        os.remove('GOAT.csv')
        os.rename('best.csv', 'GOAT.csv')
        print "FOUND NEW GOAT: {}".format(goatfit)