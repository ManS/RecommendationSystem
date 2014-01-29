#Returns the best matches for person from the prefs dictionary 
#Number of results and similarity fucntion are optional params.

from similarity import sim_pearson
from similarity import sim_distance
from math import sqrt

def topMatches(prefs, person, n=5, similarity = sim_pearson):
  scores = [(similarity(prefs,person,other,),other) for other in prefs if other != person]
  #Sort the list so the highest scores appears at the top
  scores.sort()
  scores.reverse()
  return scores[0:n]
