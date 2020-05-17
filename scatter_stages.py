import helper_function, Simulation_Register
import utils
import random
# import important function



def FIFO():

    if Simulation_Register.Stall_Whole_Pipeline["STALL"] == 0:
        if (utils.countforlines("sillygraph.txt") - helper_function.EdgesRead > 8) | (utils.countforlines("sillygraph.txt") - helper_function.EdgesRead == 8):
            helper_function.counter = helper_function.counter + 1 
            EdgeInputFIFO = utils.readFile("sillygraph.txt", helper_function.EdgesRead)
            print(EdgeInputFIFO)
            try:
                Simulation_Register.FIFO_BCR["Edge_SRC_0"] = EdgeInputFIFO[0][0]
                Simulation_Register.FIFO_BCR["Edge_DEST_0"] = EdgeInputFIFO[0][1]
                Simulation_Register.FIFO_BCR["Edge_SRC_1"] = EdgeInputFIFO[1][0]
                Simulation_Register.FIFO_BCR["Edge_DEST_1"] = EdgeInputFIFO[1][1]
                Simulation_Register.FIFO_BCR["Edge_SRC_2"] = EdgeInputFIFO[2][0]
                Simulation_Register.FIFO_BCR["Edge_DEST_2"] = EdgeInputFIFO[2][1]
                Simulation_Register.FIFO_BCR["Edge_SRC_3"] = EdgeInputFIFO[3][0]
                Simulation_Register.FIFO_BCR["Edge_DEST_3"] = EdgeInputFIFO[3][1]
                Simulation_Register.FIFO_BCR["Edge_SRC_4"] = EdgeInputFIFO[4][0]
                Simulation_Register.FIFO_BCR["Edge_DEST_4"] = EdgeInputFIFO[4][1]
                Simulation_Register.FIFO_BCR["Edge_SRC_5"] = EdgeInputFIFO[5][0]
                Simulation_Register.FIFO_BCR["Edge_DEST_5"] = EdgeInputFIFO[5][1]
                Simulation_Register.FIFO_BCR["Edge_SRC_6"] = EdgeInputFIFO[6][0]
                Simulation_Register.FIFO_BCR["Edge_DEST_6"] = EdgeInputFIFO[6][1]
                Simulation_Register.FIFO_BCR["Edge_SRC_7"] = EdgeInputFIFO[7][0]
                Simulation_Register.FIFO_BCR["Edge_DEST_7"] = EdgeInputFIFO[7][1]
                #helper_function.EdgesRead = helper_function.EdgesRead + 8
                #print(helper_function.EdgesRead)
                #print(Simulation_Register.FIFO_BCR)
            except:
                pass
        if utils.countforlines("sillygraph.txt") - helper_function.EdgesRead < 8:
            print("we need " + str(utils.countforlines("sillygraph.txt") - helper_function.EdgesRead) + " to read the rest of the graph")
            helper_function.counter = helper_function.counter + 1
            EdgeInputFIFO = utils.readFiletoEnd("sillygraph.txt")
            print(EdgeInputFIFO)
            try:
                Simulation_Register.FIFO_BCR["Edge_SRC_0"] = EdgeInputFIFO[0][0]
                Simulation_Register.FIFO_BCR["Edge_DEST_0"] = EdgeInputFIFO[0][1]
                Simulation_Register.FIFO_BCR["Edge_SRC_1"] = EdgeInputFIFO[1][0]
                Simulation_Register.FIFO_BCR["Edge_DEST_1"] = EdgeInputFIFO[1][1]
                Simulation_Register.FIFO_BCR["Edge_SRC_2"] = EdgeInputFIFO[2][0]
                Simulation_Register.FIFO_BCR["Edge_DEST_2"] = EdgeInputFIFO[2][1]
                Simulation_Register.FIFO_BCR["Edge_SRC_3"] = EdgeInputFIFO[3][0]
                Simulation_Register.FIFO_BCR["Edge_DEST_3"] = EdgeInputFIFO[3][1]
                Simulation_Register.FIFO_BCR["Edge_SRC_4"] = EdgeInputFIFO[4][0]
                Simulation_Register.FIFO_BCR["Edge_DEST_4"] = EdgeInputFIFO[4][1]
                Simulation_Register.FIFO_BCR["Edge_SRC_5"] = EdgeInputFIFO[5][0]
                Simulation_Register.FIFO_BCR["Edge_DEST_5"] = EdgeInputFIFO[5][1]
                Simulation_Register.FIFO_BCR["Edge_SRC_6"] = EdgeInputFIFO[6][0]
                Simulation_Register.FIFO_BCR["Edge_DEST_6"] = EdgeInputFIFO[6][1]
                Simulation_Register.FIFO_BCR["Edge_SRC_7"] = EdgeInputFIFO[7][0]
                Simulation_Register.FIFO_BCR["Edge_DEST_7"] = EdgeInputFIFO[7][1]
                #print(Simulation_Register.FIFO_BCR)
            except:
                pass

    else:
        helper_function.counter = helper_function.counter + helper_function.STALLCYCLE
        EdgeInputFIFO = utils.readFile("sillygraph.txt", helper_function.EdgesRead)
        #print(EdgeInputFIFO)
        Simulation_Register.FIFO_BCR["Edge_SRC_0"] = 0
        Simulation_Register.FIFO_BCR["Edge_DEST_0"] = 0
        Simulation_Register.FIFO_BCR["Edge_SRC_1"] = 0
        Simulation_Register.FIFO_BCR["Edge_DEST_1"] = 0
        Simulation_Register.FIFO_BCR["Edge_SRC_2"] = 0
        Simulation_Register.FIFO_BCR["Edge_DEST_2"] = 0
        Simulation_Register.FIFO_BCR["Edge_SRC_3"] = 0
        Simulation_Register.FIFO_BCR["Edge_DEST_3"] = 0
        Simulation_Register.FIFO_BCR["Edge_SRC_4"] = 0
        Simulation_Register.FIFO_BCR["Edge_DEST_4"] = 0
        Simulation_Register.FIFO_BCR["Edge_SRC_5"] = 0
        Simulation_Register.FIFO_BCR["Edge_DEST_5"] = 0
        Simulation_Register.FIFO_BCR["Edge_SRC_6"] = 0
        Simulation_Register.FIFO_BCR["Edge_DEST_6"] = 0
        Simulation_Register.FIFO_BCR["Edge_SRC_7"] = 0
        Simulation_Register.FIFO_BCR["Edge_DEST_7"] = 0
        #helper_function.EdgesRead = helper_function.EdgesRead + 8
        #print (helper_function.counter)
        #print(Simulation_Register.FIFO_BCR)

