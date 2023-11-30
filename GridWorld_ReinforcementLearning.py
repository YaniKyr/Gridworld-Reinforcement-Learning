import BST as bst
import GridSolver as grd
import matplotlib.pyplot as plt 
import GridGenerator as gnrt
reward = 20

llava = -10
end = 50
g = 0.01

moveprob = {"right":0.3,"left":0.2,"up":0.2,"down":0.3}



#value = b if a > 10 else c
maze1= [[-1,-1,-1],
         [-1,-10,-1],
         [-1,-1,50]]

maze2 = [[-1,-1,-1,-1],
        [-1,-10,-10,-1],
        [-1,-10,-10,-1],
        [-1,-1,-1,50]]
cost1_arr = [[0,0,0],
             [0,0,0],
             [0,0,0]]
temparr = [[0,0,0],
             [0,0,0],
             [0,0,0]]

jLabyr = [[-1,-1,-1,-10,-1,-1,-1,-1,-10,-1],
          [-1,-1,-1,-10,-10,-10,-1,-1,-10,-1],
          [-1,-1,-1,-10,-1,-1,-1,-10,-10,-1],
          [-1,-10,-1,-1,-10,-1,-1,-1,-10,-1],
          [-1,-1,-1,-1,-1,-10,-1,-1,-10,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-10,-1],
          [-1,-1,-10,-1,-1,-1,-10,-1,-10,-1],
          [-10,-10,-10,-1,-1,-1,-10,-1,-1,-1],
          [-1,-1,-1,-10,-10,-10,-10,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,50,-1]]


cost2_arr = [[0,0,0,0],
             [0,0,0,0],
             [0,0,0,0],
             [0,0,0,0]],
jcost = [[0 for i in range(len(jLabyr))]for j in range(len(jLabyr))]


def fMain(arr,costOs):
   
    grid = grd.Grid(costOs,moveprob)

    costOs = grid.CalcFunc(arr,30)


    memo = bst.Tree()
    Sol = grid.FindGreedySolution(costOs,memo)
    #memo.Print_tree()
    #print(Sol)
    arr[0][0] = 30
    #print(np.array(arr))

    plt.imshow(arr)
    #plt.imshow(costOs)
    plt.colorbar()
    
    for sol in Sol:
        plt.scatter(sol[1],sol[0],color = "green")
    
    plt.show()
    print(costOs)
    return costOs

def Main():  
    M =10
    N=10
    lava =20
    endstates = 1
    costarr = [[0 for j in range(M)]for i in range(N)]
    maze = gnrt.GridGenerator(N, M, lava,endstates)

    costHeat = fMain(maze,costarr)
    plt.imshow(costHeat)
    plt.colorbar()
    plt.show()

for i in range(100):

    Main()
    
    if input("Next?   ") == 'Y':
        continue
    else: break

    