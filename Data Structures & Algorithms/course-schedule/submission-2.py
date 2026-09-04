class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        graph = defaultdict(list)
        for i in range(len(prerequisites)):
            course, prereq = prerequisites[i]
            graph[prereq].append(course)
            in_degree[course] += 1

        q = deque()
        for i in range(len(in_degree)):
            if in_degree[i] == 0:
                q.append(i)

        count = 0
        while q:
            currCourse = q.popleft()
            count += 1
            for nextClass in graph[currCourse]:
                in_degree[nextClass] -= 1
                if in_degree[nextClass] == 0:
                    q.append(nextClass)



        return count == numCourses