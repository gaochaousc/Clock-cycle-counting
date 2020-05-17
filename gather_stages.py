import helper_function, utils, Simulation_Register
## import function

import scatter_stages
#import the stage register generated before

'''def FIFO_gather():
    if Simulation_Register.Stall_Whole_Pipeline["STALL"] == 0:
        helper_function.gather_counter = helper_function.gather_counter + 1
        UpdateFIFO = readUpdate("UpdateBin.txt",helper_function.UpdateRead, helper_function.STALLPIPELINENUMBER)
        try:
            Simulation_Register.FIFO_gather["Update_DEST0"] = UpdateFIFO[0][0]
            Simulation_Register.FIFO_gather["Update0"] = UpdateFIFO[0][1]
            Simulation_Register.FIFO_gather["Update_DEST1"] = UpdateFIFO[1][0]
            Simulation_Register.FIFO_gather["Update0"] = UpdateFIFO[1][1]
            Simulation_Register.FIFO_gather["Update_DEST2"] = UpdateFIFO[2][0]
            Simulation_Register.FIFO_gather["Update0"] = UpdateFIFO[2][1]
            Simulation_Register.FIFO_gather["Update_DEST3"] = UpdateFIFO[3][0]
            Simulation_Register.FIFO_gather["Update0"] = UpdateFIFO[3][1]
            Simulation_Register.FIFO_gather["Update_DEST4"] = UpdateFIFO[4][0]
            Simulation_Register.FIFO_gather["Update0"] = UpdateFIFO[4][1]
            Simulation_Register.FIFO_gather["Update_DEST5"] = UpdateFIFO[5][0]
            Simulation_Register.FIFO_gather["Update0"] = UpdateFIFO[5][1]
            Simulation_Register.FIFO_gather["Update_DEST6"] = UpdateFIFO[6][0]
            Simulation_Register.FIFO_gather["Update0"] = UpdateFIFO[6][1]
            Simulation_Register.FIFO_gather["Update_DEST7"] = UpdateFIFO[7][0]
            Simulation_Register.FIFO_gather["Update0"] = UpdateFIFO[7][1]
        except:
            pass
    else:
        helper_function.gather_counter = helper_function.gather_counter + 1
        UpdateFIFO = readUpdate("UpdateBin.txt",helper_function.UpdateRead,8-helper_function.STALLPIPELINENUMBER)
        try:
            Simulation_Register.FIFO_gather["Update_DEST0"] = UpdateFIFO[0][0]
            Simulation_Register.FIFO_gather["Update0"] = UpdateFIFO[0][1]
            Simulation_Register.FIFO_gather["Update_DEST1"] = UpdateFIFO[1][0]
            Simulation_Register.FIFO_gather["Update0"] = UpdateFIFO[1][1]
            Simulation_Register.FIFO_gather["Update_DEST2"] = UpdateFIFO[2][0]
            Simulation_Register.FIFO_gather["Update0"] = UpdateFIFO[2][1]
            Simulation_Register.FIFO_gather["Update_DEST3"] = UpdateFIFO[3][0]
            Simulation_Register.FIFO_gather["Update0"] = UpdateFIFO[3][1]
            Simulation_Register.FIFO_gather["Update_DEST4"] = UpdateFIFO[4][0]
            Simulation_Register.FIFO_gather["Update0"] = UpdateFIFO[4][1]
            Simulation_Register.FIFO_gather["Update_DEST5"] = UpdateFIFO[5][0]
            Simulation_Register.FIFO_gather["Update0"] = UpdateFIFO[5][1]
            Simulation_Register.FIFO_gather["Update_DEST6"] = UpdateFIFO[6][0]
            Simulation_Register.FIFO_gather["Update0"] = UpdateFIFO[6][1]
            Simulation_Register.FIFO_gather["Update_DEST7"] = UpdateFIFO[7][0]
            Simulation_Register.FIFO_gather["Update0"] = UpdateFIFO[7][1]
        except:
            pass'''

