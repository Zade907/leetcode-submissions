class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        list1 = sentence.split(" ")
        flag = False
        first = list1[0]
        last = list1[len(list1)-1]
        for i in range (len(list1)-1):
            temp = list1[i]
            temp1 = list1[i+1]
            char = temp[len(temp)-1]
            if(char==temp1[0]):
                flag = True
            else:
                flag = False 
                break
        if(first[0]!=last[len(last)-1]):
            flag = False
        
        if(len(list1)==1 and sentence[0]==sentence[len(sentence)-1]):
            flag = True
        return flag
