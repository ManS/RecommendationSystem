from math import sqrt
# Returns a distance-based similarity score for person1 and person2
def sim_distance(prefs, person1, person2):
    # Get the list of shared_items
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1

    # if they have no ratings in common, return 0
    if len(si)==0 : return 0

    # Add up the squares of all the differences
    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item],2)
                          for item in prefs[person1] if item in prefs[person2]])
    return 1/(1+sum_of_squares);


#Returns the pearson correlation coefficient for person1 and person2
def sim_pearson(prefs, person1, person2):
  # Get the list of mutuallty rated items
  si = {}
  for item in prefs[person1]:
    if item in prefs[person2]:
      si[item]=1

  #find the number of elements
  n = len(si)

  #if there are no ratings in common, return 0
  if n==0: return 0

  # Add up all the preferences
  sum1 = sum([prefs[person1][it] for it in si])
  sum2 = sum([prefs[person2][it] for it in si])

  #sum up the squares 
  sum1Sq = sum([pow(prefs[person1][it],2)for it in si])
  sum2Sq = sum([pow(prefs[person2][it],2)for it in si])

  #sum up the products
  pSum = sum([prefs[person1][it] * prefs[person2][it] for it in si])

  #calculate pearson score
  num = pSum - (sum1*sum2/n)
  den = sqrt((sum1Sq - pow(sum1,2)/n)*(sum2Sq - pow(sum2,2)/n))

  if den ==0: return 0

  r = num/den

  return r