def FIFO_gather():
    try:
        if (helper_function.waitingvertexnumber0 != 0) | (helper_function.pipelineworkingcounter0 != 0) | (helper_function.pipelinestallingcounter0 == 0):
            Simulation_Register.FIFO_gather["Update_DEST0"] = 0
            Simulation_Register.FIFO_gather["Update0"]=0
        if (helper_function.waitingvertexnumber0 == 0) & (helper_function.pipelineworkingcounter0 == 0) & (helper_function.pipelinestallingcounter0 == 0):
            UpdateFIFO = utils.readUpdate("UpdateBin.txt",helper_function.UpdateRead,1)
            print("here is updateFIFO")
            print(UpdateFIFO)
            print(helper_function.UpdateRead)
            Simulation_Register.FIFO_gather["Update_DEST0"] = UpdateFIFO[0][0]
            Simulation_Register.FIFO_gather["Update0"]= UpdateFIFO[0][1]
            helper_function.UpdateRead = helper_function.UpdateRead + 1

        if (helper_function.waitingvertexnumber1 != 0) | (helper_function.pipelineworkingcounter1 != 0) | (helper_function.pipelinestallingcounter1 == 0):
            Simulation_Register.FIFO_gather["Update_DEST1"] = 0
            Simulation_Register.FIFO_gather["Update1"]=0
        if (helper_function.waitingvertexnumber1 == 0) & (helper_function.pipelineworkingcounter1 == 0) & (helper_function.pipelinestallingcounter1 == 0):
            UpdateFIFO = utils.readUpdate("UpdateBin.txt",helper_function.UpdateRead,1)
            print("here is updateFIFO")
            print(UpdateFIFO)
            print(helper_function.UpdateRead)
            Simulation_Register.FIFO_gather["Update_DEST1"] = UpdateFIFO[0][0]
            Simulation_Register.FIFO_gather["Update1"]= UpdateFIFO[0][1]
            helper_function.UpdateRead = helper_function.UpdateRead + 1

        if (helper_function.waitingvertexnumber2 != 0) | (helper_function.pipelineworkingcounter2 != 0) | (helper_function.pipelinestallingcounter2 == 0):
            Simulation_Register.FIFO_gather["Update_DEST2"] = 0
            Simulation_Register.FIFO_gather["Update2"]=0
        if (helper_function.waitingvertexnumber2 == 0) & (helper_function.pipelineworkingcounter2 == 0) & (helper_function.pipelinestallingcounter2 == 0):
            UpdateFIFO = utils.readUpdate("UpdateBin.txt",helper_function.UpdateRead,1)
            print("here is updateFIFO")
            print(UpdateFIFO)
            print(helper_function.UpdateRead)
            Simulation_Register.FIFO_gather["Update_DEST2"] = UpdateFIFO[0][0]
            Simulation_Register.FIFO_gather["Update2"]= UpdateFIFO[0][1]
            helper_function.UpdateRead = helper_function.UpdateRead + 1

        if (helper_function.waitingvertexnumber3 != 0) | (helper_function.pipelineworkingcounter3 != 0) | (helper_function.pipelinestallingcounter3 == 0):
            Simulation_Register.FIFO_gather["Update_DEST3"] = 0
            Simulation_Register.FIFO_gather["Update3"]=0
        if (helper_function.waitingvertexnumber3 == 0) & (helper_function.pipelineworkingcounter3 == 0) & (helper_function.pipelinestallingcounter3 == 0):
            UpdateFIFO = utils.readUpdate("UpdateBin.txt",helper_function.UpdateRead,1)
            print("here is updateFIFO")
            print(UpdateFIFO)
            print(helper_function.UpdateRead)
            Simulation_Register.FIFO_gather["Update_DEST3"] = UpdateFIFO[0][0]
            Simulation_Register.FIFO_gather["Update3"]= UpdateFIFO[0][1]
            helper_function.UpdateRead = helper_function.UpdateRead + 1

        if (helper_function.waitingvertexnumber4 != 0) | (helper_function.pipelineworkingcounter4 != 0) | (helper_function.pipelinestallingcounter4 == 0):
            Simulation_Register.FIFO_gather["Update_DEST4"] = 0
            Simulation_Register.FIFO_gather["Update4"]=0
        if (helper_function.waitingvertexnumber4 == 0) & (helper_function.pipelineworkingcounter4 == 0) & (helper_function.pipelinestallingcounter4 == 0):
            UpdateFIFO = utils.readUpdate("UpdateBin.txt",helper_function.UpdateRead,1)
            print("here is updateFIFO")
            print(UpdateFIFO)
            print(helper_function.UpdateRead)
            Simulation_Register.FIFO_gather["Update_DEST4"] = UpdateFIFO[0][0]
            Simulation_Register.FIFO_gather["Update4"]= UpdateFIFO[0][1]
            helper_function.UpdateRead = helper_function.UpdateRead + 1

        if (helper_function.waitingvertexnumber5 != 0) | (helper_function.pipelineworkingcounter5 != 0) | (helper_function.pipelinestallingcounter5 == 0):
            Simulation_Register.FIFO_gather["Update_DEST5"] = 0
            Simulation_Register.FIFO_gather["Update5"]=0
        if (helper_function.waitingvertexnumber5 == 0) & (helper_function.pipelineworkingcounter5 == 0) & (helper_function.pipelinestallingcounter5 == 0):
            UpdateFIFO = utils.readUpdate("UpdateBin.txt",helper_function.UpdateRead,1)
            Simulation_Register.FIFO_gather["Update_DEST5"] = UpdateFIFO[0][0]
            Simulation_Register.FIFO_gather["Update5"]= UpdateFIFO[0][1]
            helper_function.UpdateRead = helper_function.UpdateRead + 1

        if (helper_function.waitingvertexnumber6 != 0) | (helper_function.pipelineworkingcounter6 != 0) | (helper_function.pipelinestallingcounter6 == 0):
            Simulation_Register.FIFO_gather["Update_DEST3"] = 0
            Simulation_Register.FIFO_gather["Update3"]=0
        if (helper_function.waitingvertexnumber6 == 0) & (helper_function.pipelineworkingcounter6 == 0) & (helper_function.pipelinestallingcounter6 == 0):
            UpdateFIFO = utils.readUpdate("UpdateBin.txt",helper_function.UpdateRead,1)
            Simulation_Register.FIFO_gather["Update_DEST6"] = UpdateFIFO[0][0]
            Simulation_Register.FIFO_gather["Update6"]= UpdateFIFO[0][1]
            helper_function.UpdateRead = helper_function.UpdateRead + 1

        if (helper_function.waitingvertexnumber7 != 0) | (helper_function.pipelineworkingcounter7 != 0) | (helper_function.pipelinestallingcounter7 == 0):
            Simulation_Register.FIFO_gather["Update_DEST7"] = 0
            Simulation_Register.FIFO_gather["Update7"]=0
        if (helper_function.waitingvertexnumber7 == 0) & (helper_function.pipelineworkingcounter7 == 0) & (helper_function.pipelinestallingcounter7 == 0):
            UpdateFIFO = utils.readUpdate("UpdateBin.txt",helper_function.UpdateRead,1)
            Simulation_Register.FIFO_gather["Update_DEST7"] = UpdateFIFO[0][0]
            Simulation_Register.FIFO_gather["Update7"]= UpdateFIFO[0][1]
            helper_function.UpdateRead = helper_function.UpdateRead + 1
    except:
        pass
    print(Simulation_Register.FIFO_gather)
