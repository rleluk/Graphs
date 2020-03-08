from structures.adjacency_list import AdjacencyList

import tkinter as tk
from math import cos, sin, pi


def create_circle(canvas, x, y, r):
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1, fill="white")


def draw_graph(canvas, graph):
    canvas.delete("all")

    graph_to_draw = graph
    if not isinstance(graph, AdjacencyList):
        graph_to_draw = graph.to_adjacency_list()

    n = len(graph_to_draw.graph)
    center = (canvas.winfo_width() / 2,
              canvas.winfo_height() / 2)  # needed to convert from cartesian to screen coordinates
    r = min(center) / 1.5

    diff_angle = 2 * pi / n
    for i in range(n):
        # calculate node coordinates
        angle = diff_angle * i
        x = center[0] + r * sin(angle)
        y = center[1] - r * cos(angle)

        # drawing edges
        for neighbour in graph_to_draw.graph[i]:
            if neighbour <= i:
                continue
            neighbour_angle = diff_angle * neighbour
            neighbour_x = center[0] + r * sin(neighbour_angle)
            neighbour_y = center[1] - r * cos(neighbour_angle)

            canvas.create_line(x, y, neighbour_x, neighbour_y)

        create_circle(canvas, x, y, r * 0.2)

        canvas.create_text(x, y, text=str(i))