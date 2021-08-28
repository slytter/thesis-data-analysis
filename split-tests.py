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
from scipy.stats import fligner, bartlett


def printMannwhitneyu(experiment, control, set):
  x = removeItem(set[experiment], 4)
  y = removeItem(set[control], 4)
  dataX = fromHistToData(x)
  dataY = fromHistToData(y)

  experimentMean = mean(dataX)
  controlMean = mean(dataY)

  result = stats.mannwhitneyu(dataX, dataY, alternative='two-sided')

  if(result.pvalue < 0.05):
    if(experimentMean > controlMean):
      #print(experiment, '--', control, '&', result.pvalue, '&', 'Accepted', '&', experiment, '\\\\ \\hline')
      print(experiment, '>', control, 'p', round2dec(result.pvalue))
    else:
      # print(control, '--', experiment, '&', round2dec(result.pvalue), '&', 'Accepted', '&', control, '\\\\ \\hline')
      print(control, '>', experiment, 'p', round2dec(result.pvalue))
  else:
    largestMean = experiment if (experimentMean > controlMean) else control
    #print(experiment, '--', control, '&', result.pvalue, '&', 'Rejected', '&', largestMean, '\\\\ \\hline')
    print('No diff', experiment, 'and', control, 'p-value: ', round2dec(result.pvalue))

    pass






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

#printMannwhitneyu("CHAINED", "NOT_CHAINED", ing)
#printMannwhitneyu("LOCKED", "NOT_LOCKED", ing)




def printTests ():
  printMannwhitneyu(AA, BB, histSets)
  printMannwhitneyu(AB, BA, histSets)

  printMannwhitneyu(AA, AB, histSets)
  printMannwhitneyu(BB, AB, histSets)

  printMannwhitneyu(AA, BA, histSets)
  printMannwhitneyu(BB, BA, histSets)

printTests()


def stats(set, proto):
  set = removeItem(set, 4)
  data = fromHistToData(set)
  m = mean(data)
  std = stdev(data)
  print(proto, 'mean', round2dec(m), 'std', round2dec(std))

# stats(histSets[AB], AB)
# stats(histSets[AA], AA)
# stats(histSets[BB], BB)
# stats(histSets[BA], BA)


# boxPlots([histSets[AA], histSets[BB], histSets[BA], histSets[AB]], [AA, BB, BA, AB])
def printBarPlots():
  barPlot(histSets[AB], AB)
  barPlot(histSets[AA], AA)
  barPlot(histSets[BB], BB)
  barPlot(histSets[BA], BA)



maxsum = 2000


print(fligner(histSets[AA], histSets[BB], histSets[AB],histSets[BA],))

totalChallengeForProto = {
  AA: 919,
  AB: 950,
  BB: 941,
  BA: 986,
}


def plotCumSum (data, proto):
  cum = np.cumsum(data)
  max = totalChallengeForProto[proto]
  title = 'Drop-off (-5.) for prototype - '
  title = 'Drop-off for prototype - '
  barPlot(max - cum, proto, 986, title)


def printBarPlotsNoFriction():
  print(len(histSets[AB]))
  print(len(removeItem(histSets[AB], 4)))
  plotCumSum(removeItem(histSets[AB], 4), AB)
  plotCumSum(removeItem(histSets[AA], 4), AA)
  plotCumSum(removeItem(histSets[BB], 4), BB)
  plotCumSum(removeItem(histSets[BA], 4), BA)

# printBarPlotsNoFriction()

#
# barPlot(histSets[AB], AB)
# barPlot(histSets[AA], AA)
# barPlot(histSets[BB], BB)
# barPlot(histSets[BA], BA)


