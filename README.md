# To Start Project

```
$> run python grid.py
```

## Data Structures Adopted

 - **Priority Queue**: a `priority queue` was used to bubble nodes with the shortset `f score` to the top 
 - **Sets** : python `set` was used to fast look up to be sure we don't reconsider a node already in consideration
 - **Dictionary**: were used to store all possible nodes under consideration and update values of `f` and `g` `scores`

## Comparison function used
the comparison function 
```
 def __lt__(self, other):
        x1, y1 = self.get_pos()
        x2, y2 = other.get_pos()
        diff = (x1 - x2) + (y1 - y2)
        if diff > 0:
            return True
        return False
```
is used as a comparison between two nodes 

The **heuristic function** `h(p1,p2)` is calculated based on **Manhattan Distance** .

The **Manhattan Distance** is defined as such; the distance between two points measured along axes at right angles. In a plane with p1 at `(x1, y1)` and p2 at `(x2, y2)`, it is `|x1 - x2| + |y1 - y2|`.

```
def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)
```

although the function `h` can be modified the heuristic solution for any node `n` must be less than or equal to
the actual distance between any node `n` and the end node `e` for a valid `h(n,e)`. 