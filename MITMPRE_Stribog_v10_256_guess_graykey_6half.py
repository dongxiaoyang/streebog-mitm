from CPMITM import *
from gurobipy import * 

class Vars_generator:
    @staticmethod
    def genVars_input1_of_round(r):   
        if r >= 0:
            return ['IS1_' + str(j) + '_r' + str(r) for j in range(64)]
        else:
            return ['minusIS1_' + str(j) + '_r_' + str(-r) for j in range(64)]
 
    def genVars_input2_of_round(r): 
        if r >= 0:
            return ['IS2_' + str(j) + '_r' + str(r) for j in range(64)] 
        else:
            return ['minusIS2_' + str(j) + '_r_' + str(-r) for j in range(64)]  
    
    def genVars_input1_of_L(r):
        return ['IM1_' + str(j) + '_r' + str(r) for j in range(64)]

    def genVars_input2_of_L( r):
        return ['IM2_' + str(j) + '_r' + str(r) for j in range(64)]
        
    def genVars_input1_of_L_dual(r):
        return ['Dual_IM1_' + str(j) + '_r' + str(r) for j in range(64)]

    def genVars_input2_of_L_dual( r):
        return ['Dual_IM2_' + str(j) + '_r' + str(r) for j in range(64)]        
    
    def genVars_input1_of_next(r):
        return ['IAK1_' + str(j) + '_r' + str(r) for j in range(64)]

    def genVars_input2_of_next(r):
        return ['IAK2_' + str(j) + '_r' + str(r) for j in range(64)]
        
    def genVars_input1_of_next_dual(r):
        return ['Dual_IAK1_' + str(j) + '_r' + str(r) for j in range(64)]

    def genVars_input2_of_next_dual(r):
        return ['Dual_IAK2_' + str(j) + '_r' + str(r) for j in range(64)]        

    def genVars_AllOne1_of_MixColumn(r):
        return ['AO1_' + str(j) + '_r' + str(r) for j in range(8)]
    
    def genVars_AllOne2_of_MixColumn(r):
        return ['AO2_' + str(j) + '_r' + str(r) for j in range(8)]
   
    def genVars_AllZero_of_MixColumn(r):
        return ['AZ_' + str(j) + '_r' + str(r) for j in range(64)]
    
    def genVars_SumOne_of_MixColumn(r):
        return ['GSO_'  + str(j) + '_r' + str(r) for j in range(8)]
    
    def genVars_Exist_dubbleZero(r):
        return ['EDZ_' + str(j) + '_r' + str(r) for j in range(8)]
    
    def genVars_ConsumedDeg_of_MixColumn(r):
        return ['CDeg_' + str(j) + '_r' + str(r) for j in range(64)]
        
    def genVars_guess(r):
        return ['Pguess_' + str(j) + '_r' + str(r) for j in range(64)]        
   
    def genVars_degree_forward():
        return ['deg_f' + str(j) for j in range(64)]
    
    def genVars_degree_backward():
        return ['deg_b' + str(j) for j in range(64)]
        
    def genVars_matching():
        return ['match_' + str(j)for j in range(64)]  
        
    def genVars_matchvar1():
        return ['matchvar1_' +str(j) for j in range(64)]
        
    def genVars_matchvar2():
        return ['matchvar2_' +str(j) for j in range(64)]        
    
    def genVars_M1_matching():
        return ['m1_' + str(j)for j in range(8)]
    
    def genVars_M2_matching():
        return ['m2_' + str(j) for j in range(8)]
    
    def genVars_M3_matching():
        return ['m3_' + str(j) for j in range(8)]

    def genVars_M4_matching():
        return ['m4_' + str(j) for j in range(8)]
        
    def genVars_M5_matching():
        return ['m5_' + str(j)for j in range(8)]
    
    def genVars_M6_matching():
        return ['m6_' + str(j) for j in range(8)]
    
    def genVars_M7_matching():
        return ['m7_' + str(j) for j in range(8)]

    def genVars_M8_matching():
        return ['m8_' + str(j) for j in range(8)]       
    
