import numpy as np


def expected_winnings(iteration, states, payoff, absorbing_state):
    for n in range(iteration + 1):
        stopping_set = np.array([], dtype=int)
        s2_sum = 0
        if n == 0:
            for x in range(len(states)):
                if x == absorbing_state:
                    states[x] = 0
                    continue
                elif states[x] < payoff.max():
                    states[x] = payoff.max()
                else:
                    stopping_set = np.append(stopping_set, x)
                    continue
            for s in range(len(stopping_set)):
                s2_sum += states[stopping_set[s]]
            p = (states.max() * (len(states) - len(stopping_set) - 1) + s2_sum) / len(states)
        else:
            for y in range(len(states)):
                if y == absorbing_state:
                    states[y] = 0
                    continue
                elif payoff[y] < p:
                    states[y] = p
                else:
                    states[y] = payoff[y]
                    stopping_set = np.append(stopping_set, y)
            for k in range(len(stopping_set)):
                s2_sum += states[stopping_set[k]]
            p = (p * (len(states) - len(stopping_set) - 1) + s2_sum) / len(states)

    return states


def expected_winnings_with_cost(iteration, states, payoff, absorbing_state, cost):
    for n in range(iteration + 1):
        stopping_set = np.array([], dtype=int)
        s2_sum = 0
        if n == 0:
            for x in range(len(states)):
                if x == absorbing_state:
                    states[x] = 0
                    continue
                elif states[x] < payoff.max():
                    states[x] = payoff.max()
                else:
                    stopping_set = np.append(stopping_set, x)
                    continue
            for s in range(len(stopping_set)):
                s2_sum += states[stopping_set[s]]
            p = (states.max() * (len(states) - len(stopping_set) - 1) + s2_sum) / len(states) - cost
        else:
            for y in range(len(states)):
                if y == absorbing_state:
                    states[y] = 0
                    continue
                elif payoff[y] < p:
                    states[y] = p
                else:
                    states[y] = payoff[y]
                    stopping_set = np.append(stopping_set, y)
            for k in range(len(stopping_set)):
                s2_sum += states[stopping_set[k]]
            p = (p * (len(states) - len(stopping_set) - 1) + s2_sum) / len(states) - cost

    return states


# Problem 4 Setup
u1 = np.array([], dtype=int)
for i in range(51):
    u1 = np.append(u1, [i])

f1 = u1

# Problem 4.1
v1 = expected_winnings(iteration=101, states=np.array(u1.copy(), dtype=float),
                       payoff=f1, absorbing_state=0)

# Problem 4.2
v2 = expected_winnings_with_cost(iteration=101, states=np.array(u1.copy(), dtype=float),
                                 payoff=f1, absorbing_state=0, cost=5)
