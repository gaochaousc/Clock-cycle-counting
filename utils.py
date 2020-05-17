#Read Next 8 Edges from external memory and put them into a content
import helper_function
from collections import Counter
def countforlines(fileIn):
    f=open(fileIn,'r')
    cont= len(f.readlines())
    return cont

def readFile(filename, EdgeRead):
    content = []
    f = open (filename,'r')
    for line in f.readlines()[helper_function.EdgesRead:helper_function.EdgesRead+8]:
        l = line.split()
        content.append(l)
    
    return content

def CaC(A,A_value,B,B_value):
    output = []
    if A == B:
        A = A
        A_value = A_value + B_value
        B = 0
        B_value = 0
    elif A > B:
        C = A
        C_value = A_value
        A = B
        A_value = B_value
        B = C
        B = C_value
    else:
        A = A
        A_value = A_value
        B = B
        B_value = B_value
    output = [A,A_value,B,B_value]
    return output

def CompareandCombaine(A=[],B=[],C=[],D=[]):
    i = 0
    j = 0
    Inter_addr = 0
    Inter_update = 0
    Addrlist = [A[0],A[2],B[0],B[2],C[0],C[2],D[0],D[2]]
    Updatelist = [A[1],A[3],B[1],B[3],C[1],C[3],D[1],D[3]]
    for i in range (8):
        #print(type(Addrlist[i]))
        j = 0
        for j in range (7):
            #print(type(Addrlist[i+1]))
            if (Addrlist[j] != 0) & (Addrlist[j+1] != 0):
                #print(type(Addrlist[j]))
                #print(type(Addrlist[j+1]))
                if Addrlist[j] > Addrlist[j+1]:
                    Inter_addr = Addrlist[j]
                    Addrlist[j] = Addrlist[j+1]
                    Addrlist[j+1] = Inter_addr
                    Inter_update = Updatelist[j]
                    Updatelist[j+1] = Updatelist[j]
                    Updatelist[j] = Inter_update
                elif Addrlist[j] == Addrlist[j+1]:
                    Addrlist[j + 1] = 0
                    Updatelist[j+1] = 0
                    Addrlist[j] = Addrlist[j]
                    Updatelist[j] = Updatelist[j] + Updatelist[j+1]
            elif (Addrlist[j] == 0) & (Addrlist[j+1] != 0 ):
                Addrlist[j] = Addrlist[j+1]
                Updatelist[j] = Updatelist[j+1]
                Addrlist[j+1] = 0
                Updatelist[j+1] = 0
            else:
                Addrlist[j] = Addrlist[j]
                Addrlist[j+1] = Addrlist[j+1]
                Updatelist[j] = Updatelist[j]
                Updatelist[j+1] = Updatelist[j+1]
            j = j+1
        i = i + 1
    
    CombineList = [Addrlist[0],Updatelist[0],Addrlist[1],Updatelist[1],Addrlist[2],Updatelist[2],Addrlist[3],Updatelist[3],Addrlist[4],Updatelist[4],Addrlist[5],Updatelist[5],Addrlist[6],Updatelist[6],Addrlist[7],Updatelist[7]]
    return CombineList

def Eliminate_ZeroFromFile(fileIn):
    f = open(fileIn, 'r')
    UB = open("UpdateBin.txt", 'a+')
    #UpdateBin = f.readlines()
    for line in f:
        line.split()
        if line[0] != str(0):
            UB.write(line)
        
