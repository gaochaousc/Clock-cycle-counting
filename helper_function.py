###
# File to store simulator global varibles
###

#Global Counter
EdgesRead = 0
UpdateRead = 0
gather_processing_signal = 0
#counter
counter = 0
gather_counter = 0

#Stall Cycle
STALLCYCLE = 0
STALLPIPELINENUMBER = 0
#signal that judge whether the pipeline is allowed to go again
pipelineworkingcounter0 = 0
pipelineworkingcounter1 = 0
pipelineworkingcounter2 = 0
pipelineworkingcounter3 = 0
pipelineworkingcounter4 = 0
pipelineworkingcounter5 = 0
pipelineworkingcounter6 = 0
pipelineworkingcounter7 = 0
#counter for generating bubble
pipelinestallingcounter0 = 0
pipelinestallingcounter1 = 0
pipelinestallingcounter2 = 0
pipelinestallingcounter3 = 0
pipelinestallingcounter4 = 0
pipelinestallingcounter5 = 0
pipelinestallingcounter6 = 0
pipelinestallingcounter7 = 0
#stalling counter for waiting vertex
waitingvertexnumber0 = 0
waitingvertexnumber1 = 0
waitingvertexnumber2 = 0
waitingvertexnumber3 = 0
waitingvertexnumber4 = 0
waitingvertexnumber5 = 0
waitingvertexnumber6 = 0
waitingvertexnumber7 = 0
#store list for stalling pipeline
Addstorelist0 = []
Addstorelist1 = []
Addstorelist2 = []
Addstorelist3 = []
Addstorelist4 = []
Addstorelist5 = []
Addstorelist6 = []
Addstorelist7 = []
Datastorelist0 = []
Datastorelist1 = []
Datastorelist2 = []
Datastorelist3 = []
Datastorelist4 = []
Datastorelist5 = []
Datastorelist6 = []
Datastorelist7 = []
Addstorelist = [Addstorelist0,Addstorelist1,Addstorelist2,Addstorelist3,Addstorelist4,Addstorelist5,Addstorelist6,Addstorelist7]
##dictionary for simple instruction

#Edge_Size
SourceAddress_Size = 32
Data_Size = 32
DestAddress_Size = 32

# Enable for HDU
data_hzd = True
