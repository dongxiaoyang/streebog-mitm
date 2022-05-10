from abc import ABCMeta, abstractmethod
from functools import reduce
import math
import random



class BasicTools:

    @staticmethod
    def plusTerm(in_vars):
        t = ''
        for v in in_vars:
            t = t + v + ' + '
        return t[0:-3]

    @staticmethod
    def MinusTerm(in_vars):
        t = ''
        for v in in_vars:
            t = t + v + ' - '
        return t[0:-3]


    @staticmethod
    def getVariables_From_Constraints(C):
        V = set([])
        for s in C:
            temp = s.strip()
            temp = temp.replace('+', ' ')
            temp = temp.replace('-', ' ')
            temp = temp.replace('>=', ' ')
            temp = temp.replace('<=', ' ')
            temp = temp.replace('=', ' ')
            temp = temp.split()
            for v in temp:
                if not v.isdecimal():
                    V.add(v)
        return V


class MITMPreConstraints:
    @staticmethod
    def Consume_degree(Allone, V, cd):
        constr = []
        constr = constr + [cd + ' - ' + V + ' <= 0']
        constr = constr + [cd + ' - ' + V + ' + ' + Allone + ' >= 0']
        constr = constr + [cd + ' + ' + V + ' + ' + Allone + ' <= 2']
        return constr
        
    @staticmethod
    def Consume_degree_indicator0(Allone, V, cd, ind):
        constr = []
        constr = constr + [ind + ' = 0 -> ' + cd + ' - ' + V + ' <= 0']
        constr = constr + [ind + ' = 0 -> ' + cd + ' - ' + V + ' + ' + Allone + ' >= 0']
        constr = constr + [ind + ' = 0 -> ' + cd + ' + ' + V + ' + ' + Allone + ' <= 2']
        return constr        
    
    @staticmethod
    def Consume_degree_indicator1(Allone, V, cd, ind):
        constr = []
        constr = constr + [ind + ' = 1 -> ' + cd + ' - ' + V + ' <= 0']
        constr = constr + [ind + ' = 1 -> ' + cd + ' - ' + V + ' + ' + Allone + ' >= 0']
        constr = constr + [ind + ' = 1 -> ' + cd + ' + ' + V + ' + ' + Allone + ' <= 2']
        return constr      
    
    @staticmethod
    def Determine_Allone(V_in, V_out):
        m = len(V_in)
        constr = []
        constr = constr + [V_out + ' - ' + BasicTools.MinusTerm(V_in) + ' >= ' + str(1-m)]
        constr = constr + [BasicTools.plusTerm(V_in) + ' - ' + str(m) + ' ' + V_out + ' >= 0']
        return constr
        
    @staticmethod
    def Determine_Allone_indicator0(V_in, V_out,ind):
        m = len(V_in)
        constr = []
        constr = constr + [ind + ' = 0 -> ' + V_out + ' - ' + BasicTools.MinusTerm(V_in) + ' >= ' + str(1-m)]
        constr = constr + [ind + ' = 0 -> ' + BasicTools.plusTerm(V_in) + ' - ' + str(m) + ' ' + V_out + ' >= 0']
        return constr  

    @staticmethod
    def Determine_Allone_indicator1(V_in, V_out,ind):
        m = len(V_in)
        constr = []
        constr = constr + [ind + ' = 1 -> ' + V_out + ' - ' + BasicTools.MinusTerm(V_in) + ' >= ' + str(1-m)]
        constr = constr + [ind + ' = 1 -> ' + BasicTools.plusTerm(V_in) + ' - ' + str(m) + ' ' + V_out + ' >= 0']
        return constr         

    @staticmethod
    def Determine_Allzero(V_in, V_out):
        m = len(V_in)
        constr = []
        constr = constr + [V_out + ' + ' + BasicTools.plusTerm(V_in) + ' >= ' + str(1)]
        for j in range(m):
            constr = constr + [V_in[j] + ' + ' + V_out + ' <= 1']
        return constr 

    @staticmethod
    def Determine_Allzero_indicator0(V_in, V_out,ind):
        m = len(V_in)
        constr = []
        constr = constr + [ind + ' = 0 -> ' + V_out + ' + ' + BasicTools.plusTerm(V_in) + ' >= ' + str(1)]
        for j in range(m):
            constr = constr + [ind + ' = 0 -> ' + V_in[j] + ' + ' + V_out + ' <= 1']
        return constr  

    @staticmethod
    def Determine_Allzero_indicator1(V_in, V_out,ind):
        m = len(V_in)
        constr = []
        constr = constr + [ind + ' = 1 -> ' + V_out + ' + ' + BasicTools.plusTerm(V_in) + ' >= ' + str(1)]
        for j in range(m):
            constr = constr + [ind + ' = 1 -> ' + V_in[j] + ' + ' + V_out + ' <= 1']
        return constr        

    @staticmethod
    def Determine_ExistOne(V_in, V_out):
        m = len(V_in)
        constr = []
        constr = constr + [str(m) + ' ' + V_out + ' - ' + BasicTools.MinusTerm(V_in) + ' >= ' + str(0)]
        constr = constr + [V_out + ' - ' + BasicTools.MinusTerm(V_in) + ' <= ' + str(0)]
        return constr 
        
    @staticmethod
    def Determine_ExistOne_indicator0(V_in, V_out,ind):
        m = len(V_in)
        constr = []
        constr = constr + [ind + ' = 0 -> ' + str(m) + ' ' + V_out + ' - ' + BasicTools.MinusTerm(V_in) + ' >= ' + str(0)]
        constr = constr + [ind + ' = 0 -> ' + V_out + ' - ' + BasicTools.MinusTerm(V_in) + ' <= ' + str(0)]
        return constr   

    @staticmethod
    def Determine_ExistOne_indicator1(V_in, V_out,ind): #############################################################################################here
        m = len(V_in)
        constr = []
        constr = constr + [ind + ' = 1 -> ' + str(m) + ' ' + V_out + ' - ' + BasicTools.MinusTerm(V_in) + ' >= ' + str(0)]
        constr = constr + [ind + ' = 1 -> ' + V_out + ' - ' + BasicTools.MinusTerm(V_in) + ' <= ' + str(0)]
        return constr         
        
    @staticmethod
    def XOR_forward(V1_in, V2_in, V1_out, V2_out, cd):
        constr=[]
        constr=constr+[V2_in[0] + ' - ' + V2_out + ' >= 0']
        constr=constr+[V1_in[1] + ' - ' + V1_out + ' + ' + cd + ' >= 0']
        constr=constr+[V2_in[1] + ' - ' + V2_out + ' >= 0']
        constr=constr+[V2_out + ' - ' + V2_in[0] + ' - ' + V2_in[1] + ' >= -1']
        constr=constr+[V1_in[0] + ' - ' + V1_out + ' + ' + cd + ' >= 0']
        constr=constr+[V1_out + ' - ' + V1_in[0] + ' - ' + V1_in[1] + ' - 2 ' + cd + ' >= -1']
        constr=constr+[V2_out + ' - ' + cd + ' >= 0']
        return constr
        
    @staticmethod
    def XOR_forward_indicator0(V1_in, V2_in, V1_out, V2_out, cd, ind):
        constr=[]
        constr=constr+[ind + ' = 0 -> ' + V2_in[0] + ' - ' + V2_out + ' >= 0']
        constr=constr+[ind + ' = 0 -> ' + V1_in[1] + ' - ' + V1_out + ' + ' + cd + ' >= 0']
        constr=constr+[ind + ' = 0 -> ' + V2_in[1] + ' - ' + V2_out + ' >= 0']
        constr=constr+[ind + ' = 0 -> ' + V2_out + ' - ' + V2_in[0] + ' - ' + V2_in[1] + ' >= -1']
        constr=constr+[ind + ' = 0 -> ' + V1_in[0] + ' - ' + V1_out + ' + ' + cd + ' >= 0']
        constr=constr+[ind + ' = 0 -> ' + V1_out + ' - ' + V1_in[0] + ' - ' + V1_in[1] + ' - 2 ' + cd + ' >= -1']
        constr=constr+[ind + ' = 0 -> ' + V2_out + ' - ' + cd + ' >= 0']
        return constr   

    @staticmethod
    def XOR_forward_indicator1(V1_in, V2_in, V1_out, V2_out, cd, ind):
        constr=[]
        constr=constr+[ind + ' = 1 -> ' + V2_in[0] + ' - ' + V2_out + ' >= 0']
        constr=constr+[ind + ' = 1 -> ' + V1_in[1] + ' - ' + V1_out + ' + ' + cd + ' >= 0']
        constr=constr+[ind + ' = 1 -> ' + V2_in[1] + ' - ' + V2_out + ' >= 0']
        constr=constr+[ind + ' = 1 -> ' + V2_out + ' - ' + V2_in[0] + ' - ' + V2_in[1] + ' >= -1']
        constr=constr+[ind + ' = 1 -> ' + V1_in[0] + ' - ' + V1_out + ' + ' + cd + ' >= 0']
        constr=constr+[ind + ' = 1 -> ' + V1_out + ' - ' + V1_in[0] + ' - ' + V1_in[1] + ' - 2 ' + cd + ' >= -1']
        constr=constr+[ind + ' = 1 -> ' + V2_out + ' - ' + cd + ' >= 0']
        return constr         


    @staticmethod
    def XOR_backward(V1_in, V2_in, V1_out, V2_out, cd):
        constr=[]
        constr=constr+[V1_in[0] + ' - ' + V1_out + ' >= 0']
        constr=constr+[V2_in[1] + ' - ' + V2_out + ' + ' + cd + ' >= 0']
        constr=constr+[V1_in[1] + ' - ' + V1_out + ' >= 0']
        constr=constr+[V1_out + ' - ' + V1_in[0] + ' - ' + V1_in[1] + ' >= -1']
        constr=constr+[V2_in[0] + ' - ' + V2_out + ' + ' + cd + ' >= 0']
        constr=constr+[V2_out + ' - ' + V2_in[0] + ' - ' + V2_in[1] + ' - 2 ' + cd + ' >= -1']
        constr=constr+[V1_out + ' - ' + cd + ' >= 0']
        return constr   
        
    @staticmethod
    def XOR_backward_indicator0(V1_in, V2_in, V1_out, V2_out, cd, ind):
        constr=[]
        constr=constr+[ind + ' = 0 -> ' + V1_in[0] + ' - ' + V1_out + ' >= 0']
        constr=constr+[ind + ' = 0 -> ' + V2_in[1] + ' - ' + V2_out + ' + ' + cd + ' >= 0']
        constr=constr+[ind + ' = 0 -> ' + V1_in[1] + ' - ' + V1_out + ' >= 0']
        constr=constr+[ind + ' = 0 -> ' + V1_out + ' - ' + V1_in[0] + ' - ' + V1_in[1] + ' >= -1']
        constr=constr+[ind + ' = 0 -> ' + V2_in[0] + ' - ' + V2_out + ' + ' + cd + ' >= 0']
        constr=constr+[ind + ' = 0 -> ' + V2_out + ' - ' + V2_in[0] + ' - ' + V2_in[1] + ' - 2 ' + cd + ' >= -1']
        constr=constr+[ind + ' = 0 -> ' + V1_out + ' - ' + cd + ' >= 0']
        return constr 

    @staticmethod
    def XOR_backward_indicator1(V1_in, V2_in, V1_out, V2_out, cd, ind):
        constr=[]
        constr=constr+[ind + ' = 1 -> ' + V1_in[0] + ' - ' + V1_out + ' >= 0']
        constr=constr+[ind + ' = 1 -> ' + V2_in[1] + ' - ' + V2_out + ' + ' + cd + ' >= 0']
        constr=constr+[ind + ' = 1 -> ' + V1_in[1] + ' - ' + V1_out + ' >= 0']
        constr=constr+[ind + ' = 1 -> ' + V1_out + ' - ' + V1_in[0] + ' - ' + V1_in[1] + ' >= -1']
        constr=constr+[ind + ' = 1 -> ' + V2_in[0] + ' - ' + V2_out + ' + ' + cd + ' >= 0']
        constr=constr+[ind + ' = 1 -> ' + V2_out + ' - ' + V2_in[0] + ' - ' + V2_in[1] + ' - 2 ' + cd + ' >= -1']
        constr=constr+[ind + ' = 1 -> ' + V1_out + ' - ' + cd + ' >= 0']
        return constr        
        
    # @staticmethod
    # def P_guess(x1, y1, x2, y2, gu):
        # constr=[]
        # constr=constr+[y1 + ' - ' + y2 + ' + ' + gu + ' = 0']
        # constr=constr+[x1 + ' - ' + x2 + ' + ' + gu + ' = 0']
        # return constr
        
    @staticmethod
    def P_guess_forward(x1, y1, x2, y2, gu):
        constr=[]
        constr=constr+[y1 + ' - ' + y2 + ' = 0']
        constr=constr+[x1 + ' - ' + x2 + ' + ' + gu + ' = 0']
        constr=constr+[y2 + ' + ' + gu + ' <= 1']
        return constr    

    @staticmethod
    def P_guess_forward_indicator0(x1, y1, x2, y2, gu, ind):
        constr=[]
        constr=constr+[ind + ' = 0 -> ' +y1 + ' - ' + y2 + ' = 0']
        constr=constr+[ind + ' = 0 -> ' +x1 + ' - ' + x2 + ' + ' + gu + ' = 0']
        constr=constr+[ind + ' = 0 -> ' +y2 + ' + ' + gu + ' <= 1']
        return constr 
        
    @staticmethod
    def P_guess_forward_indicator1(x1, y1, x2, y2, gu, ind):
        constr=[]
        constr=constr+[ind + ' = 1 -> ' +y1 + ' - ' + y2 + ' = 0']
        constr=constr+[ind + ' = 1 -> ' +x1 + ' - ' + x2 + ' + ' + gu + ' = 0']
        constr=constr+[ind + ' = 1 -> ' +y2 + ' + ' + gu + ' <= 1']
        return constr         
        
        
    @staticmethod
    def P_guess_backward(x1, y1, x2, y2, gu):
        constr=[]
        constr=constr+[x1 + ' - ' + x2 + ' = 0']
        constr=constr+[y1 + ' - ' + y2 + ' + ' + gu + ' = 0']
        constr=constr+[x2 + ' + ' + gu + ' <= 1']
        return constr  

    @staticmethod
    def P_guess_backward_indicator0(x1, y1, x2, y2, gu,ind):
        constr=[]
        constr=constr+[ind + ' = 0 -> ' +x1 + ' - ' + x2 + ' = 0']
        constr=constr+[ind + ' = 0 -> ' +y1 + ' - ' + y2 + ' + ' + gu + ' = 0']
        constr=constr+[ind + ' = 0 -> ' +x2 + ' + ' + gu + ' <= 1']
        return constr  

    @staticmethod
    def P_guess_backward_indicator1(x1, y1, x2, y2, gu,ind):
        constr=[]
        constr=constr+[ind + ' = 1 -> ' +x1 + ' - ' + x2 + ' = 0']
        constr=constr+[ind + ' = 1 -> ' +y1 + ' - ' + y2 + ' + ' + gu + ' = 0']
        constr=constr+[ind + ' = 1 -> ' +x2 + ' + ' + gu + ' <= 1']
        return constr           


    @staticmethod
    def equalConstraints(x, y):
        assert len(x) == len(y)
        c = []
        for i in range(0, len(x)):
            c = c + [x[i] + ' - ' + y[i] + ' = 0']

        return c
        
    @staticmethod
    def equalConstraints_indicator0(x, y,ind):
        assert len(x) == len(y)
        c = []
        for i in range(0, len(x)):
            c = c + [ind + ' = 0 -> ' +x[i] + ' - ' + y[i] + ' = 0']

        return c    

    @staticmethod
    def equalConstraints_indicator1(x, y,ind):
        assert len(x) == len(y)
        c = []
        for i in range(0, len(x)):
            c = c + [ind + ' = 1 -> ' +x[i] + ' - ' + y[i] + ' = 0']

        return c         
        
    @staticmethod
    def XOR_Mat(V1, V2, V3, V4, V5, V6):
        constr=[]
        constr=constr+[V3 + ' - ' + V5 + ' >= 0']
        constr=constr+[V2 + ' - ' + V6 + ' >= 0']
        constr=constr+[V6 + ' - ' + V2 + ' - ' + V3 + ' >= -1']
        constr=constr+[V1 + ' - ' + V5 + ' >= 0']
        constr=constr+[V5 + ' - ' + V1 + ' - ' + V3 + ' >= -1']
        constr=constr+[V6 + ' - ' + V2 + ' - ' + V4 + ' >= -1']
        constr=constr+[V3 + ' + ' + V4 + ' - ' + V6 + ' >= 0']
        return constr   

    @staticmethod
    def OR_backward(V1, V2, V3, V4, OR):
        constr=[]
        constr=constr+[V1 + ' + ' + V3 + ' - ' + OR + ' >= 0']
        constr=constr+[V2 + ' - ' + V1 + ' + ' + OR + ' >= 0']
        constr=constr+[V4 + ' - ' + V3 + ' + ' + OR + ' >= 0']
        constr=constr+[V2 + ' + ' + V4 + ' + ' + OR + ' <= 2']
        constr=constr+[V1 + ' - ' + V4 + ' - ' + OR + ' >= -1']
        constr=constr+[V3 + ' - ' + V2 + ' - ' + OR + ' >= -1']
        return constr        
        
    
def row(A, j):
    return [A[8*j], A[8*j+1], A[8*j+2], A[8*j+3], A[8*j+4], A[8*j+5], A[8*j+6], A[8*j+7]]
    

def P_stribog(A):
    return [A[0], A[8],A[16], A[24], A[32], A[40], A[48], A[56],\
            A[1], A[9],A[17], A[25], A[33], A[41], A[49], A[57],\
            A[2],A[10],A[18], A[26], A[34], A[42], A[50], A[58],\
            A[3],A[11],A[19], A[27], A[35], A[43], A[51], A[59],\
            A[4],A[12],A[20], A[28], A[36], A[44], A[52], A[60],\
            A[5],A[13],A[21], A[29], A[37], A[45], A[53], A[61],\
            A[6],A[14],A[22], A[30], A[38], A[46], A[54], A[62],\
            A[7],A[15],A[23], A[31], A[39], A[47], A[55], A[63]]


def main():
    pass

if __name__ == '__main__':
    a=MITMPreConstraints.XOR_forward_indicator('ab','cd','e','f','cd','ind')
    print(a)
