###
#File to store Edge_Data, Vertex_Data and Valid signal
###

import helper_function



#input Edge
Edge = 0

##Interval_Buffer
Vertex_Buffer = [0 for i in range(2**18)]


##HDU
#HDU_Buffer = [0 for i in range(2**18)]

# Scatter Pipeline Register
FIFO_BCR = {"Edge_SRC_0":0, "Edge_SRC_1":0, "Edge_SRC_2":0, "Edge_SRC_3":0, "Edge_SRC_4":0, "Edge_SRC_5":0, "Edge_SRC_6":0, "Edge_SRC_7":0, "Edge_DEST_0":0, "Edge_DEST_1":0, "Edge_DEST_2":0, "Edge_DEST_3":0, "Edge_DEST_4":0, "Edge_DEST_5":0, "Edge_DEST_6":0, "Edge_DEST_7":0}
BCR = {"Edge_SRC_0":0, "Edge_SRC_1":0, "Edge_SRC_2":0, "Edge_SRC_3":0, "Edge_SRC_4":0, "Edge_SRC_5":0, "Edge_SRC_6":0, "Edge_SRC_7":0, "Edge_DEST_0":0, "Edge_DEST_1":0, "Edge_DEST_2":0, "Edge_DEST_3":0, "Edge_DEST_4":0, "Edge_DEST_5":0, "Edge_DEST_6":0, "Edge_DEST_7":0}
VBUFF = {"Edge_DEST_0":0, "Edge_DEST_1":0, "Edge_DEST_2":0, "Edge_DEST_3":0, "Edge_DEST_4":0, "Edge_DEST_5":0, "Edge_DEST_6":0, "Edge_DEST_7":0,"Vertex_SRC0": 0, "Vertex_SRC1": 0, "Vertex_SRC2": 0, "Vertex_SRC3": 0, "Vertex_SRC4": 0, "Vertex_SRC5": 0, "Vertex_SRC6": 0, "Vertex_SRC7": 0 }
scatter_pipeline = {"Update_DEST0": 0, "Update_DEST1": 0, "Update_DEST2": 0, "Update_DEST3": 0, "Update_DEST4": 0, "Update_DEST5": 0, "Update_DEST6": 0, "Update_DEST7": 0, "Update0": 0, "Update1": 0, "Update2": 0, "Update3": 0, "Update4": 0, "Update5": 0, "Update6": 0, "Update7": 0}
CN = {"Update_DEST0": 0, "Update_DEST1": 0, "Update_DEST2": 0, "Update_DEST3": 0, "Update_DEST4": 0, "Update_DEST5": 0, "Update_DEST6": 0, "Update_DEST7": 0, "Update0": 0, "Update1": 0, "Update2": 0, "Update3": 0, "Update4": 0, "Update5": 0, "Update6": 0, "Update7": 0}
gather_HDU = {"Update_DEST0": 0, "Update_DEST1": 0, "Update_DEST2": 0, "Update_DEST3": 0, "Update_DEST4": 0, "Update_DEST5": 0, "Update_DEST6": 0, "Update_DEST7": 0, "Update0": 0, "Update1": 0, "Update2": 0, "Update3": 0, "Update4": 0, "Update5": 0, "Update6": 0, "Update7": 0}
FIFO_gather = {"Update_DEST0": 0, "Update_DEST1": 0, "Update_DEST2": 0, "Update_DEST3": 0, "Update_DEST4": 0, "Update_DEST5": 0, "Update_DEST6": 0, "Update_DEST7": 0, "Update0": 0, "Update1": 0, "Update2": 0, "Update3": 0, "Update4": 0, "Update5": 0, "Update6": 0, "Update7": 0}
BCR_gather = {"Update_DEST0": 0, "Update_DEST1": 0, "Update_DEST2": 0, "Update_DEST3": 0, "Update_DEST4": 0, "Update_DEST5": 0, "Update_DEST6": 0, "Update_DEST7": 0, "Update0": 0, "Update1": 0, "Update2": 0, "Update3": 0, "Update4": 0, "Update5": 0, "Update6": 0, "Update7": 0}
gather_pipeline = {"Update_DEST0": 0, "Update_DEST1": 0, "Update_DEST2": 0, "Update_DEST3": 0, "Update_DEST4": 0, "Update_DEST5": 0, "Update_DEST6": 0, "Update_DEST7": 0, "Update0": 0, "Update1": 0, "Update2": 0, "Update3": 0, "Update4": 0, "Update5": 0, "Update6": 0, "Update7": 0}
gather_VBUFF = {"Update_DEST0": 0, "Update_DEST1": 0, "Update_DEST2": 0, "Update_DEST3": 0, "Update_DEST4": 0, "Update_DEST5": 0, "Update_DEST6": 0, "Update_DEST7": 0, "Update0": 0, "Update1": 0, "Update2": 0, "Update3": 0, "Update4": 0, "Update5": 0, "Update6": 0, "Update7": 0}

#Stalling Unit
Stall_Whole_Pipeline = {"STALL" : 0}

