import csv
import statistics
from statistics import stdev

import numpy as np
from numpy import mean
from numpy.matlib import randn

from tools import round2dec, fromHistToData


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