def BCR():
    if Simulation_Register.Stall_Whole_Pipeline["STALL"] == 0:
        Simulation_Register.BCR["Edge_SRC_0"] = Simulation_Register.FIFO_BCR["Edge_SRC_0"]
        Simulation_Register.BCR["Edge_DEST_0"] = Simulation_Register.FIFO_BCR["Edge_DEST_0"]
        Simulation_Register.BCR["Edge_SRC_1"] = Simulation_Register.FIFO_BCR["Edge_SRC_1"]
        Simulation_Register.BCR["Edge_DEST_1"] = Simulation_Register.FIFO_BCR["Edge_DEST_1"]
        Simulation_Register.BCR["Edge_SRC_2"] = Simulation_Register.FIFO_BCR["Edge_SRC_2"]
        Simulation_Register.BCR["Edge_DEST_2"] = Simulation_Register.FIFO_BCR["Edge_DEST_2"]
        Simulation_Register.BCR["Edge_SRC_3"] = Simulation_Register.FIFO_BCR["Edge_SRC_3"]
        Simulation_Register.BCR["Edge_DEST_3"] = Simulation_Register.FIFO_BCR["Edge_DEST_3"]
        Simulation_Register.BCR["Edge_SRC_4"] = Simulation_Register.FIFO_BCR["Edge_SRC_4"]
        Simulation_Register.BCR["Edge_DEST_4"] = Simulation_Register.FIFO_BCR["Edge_DEST_4"]
        Simulation_Register.BCR["Edge_SRC_5"] = Simulation_Register.FIFO_BCR["Edge_SRC_5"]
        Simulation_Register.BCR["Edge_DEST_5"] = Simulation_Register.FIFO_BCR["Edge_DEST_5"]
        Simulation_Register.BCR["Edge_SRC_6"] = Simulation_Register.FIFO_BCR["Edge_SRC_6"]
        Simulation_Register.BCR["Edge_DEST_6"] = Simulation_Register.FIFO_BCR["Edge_DEST_6"]
        Simulation_Register.BCR["Edge_SRC_7"] = Simulation_Register.FIFO_BCR["Edge_SRC_7"]
        Simulation_Register.BCR["Edge_DEST_7"] = Simulation_Register.FIFO_BCR["Edge_DEST_7"]
        #print(Simulation_Register.BCR)
    else:
        Simulation_Register.BCR["Edge_SRC_0"] = 0
        Simulation_Register.BCR["Edge_DEST_0"] = 0
        Simulation_Register.BCR["Edge_SRC_1"] = 0
        Simulation_Register.BCR["Edge_DEST_1"] = 0
        Simulation_Register.BCR["Edge_SRC_2"] = 0
        Simulation_Register.BCR["Edge_DEST_2"] = 0
        Simulation_Register.BCR["Edge_SRC_3"] = 0
        Simulation_Register.BCR["Edge_DEST_3"] = 0
        Simulation_Register.BCR["Edge_SRC_4"] = 0
        Simulation_Register.BCR["Edge_DEST_4"] = 0
        Simulation_Register.BCR["Edge_SRC_5"] = 0
        Simulation_Register.BCR["Edge_DEST_5"] = 0
        Simulation_Register.BCR["Edge_SRC_6"] = 0
        Simulation_Register.BCR["Edge_DEST_6"] = 0
        Simulation_Register.BCR["Edge_SRC_7"] = 0
        Simulation_Register.BCR["Edge_DEST_7"] = 0


