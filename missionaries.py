from __future__ import annotations
from typing import List, Optional
from BFS_Search import node_to_path, bfs

MAX_NUM = 3

class MCState:
    def __init__(self, missionaries: int, cannibals: int, boat: bool) -> None:
        self.wm = missionaries # West bank missionaries
        self.wc = cannibals # West bank cannibals
        self.em = MAX_NUM - self.wm # East bank missionaries
        self.ec = MAX_NUM - self.wc # East bank cannibals
        self.boat = boat
        
    def __str__(self) -> str:
        return ("On the west bank there are {} missionaries and {} cannibals. \n"
                "On the the east bank there are {} missionaries and {} cannibals. \n"
                "The boat is on the {} bank.")\
                    .format(self.wm, self.wc, self.em, self.ec, ("west" if self.boat else "east"))
    
    def goal_test(self) -> bool:
        return self.is_legal and self.em == MAX_NUM and self.ec == MAX_NUM
    
    @property
    def is_legal(self) -> bool:
        if self.wm < self.wc and self.wm > 0:
            return False
        if self.em < self.ec and self.em > 0:
            return False
        return True
        
        # Verbose move check
    def successors(self) -> List[MCState]:
        sucs = []
        if self.boat: # boat is on the west bank
            if self.wm > 1:
                sucs.append(MCState(self.wm - 2, self.wc, not self.boat))
            if self.wm > 0:
                sucs.append(MCState(self.wm - 1, self.wc, not self.boat))
            if self.wc > 1:
                sucs.append(MCState(self.wm, self.wc - 2, not self.boat))
            if self.wc > 0:
                sucs.append(MCState(self.wm, self.wc - 1, not self.boat))
            if (self.wc > 0) and (self.wm > 0):
                sucs.append(MCState(self.wm - 1, self.wc - 1, not self.boat))
        else: # boat is on the east bank
            if self.em > 1:
                sucs.append(MCState(self.wm + 2, self.wc, not self.boat))
            if self.em > 0:
                sucs.append(MCState(self.wm + 1, self.wc, not self.boat))
            if self.ec > 1:
                sucs.append(MCState(self.wm, self.wc + 2, not self.boat))
            if self.ec > 0:
                sucs.append(MCState(self.wm, self.wc + 1, not self.boat))
            if (self.em > 0) and (self.ec > 0):
                sucs.append(MCState(self.wm + 1, self.wc + 1, not self.boat))
        return [x for x in sucs if x.is_legal]
    
def display_solution(path: List[MCState]):
    if len(path) == 0: # sanity check
        return
    
    old_state = path[0]
    print(old_state)
    
    for current_state in path[1:]:
        if current_state.boat:
            print("{} missionaries and {} cannibals moved from the east bank to the west bank. \n"
                    .format(old_state.em - current_state.em, old_state.ec - current_state.ec))
        else:
            print("{} missionaries and {} cannibals moved from the west bank to the east bank. \n"
                  .format(old_state.wm - current_state.wm, old_state.wc - current_state.wc))

        print(current_state)
        old_state = current_state

if __name__ == '__main__':
    start = MCState(MAX_NUM, MAX_NUM, True)
    solution = bfs(start, MCState.goal_test, MCState.successors)
    if solution is None:
        print("No Solution Found!")
    else:
        path = node_to_path(solution)
        display_solution(path)
