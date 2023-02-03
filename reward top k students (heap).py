class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str],
                    student_id: List[int], k: int) -> List[int]:
        pq = []
        pos, neg = set(), set()
        for word in positive_feedback:
            pos.add(word)
        for word in negative_feedback:
            neg.add(word)

        for i, sentence in enumerate(report):
            lst = sentence.split(" ")
            points = 0
            for word in lst:
                if word in pos:
                    points += 3
                elif word in neg:
                    points -= 1
            heapq.heappush(pq, (-1 * points, student_id[i]))

        res = []
        while pq and k > 0:
            point, stu_id = heapq.heappop(pq)
            # print(point, stu_id)
            res.append(stu_id)
            k -= 1

        return res
