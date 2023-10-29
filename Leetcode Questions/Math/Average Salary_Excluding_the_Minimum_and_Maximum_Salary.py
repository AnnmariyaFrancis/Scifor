"""You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

 """
class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        salary_copy = []
        for i in salary:
            salary_copy.append(float(i))
        salary_copy.remove(min(salary_copy))
        salary_copy.remove(max(salary_copy))
        total = sum(salary_copy)
        length=len(salary_copy)
        average =div(total,length)
        return average

s1=Solution()
s1.average