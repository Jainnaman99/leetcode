class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        i=0
        j=0
        while(students):
            if(students[i]==sandwiches[j]):
                del students[i]
                del sandwiches[j]
            elif(students[i]!=sandwiches[j] and sandwiches[j] in students):
                students.append(students[i])
                del students[i]
            elif(sandwiches[j] not in students):
                return (len(students))
        return (len(students))