#Here we generate bubbles for those who face conflicts besides, if the conflict addresses are detected, we will go back few lines of the update bins                                                                                                                                                                                                                                                                                                                                                                
def BCR_gather():
    try:
        if Simulation_Register.Stall_Whole_Pipeline["STALL"] == 0:
            if (helper_function.pipelinestallingcounter0 == 0)&(helper_function.pipelineworkingcounter0 == 0)&(helper_function.waitingvertexnumber0==0):
                Simulation_Register.BCR_gather["Update_DEST0"] = Simulation_Register.FIFO_gather["Update_DEST0"]
                Simulation_Register.BCR_gather["Update0"]=Simulation_Register.FIFO_gather["Update0"]
            elif (helper_function.pipelinestallingcounter0==1)&(helper_function.pipelineworkingcounter0!=0):
                helper_function.pipelineworkingcounter0 = helper_function.pipelineworkingcounter0 - 1
                Simulation_Register.BCR_gather["Update_DEST0"] = 0
                Simulation_Register.BCR_gather["Update0"]=0
            elif (helper_function.pipelinestallingcounter0==1)&(helper_function.pipelineworkingcounter0 == 0)&(helper_function.waitingvertexnumber0 >= 1):
                helper_function.pipelineworkingcounter0 = helper_function.pipelineworkingcounter0 - 1
                helper_function.waitingvertexnumber0 = helper_function.waitingvertexnumber0 - 1
                Simulation_Register.BCR_gather["Update_DEST0"] = helper_function.Addstorelist0[0][helper_function.waitingvertexnumber0]
                Simulation_Register.BCR_gather["Update0"] = helper_function.Datastorelist0[0][helper_function.waitingvertexnumber0]
                helper_function.pipelineworkingcounter0 = 4
            elif (helper_function.pipelinestallingcounter0 == 1)&(helper_function.pipelineworkingcounter0 == 0)&(helper_function.waitingvertexnumber0 == 0):
                helper_function.pipelinestallingcounter0 = 0
                helper_function.pipelineworkingcounter0 = 0
                helper_function.waitingvertexnumber0 = 0
                UpdateFIFO = utils.readUpdate("UpdateBin.txt",helper_function.UpdateRead,1)
                Simulation_Register.BCR_gather["Update_DEST0"] = UpdateFIFO[0][0]
                Simulation_Register.BCR_gather["Update0"]= UpdateFIFO[0][1]
                helper_function.UpdateRead = helper_function.UpdateRead + 1
        # four situation exsisted here, first without stalling, the BCR works as a stage register, with several stalls, it generates 4*stalls bubbles, with 1 last stall, we need to eliminate the whole counter
        
        if Simulation_Register.Stall_Whole_Pipeline["STALL"] == 0:
            if (helper_function.pipelinestallingcounter1 == 0)&(helper_function.pipelineworkingcounter1 == 0)&(helper_function.waitingvertexnumber1==0):
                Simulation_Register.BCR_gather["Update_DEST1"] = Simulation_Register.FIFO_gather["Update_DEST1"]
                Simulation_Register.BCR_gather["Update1"]=Simulation_Register.FIFO_gather["Update1"]
            elif (helper_function.pipelinestallingcounter1==1)&(helper_function.pipelineworkingcounter1!=0):
                helper_function.pipelineworkingcounter0 = helper_function.pipelineworkingcounter0 - 1
                Simulation_Register.BCR_gather["Update_DEST1"] = 0
                Simulation_Register.BCR_gather["Update1"]=0
            elif (helper_function.pipelinestallingcounter1==1)&(helper_function.pipelineworkingcounter1 == 0)&(helper_function.waitingvertexnumber1 >= 1):
                helper_function.pipelineworkingcounter1 = helper_function.pipelineworkingcounter1 - 1
                helper_function.waitingvertexnumber1 = helper_function.waitingvertexnumber1 - 1
                Simulation_Register.BCR_gather["Update_DEST1"] = helper_function.Addstorelist1[0][helper_function.waitingvertexnumber1]
                Simulation_Register.BCR_gather["Update1"] = helper_function.Datastorelist1[0][helper_function.waitingvertexnumber1]
                helper_function.pipelineworkingcounter1 = 4
            elif (helper_function.pipelinestallingcounter1==1)&(helper_function.pipelineworkingcounter1 == 0)&(helper_function.waitingvertexnumber1 == 0):
                helper_function.pipelinestallingcounter1 = 0
                helper_function.pipelineworkingcounter1 = 0
                helper_function.waitingvertexnumber1 = 0
                UpdateFIFO = utils.readUpdate("UpdateBin.txt",helper_function.UpdateRead,1)
                Simulation_Register.BCR_gather["Update_DEST1"] = UpdateFIFO[0][0]
                Simulation_Register.BCR_gather["Update1"]= UpdateFIFO[0][1]
                helper_function.UpdateRead = helper_function.UpdateRead + 1
        
        
        if Simulation_Register.Stall_Whole_Pipeline["STALL"] == 0:
            if (helper_function.pipelinestallingcounter2 == 0)&(helper_function.pipelineworkingcounter2 == 0)&(helper_function.waitingvertexnumber2==0):
                Simulation_Register.BCR_gather["Update_DEST2"] = Simulation_Register.FIFO_gather["Update_DEST2"]
                Simulation_Register.BCR_gather["Update2"]=Simulation_Register.FIFO_gather["Update2"]
            elif (helper_function.pipelinestallingcounter2==1)&(helper_function.pipelineworkingcounter2!=0):
                helper_function.pipelineworkingcounter2 = helper_function.pipelineworkingcounter2 - 1
                Simulation_Register.BCR_gather["Update_DEST2"] = 0
                Simulation_Register.BCR_gather["Update2"]=0
            elif (helper_function.pipelinestallingcounter2==1)&(helper_function.pipelineworkingcounter2 == 0)&(helper_function.waitingvertexnumber2 >= 1):
                helper_function.pipelineworkingcounter2 = helper_function.pipelineworkingcounter2 - 1
                helper_function.waitingvertexnumber2 = helper_function.waitingvertexnumber2 - 1
                Simulation_Register.BCR_gather["Update_DEST2"] = helper_function.Addstorelist1[0][helper_function.waitingvertexnumber2]
                Simulation_Register.BCR_gather["Update2"] = helper_function.Datastorelist1[0][helper_function.waitingvertexnumber2]
                helper_function.pipelineworkingcounter2 = 4
            elif (helper_function.pipelinestallingcounter2 == 1)&(helper_function.pipelineworkingcounter2 == 0)&(helper_function.waitingvertexnumber2 == 0):
                helper_function.pipelinestallingcounter2 = 0
                helper_function.pipelineworkingcounter2 = 0
                helper_function.waitingvertexnumber2 = 0
                UpdateFIFO = utils.readUpdate("UpdateBin.txt",helper_function.UpdateRead,1)
                Simulation_Register.BCR_gather["Update_DEST2"] = UpdateFIFO[0][0]
                Simulation_Register.BCR_gather["Update2"]= UpdateFIFO[0][1]
                helper_function.UpdateRead = helper_function.UpdateRead + 1
        
        
        if Simulation_Register.Stall_Whole_Pipeline["STALL"] == 0:
            if (helper_function.pipelinestallingcounter3 == 0)&(helper_function.pipelineworkingcounter3 == 0)&(helper_function.waitingvertexnumber3==0):
                Simulation_Register.BCR_gather["Update_DEST3"] = Simulation_Register.FIFO_gather["Update_DEST3"]
                Simulation_Register.BCR_gather["Update3"]=Simulation_Register.FIFO_gather["Update3"]
            elif (helper_function.pipelinestallingcounter3 == 1)&(helper_function.pipelineworkingcounter3 != 0):
                helper_function.pipelineworkingcounter3 = helper_function.pipelineworkingcounter3 - 1
                Simulation_Register.BCR_gather["Update_DEST3"] = 0
                Simulation_Register.BCR_gather["Update3"]=0
            elif (helper_function.pipelinestallingcounter3 == 1)&(helper_function.pipelineworkingcounter3 == 0)&(helper_function.waitingvertexnumber3 >= 1):
                helper_function.pipelineworkingcounter3 = helper_function.pipelineworkingcounter3 - 1
                helper_function.waitingvertexnumber3 = helper_function.waitingvertexnumber3 - 1
                Simulation_Register.BCR_gather["Update_DEST3"] = helper_function.Addstorelist3[0][helper_function.waitingvertexnumber3]
                Simulation_Register.BCR_gather["Update3"] = helper_function.Datastorelist3[0][helper_function.waitingvertexnumber3]
                helper_function.pipelineworkingcounter3 = 4
            elif (helper_function.pipelinestallingcounter3==1)&(helper_function.pipelineworkingcounter3 == 0)&(helper_function.waitingvertexnumber3 == 0):
                helper_function.pipelinestallingcounter3 = 0
                helper_function.pipelineworkingcounter3 = 0
                helper_function.waitingvertexnumber3 = 0
                UpdateFIFO = utils.readUpdate("UpdateBin.txt",helper_function.UpdateRead,1)
                Simulation_Register.BCR_gather["Update_DEST3"] = UpdateFIFO[0][0]
                Simulation_Register.BCR_gather["Update3"]= UpdateFIFO[0][1]
                helper_function.UpdateRead = helper_function.UpdateRead + 1
        
        
        if Simulation_Register.Stall_Whole_Pipeline["STALL"] == 0:
            if (helper_function.pipelinestallingcounter4 == 0)&(helper_function.pipelineworkingcounter4 == 0)&(helper_function.waitingvertexnumber4==0):
                Simulation_Register.BCR_gather["Update_DEST4"] = Simulation_Register.FIFO_gather["Update_DEST4"]
                Simulation_Register.BCR_gather["Update4"]=Simulation_Register.FIFO_gather["Update4"]
            elif (helper_function.pipelinestallingcounter4==1)&(helper_function.pipelineworkingcounter4 != 0):
                helper_function.pipelineworkingcounter4 = helper_function.pipelineworkingcounter4 - 1
                Simulation_Register.BCR_gather["Update_DEST4"] = 0
                Simulation_Register.BCR_gather["Update4"]=0
            elif (helper_function.pipelinestallingcounter4 == 1)&(helper_function.pipelineworkingcounter4 == 0)&(helper_function.waitingvertexnumber4 >= 1):
                helper_function.pipelineworkingcounter4 = helper_function.pipelineworkingcounter4 - 1
                helper_function.waitingvertexnumber4 = helper_function.waitingvertexnumber4 - 1
                Simulation_Register.BCR_gather["Update_DEST4"] = helper_function.Addstorelist4[0][helper_function.waitingvertexnumber4]
                Simulation_Register.BCR_gather["Update4"] = helper_function.Datastorelist4[0][helper_function.waitingvertexnumber4]
                helper_function.pipelineworkingcounter4 = 4
            elif (helper_function.pipelinestallingcounter4 == 1)&(helper_function.pipelineworkingcounter4 == 0)&(helper_function.waitingvertexnumber4 == 0):
                helper_function.pipelinestallingcounter4 = 0
                helper_function.pipelineworkingcounter4 = 0
                helper_function.waitingvertexnumber4 = 0
                UpdateFIFO = utils.readUpdate("UpdateBin.txt",helper_function.UpdateRead,1)
                Simulation_Register.BCR_gather["Update_DEST4"] = UpdateFIFO[0][0]
                Simulation_Register.BCR_gather["Update4"]= UpdateFIFO[0][1]
                helper_function.UpdateRead = helper_function.UpdateRead + 1
        
        
        if Simulation_Register.Stall_Whole_Pipeline["STALL"] == 0:
            if (helper_function.pipelinestallingcounter5 == 0)&(helper_function.pipelineworkingcounter5 == 0)&(helper_function.waitingvertexnumber5==0):
                Simulation_Register.BCR_gather["Update_DEST5"] = Simulation_Register.FIFO_gather["Update_DEST5"]
                Simulation_Register.BCR_gather["Update4"]=Simulation_Register.FIFO_gather["Update5"]
            elif (helper_function.pipelinestallingcounter5 == 1)&(helper_function.pipelineworkingcounter5 != 0):
                helper_function.pipelineworkingcounter5 = helper_function.pipelineworkingcounter5 - 1
                Simulation_Register.BCR_gather["Update_DEST5"] = 0
                Simulation_Register.BCR_gather["Update5"]=0
            elif (helper_function.pipelinestallingcounter5 == 1)&(helper_function.pipelineworkingcounter5 == 0)&(helper_function.waitingvertexnumber5 >= 1):
                helper_function.pipelineworkingcounter5 = helper_function.pipelineworkingcounter5 - 1
                helper_function.waitingvertexnumber5 = helper_function.waitingvertexnumber5 - 1
                Simulation_Register.BCR_gather["Update_DEST5"] = helper_function.Addstorelist5[0][helper_function.waitingvertexnumber5]
                Simulation_Register.BCR_gather["Update5"] = helper_function.Datastorelist5[0][helper_function.waitingvertexnumber5]
                helper_function.pipelineworkingcounter5 = 4
            elif (helper_function.pipelinestallingcounter5 == 1)&(helper_function.pipelineworkingcounter5 == 0)&(helper_function.waitingvertexnumber5 == 0):
                helper_function.pipelinestallingcounter5 = 0
                helper_function.pipelineworkingcounter5 = 0
                helper_function.waitingvertexnumber5 = 0
                UpdateFIFO = utils.readUpdate("UpdateBin.txt",helper_function.UpdateRead,1)
                Simulation_Register.BCR_gather["Update_DEST5"] = UpdateFIFO[0][0]
                Simulation_Register.BCR_gather["Update5"]= UpdateFIFO[0][1]
                helper_function.UpdateRead = helper_function.UpdateRead + 1
        
        
        if Simulation_Register.Stall_Whole_Pipeline["STALL"] == 0:
            if (helper_function.pipelinestallingcounter6 == 0)&(helper_function.pipelineworkingcounter6 == 0)&(helper_function.waitingvertexnumber6==0):
                Simulation_Register.BCR_gather["Update_DEST6"] = Simulation_Register.FIFO_gather["Update_DEST6"]
                Simulation_Register.BCR_gather["Update6"]=Simulation_Register.FIFO_gather["Update6"]
            elif (helper_function.pipelinestallingcounter6 == 1)&(helper_function.pipelineworkingcounter6 != 0):
                helper_function.pipelineworkingcounter6 = helper_function.pipelineworkingcounter6 - 1
                Simulation_Register.BCR_gather["Update_DEST6"] = 0
                Simulation_Register.BCR_gather["Update6"]=0
            elif (helper_function.pipelinestallingcounter6 == 1)&(helper_function.pipelineworkingcounter6 == 0)&(helper_function.waitingvertexnumber6 >= 1):
                helper_function.pipelineworkingcounter6 = helper_function.pipelineworkingcounter6 - 1
                helper_function.waitingvertexnumber6 = helper_function.waitingvertexnumber6 - 1
                Simulation_Register.BCR_gather["Update_DEST6"] = helper_function.Addstorelist6[0][helper_function.waitingvertexnumber6]
                Simulation_Register.BCR_gather["Update6"] = helper_function.Datastorelist6[0][helper_function.waitingvertexnumber6]
                helper_function.pipelineworkingcounter6 = 4
            elif (helper_function.pipelinestallingcounter6 == 1)&(helper_function.pipelineworkingcounter6 == 0)&(helper_function.waitingvertexnumber6 == 0):
                helper_function.pipelinestallingcounter6 = 0
                helper_function.pipelineworkingcounter6 = 0
                helper_function.waitingvertexnumber6 = 0
                UpdateFIFO = utils.readUpdate("UpdateBin.txt",helper_function.UpdateRead,1)
                Simulation_Register.BCR_gather["Update_DEST6"] = UpdateFIFO[0][0]
                Simulation_Register.BCR_gather["Update6"]= UpdateFIFO[0][1]
                helper_function.UpdateRead = helper_function.UpdateRead + 1
        
        
        if Simulation_Register.Stall_Whole_Pipeline["STALL"] == 0:
            if (helper_function.pipelinestallingcounter7 == 0)&(helper_function.pipelineworkingcounter7 == 0)&(helper_function.waitingvertexnumber7==0):
                Simulation_Register.BCR_gather["Update_DEST7"] = Simulation_Register.FIFO_gather["Update_DEST7"]
                Simulation_Register.BCR_gather["Update7"]=Simulation_Register.FIFO_gather["Update7"]
            elif (helper_function.pipelinestallingcounter7 == 1)&(helper_function.pipelineworkingcounter7 != 0):
                helper_function.pipelineworkingcounter7 = helper_function.pipelineworkingcounter7 - 1
                Simulation_Register.BCR_gather["Update_DEST7"] = 0
                Simulation_Register.BCR_gather["Update7"]=0
            elif (helper_function.pipelinestallingcounter7 == 1)&(helper_function.pipelineworkingcounter7 == 0)&(helper_function.waitingvertexnumber7 >= 1):
                helper_function.pipelineworkingcounter7 = helper_function.pipelineworkingcounter7 - 1
                helper_function.waitingvertexnumber7 = helper_function.waitingvertexnumber7 - 1
                Simulation_Register.BCR_gather["Update_DEST7"] = helper_function.Addstorelist7[0][helper_function.waitingvertexnumber7]
                Simulation_Register.BCR_gather["Update7"] = helper_function.Datastorelist7[0][helper_function.waitingvertexnumber7]
                helper_function.pipelineworkingcounter7 = 4
            elif (helper_function.pipelinestallingcounter7 == 1)&(helper_function.pipelineworkingcounter7 == 0)&(helper_function.waitingvertexnumber7 == 0):
                helper_function.pipelinestallingcounter7 = 0
                helper_function.pipelineworkingcounter7 = 0
                helper_function.waitingvertexnumber7 = 0
                UpdateFIFO = utils.readUpdate("UpdateBin.txt",helper_function.UpdateRead,1)
                Simulation_Register.BCR_gather["Update_DEST7"] = UpdateFIFO[0][0]
                Simulation_Register.BCR_gather["Update7"]= UpdateFIFO[0][1]
                helper_function.UpdateRead = helper_function.UpdateRead + 1
    except:
        pass


    if Simulation_Register.Stall_Whole_Pipeline["STALL"] == 1:
        Simulation_Register.BCR_gather["Update_DEST0"] = 0
        Simulation_Register.BCR_gather["Update0"]=0
        Simulation_Register.BCR_gather["Update_DEST1"] = 0
        Simulation_Register.BCR_gather["Update1"]=0
        Simulation_Register.BCR_gather["Update_DEST2"] = 0
        Simulation_Register.BCR_gather["Update2"]=0
        Simulation_Register.BCR_gather["Update_DEST"] = 0
        Simulation_Register.BCR_gather["Update3"]=0
        Simulation_Register.BCR_gather["Update_DEST4"] = 0
        Simulation_Register.BCR_gather["Update4"]=0
        Simulation_Register.BCR_gather["Update_DEST5"] = 0
        Simulation_Register.BCR_gather["Update5"]=0
        Simulation_Register.BCR_gather["Update_DEST6"] = 0
        Simulation_Register.BCR_gather["Update6"]=0
        Simulation_Register.BCR_gather["Update_DEST7"] = 0
        Simulation_Register.BCR_gather["Update7"]=0

