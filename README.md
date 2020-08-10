# To Start Project

```
$> run python grid.py
```

## Data Structures Adobpted

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