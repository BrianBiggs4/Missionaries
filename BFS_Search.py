from __future__ import annotations
from typing import TypeVar, Generic, List, Callable, Optional, Deque

T = TypeVar('T')

class Queue(Generic[T]):
    def __init__(self) -> None:
        self._container = Deque()

    @property
    def empty(self) -> bool:
        return not self._container # Not is true for empty container
    
    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> None:
        return self._container.popleft() # FIFO

    def __repr__(self) -> str:
        return (repr(self._container))
    
    # Node acts as a wrapper around a state. Node that a state came from is its parent. 
class Node(Generic[T]):
    def __init__(self, state: T, parent: Optional[Node], cost: float = 0.0, heuristic: float = 0.0) -> None:
        self.state = state
        self.parent = parent

def bfs(initial: T, goal_test: Callable[[T], bool], successors: Callable[[T], List[T]]) -> Optional[Node[T]]:
    # Frontier is where we've yet to go
    frontier = Queue()
    frontier.push(Node(initial, None))

    # Explored is where we've been
    explored = {initial}
    
    # Keep going while there is more to explore
    while not frontier.empty:
        current_node = frontier.pop()
        current_state = current_node.state
        
        # If we found the goal, we're done
        if goal_test(current_state):
            return current_node
        
        # Check where we can go next and haven't explored
        for child in successors(current_state):
            if child in explored:   # Skip children we already explored
                continue
            explored.add(child)
            frontier.push(Node(child, current_node))
    return None     # Went through everything and didn't find goal

def node_to_path(node: Node[T]) -> List[T]:
    path = [node.state]
    
    # work backwards from end to front
    while node.parent is not None:
        node = node.parent
        path.append(node.state)
    path.reverse()
    return path
    
