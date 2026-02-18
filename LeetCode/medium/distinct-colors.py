class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors_tracker = {}
        balls_tracker = {}
        results = []
        for query in queries:
            target = query[0]
            color = query[1] 
            if color not in colors_tracker.keys() and target not in balls_tracker.keys():
            # new color new target
                if len(results)>0:
                    results.append(results[-1]+1)
                else:
                    results.append(1)
                colors_tracker[color] = set()
                colors_tracker[color].add(target)
                balls_tracker[target]=color
                continue
            if target in balls_tracker.keys() and color not in colors_tracker.keys():
                # target already colored, but the color is new
                if len(colors_tracker[balls_tracker[target]]) == 1: 
                    # the target was the only one having that color
                    results.append(results[-1])
                else:
                    # the target isn't the only one and the color is new
                    results.append(results[-1]+1)
                colors_tracker[balls_tracker[target]].discard(target)
                if len(colors_tracker[balls_tracker[target]]) == 0:
                    del colors_tracker[balls_tracker[target]]
                colors_tracker[color]=set()
                colors_tracker[color].add(target)
                balls_tracker[target]=color
                continue
            
            if target not in balls_tracker.keys() and color in colors_tracker.keys():
                # meaning the color exists, the target is new
                results.append(results[-1])
                colors_tracker[color].add(target)
                balls_tracker[target]=color
                continue

            if target  in balls_tracker.keys() and color in colors_tracker.keys():  
                # target exists, the color exists
                if color == balls_tracker[target]:
                    # recolor with the same color
                    results.append(results[-1])
                    continue
                if len(colors_tracker[balls_tracker[target]]) == 1:
                    # the target is the only one having that color
                    results.append(results[-1]-1)
                    
                else: 
                    # the target isn't the only one with that color, the color isn't new either, nothing changes
                    results.append(results[-1])
                
                colors_tracker[balls_tracker[target]].discard(target)
                if len(colors_tracker[balls_tracker[target]]) == 0:
                    del colors_tracker[balls_tracker[target]]
                colors_tracker[color].add(target)
                balls_tracker[target]=color
            
        return results