import statistics
import matplotlib.pyplot as plt
import numpy as np
import math


HEADER = "CCF / LF"
BA = 'CCF+NONE'
AB = 'NONE+LF'
BB = 'CCF+LF'
AA = 'NONE+NONE'


colors = {
  HEADER: 'black',
  BA: '#27AE60',
  AB: '#F7A302',
  BB: '#1D758E',
  AA: '#F9B6AA',
}

def hist(data):
  plt.hist(data, bins=len(data))
  plt.show()
  plt.clf()

def round2dec(number, round = 2):
  return math.ceil(number * (10 ** round)) / (10 ** round)


def removeItem(data, item):
  items = data.copy()
  del items[item]
  return items

def boxPlots (histData, labels):
  data_to_plot = list(map(fromHistToData, histData))
  # Create a figure instance
  fig = plt.figure(1, figsize=(9, 6), )
  # Create an axes instance
  # Create the boxplot
  plt.xlabel("Prototype")
  plt.ylabel("N challenges completed")
  ax = fig.add_subplot(111)
  bp = ax.boxplot(data_to_plot)
  plt.xticks(list(range(1, len(histData) + 1)), labels)

  plt.savefig('/Users/macbook/PycharmProjects/funnel-plotting/boxPlot.png', bbox_inches='tight', dpi=150)
  plt.show()
  plt.clf()

  # fig.savefig('fig1.png', bbox_inches='tight')

def toInt(_list):
  return list(map(int, _list))

def getDropOff (set):
  return list(-np.diff(set))

def fromHistToDataSelfmade(data):
  challenges = []
  for i in range (len(data)):
    amountOfPeople = data[i]
    amountOfChallenges = i + 1
    for person in range(amountOfPeople):
      challenges.append(amountOfChallenges)
  return challenges

def fromHistToData(counts):
  index = 0
  extendedList = []
  for num in counts:
    extendedList.extend([index] * num)
    index = index + 1
  return extendedList


def isSimiliar(data1, data2, what):
  if(data1 == data2):
    print(what, 'has equal results, they are:', data1)
  else:
    print(what, 'are not equal, they are:', data1, data2)

def get_stats(counts):
  mean = statistics.mean(counts)
  stdev = statistics.stdev(counts)
  print('mean: ')
  print(mean)
  print('standard deviation: ')
  print(stdev)
  print('num users: ')
  print(len(counts))

def barPlot(counts, protoType, maxValue = 300, title ="Challenge completed per user - "):
  x = list(range(0, len(counts)))

  #x_pos = [i for i, _ in enumerate(x)]

  plt.bar(x, counts, color=colors[protoType])
  plt.xlabel("N challenges completed", fontsize=13)
  plt.ylabel("N users", fontsize=13)
  plt.title(title + protoType, fontsize=15)

  plt.xticks(x, x)
  plt.ylim(0, maxValue)

  plt.savefig('/Users/macbook/PycharmProjects/funnel-plotting/barPlots' + protoType + '.png', bbox_inches='tight', dpi=150)
  plt.clf()

def lineChart (histData, labels):
  data_to_plot = list(map(fromHistToData, histData))
  # Create a figure instance
  fig = plt.figure(1, figsize=(9, 6), )
  # Create an axes instance
  # Create the boxplot

  ax = fig.add_subplot(111)
  bp = ax.boxplot(data_to_plot, showmeans=True)
  plt.xlabel("N challenges completed")
  plt.ylabel("N users")

  plt.xticks(list(range(1, len(histData) + 1)), labels)

  plt.savefig('/Users/macbook/PycharmProjects/funnel-plotting/boxPlot.png', bbox_inches='tight', dpi=150)
  plt.show()
  plt.clf()

  # fig.savefig('fig1.png', bbox_inches='tight')


def combine(list1, list2):
  index = 0
  list = []
  for i in list1:
    list.append(i + list2[index])
    index = index + 1
  return list


