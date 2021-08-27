import statistics

import scipy.stats
from matplotlib import pyplot
import numpy as np
from tools import removeItem, round2dec, HEADER,BA,AB,BB,AA, get_stats, barPlot, combine, fromHistToData, boxPlots, hist, toInt, getDropOff
import matplotlib.pyplot as plt
from scipy import stats
import csv
from statistics import mean, stdev
import math
from numpy.random import randn



def printMannwhitneyu(experiment, control, set):
  x = set[experiment]
  y = set[control]
  experimentMean = mean(fromHistToData(removeItem(x, 4)))
  controlMean = mean(fromHistToData(removeItem(y, 4)))

  result = stats.mannwhitneyu(fromHistToData(x), fromHistToData(y), alternative='two-sided')

  if(result.pvalue < 0.05):
    if(experimentMean > controlMean):
      print(experiment, '>', control, '&', result.pvalue, '&', 'Confirmed', '&', experiment, '\\\\ \\hline')
      # print(experiment, 'is significantly larger than', control, 'p', result.pvalue)
    else:
      print(control, '>', experiment, '&', result.pvalue, '&', 'Confirmed', '&', control, '\\\\ \\hline')
      # print(control, 'is significantly larger than', experiment, 'p', result.pvalue)
  else:
    print(experiment, '>', control, '&', result.pvalue, '&', 'Rejected', '&', '-', '\\\\ \\hline')

    pass
    # print('No significant difference found between ', experiment, 'and', control, 'p-value: ', result.pvalue)






sets = {
  HEADER: [],
  BA: [],
  AB: [],
  BB: [],
  AA: []
}


with open('/Users/macbook/PycharmProjects/funnel-plotting/full-funnel.csv', newline='') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=';')
  for row in spamreader:
      sets[row[0]] = toInt(row[1:])




histSets = {}
for key in sets.keys():
  dropOffs = getDropOff(sets[key])
  histSets[key] = dropOffs


ing = {
  "CHAINED": combine(histSets[BB], histSets[BA]),
  "NOT_CHAINED": combine(histSets[AB], histSets[AA]),
  "LOCKED": combine(histSets[BB], histSets[AB]),
  "NOT_LOCKED": combine(histSets[BA], histSets[AA])
}

# printMannwhitneyu("CHAINED", "NOT_CHAINED", ing)
# printMannwhitneyu("LOCKED", "NOT_LOCKED", ing)




def printTests ():
  printMannwhitneyu(BB, AA, histSets)
  printMannwhitneyu(BA, AB, histSets)

  printMannwhitneyu(AB, AA, histSets)
  printMannwhitneyu(AB, BB, histSets)

  printMannwhitneyu(BA, AA, histSets)
  printMannwhitneyu(BA, BB, histSets)

printTests()

# boxPlots([histSets[AA], histSets[BB], histSets[BA], histSets[AB]], [AA, BB, BA, AB])
def printBarPlots():

  barPlot(histSets[AB], AB)
  barPlot(histSets[AA], AA)
  barPlot(histSets[BB], BB)
  barPlot(histSets[BA], BA)

def printBarPlotsNoFriction():
  barPlot(removeItem(histSets[AB], 4), AB)
  barPlot(removeItem(histSets[AA], 4), AA)
  barPlot(removeItem(histSets[BB], 4), BB)
  barPlot(removeItem(histSets[BA], 4), BA)




print(stats.levene(
  fromHistToData(histSets[AB]),
  fromHistToData(histSets[AA]),
  fromHistToData(histSets[BB]),
  fromHistToData(histSets[BA])
))



maxsum = 2000

title = 'Drop-off for prototype - '



totalChallengeForProto = {
  AA: 919,
  AB: 950,
  BB: 941,
  BA: 986,
}

def plotCumSum (data, proto):
  cum = np.cumsum(data)
  max = totalChallengeForProto[proto]

  barPlot(max - cum, proto, 986, title)

#
# barPlot(histSets[AB], AB)
# barPlot(histSets[AA], AA)
# barPlot(histSets[BB], BB)
# barPlot(histSets[BA], BA)


def calcCompletionRate():

  challengesCompletions = []
  totalUsers = 3796

  with open('/Users/macbook/PycharmProjects/funnel-plotting/chalcompletions.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
      challengesCompletions.append(row)


  for challenge in challengesCompletions:
    cr = (int(challenge[1]) / totalUsers)
    challenge.append(cr)
    print(challenge[0], '&', challenge[1], '&', str(round2dec(cr * 100, 1)) + '\%', '&', '-' '\\\\ \\hline')

  crOnly = []
  nOnly = []

  for challenge in challengesCompletions:
    crOnly.append(challenge[2])
    nOnly.append(int(challenge[1]))

  cr = np.average(crOnly)

  print('\\textbf{Average}', '&', '&', str(round2dec(cr * 100, 1)) + '\%', '&', '-')

  nTotal = np.sum(nOnly)
  print('nTotal:', nTotal)


def normalDist(x):
  shapiro_test = stats.shapiro(x)
  print(shapiro_test.pvalue)

data = 5 * randn(100) + 50

def stats(sets, which):
  data = fromHistToData(sets)
  median = statistics.median(data)
  m = round2dec(mean(data))
  std = round2dec(stdev(data))
  n = (len(data))
  nchal = str(sum(data))
  print(which, '&', n, '&', m, '(n:', nchal + ')', '&', std, '&', median, '\\\\ \hline')

# stats(histSets[AB], AB)
# stats(histSets[AA], AA)
# stats(histSets[BB], BB)
# stats(histSets[BA], BA)

# hist(fromHistToData(abCounts))
# print(statistics.stdev(fromHistToData(aaCounts)))

