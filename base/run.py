# Search methods

from base import search

start = "\033[1m"
end = "\033[0;0m"

ab = search.GPSProblem('A', 'B'
                       , search.romania)
lf = search.GPSProblem('L', 'F'
                       , search.romania)
eo = search.GPSProblem('E', 'O'
                       , search.romania)
tp = search.GPSProblem('T', 'P'
                       , search.romania)



# print("Recorrido del árbol en " + start + "profundidad\n"+ end)
# x=search.breadth_first_graph_search(ab)
# print("\n")
# print(x.path(),"Coste : ",x.path_cost,". Altura del árbol: ",x.depth,"\n\n\n\n")
#
# print("Recorrido del árbol en " + start + "altura\n"+ end)
# x=search.depth_first_graph_search(ab)
# print("\n")
# print(x.path(),"Coste : ",x.path_cost,". Altura del árbol: ",x.depth,"\n\n\n\n")

print("Recorrido del árbol con el " + start + "algoritmo de ramificacion y acotacion\n"+ end)
x=search.ramificacionyacotacion(ab)
print("\n",x.path(),"Coste : ",x.path_cost,". Altura del árbol: ",x.depth,"\n\n\n\n")

print("Recorrido del árbol con el " + start + "algoritmo de ramificacion y acotacion con subestimacion (heurística)\n"+ end)
x=search.ramificacionyacotacionconsubestimacion(ab)
print("\n",x.path(),"Coste : ",x.path_cost,". Altura del árbol: ",x.depth,"\n\n\n\n")

print("Recorrido del árbol con el " + start + "algoritmo de ramificacion y acotacion\n"+ end)
x=search.ramificacionyacotacion(lf)
print("\n",x.path(),"Coste : ",x.path_cost,". Altura del árbol: ",x.depth,"\n\n\n\n")

print("Recorrido del árbol con el " + start + "algoritmo de ramificacion y acotacion con subestimacion (heurística)\n"+ end)
x=search.ramificacionyacotacionconsubestimacion(lf)
print("\n",x.path(),"Coste : ",x.path_cost,". Altura del árbol: ",x.depth,"\n\n\n\n")

print("Recorrido del árbol con el " + start + "algoritmo de ramificacion y acotacion\n"+ end)
x=search.ramificacionyacotacion(eo)
print("\n",x.path(),"Coste : ",x.path_cost,". Altura del árbol: ",x.depth,"\n\n\n\n")

print("Recorrido del árbol con el " + start + "algoritmo de ramificacion y acotacion con subestimacion (heurística)\n"+ end)
x=search.ramificacionyacotacionconsubestimacion(eo)
print("\n",x.path(),"Coste : ",x.path_cost,". Altura del árbol: ",x.depth,"\n\n\n\n")

print("Recorrido del árbol con el " + start + "algoritmo de ramificacion y acotacion\n"+ end)
x=search.ramificacionyacotacion(tp)
print("\n",x.path(),"Coste : ",x.path_cost,". Altura del árbol: ",x.depth,"\n\n\n\n")

print("Recorrido del árbol con el " + start + "algoritmo de ramificacion y acotacion con subestimacion (heurística)\n"+ end)
x=search.ramificacionyacotacionconsubestimacion(tp)
print("\n",x.path(),"Coste : ",x.path_cost,". Altura del árbol: ",x.depth,"\n\n\n\n")

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