class Constraints_generator():
    
    def __init__(self, total_round, initial_round, matching_round):
        self.ini_r = initial_round
        self.mat_r = matching_round
        self.TR = total_round

        
    def gensubConstraints_MixColumn_backward(self, input1_col, input2_col, out1_col, out2_col, Allzero_col, EDZ, Allone1, Allone2, CD_col , GSum_one):
        #_col means a 8 dim vector        
        constr = []
        for i in range(8):
            constr = constr + MITMPreConstraints.Determine_Allzero([input1_col[i], input2_col[i]], Allzero_col[i])
        constr = constr + MITMPreConstraints.Determine_ExistOne(Allzero_col, EDZ)
        
        #if (0,0) belongs  the input column
        constr = constr + [BasicTools.plusTerm(out1_col) + ' + 8 ' + EDZ + ' <= 8']
        constr = constr + [BasicTools.plusTerm(out2_col) + ' + 8 ' + EDZ + ' <= 8']
        
        #if (0,0) does not belong the input column and determine wether the second input column are all ones
        constr = constr + MITMPreConstraints.Determine_Allone(input2_col, Allone2)
        constr = constr + [GSum_one + ' - ' + BasicTools.MinusTerm(input2_col) + ' - ' + BasicTools.MinusTerm(out2_col) + ' = 0']
        constr = constr + [GSum_one + ' - 9 ' + Allone2 + ' <= 7']
        constr = constr + [GSum_one + ' - 16 ' + Allone2 + ' >= 0']            
                    
        constr = constr + MITMPreConstraints.Determine_Allone(input1_col, Allone1)        
        constr = constr + [BasicTools.plusTerm(out1_col) + ' - 8 ' + Allone1 + ' = 0']
      
        #consume degrees
        for i in range(8):
            constr = constr + MITMPreConstraints.Consume_degree(Allone2, out2_col[i], CD_col[i])
        return constr
                   

    def genConstraints_of_forwardRound(self, r):

        input1_round = Vars_generator.genVars_input1_of_round(r)
        input2_round = Vars_generator.genVars_input2_of_round(r)
        
        input1_L = Vars_generator.genVars_input1_of_L(r)
        input2_L = Vars_generator.genVars_input2_of_L(r)
        
        input1_L_dual = Vars_generator.genVars_input1_of_L_dual(r)
        input2_L_dual = Vars_generator.genVars_input2_of_L_dual(r)        
        
        input1_next = Vars_generator.genVars_input1_of_next(r)
        input2_next = Vars_generator.genVars_input2_of_next(r)
        
        Pgu = Vars_generator.genVars_guess(r)
        
        Allone1 = Vars_generator.genVars_AllOne1_of_MixColumn(r) 
        Allone2 = Vars_generator.genVars_AllOne2_of_MixColumn(r)
        
        Sum_one = Vars_generator.genVars_SumOne_of_MixColumn(r)
        
        CD = Vars_generator.genVars_ConsumedDeg_of_MixColumn(r)
        
        Allzero = Vars_generator.genVars_AllZero_of_MixColumn(r)
        EDZ = Vars_generator.genVars_Exist_dubbleZero(r)
        
       
        if r < self.TR - 1:
            next_r = r + 1
        else:
            next_r = -1
            
        out1_round = Vars_generator.genVars_input1_of_round(next_r)
        out2_round = Vars_generator.genVars_input2_of_round(next_r)
        
        constr =[]
        
        if r<self.TR-1:

            # - Constraints for  ShiftRow
            constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input1_round), input1_L)
            constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input2_round), input2_L)
    
            constr = constr + MITMPreConstraints.equalConstraints(out1_round, input1_next)
            constr = constr + MITMPreConstraints.equalConstraints(out2_round, input2_next)    
            
            # - Constraints for  Pguess
            
            for j in range(64):
                constr = constr + MITMPreConstraints.P_guess_forward(input1_L[j],input2_L[j],input1_L_dual[j],input2_L_dual[j],Pgu[j])
        
            # - Constraints for MixColumns
    
            for j in range(8):
                input1_col = row(input1_L_dual, j)
                input2_col = row(input2_L_dual, j)
                out1_col = row(input1_next, j)
                out2_col = row(input2_next, j)           
                
                #determine whether (0,0) belongs the input column, if exists, then EDZ[j] = 1
                AO_col = row(Allzero, j)
                for i in range(8):
                    constr = constr + MITMPreConstraints.Determine_Allzero([input1_col[i], input2_col[i]], AO_col[i])
                constr = constr + MITMPreConstraints.Determine_ExistOne(AO_col, EDZ[j])
                
                #if (0,0) belongs  the input column
                constr = constr + [BasicTools.plusTerm(out1_col) + ' + 8 ' + EDZ[j] + ' <= 8']
                constr = constr + [BasicTools.plusTerm(out2_col) + ' + 8 ' + EDZ[j] + ' <= 8']
                
                #if (0,0) does not belong the input column and determine wether the first input column are all ones
                constr = constr + MITMPreConstraints.Determine_Allone(input1_col, Allone1[j])
                constr = constr + [Sum_one[j] + ' - ' + BasicTools.MinusTerm(input1_col) + ' - ' + BasicTools.MinusTerm(out1_col) + ' = 0']
                constr = constr + [Sum_one[j] + ' - 9 ' + Allone1[j] + ' <= 7']
                constr = constr + [Sum_one[j] + ' - 16 ' + Allone1[j] + ' >= 0']            
                            
                constr = constr + MITMPreConstraints.Determine_Allone(input2_col, Allone2[j])
                for i in range(8):
                    constr = constr + [out2_col[i] + ' - ' + Allone2[j] + ' = 0']
            
                #consume degrees
                CD_col = row(CD, j)
                for i in range(8):
                    constr = constr + MITMPreConstraints.Consume_degree(Allone1[j], out1_col[i], CD_col[i])
        else:
            constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input1_round), input1_L)
            constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input2_round), input2_L)
            for j in range(64):
                constr = constr + MITMPreConstraints.P_guess_forward(input1_L[j],input2_L[j],input1_L_dual[j],input2_L_dual[j],Pgu[j])
            constr = constr + MITMPreConstraints.equalConstraints(out1_round, input1_L_dual)
            constr = constr + MITMPreConstraints.equalConstraints(out2_round, input2_L_dual)  
                            
        return constr

    def genConstraints_of_backwardRound(self, r):
       
        input1_round = Vars_generator.genVars_input1_of_round(r)
        input2_round = Vars_generator.genVars_input2_of_round(r)
        
        input1_L = Vars_generator.genVars_input1_of_L(r)
        input2_L = Vars_generator.genVars_input2_of_L(r)
        
        input1_next = Vars_generator.genVars_input1_of_next(r)
        input2_next = Vars_generator.genVars_input2_of_next(r)
        
        Pgu = Vars_generator.genVars_guess(r)
        
        input1_next_dual = Vars_generator.genVars_input1_of_next_dual(r)
        input2_next_dual = Vars_generator.genVars_input2_of_next_dual(r)        
        
        Allone1 = Vars_generator.genVars_AllOne1_of_MixColumn(r)
        Allone2 = Vars_generator.genVars_AllOne2_of_MixColumn(r)       
        
        GSum_one = Vars_generator.genVars_SumOne_of_MixColumn(r)
        
        CD = Vars_generator.genVars_ConsumedDeg_of_MixColumn(r)
        
        AZ = Vars_generator.genVars_AllZero_of_MixColumn(r)
        EDZ = Vars_generator.genVars_Exist_dubbleZero(r) 
        

        if r < self.TR - 1:
            next_r = r + 1
        else:
            next_r = -1
            
        out1_round = Vars_generator.genVars_input1_of_round(next_r)
        out2_round = Vars_generator.genVars_input2_of_round(next_r)
    
        constr =[]
            
        if r< self.TR-1:
            # - Constraints for  ShiftRow
            constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input1_round), input1_L)
            constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input2_round), input2_L)
    
    
            constr = constr + MITMPreConstraints.equalConstraints(out1_round, input1_next)
            constr = constr + MITMPreConstraints.equalConstraints(out2_round, input2_next) 
            
            # - Constraints for  Pguess
            
            for j in range(64):
                constr = constr + MITMPreConstraints.P_guess_backward(input1_next[j],input2_next[j],input1_next_dual[j],input2_next_dual[j],Pgu[j])        
    
            # - Constraints for MixColumns         
            for j in range(8):
                input1_col = row(input1_next_dual, j)
                input2_col = row(input2_next_dual, j)
                out1_col = row(input1_L, j)
                out2_col = row(input2_L, j)
                
                Allzero_col = row(AZ, j)
                
                CD_col = row(CD, j)
                
                constr = constr + self.gensubConstraints_MixColumn_backward(input1_col, input2_col, out1_col, out2_col, Allzero_col, EDZ[j], Allone1[j], Allone2[j], CD_col, GSum_one[j])
        else:
            constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input1_round), input1_next_dual)
            constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input2_round), input2_next_dual)
            for j in range(64):
                constr = constr + MITMPreConstraints.P_guess_backward(input1_next[j],input2_next[j],input1_next_dual[j],input2_next_dual[j],Pgu[j])              
            constr = constr + MITMPreConstraints.equalConstraints(out1_round, input1_next)
            constr = constr + MITMPreConstraints.equalConstraints(out2_round, input2_next)             

        return constr
              
    def genConstraints_minus1(self):
        constr = []
        input1 = Vars_generator.genVars_input1_of_round(-1)
        input2 = Vars_generator.genVars_input2_of_round(-1)
        
        out1 = Vars_generator.genVars_input1_of_round(0)
        out2 = Vars_generator.genVars_input2_of_round(0)
        
        
        if self.mat_r < self.ini_r:
            constr = constr + [BasicTools.plusTerm(out1[32:64])+ ' = 0']
            constr = constr + [BasicTools.plusTerm(out2[32:64])+ ' = 0']
            
            constr = constr + MITMPreConstraints.equalConstraints(out1[0:32], input1[0:32])
            constr = constr + MITMPreConstraints.equalConstraints(out2[0:32], input2[0:32])                

        if self.mat_r > self.ini_r:
            constr = constr + [BasicTools.plusTerm(input1[32:64])+ ' = 0']
            constr = constr + [BasicTools.plusTerm(input2[32:64])+ ' = 0']
            
            constr = constr + MITMPreConstraints.equalConstraints(out1[0:32], input1[0:32])
            constr = constr + MITMPreConstraints.equalConstraints(out2[0:32], input2[0:32])              
     
        return constr
    
    def genConstraints_ini_degree(self):
        
        input1 = Vars_generator.genVars_input1_of_round(self.ini_r)
        input2 = Vars_generator.genVars_input2_of_round(self.ini_r)
        
        
        d1 = Vars_generator.genVars_degree_forward()
        d2 = Vars_generator.genVars_degree_backward()
        
        constr = []
        
        for j in range(64):
            
            constr = constr + [input1[j] + ' - ' + d1[j] + ' >= 0']
            constr = constr + [input2[j] + ' - ' + input1[j] + ' + ' + d1[j] + ' >= 0']
            constr = constr + [input2[j] + ' + ' + d1[j] + ' <= 1']
            
            constr = constr + [input2[j] + ' - ' + d2[j] + ' >= 0']
            constr = constr + [input1[j] + ' - ' + input2[j] + ' + ' + d2[j] + ' >= 0']
            constr = constr + [input1[j] + ' + ' + d2[j] + ' <= 1']
            
      
        return constr
   
        
    def genConstraints_matching_round(self): 
        constr = []
        input1_round = Vars_generator.genVars_input1_of_round(self.mat_r)
        input2_round = Vars_generator.genVars_input2_of_round(self.mat_r)
        
        if self.mat_r < self.TR -1:
            next_r = self.mat_r+1
        else :
            next_r = -1
        
        out1_round = Vars_generator.genVars_input1_of_round(next_r)
        out2_round = Vars_generator.genVars_input2_of_round(next_r)
        
        input1_L = Vars_generator.genVars_input1_of_L(self.mat_r)
        input2_L = Vars_generator.genVars_input2_of_L(self.mat_r)
        
        input1_next = Vars_generator.genVars_input1_of_next(self.mat_r)
        input2_next = Vars_generator.genVars_input2_of_next(self.mat_r)
        
       
        # - Constraints for  ShiftRow
        constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input1_round), input1_L)
        constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input2_round), input2_L)
        
        constr = constr + MITMPreConstraints.equalConstraints(out1_round, input1_next)
        constr = constr + MITMPreConstraints.equalConstraints(out2_round, input2_next) 

        return constr      
    
    
    def genConstraints_additional(self):
        constr = []
        CD1_f = []
        CD2_b = []
        
        Pguess_f = []
        Pguess_b = []
               
        if self.mat_r < self.ini_r:

            for r in range(0, self.mat_r):
                CD1_f = CD1_f + Vars_generator.genVars_ConsumedDeg_of_MixColumn(r)
                Pguess_f = Pguess_f + Vars_generator.genVars_guess(r)
            
            for r in range(self.ini_r, self.TR-1):
                CD1_f = CD1_f + Vars_generator.genVars_ConsumedDeg_of_MixColumn(r) 
                Pguess_f = Pguess_f + Vars_generator.genVars_guess(r)
            Pguess_f = Pguess_f + Vars_generator.genVars_guess(self.TR-1)
                
            for r in range(self.mat_r + 1, self.ini_r):
                CD2_b = CD2_b + Vars_generator.genVars_ConsumedDeg_of_MixColumn(r)
                Pguess_b = Pguess_b + Vars_generator.genVars_guess(r)
                
        if self.mat_r > self.ini_r:
            for r in range(self.ini_r, self.mat_r):
                CD1_f = CD1_f + Vars_generator.genVars_ConsumedDeg_of_MixColumn(r)
                Pguess_f = Pguess_f + Vars_generator.genVars_guess(r)
                
            for r in range(0, self.ini_r):
                CD2_b = CD2_b + Vars_generator.genVars_ConsumedDeg_of_MixColumn(r)
                Pguess_b = Pguess_b + Vars_generator.genVars_guess(r)
            
            for r in range(self.mat_r + 1, self.TR-1):
                CD2_b = CD2_b + Vars_generator.genVars_ConsumedDeg_of_MixColumn(r)
                Pguess_b = Pguess_b + Vars_generator.genVars_guess(r)                
            Pguess_b = Pguess_b + Vars_generator.genVars_guess(self.TR-1)
    
        d1 = Vars_generator.genVars_degree_forward()
        d2 = Vars_generator.genVars_degree_backward()               
        
        Deg1 = 'GDeg1'
        Deg2 = 'GDeg2'
        if len(CD2_b + Pguess_b) > 0:
            constr = constr + ['GDeg1' + ' - ' + BasicTools.MinusTerm(d1) + ' + ' + BasicTools.plusTerm(CD2_b+Pguess_b) + ' = 0']
        else:
            constr = constr + ['GDeg1' + ' - ' + BasicTools.MinusTerm(d1) + ' = 0']
            
        if len(CD1_f + Pguess_f) > 0:
            constr = constr + ['GDeg2' + ' - ' + BasicTools.MinusTerm(d2) + ' + ' + BasicTools.plusTerm(CD1_f+Pguess_f) + ' = 0']
        else:
            constr = constr + ['GDeg2' + ' - ' + BasicTools.MinusTerm(d2) + ' = 0 ']
            
        constr = constr + ['GDeg1' + ' >= 1']
        constr = constr + ['GDeg2' + ' >= 1']
        
        #constr = constr + [BasicTools.plusTerm(d1) + ' <= 26']
        #constr = constr + [BasicTools.plusTerm(d2) + ' <= 26']
       
        input1_mat = Vars_generator.genVars_input1_of_L(self.mat_r)
        input2_mat = Vars_generator.genVars_input2_of_L(self.mat_r)
        out1_mat = Vars_generator.genVars_input1_of_next(self.mat_r)
        out2_mat = Vars_generator.genVars_input2_of_next(self.mat_r)
        
        #match = Vars_generator.genVars_matching()
        matchvar1 = Vars_generator.genVars_matchvar1()
        matchvar2 = Vars_generator.genVars_matchvar2()

        for j in range(64):
            constr = constr + [input1_mat[j] + ' - ' + matchvar1[j] + ' <= 0']
            constr = constr + [input2_mat[j] + ' - ' + matchvar1[j] + ' <= 0']
            constr = constr + [input2_mat[j] + ' + ' + input1_mat[j] + ' - ' + matchvar1[j] + ' >= 0']
            #constr = constr + [input2_mat[j] + ' + ' + matchvar1[j] + ' <= 1'] 
            
            constr = constr + [out2_mat[j] + ' - ' + matchvar2[j] + ' <= 0']
            constr = constr + [out1_mat[j] + ' - ' + matchvar2[j] + ' <= 0']
            constr = constr + [out1_mat[j] + ' + ' + out2_mat[j] + ' - ' + matchvar2[j] + ' >= 0']
            #constr = constr + [out1_mat[j] + ' + ' + matchvar2[j] + ' <= 1']          

                       
        Gsum = Vars_generator.genVars_SumOne_of_MixColumn(self.mat_r)
        m1 = Vars_generator.genVars_M1_matching()
        m2 = Vars_generator.genVars_M2_matching()
        m3 = Vars_generator.genVars_M3_matching()
        m4 = Vars_generator.genVars_M4_matching()
        m5 = Vars_generator.genVars_M5_matching()
        m6 = Vars_generator.genVars_M6_matching()
        m7 = Vars_generator.genVars_M7_matching()
        m8 = Vars_generator.genVars_M8_matching()
        
        for j in range(8):
            constr = constr + [Gsum[j] + ' - ' + BasicTools.MinusTerm(row(matchvar1, j) + row(matchvar2, j)) + ' = 0']

            constr = constr + ['16 ' + m1[j] + ' - ' + Gsum[j] + ' <= 0']
            constr = constr + ['1 ' + m1[j] + ' - ' + Gsum[j] + ' >= -15']
            
            constr = constr + ['15 ' + m2[j] + ' - ' + Gsum[j] + ' <= 0']
            constr = constr + ['2 ' + m2[j] + ' - ' + Gsum[j] + ' >= -14']
            
            constr = constr + ['14 ' + m3[j] + ' - ' + Gsum[j] + ' <= 0']
            constr = constr + ['3 ' + m3[j] + ' - ' + Gsum[j] + ' >= -13']
            
            constr = constr + ['13 ' + m4[j] + ' - ' + Gsum[j] + ' <= 0']
            constr = constr + ['4 ' + m4[j] + ' - ' + Gsum[j] + ' >= -12']
            
            constr = constr + ['12 ' + m5[j] + ' - ' + Gsum[j] + ' <= 0']
            constr = constr + ['5 ' + m5[j] + ' - ' + Gsum[j] + ' >= -11']
            
            constr = constr + ['11 ' + m6[j] + ' - ' + Gsum[j] + ' <= 0']
            constr = constr + ['6 ' + m6[j] + ' - ' + Gsum[j] + ' >= -10']
           
            constr = constr + ['10 ' + m7[j] + ' - ' + Gsum[j] + ' <= 0']
            constr = constr + ['7 ' + m7[j] + ' - ' + Gsum[j] + ' >= -9']
            
            constr = constr + ['9 ' + m8[j] + ' - ' + Gsum[j] + ' <= 0']
            constr = constr + ['8 ' + m8[j] + ' - ' + Gsum[j] + ' >= -8']           
              
        GM = 'GMat'
        if len(Pguess_b + Pguess_f) > 0:
            constr = constr + [GM + ' - ' + BasicTools.MinusTerm(m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8) + ' + ' + BasicTools.plusTerm(Pguess_b + Pguess_f) + ' = 0']
        else:
            constr = constr + [GM + ' - ' + BasicTools.MinusTerm(m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8) + ' = 0']
        constr = constr + [GM + ' >= 1']
       
        return [constr, Deg1, Deg2, GM]
           
    def genConstraints_total(self):
        constr = []
        
        constr = constr + self.genConstraints_ini_degree()
        
        #state
        if self.mat_r < self.ini_r:
            for r in range(self.ini_r, self.TR):
                constr = constr + self.genConstraints_of_forwardRound(r)
                
            
            for r in range(0, self.mat_r):
                constr = constr + self.genConstraints_of_forwardRound(r)
                
            constr = constr + self.genConstraints_matching_round()
            constr = constr + self.genConstraints_minus1()
                
            for r in range(self.mat_r + 1, self.ini_r):
                constr = constr + self.genConstraints_of_backwardRound(r)
                
                
        if self.mat_r > self.ini_r:
            
            for r in range(self.ini_r, self.mat_r):
                constr = constr + self.genConstraints_of_forwardRound(r)
                
            constr = constr + self.genConstraints_matching_round()
            constr = constr + self.genConstraints_minus1()
            
            for r in range(self.mat_r + 1, self.TR):
                constr = constr + self.genConstraints_of_backwardRound(r)
            
            
            for r in range(0, self.ini_r):
                constr = constr + self.genConstraints_of_backwardRound(r)
             
        #degree
        constr = constr + self.genConstraints_ini_degree()
        
        #mathcing and additional
        constr = constr + self.genConstraints_additional()[0]
        
        return constr     
        

    def genModel(self, filename):

        V = set([])
        constr = list([])
        constr = constr + self.genConstraints_total()
        
        constr = constr + ['GObj - GDeg1 <= 0']
        constr = constr + ['GObj - GDeg2 <= 0']
        constr = constr + ['GObj - GMat <= 0']
        #constr = constr + ['GObj >= 4']
        #constr = constr + ['GObj <= 6']
        V = BasicTools.getVariables_From_Constraints(constr)
        #fid = open('./Model/v2.lp', 'w')
        fid = open('./Model/TR' + str(self.TR) + '_ini' + str(self.ini_r) + '_matr' + str(self.mat_r) + '_256.lp', 'w')
        
        fid.write('Maximize' + '\n')
        fid.write('GObj' + '\n')
        fid.write('\n')
        fid.write('Subject To')
        fid.write('\n')
        for c in constr:
            fid.write(c)
            fid.write('\n')        

        GV = []
        BV =[]
        for v in V:
            if v[0] == 'G':
                GV.append(v)
            else:
                BV.append(v)
                

        fid.write('Binary' + '\n')
        for bv in BV:
            fid.write(bv + '\n')
            
        fid.write('Generals' + '\n')
        for gv in GV:
            fid.write(gv + '\n') 
            
        fid.close()

