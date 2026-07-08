from collections import defaultdict, deque
class DependencyPlanner:
   def build_plan(self, classes):
       graph = defaultdict(list)
       indegree = defaultdict(int)
       # Initialize graph
       for cls in classes:
           graph[cls.name]
           indegree[cls.name]
       # Build dependency graph
       for cls in classes:
           if cls.extends:
               graph[cls.extends].append(cls.name)
               indegree[cls.name] += 1
       # Topological sort
       queue = deque()
       for cls in classes:
           if indegree[cls.name] == 0:
               queue.append(cls.name)
       order = []
       while queue:
           current = queue.popleft()
           order.append(current)
           for child in graph[current]:
               indegree[child] -= 1
               if indegree[child] == 0:
                   queue.append(child)
       return order