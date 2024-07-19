# Water Jug Problem Solution using A* Algorithm with Dijkstra's Heuristic

This is a Python implementation of the classic Water Jug Problem using A* algorithm with Dijkstra's heuristic.

The Water Jug Problem is a classic problem in AI, where the objective is to determine how to measure out a specific quantity of water with two jugs of different sizes. In this implementation, we use A* algorithm with Dijkstra's heuristic to find the shortest possible path to measure out a specific quantity of water.

## Overview
1. The function `a_star` implements the A-star algorithm to solve the Water Jug problem. 
2. Given a tuple `rootNode` representing the initial state of the jugs, 
3. And another tuple `destinationNode` representing the final state, 
3. The function attempts to find a sequence of moves that would take the jugs from the initial state to the final state.


## Breakdown
The algorithm works as follows: 

- it starts with a list of paths containing only the start node. 
- For Each Step: 
  1. it takes the smallest path from the list of paths, 
  2. calculates the possible moves from the last node of this path, 
  3. removes any cycles in the resulting paths, 
  4. calculates the heuristic score for each of these paths. 
        - The heuristic score is calculated by a separate function, `heuristic`, 
        - which adds the length of the path to the sum of the absolute differences between the current node and the final node.
  
  5. The resulting score is added to the length of the path, 
  6. and the path is added to the list of paths. 
  7. If the last node of a path is equal to the destination node, the path is returned as the solution.



There are several helper functions in the code, including:

- `is_empty`: a function that checks if an object is empty.
- `get_smaller_path`: a function that returns the smallest path in a list of paths.
- `pop_smaller_path`: a function that removes the smallest path from a list of paths and returns it.
- `get_last_node`: a function that returns the last node of a path.
- `get_childrens`: a function that calculates the possible moves from a given node.
- `remove_cycles`: a function that removes any cycles from a list of paths.
- `dont_have_path_end_with_node`: a function that checks if a list of paths contains any paths that end with a given node.
- `get_smaller_path_end_with_node`: a function that returns the smallest path in a list of paths that ends with a given node.
- `remove_paths_end_with_node`: a function that removes all paths from a list of paths that end with a given node.

## Output
The code prints out the paths it is currently exploring, so the user can see how the algorithm is progressing.