def VertexBuffer():
    #Simulation_Register.VBUFF["Edge_SRC_0"] = Simulation_Register.BCR["Edge_SRC_0"]
    Simulation_Register.VBUFF["Edge_DEST_0"] = Simulation_Register.BCR["Edge_DEST_0"]
    #Simulation_Register.VBUFF["Edge_SRC_1"] = Simulation_Register.BCR["Edge_SRC_1"]
    Simulation_Register.VBUFF["Edge_DEST_1"] = Simulation_Register.BCR["Edge_DEST_1"]
    #Simulation_Register.VBUFF["Edge_SRC_2"] = Simulation_Register.BCR["Edge_SRC_2"]
    Simulation_Register.VBUFF["Edge_DEST_2"] = Simulation_Register.BCR["Edge_DEST_2"]
    #Simulation_Register.VBUFF["Edge_SRC_3"] = Simulation_Register.BCR["Edge_SRC_3"]
    Simulation_Register.VBUFF["Edge_DEST_3"] = Simulation_Register.BCR["Edge_DEST_3"]
    #Simulation_Register.VBUFF["Edge_SRC_4"] = Simulation_Register.BCR["Edge_SRC_4"]
    Simulation_Register.VBUFF["Edge_DEST_4"] = Simulation_Register.BCR["Edge_DEST_4"]
    #Simulation_Register.VBUFF["Edge_SRC_5"] = Simulation_Register.BCR["Edge_SRC_5"]
    Simulation_Register.VBUFF["Edge_DEST_5"] = Simulation_Register.BCR["Edge_DEST_5"]
    #Simulation_Register.VBUFF["Edge_SRC_6"] = Simulation_Register.BCR["Edge_SRC_6"]
    Simulation_Register.VBUFF["Edge_DEST_6"] = Simulation_Register.BCR["Edge_DEST_6"]
    #Simulation_Register.VBUFF["Edge_SRC_7"] = Simulation_Register.BCR["Edge_SRC_7"]
    Simulation_Register.VBUFF["Edge_DEST_7"] = Simulation_Register.BCR["Edge_DEST_7"]
    Simulation_Register.VBUFF["Vertex_SRC0"] = 1
    Simulation_Register.VBUFF["Vertex_SRC1"] = 2
    Simulation_Register.VBUFF["Vertex_SRC2"] = 3
    Simulation_Register.VBUFF["Vertex_SRC3"] = 4
    Simulation_Register.VBUFF["Vertex_SRC4"] = 5
    Simulation_Register.VBUFF["Vertex_SRC5"] = 6
    Simulation_Register.VBUFF["Vertex_SRC6"] = 7
    Simulation_Register.VBUFF["Vertex_SRC7"] = 8

