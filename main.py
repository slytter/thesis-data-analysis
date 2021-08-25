# $('.yaxislayer-above').style.transform = "translateX(-10px)"

from plotly import graph_objects as go

steps = ['Entering intro screen', 'Starting informational cards', 'Starting input cards', 'Completed challenge']

fig = go.Figure()

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
    textinfo = "value+percent initial"))

fig.add_trace(go.Funnel(
    name = 'Flight free',
    orientation = "h",
    y = steps,
    x = [399, 214, 133, 121,],
    textposition = "inside",
    textinfo = "value+percent initial"))

fig.add_trace(go.Funnel(
    name = 'Buy LED quiz',
    orientation = "h",
    y = steps,
    x = [226, 199, 192, 185],
    textposition = "inside",
    textinfo = "value+percent initial"))
#
fig.add_trace(go.Funnel(
    name = 'Buy LED challenge',
    orientation = "h",
    y = steps,
    x = [176, None, None, 137,],
    textposition = "inside",
    textinfo = "value+percent initial"))
#
#
#





fig.show()

