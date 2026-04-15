class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        flag = [0]*len(strs)
        answer = []

        for i in range(0, len(strs)):
            if flag[i] == 0:
                sub_answer = []
                sub_answer.append(strs[i])
                flag[i] = 1
                for j in range(i+1, len(strs)):
                    if Counter(strs[i]) == Counter(strs[j]):
                        sub_answer.append(strs[j])
                        flag[j] = 1
                answer.append(sub_answer)

        return answer
        