def ConflictFinderBetweenParallel(A=[],B=[],C=[],D=[]):
    Addresslist = [A[0],A[2],B[0],B[2],C[0],C[2],D[0],D[2]]
    Updatelist = [A[1],A[3],B[1],B[3],C[1],C[3],D[1],D[3]]
    print(Addresslist)
    print(Updatelist)
    SameBucket0 = []
    SameBucket1 = []
    SameBucket2 = []
    SameBucket3 = []
    SameBucket4 = []
    SameBucket5 = []
    SameBucket6 = []
    SameDATA0 = []
    SameDATA1 = []
    SameDATA2 = []
    SameDATA3 = []
    SameDATA4 = []
    SameDATA5 = []
    SameDATA6 = []
    SameCount0 = 0
    SameCount1 = 0
    SameCount2 = 0
    SameCount3 = 0
    SameCount4 = 0
    SameCount5 = 0
    SameCount6 = 0
    Repeat = []
    for i in range (7):
        if (Addresslist[0]!=0)&(Addresslist[i+1] == Addresslist[0]):
            SameBucket0.append(Addresslist[i+1])
            SameDATA0.append(Updatelist[i+1])
            #del Updatelist[i+1]
    for j in range(6):
        if (Addresslist[1]!=0)&(Addresslist[j+2] == Addresslist[1])&(Addresslist[j+2]!=Addresslist[0]):
            SameBucket1.append(Addresslist[j+2])
            SameDATA1.append(Updatelist[j+2])
            #del Addresslist[j+2]
            #del Updatelist[j+2]
    for k in range (5):
        if (Addresslist[2]!=0)&(Addresslist[k+3] == Addresslist[2])&(Addresslist[k+3]!=Addresslist[0])&(Addresslist[k+3]!=Addresslist[1]):
            print(Addresslist[k+3])
            SameBucket2.append(Addresslist[k+3])
            SameDATA2.append(Updatelist[k+3])
            #del Addresslist[k+3]
            #del Updatelist[k+3]
    for l in range(4):
        if (Addresslist[3]!=0)&(Addresslist[l+4] == Addresslist[3])&(Addresslist[l+4]!=Addresslist[0])&(Addresslist[l+4]!=Addresslist[1])&(Addresslist[l+4]!=Addresslist[2]):
            SameBucket3.append(Addresslist[l+4])
            SameDATA3.append(Updatelist[l+4])
            #del Addresslist[l+4]
            #el Updatelist[l+4]
    for m in range (3):
        if (Addresslist[4]!=0)&(Addresslist[m+5] == Addresslist[4])&(Addresslist[m+5]!=Addresslist[0])&(Addresslist[m+5]!=Addresslist[1])&(Addresslist[m+5]!=Addresslist[2])&(Addresslist[m+5]!=Addresslist[3]):
            SameBucket4.append(Addresslist[m+5])
            SameDATA4.append(Updatelist[m+5])
            #del Addresslist[m+5]
            #del Updatelist[m+5]
    for n in range (2):
        if (Addresslist[5]!=0)&(Addresslist[n+6] == Addresslist[5])&(Addresslist[n+6]!=Addresslist[0])&(Addresslist[n+6]!=Addresslist[1])&(Addresslist[n+6]!=Addresslist[2])&(Addresslist[n+6]!=Addresslist[3])&(Addresslist[n+6]!=Addresslist[4]):
            SameBucket5.append(Addresslist[n+6])
            SameDATA5.append(Updatelist[n+6])
            #del Addresslist[n+6]
            #del Updatelist[n+6]
    for o in range(1):
        if (Addresslist[6]!=0)&(Addresslist[o+7] == Addresslist[6])&(Addresslist[o+7]!=Addresslist[0])&(Addresslist[o+7]!=Addresslist[1])&(Addresslist[o+7]!=Addresslist[2])&(Addresslist[o+7]!=Addresslist[3])&(Addresslist[o+7]!=Addresslist[4])&(Addresslist[o+7]!=Addresslist[5]):
            SameBucket6.append(Addresslist[o+7])
            SameDATA6.append(Updatelist[o+7])
            #del Addresslist[o+7]
            #del Updatelist[o+7]
    SameCount0 = len(SameBucket0)
    SameCount1 = len(SameBucket1)
    SameCount2 = len(SameBucket2)
    SameCount3 = len(SameBucket3)
    SameCount4 = len(SameBucket4)
    SameCount5 = len(SameBucket5)
    SameCount6 = len(SameBucket6)
    Repeat = [[SameBucket0],[SameDATA0],SameCount0,[SameBucket1],[SameDATA1],SameCount1,[SameBucket2],[SameDATA2],SameCount2,[SameBucket3],[SameDATA3],SameCount3,[SameBucket4],[SameDATA4],SameBucket4,[SameBucket5],[SameDATA5],SameDATA5,[SameBucket6],[SameDATA6],SameDATA6]
    return Repeat
    #SameBucketx is the Address that need to get stalling
    #SameDATAx is the DATA that needs to be stalled
    #SameCountx is the Times that vertex need to wait


def readUpdate(filename, UpdateRead, Range):
    content = []
    f = open (filename,'r')
    for line in f.readlines()[UpdateRead:UpdateRead+Range]:
        l = line.split()
        content.append(l)
    
    return content

def readFiletoEnd(filename):
    content = []
    f = open (filename,'r')
    for line in f.readlines()[helper_function.EdgesRead:]:
        l = line.split()
        content.append(l)
    
    return content


    
def readUpdate(filename, UpdateRead, Range):
    content = []
    f = open (filename,'r')
    for line in f.readlines()[UpdateRead:UpdateRead+Range]:
        l = line.split()
        content.append(l)
    
    return content

#def DetectDependency(A=[],B=[],C=[],D=[]):
def Eliminate_ZeroFromFile_Update(fileIn):
    f = open(fileIn, 'r')
    UB = open("NewVector.txt", 'a+')
    #UpdateBin = f.readlines()
    for line in f:
        line.split()
        if line[0] != str(0):
            UB.write(line)


def main():
    #print(CompareandCombaine(A=[10,1,5,2],B=[6,1,8,1],C=[10,1,0,1],D=[0,2,0,2]))
    #Eliminate_ZeroFromFile("SillyGraphUpdate.txt")
    #print(ConflictFinderBetweenParallel(A=[10,1,5,2],B=[6,1,8,1],C=[10,1,0,1],D=[0,2,0,2]))
    print(readUpdate("sillygraph.txt",10,2))
if __name__ == "__main__":
    	main()