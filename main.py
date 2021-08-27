# $('.yaxislayer-above').style.transform = "translateX(-10px)"

from tools import round2dec, getDropOff
from plotly import graph_objects as go


fig = go.Figure()

x1 = [415, 0, 220, 155],
x2 = [501, 365, 319, 222,],
x3 = [720, 446, 430, 61],
x4 = [399, 214, 133, 121,],

y1=[668, 303, 93, 71],
y2=[651, 398, 274, 172, ],
y3=[498, 423, 310, 17],
y4=[218, 176, 117, 109, ],


def newNumbers():
    steps = ['Entering intro screen', 'Starting intro chat', 'Starting input cards', 'Completed challenge']

    fig.add_trace(go.Funnel(
        name='No paper ads',
        orientation="h",
        y=steps,
        x=[668,303,93, 71],
        textposition="inside",
        textinfo="value+percent initial"))

    fig.add_trace(go.Funnel(
        name='Citizen Proposal',
        orientation="h",
        y=steps,
        x=[651, 398, 274, 172, ],
        textposition="inside",
        textinfo="value+percent initial"))

    fig.add_trace(go.Funnel(
        name='Switch electricy',
        y=steps,
        x=[498, 423, 310, 17],
        textinfo="value+percent initial"))


    fig.add_trace(go.Funnel(
        name='Flight free',
        orientation="h",
        y=steps,
        x=[218, 176, 117, 109, ],
        textposition="inside",
        textinfo="value+percent initial"))

def baselineNumbers():
    steps = ['Entering intro screen', 'Starting intro cards', 'Starting input cards', 'Completed challenge']

    fig.add_trace(go.Funnel(
        name = 'No paper ads',
        orientation = "h",
        y = steps,
        x = [415, None, 220, 155],
        textposition = "inside",
        textinfo = "value+percent initial"))

    fig.add_trace(go.Funnel(
        name = 'Citizen Proposal',
        orientation = "h",
        y = steps,
        x = [501, 365, 319, 222,],
        textposition = "inside",
        textinfo = "value+percent initial"))


    fig.add_trace(go.Funnel(
        name = 'Switch electricy',
        y = steps,
        x = [720, 446, 430, 61],
        textposition="outside",
        textinfo = "value+percent initial"))

    fig.add_trace(go.Funnel(
        name = 'Flight free',
        orientation = "h",
        y = steps,
        x = [399, 214, 133, 121,],
        textposition = "inside",
        textinfo = "value+percent initial"))

    # fig.add_trace(go.Funnel(
    #     name = 'Buy LED quiz',
    #     orientation = "h",
    #     y = steps,
    #     x = [226, 199, 192, 185],
    #     textposition = "inside",
    #     textinfo = "value+percent initial"))
    # #
    # fig.add_trace(go.Funnel(
    #     name = 'Buy LED challenge',
    #     orientation = "h",
    #     y = steps,
    #     x = [176, None, None, 137,],
    #     textposition = "inside",
    #     textinfo = "value+percent initial"))
    #




# baselineNumbers()
# newNumbers()

#fig.show()

