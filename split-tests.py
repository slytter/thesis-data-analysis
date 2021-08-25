from matplotlib import pyplot
import numpy as np
from tools import removeItem, HEADER,BA,AB,BB,AA, get_stats, barPlot, combine, fromHistToData, boxPlots, hist, toInt, getDropOff
import matplotlib.pyplot as plt
from scipy import stats
import csv
from statistics import mean

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


def printMannwhitneyu(experiment, control, set):
  x = set[experiment]
  y = set[control]
  result = stats.mannwhitneyu(fromHistToData(x), fromHistToData(y), alternative='two-sided')
  if(result.pvalue < 0.05):
    if(mean(x) > mean(y)):
      print(experiment, 'is significantly larger than', control, 'p', result.pvalue)
    else:
      print(control, 'is significantly larger than', experiment, 'p', result.pvalue)
  else:
    pass
    # print('No significant difference found between ', experiment, 'and', control, 'p-value: ', result.pvalue)


histSets = {}
for key in sets.keys():
  dropOffs = getDropOff(sets[key])
  histSets[key] = removeItem(dropOffs, 4)


printMannwhitneyu(BB, AA, histSets)
printMannwhitneyu(BA, AB, histSets)

printMannwhitneyu(AB, AA, histSets)
printMannwhitneyu(AB, BB, histSets)

printMannwhitneyu(BA, AA, histSets)
printMannwhitneyu(BA, BB, histSets)

boxPlots([histSets[BA], histSets[AB]])
barPlot(histSets[AB], AB)

# hist(fromHistToData(abCounts))
# print(statistics.stdev(fromHistToData(aaCounts)))


def createDistributions ():
  # none none
  aaCounts = [64, 50, 71, 63, 75, 56, 36, 51, 61, 38, 30, 42, 40, 24, 35, 19, 27, 22, 13, 20, 17, 13, 9]

  # chained none
  abCounts = [86, 84, 53, 92, 240, 50, 19, 27, 35, 17, 16, 4, 6, 8, 19, 20, 13, 15, 26, 34, 16, 23, 9]

  # none locked
  baCounts = [72, 63, 56, 71, 127, 51, 40, 71, 37, 34, 18, 25, 17, 33, 31, 18, 29, 36, 29, 27, 25, 16, 12]

  # chained locked
  bbCounts = [74, 54, 47, 88, 208, 40, 23, 37, 34, 9, 15, 12, 5, 22, 24, 15, 20, 18, 47, 40, 40, 20, 18]

  aa = fromHistToData(aaCounts)
  print('aa')
  get_stats(aa)
  barPlot(aaCounts)

  ab = fromHistToData(abCounts)
  print('Chained: a; Unlock: b')
  get_stats(ab)
  barPlot(abCounts)

  ba = fromHistToData(baCounts)
  print('Chained: b; Unlock: a')
  get_stats(ba)
  barPlot(baCounts)

  bb = fromHistToData(bbCounts)
  print('bb')
  get_stats(bb)
  barPlot(bbCounts)




  print('Chained: a')
  aCounts = combine(aaCounts, abCounts)
  a = fromHistToData(aCounts)
  get_stats(a)
  barPlot(aCounts)

  print('Chained: b')
  bCounts = combine(baCounts, bbCounts)
  b = fromHistToData(bCounts)
  get_stats(b)
  barPlot(bCounts)

  print('aa vs ba (none, none vs chained no lock)')
  aCounts = combine(aaCounts, baCounts)
  a = fromHistToData(aCounts)
  get_stats(a)
  barPlot(aCounts)

  print('Unlocked: b')
  bCounts = combine(abCounts, bbCounts)
  b = fromHistToData(bCounts)
  get_stats(b)
  barPlot(bCounts)

