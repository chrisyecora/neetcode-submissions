class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs_needed = [0] * numCourses
        adj = defaultdict(list)
        for i in range(len(prerequisites)):
            course, prereq = prerequisites[i]
            adj[prereq].append(course)
            prereqs_needed[course] += 1
        

        q = deque()
        for i in range(len(prereqs_needed)):
            if not prereqs_needed[i]:
                q.append(i)
        

        
        count = 0
        while q:
            currCourse = q.popleft()
            count += 1
            for course in adj[currCourse]:
                prereqs_needed[course] -= 1
                if prereqs_needed[course] == 0:
                    q.append(course)

        return count == numCourses