def scatter_pipeline():
    Simulation_Register.scatter_pipeline["Update_DEST0"] = 1 * Simulation_Register.VBUFF["Edge_DEST_0"]
    Simulation_Register.scatter_pipeline["Update_DEST1"] = 1 * Simulation_Register.VBUFF["Edge_DEST_1"]
    Simulation_Register.scatter_pipeline["Update_DEST2"] = 1 * Simulation_Register.VBUFF["Edge_DEST_2"]
    Simulation_Register.scatter_pipeline["Update_DEST3"] = 1 * Simulation_Register.VBUFF["Edge_DEST_3"]
    Simulation_Register.scatter_pipeline["Update_DEST4"] = 1 * Simulation_Register.VBUFF["Edge_DEST_4"]
    Simulation_Register.scatter_pipeline["Update_DEST5"] = 1 * Simulation_Register.VBUFF["Edge_DEST_5"]
    Simulation_Register.scatter_pipeline["Update_DEST6"] = 1 * Simulation_Register.VBUFF["Edge_DEST_6"]
    Simulation_Register.scatter_pipeline["Update_DEST7"] = 1 * Simulation_Register.VBUFF["Edge_DEST_7"]
    Simulation_Register.scatter_pipeline["Update0"] = 1 * Simulation_Register.VBUFF["Vertex_SRC0"]
    Simulation_Register.scatter_pipeline["Update1"] = 1 * Simulation_Register.VBUFF["Vertex_SRC1"]
    Simulation_Register.scatter_pipeline["Update2"] = 1 * Simulation_Register.VBUFF["Vertex_SRC2"]
    Simulation_Register.scatter_pipeline["Update3"] = 1 * Simulation_Register.VBUFF["Vertex_SRC3"]
    Simulation_Register.scatter_pipeline["Update4"] = 1 * Simulation_Register.VBUFF["Vertex_SRC4"]
    Simulation_Register.scatter_pipeline["Update5"] = 1 * Simulation_Register.VBUFF["Vertex_SRC5"]
    Simulation_Register.scatter_pipeline["Update6"] = 1 * Simulation_Register.VBUFF["Vertex_SRC6"]
    Simulation_Register.scatter_pipeline["Update7"] = 1 * Simulation_Register.VBUFF["Vertex_SRC7"]
    #print(Simulation_Register.scatter_pipeline)

def Combining_Network():
    A = [int(Simulation_Register.scatter_pipeline["Update_DEST0"]),Simulation_Register.scatter_pipeline["Update0"],int(Simulation_Register.scatter_pipeline["Update_DEST1"]),Simulation_Register.scatter_pipeline["Update1"]]
    B = [int(Simulation_Register.scatter_pipeline["Update_DEST2"]),Simulation_Register.scatter_pipeline["Update2"],int(Simulation_Register.scatter_pipeline["Update_DEST3"]),Simulation_Register.scatter_pipeline["Update3"]]
    C = [int(Simulation_Register.scatter_pipeline["Update_DEST4"]),Simulation_Register.scatter_pipeline["Update4"],int(Simulation_Register.scatter_pipeline["Update_DEST5"]),Simulation_Register.scatter_pipeline["Update5"]]
    D = [int(Simulation_Register.scatter_pipeline["Update_DEST6"]),Simulation_Register.scatter_pipeline["Update6"],int(Simulation_Register.scatter_pipeline["Update_DEST7"]),Simulation_Register.scatter_pipeline["Update7"]]
    #print(A)
    #print(B)
    #print(C)
    #print(D)
    AfterCombine = utils.CompareandCombaine(A,B,C,D)
    #print(AfterCombine)
    Simulation_Register.CN["Update_DEST0"] = AfterCombine[0]
    Simulation_Register.CN["Update0"] = AfterCombine[1]
    Simulation_Register.CN["Update_DEST1"] = AfterCombine[2]
    Simulation_Register.CN["Update1"] = AfterCombine[3]
    Simulation_Register.CN["Update_DEST2"] = AfterCombine[4]
    Simulation_Register.CN["Update2"] = AfterCombine[5]
    Simulation_Register.CN["Update_DEST3"] = AfterCombine[6]
    Simulation_Register.CN["Update3"] = AfterCombine[7]
    Simulation_Register.CN["Update_DEST4"] = AfterCombine[8]
    Simulation_Register.CN["Update4"] = AfterCombine[9]
    Simulation_Register.CN["Update_DEST5"] = AfterCombine[10]
    Simulation_Register.CN["Update5"] = AfterCombine[11]
    Simulation_Register.CN["Update_DEST6"] = AfterCombine[12]
    Simulation_Register.CN["Update6"] = AfterCombine[13]
    Simulation_Register.CN["Update_DEST7"] = AfterCombine[14]
    Simulation_Register.CN["Update7"] = AfterCombine[15]
    i = 0
    j = 0
    for i in range (8):
        if AfterCombine[2*i] == 0:
            j = j + 1
    helper_function.STALLCYCLE = 8 - j
    #return AfterCombine
    #print(Simulation_Register.CN)


