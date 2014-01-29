from similarity import sim_pearson
from similarity import sim_distance
from Ranking import topMatches

#a dictionary of movie critics and their ratings of a small set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
                       'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,
                       'The Night Listener': 3.0},
         'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,
                          'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,
                          'You, Me and Dupree': 3.5},
         'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
                             'Superman Returns': 3.5, 'The Night Listener': 4.0},
         'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
                          'The Night Listener': 4.5, 'Superman Returns': 4.0,
                          'You, Me and Dupree': 2.5},
         'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                          'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
                          'You, Me and Dupree': 2.0},
         'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
                           'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
         'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}



# Gets recommendations for a person by using a weighted average
# of every other user's rankings
def getRecommendations(prefs,person,similarity=sim_pearson):
  totals={}
  simSums={}
  for other in prefs:
    # don't compare me to myself
    if other==person: continue
    sim=similarity(prefs,person,other)
    # ignore scores of zero or lower
    if sim<=0: continue
    for item in prefs[other]:
      # only score movies I haven't seen yet
      if item not in prefs[person] or prefs[person][item]==0:
        # Similarity * Score
        totals.setdefault(item,0)
        totals[item]+=prefs[other][item]*sim
        # Sum of similarities
        simSums.setdefault(item,0)
        simSums[item]+=sim
  # Create the normalized list
  rankings=[(total/simSums[item],item) for item,total in totals.items( )]
  # Return the sorted list
  rankings.sort( )
  rankings.reverse( )
  return rankings


def transformPrefs(prefs):
  result={}
  for person in prefs:
    for item in prefs[person]:
      result.setdefault(item,{})
      # Flip item and person
      result[item][person]=prefs[person][item]
  return result

  
# generate a dataset
def calculateSimilarItems(prefs, n=10):
  #Create a dictionary of items showing which other items they are most similar  to.
  result={}
  #Invert the preference matrix to be item-centric
  itemPrefs = transformPrefs(prefs)
  c=0
  for item in itemPrefs:
    #status updates for large datasets
    c+=1
    if c%100==0: print ("%d / %d" %(c,len(itemPrefs)))
    #Find the most similar items to this one
    scores = topMatches(itemPrefs,item,n=n,similarity = sim_distance)
    result[item]=scores
  return result
