import numpy as np

class Grid:
    def __init__(self,cost_array,moveprob):
        self.cost_array = cost_array
        self.moveprob = moveprob
        self.g = 1

    def isOutOfRange(self,i,length):
        if i < 0 or i>=length:
            return True


    def CalcValueFunction(self,arr):
        temp = [[0 for i in range(len(self.cost_array[j]))]for j in range(len(self.cost_array))]
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                left = i-1
                right = i+1
                up = j-1
                down = j+1
                if(self.isOutOfRange(left,len(arr)) is True): left = i
                if(self.isOutOfRange(right,len(arr)) is True): right = i
                if(self.isOutOfRange(up,len(arr)) is True): up = j
                if(self.isOutOfRange(down,len(arr)) is True): down = j

                if arr[i][j] ==-10:
                    temp[i][j]=-10
                elif  arr[i][j] ==50:
                    temp[i][j] =50
                else:
                    temp[i][j]= self.moveprob["up"] *(arr[i][up]+ self.g * self.cost_array[i][up]) + \
                        self.moveprob["down"] *(arr[i][down]+ self.g * self.cost_array[i][down])+\
                        self.moveprob["right"] *(arr[right][j]+self.g * self.cost_array[right][j])+\
                        self.moveprob["left"] *(arr[left][j] +self.g * self.cost_array[left][j])
       
        return temp   

                
    def CalcFunc(self,arr,iterations = 2):
        myarr = self.cost_array
        
        for _ in range(iterations):
            myarr= self.CalcValueFunction(arr)
            arr = np.array(myarr)
            
            #print("The formated array is\n ",arr)
            #print(arr)
            #print('\n','===================================================================')
        return arr


    #Create a function that spots the greedy solutino

    def FindGreedySolution(self,array,mem):
        solutionIndex = 0
        movei,movej=0,0
        
        count =0
        list = []
        while solutionIndex!=50:
            right = movei+1
            left = movei-1
            up = movej-1
            down = movej+1
            if self.isOutOfRange(left,len(array[0])) is True: left = movei
            if self.isOutOfRange(right,len(array[0])) is True: right = movei
            if self.isOutOfRange(up,len(array)) is True: up = movej
            if self.isOutOfRange(down,len(array)) is True: down = movej

            moves =[array[left,movej],array[right,movej],array[movei,down],array[movei,up]]
            solutionIndex = max(moves)
            posLi = moves.index(solutionIndex)
            #print("Found the best path:",solutionIndex)
            tempos =0
            
            if posLi ==0:
            
                list.append([left,movej])
                movei = left
                #print("The array is :",array[movei,movej])
                if mem.Search_tree(array[movei,movej]) is False:
                    print("FOUND")
                    movei = right
                else:
                    
                    mem.insert([movei,movej],array[movei,movej])
            elif posLi==1:
                list.append([right,movej])
                movei = right
                #print("The array is :",array[movei,movej])
                if mem.Search_tree(array[movei,movej]) is False:
                    print("FOUND")
                    movei=left
                else:
                    mem.insert([movei,movej],array[movei,movej])      

            elif posLi==2:
                list.append([movei,down])
                movej=down
                #print("The array is :",array[movei,movej])
                if mem.Search_tree(array[movei,movej]) is False:
                    print("FOUND")
                    movej=up
                else:
                    mem.insert([movei,movej],array[movei,movej])  
            else:
                list.append([movei,up])
                movej=up
                #print("The array is :",array[movei,movej])
                if mem.Search_tree(array[movei,movej]) is False:
                    print("FOUND")
                    movei=down
                else:
                    mem.insert([movei,movej],array[movei,movej])  
            
            count+=1
            if(count>=1000):
                print("Stuck in circles")
                break
        return list
