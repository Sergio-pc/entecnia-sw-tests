
from __future__ import print_function, division
from builtins import range
# Note: you may need to update your version of future
# sudo pip install -U future


import numpy as np
from grid_world import standard_grid, ACTION_SPACE


SMALL_ENOUGH = 1e-3
GAMMA = 0.9


def get_transition_probs_and_rewards(grid):
  ### define transition probabilities and grid ###
  # the key is (s, a, s'), the value is the probability
  # that is, transition_probs[(s, a, s')] = p(s' | s, a)
  # any key NOT present will considered to be impossible (i.e. probability 0)
  transition_probs = {}

  # to reduce the dimensionality of the dictionary, we'll use deterministic
  # rewards, r(s, a, s')
  # note: you could make it simpler by using r(s') since the reward doesn't
  # actually depend on (s, a)
  rewards = {}

  for i in range(grid.rows):
    for j in range(grid.cols):
      s = (i, j)
      if not grid.is_terminal(s):
        for a in ACTION_SPACE:
          s2 = grid.get_next_state(s, a)
          transition_probs[(s, a, s2)] = 1
          if s2 in grid.rewards:
            rewards[(s, a, s2)] = grid.rewards[s2]

  return transition_probs, rewards

def print_values(V, g):
  for i in range(g.rows):
    print("---------------------------")
    for j in range(g.cols):
      v = V.get((i,j), 0) #Value dictionary V. If the postion i,j is not in the values dictionary, it is get a zero.
      #get is used to find in dicitonaries, V is teh dictionary
      if v >= 0: #We check it is not negative. Negative sign takes a extra space.
        print(" %.2f|" % v, end="") #the values is rounded to 2 decimals
      else:
        print("%.2f|" % v, end="") # -ve sign takes up an extra space
    print("") #to go to the next line.
 
    
def print_policy(P, g):
  for i in range(g.rows):
    print("---------------------------")
    for j in range(g.cols):
      a = P.get((i,j), ' ') #We grab a action for the corresponding state(i,j). In case of no action, it is retrun a space
      print("  %s  |" % a, end="") #print a action
    print("") #new line

    
def evaluate_deterministic_policy(grid, policy):
     #Prediction problem. Calculation of V(s)
  # initialize V(s) = 0
  V = {}
  for s in grid.all_states():
    V[s] = 0

  # repeat until convergence
  it = 0
  while True:
    biggest_change = 0
    for s in grid.all_states():
      if not grid.is_terminal(s):
        old_v = V[s]
        new_v = 0 # we will accumulate the answer
        for a in ACTION_SPACE:
          for s2 in grid.all_states():

            # action probability is deterministic
            action_prob = 1 if policy.get(s) == a else 0
            
            # reward is a function of (s, a, s'), 0 if not specified
            r = rewards.get((s, a, s2), 0)
            new_v += action_prob * transition_probs.get((s, a, s2), 0) * (r + GAMMA * V[s2])

        # after done getting the new value, update the value table
        V[s] = new_v
        biggest_change = max(biggest_change, np.abs(old_v - V[s]))
    it += 1

    if biggest_change < SMALL_ENOUGH:
      break
  return V


if __name__ == '__main__':

  grid = standard_grid() # to instance the environment
  transition_probs, rewards = get_transition_probs_and_rewards(grid)

  # print rewards
  print("rewards:")
  print_values(grid.rewards, grid)

  # state -> action
  # we'll randomly choose an action and update as we learn
  policy = {}
  for s in grid.actions.keys():
    policy[s] = np.random.choice(ACTION_SPACE)

  # initial policy
  print("initial policy:")
  print_policy(policy, grid)

  # repeat until convergence - will break out when policy does not change
  while True: #infinite loop
  #COMPLETE THE CODE HERE
  #Target: Find the optimal policy[s] for the agent to find the exit position.
  # s is the state, position (i,j) 
  #Methodlogy: 
  #1-Use value function (V[s]) to evaluate the maximum return
  #2-Test all actions for every state to get the value function Q(s,a).
  #3-Finally the optimum action for every state (s) is equal to the maximum Q(s,a) for the same state (s)
  #4-Store the optimum actions (a) for every state (s) in the dictionary policy[s]
  
  

      


  # once we're done, print the final policy and values
  print("values:")
  print_values(V, grid)
  print("policy:")
  print_policy(policy, grid)
