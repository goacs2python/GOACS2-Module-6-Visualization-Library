# Run this file to test your library functions.

from visualization import *
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
import random
import numpy as np

def randomcolor():
    return (random.randint(50,255),random.randint(50,255),random.randint(50,255))
# specific color names can be found at https://www.w3schools.com/colors/colors_groups.asp

# Sets of random data in different distributions
randomdata = []
for i in range(20):
    randomdata.append(random.randint(-10,10))
randomlow = min(randomdata)
randomhigh = max(randomdata)
normaldistdata = []
for i in range(500):
    normaldistdata.append(np.random.normal(-3,5))
normallow = min(normaldistdata)
normalhigh = max(normaldistdata)
poissondistdata = []
for i in range(500):
    poissondistdata.append(np.random.poisson(2))
poissonlow = min(poissondistdata)
poissonhigh = max(poissondistdata)


# Box and Whisker Plot Tests
boxplotsfig = figure(title="Boxplots graph")

boxplotdata1 = [1,2,3,4,5,6]
boxplotdata2 = [1,3,5,7,9,15]
boxplotdata3 = [0,-8,-12,-16,-17]

boxplot(boxplotdata1,1,"orange",boxplotsfig)
boxplot(boxplotdata2,3,"green",boxplotsfig)
boxplot(boxplotdata3,11,randomcolor(),boxplotsfig)
boxplot(randomdata,5,(17,168,103),boxplotsfig)
boxplot(normaldistdata,7,(255,51,221),boxplotsfig)
boxplot(poissondistdata,9,'#084594',boxplotsfig)

histfig1 = figure(title="Random Histogram")
histfig2 = figure(title="Normal Histogram")
histfig3 = figure(title="Poisson Histogram")

histogram(randomdata,10,(-10,10),"yellow",histfig1)
histogram(normaldistdata,10,(normallow,normalhigh),'#4f0e37',histfig2)
histogram(poissondistdata,8,(poissonlow,poissonhigh),randomcolor(),histfig3)


# Pie Chart Tests
piechartf1 = figure(title="Pie Chart 1")

piechartdata1 = [5,8,6,2]
piechartnames1 = ["a","b","c","d"]
piechartcolors1 = [randomcolor(),randomcolor(),randomcolor(),randomcolor()]

piechart(piechartdata1,piechartnames1,piechartcolors1,1,1,piechartf1)

piechartf2 = figure (title="Pie Chart 2")

piechartdata2 = [random.randint(1,5),random.randint(1,5),random.randint(1,5),random.randint(1,5),random.randint(1,5)]
piechartnames2 = ["Windows","macOS","Linux","ChromeOS","Other"]
piechartcolors2 = ["blue","grey","red","yellow","purple"]

piechart(piechartdata2,piechartnames2,piechartcolors2,25,3,piechartf2)


# Scatter Plot Tests
scatterplotf = figure(title="Scatterplot")

scatterplotx = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1, 23.4, 18.1, 22.6, 17.2]
scatterploty = [215, 325, 185, 332, 406, 522, 412, 614, 543, 421, 445, 408]
scatterplotsizes = [10]*len(scatterplotx)
scatterplotcolors = ["MediumSeaGreen"]*len(scatterplotx)

scatterplot(scatterplotx,scatterploty,scatterplotsizes,scatterplotcolors,scatterplotf)

scatterplotf2 = figure(title="Varied Scatterplot")

scatterplotx2 = normaldistdata
scatterploty2 = poissondistdata
scatterplotsizes2 = []
for point in normaldistdata:
    scatterplotsizes2.append(point+25)
scatterplotcolors2 = []
for point in poissondistdata:
    scatterplotcolors2.append((int(255*(point/poissonhigh)),0,0))

scatterplot(scatterplotx2,scatterploty2,scatterplotsizes2,scatterplotcolors2,scatterplotf2)


# Showing all of the plots
grid = gridplot([[boxplotsfig, histfig1],[histfig2,histfig3],[piechartf1,piechartf2],[scatterplotf,scatterplotf2]])

show(grid)