def cmd():
    rd = open('./Model/Result_6half_guess_2.txt', 'w')
    rd.write('TR, ini_r, ini_k, mat_r: d1, d2, m' + '\n' )
    for TR in range(7, 8):
        #for ini_r in range(3, 4):
        for ini_r in range(0, TR-1):
            #for mat_r in range(4, 5):
            for mat_r in range(0, TR-1):
                if mat_r != ini_r:                        
                    #name = './Model/TR' + str(TR) + '_ini' + str(ini_r) + '_matr' + str(mat_r) + '_guess'
                    A = Constraints_generator(TR, ini_r, mat_r)
                    A.genModel('')
                    name = './Model/TR' + str(TR) + '_ini' + str(ini_r) + '_matr' + str(mat_r) + '_256'
                    #Model = read('./Model/v2.lp')
                    Model = read(name+'.lp')
                    Model.optimize()
                    
                    if Model.SolCount == 0:
                        pass  
                    else:
                        
                        Model.write(name + '.sol')
                        solFile = open('./' + name + '.sol', 'r')  
               
                        Sol = dict()
                
                        for line in solFile:
                            if line[0] != '#':
                                temp = line
                                temp = temp.replace('-', ' ')
                                temp = temp.split()
                                Sol[temp[0]] = int(temp[1])
                        rd.write(str(TR) + ',' + str(ini_r) + ',' + str(mat_r) + ':') 
                        rd.write(str(Sol['GDeg1'])+','+ str(Sol['GDeg2'])+ ','+ str(Sol['GMat']) + '\n')
                        rd.flush()
if __name__== "__main__":
    cmd()
    