#HDU at most generate 6 stall signals because there is at least one pipeline is working
def HDU_gather():
    A = [int(Simulation_Register.BCR_gather["Update_DEST0"]),int(Simulation_Register.BCR_gather["Update0"]),int(Simulation_Register.BCR_gather["Update_DEST1"]),int(Simulation_Register.BCR_gather["Update1"])]
    B = [int(Simulation_Register.BCR_gather["Update_DEST2"]),int(Simulation_Register.BCR_gather["Update2"]),int(Simulation_Register.BCR_gather["Update_DEST3"]),int(Simulation_Register.BCR_gather["Update3"])]
    C = [int(Simulation_Register.BCR_gather["Update_DEST4"]),int(Simulation_Register.BCR_gather["Update4"]),int(Simulation_Register.BCR_gather["Update_DEST5"]),int(Simulation_Register.BCR_gather["Update5"])]
    D = [int(Simulation_Register.BCR_gather["Update_DEST6"]),int(Simulation_Register.BCR_gather["Update6"]),int(Simulation_Register.BCR_gather["Update_DEST7"]),int(Simulation_Register.BCR_gather["Update7"])]
    Repeat_Information = utils.ConflictFinderBetweenParallel(A,B,C,D)
    #print(Repeat_Information)
    try:
        helper_function.Addstorelist0 = Repeat_Information[0]
        helper_function.Datastorelist0 = Repeat_Information[1]
        print(helper_function.Addstorelist0)
        helper_function.waitingvertexnumber0 = int(Repeat_Information[2])
        if helper_function.waitingvertexnumber0 != 0:
            helper_function.pipelinestallingcounter0 = 1
        
        helper_function.Addstorelist1 = Repeat_Information[3]
        helper_function.Datastorelist1 = Repeat_Information[4]
        helper_function.waitingvertexnumber1 = int(Repeat_Information[5])
        if helper_function.waitingvertexnumber1 != 0:
            helper_function.pipelinestallingcounter1 = 1

        helper_function.Addstorelist2 = Repeat_Information[6]
        helper_function.Datastorelist2 = Repeat_Information[7]
        helper_function.waitingvertexnumber2 = int(Repeat_Information[8])
        if helper_function.waitingvertexnumber2 != 0:
            helper_function.pipelinestallingcounter2 = 1

        helper_function.Addstorelist3 = Repeat_Information[9]
        helper_function.Datastorelist3 = Repeat_Information[10]
        helper_function.waitingvertexnumber3 = int(Repeat_Information[11])
        if helper_function.waitingvertexnumber3 != 0:
            helper_function.pipelinestallingcounter3 = 1

        helper_function.Addstorelist4 = Repeat_Information[12]
        helper_function.Datastorelist4 = Repeat_Information[13]
        helper_function.waitingvertexnumber4 = int(Repeat_Information[14])
        if helper_function.waitingvertexnumber4 != 0:
            helper_function.pipelinestallingcounter4 = 1

        helper_function.Addstorelist5 = Repeat_Information[15]
        helper_function.Datastorelist5 = Repeat_Information[16]
        helper_function.waitingvertexnumber5 = int(Repeat_Information[17])
        if helper_function.waitingvertexnumber5 != 0:
            helper_function.pipelinestallingcounter5 = 1

        helper_function.Addstorelist6 = Repeat_Information[18]
        helper_function.Datastorelist6 = Repeat_Information[19]
        helper_function.waitingvertexnumber6 = int(Repeat_Information[20])
        if helper_function.waitingvertexnumber6 != 0:
            helper_function.pipelinestallingcounter6 = 1

        '''helper_function.Addstorelist7 = Repeat_Information[21]
        helper_function.Datastorelist7 = Repeat_Information[22]
        helper_function.waitingvertexnumber7 = int(Repeat_Information[23])'''
    except:
        pass
    #generate stall signal for BCR
    

    Simulation_Register.gather_HDU["Update_DEST0"] = Simulation_Register.BCR_gather["Update_DEST0"] if (helper_function.waitingvertexnumber0 == 0)|(helper_function.pipelineworkingcounter0==4) else 0
    Simulation_Register.gather_HDU["Update0"] = Simulation_Register.BCR_gather["Update0"] if helper_function.waitingvertexnumber0 == 0 else 0
    
    Simulation_Register.gather_HDU["Update_DEST1"] = Simulation_Register.BCR_gather["Update_DEST1"] if (helper_function.waitingvertexnumber1 == 0)|(helper_function.pipelineworkingcounter1 == 4) else 0
    Simulation_Register.gather_HDU["Update1"] = Simulation_Register.BCR_gather["Update1"] if helper_function.waitingvertexnumber1 == 0 else 0

    Simulation_Register.gather_HDU["Update_DEST2"] = Simulation_Register.BCR_gather["Update_DEST2"] if (helper_function.waitingvertexnumber2 == 0)|(helper_function.pipelineworkingcounter2 == 4) else 0
    Simulation_Register.gather_HDU["Update2"] = Simulation_Register.BCR_gather["Update2"] if helper_function.waitingvertexnumber2 == 0 else 0
    
    Simulation_Register.gather_HDU["Update_DEST3"] = Simulation_Register.BCR_gather["Update_DEST3"] if (helper_function.waitingvertexnumber3 == 0)|(helper_function.pipelineworkingcounter3 == 4) else 0
    Simulation_Register.gather_HDU["Update3"] = Simulation_Register.BCR_gather["Update3"] if helper_function.waitingvertexnumber3 == 0 else 0

    Simulation_Register.gather_HDU["Update_DEST4"] = Simulation_Register.BCR_gather["Update_DEST4"] if (helper_function.waitingvertexnumber4 == 0)|(helper_function.pipelineworkingcounter4 == 4)  else 0
    Simulation_Register.gather_HDU["Update4"] = Simulation_Register.BCR_gather["Update4"] if helper_function.waitingvertexnumber4 == 0 else 0
    
    Simulation_Register.gather_HDU["Update_DEST5"] = Simulation_Register.BCR_gather["Update_DEST5"] if (helper_function.waitingvertexnumber5 == 0)|(helper_function.pipelineworkingcounter5 == 4)   else 0
    Simulation_Register.gather_HDU["Update5"] = Simulation_Register.BCR_gather["Update5"] if helper_function.waitingvertexnumber5 == 0 else 0

    Simulation_Register.gather_HDU["Update_DEST6"] = Simulation_Register.BCR_gather["Update_DEST6"] if (helper_function.waitingvertexnumber6 == 0)|(helper_function.pipelineworkingcounter6 == 4)   else 0
    Simulation_Register.gather_HDU["Update6"] = Simulation_Register.BCR_gather["Update6"] if helper_function.waitingvertexnumber6 == 0 else 0
    
    Simulation_Register.gather_HDU["Update_DEST7"] = Simulation_Register.BCR_gather["Update_DEST7"] if (helper_function.waitingvertexnumber7 == 0)|(helper_function.pipelineworkingcounter7 == 4)  else 0
    Simulation_Register.gather_HDU["Update7"] = Simulation_Register.BCR_gather["Update7"] if helper_function.waitingvertexnumber7 == 0 else 0