def main():
    #i = 0 
    #print(utils.countforlines("sillygraph.txt"))
    while helper_function.EdgesRead < utils.countforlines("sillygraph.txt"):
        
        
        UpdateSillyGraph = open('SillyGraphUpdate.txt','a+')
        FIFO()
        print(Simulation_Register.FIFO_BCR)
        BCR()
        
        VertexBuffer()
        
        scatter_pipeline()
        
        Combining_Network()
       
        if (utils.countforlines("sillygraph.txt") - helper_function.EdgesRead > 8) | (utils.countforlines("sillygraph.txt") - helper_function.EdgesRead == 8) | (utils.countforlines("sillygraph.txt") - helper_function.EdgesRead < 8):
            UpdateSillyGraph.write(str(Simulation_Register.CN["Update_DEST0"]) + ' ' + str(Simulation_Register.CN["Update0"]) + '\n')
            
            UpdateSillyGraph.write(str(Simulation_Register.CN["Update_DEST1"]) + ' ' + str(Simulation_Register.CN["Update1"]) + '\n')
            
            UpdateSillyGraph.write(str(Simulation_Register.CN["Update_DEST2"]) + ' ' + str(Simulation_Register.CN["Update2"]) + '\n')
            
            UpdateSillyGraph.write(str(Simulation_Register.CN["Update_DEST3"]) + ' ' + str(Simulation_Register.CN["Update3"]) + '\n')
            
            UpdateSillyGraph.write(str(Simulation_Register.CN["Update_DEST4"]) + ' ' + str(Simulation_Register.CN["Update4"]) + '\n')
            
            UpdateSillyGraph.write(str(Simulation_Register.CN["Update_DEST5"]) + ' ' + str(Simulation_Register.CN["Update5"]) + '\n')
            
            UpdateSillyGraph.write(str(Simulation_Register.CN["Update_DEST6"]) + ' ' + str(Simulation_Register.CN["Update6"]) + '\n')
            
            UpdateSillyGraph.write(str(Simulation_Register.CN["Update_DEST7"]) + ' ' + str(Simulation_Register.CN["Update7"]) + '\n')
            
            UpdateSillyGraph.close()
            helper_function.EdgesRead = helper_function.EdgesRead + 8
        
        helper_function.counter = helper_function.counter + helper_function.STALLCYCLE
        #Now for simulation we just reset all the register file
        Simulation_Register.FIFO_BCR["Edge_SRC_0"] = 0
        Simulation_Register.FIFO_BCR["Edge_DEST_0"] = 0
        Simulation_Register.FIFO_BCR["Edge_SRC_1"] = 0
        Simulation_Register.FIFO_BCR["Edge_DEST_1"] = 0
        Simulation_Register.FIFO_BCR["Edge_SRC_2"] = 0
        Simulation_Register.FIFO_BCR["Edge_DEST_2"] = 0
        Simulation_Register.FIFO_BCR["Edge_SRC_3"] = 0
        Simulation_Register.FIFO_BCR["Edge_DEST_3"] = 0
        Simulation_Register.FIFO_BCR["Edge_SRC_4"] = 0
        Simulation_Register.FIFO_BCR["Edge_DEST_4"] = 0
        Simulation_Register.FIFO_BCR["Edge_SRC_5"] = 0
        Simulation_Register.FIFO_BCR["Edge_DEST_5"] = 0
        Simulation_Register.FIFO_BCR["Edge_SRC_6"] = 0
        Simulation_Register.FIFO_BCR["Edge_DEST_6"] = 0
        Simulation_Register.FIFO_BCR["Edge_SRC_7"] = 0
        Simulation_Register.FIFO_BCR["Edge_DEST_7"] = 0
        Simulation_Register.BCR["Edge_SRC_0"] = 0
        Simulation_Register.BCR["Edge_DEST_0"] = 0
        Simulation_Register.BCR["Edge_SRC_1"] = 0
        Simulation_Register.BCR["Edge_DEST_1"] = 0
        Simulation_Register.BCR["Edge_SRC_2"] = 0
        Simulation_Register.BCR["Edge_DEST_2"] = 0
        Simulation_Register.BCR["Edge_SRC_3"] = 0
        Simulation_Register.BCR["Edge_DEST_3"] = 0
        Simulation_Register.BCR["Edge_SRC_4"] = 0
        Simulation_Register.BCR["Edge_DEST_4"] = 0
        Simulation_Register.BCR["Edge_SRC_5"] = 0
        Simulation_Register.BCR["Edge_DEST_5"] = 0
        Simulation_Register.BCR["Edge_SRC_6"] = 0
        Simulation_Register.BCR["Edge_DEST_6"] = 0
        Simulation_Register.BCR["Edge_SRC_7"] = 0
        Simulation_Register.BCR["Edge_DEST_7"] = 0
        #Simulation_Register.VBUFF["Edge_SRC_0"] = 0
        Simulation_Register.VBUFF["Edge_DEST_0"] = 0
        #Simulation_Register.VBUFF["Edge_SRC_1"] = 0
        Simulation_Register.VBUFF["Edge_DEST_1"] = 0
        #Simulation_Register.VBUFF["Edge_SRC_2"] = 0
        Simulation_Register.VBUFF["Edge_DEST_2"] = 0
        #Simulation_Register.VBUFF["Edge_SRC_3"] = 0
        Simulation_Register.VBUFF["Edge_DEST_3"] = 0
        #Simulation_Register.VBUFF["Edge_SRC_4"] = 0
        Simulation_Register.VBUFF["Edge_DEST_4"] = 0
        #Simulation_Register.VBUFF["Edge_SRC_5"] = 0
        Simulation_Register.VBUFF["Edge_DEST_5"] = 0
        #Simulation_Register.VBUFF["Edge_SRC_6"] = 0
        Simulation_Register.VBUFF["Edge_DEST_6"] = 0
        #Simulation_Register.VBUFF["Edge_SRC_7"] = 0
        Simulation_Register.VBUFF["Edge_DEST_7"] = 0
        Simulation_Register.VBUFF["Vertex_SRC0"] = 0
        Simulation_Register.VBUFF["Vertex_SRC1"] = 0
        Simulation_Register.VBUFF["Vertex_SRC2"] = 0
        Simulation_Register.VBUFF["Vertex_SRC3"] = 0
        Simulation_Register.VBUFF["Vertex_SRC4"] = 0
        Simulation_Register.VBUFF["Vertex_SRC5"] = 0
        Simulation_Register.VBUFF["Vertex_SRC6"] = 0
        Simulation_Register.VBUFF["Vertex_SRC7"] = 0
        Simulation_Register.scatter_pipeline["Update_DEST0"] = 0
        Simulation_Register.scatter_pipeline["Update_DEST1"] = 0
        Simulation_Register.scatter_pipeline["Update_DEST2"] = 0
        Simulation_Register.scatter_pipeline["Update_DEST3"] = 0
        Simulation_Register.scatter_pipeline["Update_DEST4"] = 0
        Simulation_Register.scatter_pipeline["Update_DEST5"] = 0
        Simulation_Register.scatter_pipeline["Update_DEST6"] = 0
        Simulation_Register.scatter_pipeline["Update_DEST7"] = 0
        Simulation_Register.scatter_pipeline["Update0"] = 0
        Simulation_Register.scatter_pipeline["Update1"] = 0
        Simulation_Register.scatter_pipeline["Update2"] = 0
        Simulation_Register.scatter_pipeline["Update3"] = 0
        Simulation_Register.scatter_pipeline["Update4"] = 0
        Simulation_Register.scatter_pipeline["Update5"] = 0
        Simulation_Register.scatter_pipeline["Update6"] = 0
        Simulation_Register.scatter_pipeline["Update7"] = 0
        Simulation_Register.CN["Update_DEST0"] = 0
        Simulation_Register.CN["Update0"] = 0
        Simulation_Register.CN["Update_DEST1"] = 0
        Simulation_Register.CN["Update1"] = 0
        Simulation_Register.CN["Update_DEST2"] = 0
        Simulation_Register.CN["Update2"] = 0
        Simulation_Register.CN["Update_DEST3"] = 0
        Simulation_Register.CN["Update3"] = 0
        Simulation_Register.CN["Update_DEST4"] = 0
        Simulation_Register.CN["Update4"] = 0
        Simulation_Register.CN["Update_DEST5"] = 0
        Simulation_Register.CN["Update5"] = 0
        Simulation_Register.CN["Update_DEST6"] = 0
        Simulation_Register.CN["Update6"] = 0
        Simulation_Register.CN["Update_DEST7"] = 0
        Simulation_Register.CN["Update7"] = 0

    utils.Eliminate_ZeroFromFile("SillyGraphUpdate.txt")
    helper_function.counter =helper_function.counter + 44
    print("this is the whole clock cycle " + str(helper_function.counter))

if __name__ == "__main__":
    	main()