#for gather pipeline, there is no calculation
def gather_pipeline():
    Simulation_Register.gather_pipeline["Update_DEST0"] = Simulation_Register.gather_HDU["Update_DEST0"]
    Simulation_Register.gather_pipeline["Update0"] = Simulation_Register.gather_HDU["Update0"]

    Simulation_Register.gather_pipeline["Update_DEST1"] = Simulation_Register.gather_HDU["Update_DEST1"]
    Simulation_Register.gather_pipeline["Update1"] = Simulation_Register.gather_HDU["Update1"]
    
    Simulation_Register.gather_pipeline["Update_DEST2"] = Simulation_Register.gather_HDU["Update_DEST2"]
    Simulation_Register.gather_pipeline["Update2"] = Simulation_Register.gather_HDU["Update2"]

    Simulation_Register.gather_pipeline["Update_DEST3"] = Simulation_Register.gather_HDU["Update_DEST3"]
    Simulation_Register.gather_pipeline["Update3"] = Simulation_Register.gather_HDU["Update3"]

    Simulation_Register.gather_pipeline["Update_DEST4"] = Simulation_Register.gather_HDU["Update_DEST4"]
    Simulation_Register.gather_pipeline["Update4"] = Simulation_Register.gather_HDU["Update4"]

    Simulation_Register.gather_pipeline["Update_DEST5"] = Simulation_Register.gather_HDU["Update_DEST5"]
    Simulation_Register.gather_pipeline["Update5"] = Simulation_Register.gather_HDU["Update5"]
    
    Simulation_Register.gather_pipeline["Update_DEST6"] = Simulation_Register.gather_HDU["Update_DEST6"]
    Simulation_Register.gather_pipeline["Update6"] = Simulation_Register.gather_HDU["Update6"]

    Simulation_Register.gather_pipeline["Update_DEST7"] = Simulation_Register.gather_HDU["Update_DEST7"]
    Simulation_Register.gather_pipeline["Update7"] = Simulation_Register.gather_HDU["Update7"]


    helper_function.STALLPIPELINENUMBER = helper_function.pipelinestallingcounter0 + helper_function.pipelinestallingcounter1 + helper_function.pipelinestallingcounter2 + helper_function.pipelinestallingcounter3 + helper_function.pipelinestallingcounter4 + helper_function.pipelinestallingcounter5 + helper_function.pipelinestallingcounter6 + helper_function.pipelinestallingcounter7
    print("this is the stall cycle we need for the 8 pipelines in total")
    print(helper_function.STALLPIPELINENUMBER)
#def CNx8():



def readUpdate(filename, UpdateRead, Range):
    content = []
    f = open (filename,'r')
    for line in f.readlines()[UpdateRead:UpdateRead+Range]:
        l = line.split()
        content.append(l)
    
    return content



def main():
    print(utils.countforlines("UpdateBin.txt"))
    print(helper_function.gather_counter)
    while (helper_function.gather_processing_signal < utils.countforlines("UpdateBin.txt"))|(helper_function.STALLPIPELINENUMBER != 0):
        print("\n")
        print("This is the new cycle results")
        print(helper_function.UpdateRead)
        '''NewVector = open('DenseVector.txt','a+')'''
        FIFO_gather()
        print("Here is the FIFO_output value")
        print(Simulation_Register.FIFO_gather)
        BCR_gather()
        print("Here is the BCR output value")
        print(Simulation_Register.FIFO_gather)
        HDU_gather()
        print("This is the HDU value")
        gather_pipeline()
        print("This is the gather phase's output")
        

        '''NewVector.write(str(Simulation_Register.BCR_gather["Update_DEST0"]) + ' ' + str(Simulation_Register.FIFO_gather["Update0"]) + '\n')
        NewVector.write(str(Simulation_Register.BCR_gather["Update_DEST1"]) + ' ' + str(Simulation_Register.FIFO_gather["Update1"]) + '\n')
        NewVector.write(str(Simulation_Register.BCR_gather["Update_DEST2"]) + ' ' + str(Simulation_Register.FIFO_gather["Update2"]) + '\n')
        NewVector.write(str(Simulation_Register.BCR_gather["Update_DEST3"]) + ' ' + str(Simulation_Register.FIFO_gather["Update3"]) + '\n')
        NewVector.write(str(Simulation_Register.BCR_gather["Update_DEST4"]) + ' ' + str(Simulation_Register.FIFO_gather["Update4"]) + '\n')
        NewVector.write(str(Simulation_Register.BCR_gather["Update_DEST5"]) + ' ' + str(Simulation_Register.FIFO_gather["Update5"]) + '\n')
        NewVector.write(str(Simulation_Register.BCR_gather["Update_DEST6"]) + ' ' + str(Simulation_Register.FIFO_gather["Update6"]) + '\n')
        NewVector.write(str(Simulation_Register.BCR_gather["Update_DEST7"]) + ' ' + str(Simulation_Register.FIFO_gather["Update7"]) + '\n')'''
        #Reset Register for FIFO
        Simulation_Register.FIFO_gather["Update_DEST0"] = 0
        Simulation_Register.FIFO_gather["Update0"] = 0
        Simulation_Register.FIFO_gather["Update_DEST1"] = 0
        Simulation_Register.FIFO_gather["Update1"] = 0
        Simulation_Register.FIFO_gather["Update_DEST2"] = 0
        Simulation_Register.FIFO_gather["Update2"] = 0
        Simulation_Register.FIFO_gather["Update_DEST3"] = 0
        Simulation_Register.FIFO_gather["Update3"] = 0
        Simulation_Register.FIFO_gather["Update_DEST4"] = 0
        Simulation_Register.FIFO_gather["Update4"] = 0
        Simulation_Register.FIFO_gather["Update_DEST5"] = 0
        Simulation_Register.FIFO_gather["Update5"] = 0
        Simulation_Register.FIFO_gather["Update_DEST6"] = 0
        Simulation_Register.FIFO_gather["Update6"] = 0
        Simulation_Register.FIFO_gather["Update_DEST7"] = 0
        Simulation_Register.FIFO_gather["Update7"] = 0
        #Reset for BCR
        Simulation_Register.BCR_gather["Update_DEST0"] = 0
        Simulation_Register.BCR_gather["Update0"]=0
        Simulation_Register.BCR_gather["Update_DEST1"] = 0
        Simulation_Register.BCR_gather["Update1"]=0
        Simulation_Register.BCR_gather["Update_DEST2"] = 0
        Simulation_Register.BCR_gather["Update2"]=0
        Simulation_Register.BCR_gather["Update_DEST"] = 0
        Simulation_Register.BCR_gather["Update3"]=0
        Simulation_Register.BCR_gather["Update_DEST4"] = 0
        Simulation_Register.BCR_gather["Update4"]=0
        Simulation_Register.BCR_gather["Update_DEST5"] = 0
        Simulation_Register.BCR_gather["Update5"]=0
        Simulation_Register.BCR_gather["Update_DEST6"] = 0
        Simulation_Register.BCR_gather["Update6"]=0
        Simulation_Register.BCR_gather["Update_DEST7"] = 0
        Simulation_Register.BCR_gather["Update7"]=0
        #reset for gather_pipeline
        Simulation_Register.gather_pipeline["Update_DEST0"] = 0
        Simulation_Register.gather_pipeline["Update0"] = 0
        Simulation_Register.gather_pipeline["Update_DEST1"] = 0
        Simulation_Register.gather_pipeline["Update1"] = 0
        Simulation_Register.gather_pipeline["Update_DEST2"] = 0
        Simulation_Register.gather_pipeline["Update2"] = 0
        Simulation_Register.gather_pipeline["Update_DEST3"] = 0
        Simulation_Register.gather_pipeline["Update3"] = 0
        Simulation_Register.gather_pipeline["Update_DEST4"] = 0
        Simulation_Register.gather_pipeline["Update4"] = 0
        Simulation_Register.gather_pipeline["Update_DEST5"] = 0
        Simulation_Register.gather_pipeline["Update5"] = 0
        Simulation_Register.gather_pipeline["Update_DEST6"] = 0
        Simulation_Register.gather_pipeline["Update6"] = 0
        Simulation_Register.gather_pipeline["Update_DEST7"] = 0
        Simulation_Register.gather_pipeline["Update7"] = 0
        #reset for HDU
        Simulation_Register.gather_HDU["Update_DEST0"] = 0
        Simulation_Register.gather_HDU["Update0"] = 0
        Simulation_Register.gather_HDU["Update_DEST1"] = 0
        Simulation_Register.gather_HDU["Update1"] = 0
        Simulation_Register.gather_HDU["Update_DEST2"] = 0
        Simulation_Register.gather_HDU["Update2"] = 0
        Simulation_Register.gather_HDU["Update_DEST3"] = 0
        Simulation_Register.gather_HDU["Update3"] = 0
        Simulation_Register.gather_HDU["Update_DEST4"] = 0
        Simulation_Register.gather_HDU["Update4"] = 0
        Simulation_Register.gather_HDU["Update_DEST5"] = 0
        Simulation_Register.gather_HDU["Update5"] = 0
        Simulation_Register.gather_HDU["Update_DEST6"] = 0
        Simulation_Register.gather_HDU["Update6"] = 0
        Simulation_Register.gather_HDU["Update_DEST7"] = 0
        Simulation_Register.gather_HDU["Update7"] = 0
        helper_function.gather_processing_signal = helper_function.UpdateRead
        helper_function.gather_counter = helper_function.gather_counter + 1

    
    #utils.Eliminate_ZeroFromFile_Update("DenseVector.txt")
    helper_function.gather_counter = helper_function.gather_counter + 5
    print("We need "+ str(helper_function.gather_counter)+ " clock cycles to finish the processing.")



if __name__ == "__main__":
    	main()