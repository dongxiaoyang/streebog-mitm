from CPMITM import *
from gurobipy import * 
import random

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

    def genVars_indicator(r):
        return ['Indicator1_' + str(j) + '_r' + str(r) for j in range(1)]
            
    
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

    def genVars_input1_of_keyround(r):   
        return ['KeyIS1_' + str(j) + '_r' + str(r) for j in range(64)]
 
    def genVars_input2_of_keyround(r): 
        return ['KeyIS2_' + str(j) + '_r' + str(r) for j in range(64)]    
    
    def genVars_input1_of_keyL(r):
        return ['KeyIM1_' + str(j) + '_r' + str(r) for j in range(64)]

    def genVars_input2_of_keyL( r):
        return ['KeyIM2_' + str(j) + '_r' + str(r) for j in range(64)]
        
    def genVars_input1_of_keyL_dual(r):
        return ['KeyDual_IM1_' + str(j) + '_r' + str(r) for j in range(64)]

    def genVars_input2_of_keyL_dual( r):
        return ['KeyDual_IM2_' + str(j) + '_r' + str(r) for j in range(64)]        
    
    def genVars_input1_of_keynext(r):
        return ['KeyIAK1_' + str(j) + '_r' + str(r) for j in range(64)]

    def genVars_input2_of_keynext(r):
        return ['KeyIAK2_' + str(j) + '_r' + str(r) for j in range(64)]
        
    def genVars_input1_of_keynext_dual(r):
        return ['KeyDual_IAK1_' + str(j) + '_r' + str(r) for j in range(64)]

    def genVars_input2_of_keynext_dual(r):
        return ['KeyDual_IAK2_' + str(j) + '_r' + str(r) for j in range(64)]         

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
        
    def genVars_ConsumedDeg_of_Addkey(r):
        if r>=0:
            return ['CDegAK_' + str(j) + '_r' + str(r) for j in range(64)]     
        else:
            return ['CDegAK_' + str(j) + '_r_minus' + str(-r) for j in range(32)]
        
    def genVars_AllOne1_of_keyMixColumn(r):
        return ['AO1key_' + str(j) + '_r' + str(r) for j in range(8)]
    
    def genVars_AllOne2_of_keyMixColumn(r):
        return ['AO2key_' + str(j) + '_r' + str(r) for j in range(8)]
   
    def genVars_AllZero_of_keyMixColumn(r):
        return ['AZkey_' + str(j) + '_r' + str(r) for j in range(64)]
    
    def genVars_SumOne_of_keyMixColumn(r):
        return ['GSOkey_'  + str(j) + '_r' + str(r) for j in range(8)]
    
    def genVars_Exist_keydubbleZero(r):
        return ['EDZkey_' + str(j) + '_r' + str(r) for j in range(8)]
    
    def genVars_ConsumedDeg_of_keyMixColumn(r):
        return ['CDegkey_' + str(j) + '_r' + str(r) for j in range(64)]    

    def genVars_AllZero_of_MixColumn_KeyAddition(r):
        return ['AZ_MC_KAD_' + str(j) + '_r' + str(r) for j in range(64)]

    def genVars_OR_MixColumn_KeyAddition(r):
        return ['OR_MC_KAD_' + str(j) + '_r' + str(r) for j in range(64)]        
        
    def genVars_guess(r):
        return ['Pguess_' + str(j) + '_r' + str(r) for j in range(64)]        
   
    def genVars_degree_forward():
        return ['deg_f' + str(j) for j in range(64)]
    
    def genVars_degree_backward():
        return ['deg_b' + str(j) for j in range(64)]
        
    def genVars_keyguess(r):
        return ['Pguesskey_' + str(j) + '_r' + str(r) for j in range(64)]        
   
    def genVars_degree_keyforward():
        return ['deg_keyf' + str(j) for j in range(64)]
    
    def genVars_degree_keybackward():
        return ['deg_keyb' + str(j) for j in range(64)]        
        
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
    
    def __init__(self, total_round, initial_round, initial_key, matching_round):
        self.ini_r = initial_round
        self.mat_r = matching_round
        self.ini_k = initial_key
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
        
    def gensubConstraints_MixColumn_KeyAddition_backward(self, input1_col, input2_col, input1_MC_KAD_col, input2_MC_KAD_col, OR_MC_KAD_col, out1_col, out2_col, Allzero_col, Allzero_MC_KAD_col, EDZ, Allone1, Allone2, CD_col, GSum_one):
        #_col means a 8 dim vector        
        constr = []
        for i in range(8):
            constr = constr + MITMPreConstraints.Determine_Allzero([input1_col[i], input2_col[i]], Allzero_col[i])
            constr = constr + MITMPreConstraints.Determine_Allzero([input1_MC_KAD_col[i], input2_MC_KAD_col[i]], Allzero_MC_KAD_col[i])
        constr = constr + MITMPreConstraints.Determine_ExistOne(Allzero_col + Allzero_MC_KAD_col, EDZ)
        
        constr = constr + [BasicTools.plusTerm(out1_col) + ' + 8 ' + EDZ + ' <= 8']
        constr = constr + [BasicTools.plusTerm(out2_col) + ' + 8 ' + EDZ + ' <= 8']
        
        constr = constr + MITMPreConstraints.Determine_Allone(input1_col + input1_MC_KAD_col, Allone1)
        constr = constr + [BasicTools.plusTerm(out1_col) + ' - 8 ' + Allone1 + ' = 0']
        
        constr = constr + MITMPreConstraints.Determine_Allone(input2_col + input2_MC_KAD_col, Allone2)
        for i in range(8):
            constr = constr + MITMPreConstraints.OR_backward(input1_col[i], input2_col[i], input1_MC_KAD_col[i], input2_MC_KAD_col[i], OR_MC_KAD_col[i])
        constr = constr + [GSum_one + ' + ' + BasicTools.plusTerm(OR_MC_KAD_col) + ' - ' + BasicTools.MinusTerm(out2_col) + ' = 8']
        constr = constr + [GSum_one + ' - 9 ' + Allone2 +  ' - ' + EDZ + ' <= 7']
        constr = constr + [GSum_one + ' - 16 ' + Allone2 + ' >= 0']

        #consume degrees
        for i in range(8):
            constr = constr + MITMPreConstraints.Consume_degree(Allone2, out2_col[i], CD_col[i])
        return constr         
                   
    def genConstraints_of_startRound(self, r):
        input1_round = Vars_generator.genVars_input1_of_round(r)
        input2_round = Vars_generator.genVars_input2_of_round(r)
        
        input1_P = Vars_generator.genVars_input1_of_next(r)
        input2_P = Vars_generator.genVars_input2_of_next(r)        
        
        input1_key = Vars_generator.genVars_input1_of_keyround(r+1)
        input2_key = Vars_generator.genVars_input2_of_keyround(r+1)        
        
        input1_L = Vars_generator.genVars_input1_of_L(r)
        input2_L = Vars_generator.genVars_input2_of_L(r)
        
        # input1_L_dual = Vars_generator.genVars_input1_of_L_dual(r)
        # input2_L_dual = Vars_generator.genVars_input2_of_L_dual(r)        
        
        # Pgu = Vars_generator.genVars_guess(r)
        
        Allone1 = Vars_generator.genVars_AllOne1_of_MixColumn(r) 
        Allone2 = Vars_generator.genVars_AllOne2_of_MixColumn(r)
        
        Sum_one = Vars_generator.genVars_SumOne_of_MixColumn(r)
        
        CD = Vars_generator.genVars_ConsumedDeg_of_MixColumn(r)
        
        CD_AK = Vars_generator.genVars_ConsumedDeg_of_Addkey(r)
        
        Allzero = Vars_generator.genVars_AllZero_of_MixColumn(r)
        EDZ = Vars_generator.genVars_Exist_dubbleZero(r)
        
       
        if r < self.TR - 1:
            next_r = r + 1
        else:
            next_r = -1
            
        out1_round = Vars_generator.genVars_input1_of_round(next_r)
        out2_round = Vars_generator.genVars_input2_of_round(next_r)
        
        constr =[]
        
        for j in range(64):
            constr = constr + MITMPreConstraints.XOR_forward([input1_P[j],input1_key[j]],[input2_P[j],input2_key[j]],out1_round[j],out2_round[j],CD_AK[j])   

        constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input1_round), input1_L)
        constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input2_round), input2_L)   

        for j in range(8):
            input1_col = row(input1_P, j)
            input2_col = row(input2_P, j)           
            out1_col = row(input1_L, j)
            out2_col = row(input2_L, j)
            
            Allzero_col = row(Allzero, j)           
            CD_col = row(CD, j)
            
            constr = constr + self.gensubConstraints_MixColumn_backward(input1_col, input2_col, out1_col, out2_col, Allzero_col, EDZ[j], Allone1[j], Allone2[j], CD_col, Sum_one[j])
            #constr = constr + self.gensubConstraints_MixColumn_KeyAddition_backward(input1_col, input2_col, input1_MC_KAD_col, input2_MC_KAD_col, OR_MC_KAD_col, out1_col, out2_col, Allzero_col, Allzero_MC_KAD_col, EDZ[j], Allone1[j], Allone2[j], CD_col, GSum_one[j])        
        
        
        

        return constr   

    def genConstraints_of_forwardRound(self, r):

        input1_round = Vars_generator.genVars_input1_of_round(r)
        input2_round = Vars_generator.genVars_input2_of_round(r)
        
        #ind_0 = Vars_generator.genVars_indicator(r-1)
        ind = Vars_generator.genVars_indicator(r)################################################
        
        input1_P = Vars_generator.genVars_input1_of_next(r)
        input2_P = Vars_generator.genVars_input2_of_next(r)        
        
        input1_key = Vars_generator.genVars_input1_of_keyround(r+1)
        input2_key = Vars_generator.genVars_input2_of_keyround(r+1)        
        
        input1_keyL = Vars_generator.genVars_input1_of_keyL(r)
        input2_keyL = Vars_generator.genVars_input2_of_keyL(r) ############################################               
        
        input1_L = Vars_generator.genVars_input1_of_L(r)
        input2_L = Vars_generator.genVars_input2_of_L(r)
        
        input1_L_dual = Vars_generator.genVars_input1_of_L_dual(r)
        input2_L_dual = Vars_generator.genVars_input2_of_L_dual(r)        
        
        Pgu = Vars_generator.genVars_guess(r)
        
        Allone1 = Vars_generator.genVars_AllOne1_of_MixColumn(r) 
        Allone2 = Vars_generator.genVars_AllOne2_of_MixColumn(r)
        
        Sum_one = Vars_generator.genVars_SumOne_of_MixColumn(r)
        
        CD = Vars_generator.genVars_ConsumedDeg_of_MixColumn(r)
        
        CD_AK = Vars_generator.genVars_ConsumedDeg_of_Addkey(r)
        
        Allzero = Vars_generator.genVars_AllZero_of_MixColumn(r)
        EDZ = Vars_generator.genVars_Exist_dubbleZero(r)
        
       
        if r < self.TR - 1:
            next_r = r + 1
        else:
            next_r = -1
            
        out1_round = Vars_generator.genVars_input1_of_round(next_r)
        out2_round = Vars_generator.genVars_input2_of_round(next_r)
        
        constr =[]
        
        if r <self.TR-1:

            
    
            # - Constraints for  ShiftRow
            constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input1_round), input1_L)
            constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input2_round), input2_L)
    
            # constr = constr + MITMPreConstraints.equalConstraints(out1_round, input1_next)
            # constr = constr + MITMPreConstraints.equalConstraints(out2_round, input2_next)    
            
            
            # - Constraints for  Pguess
            
            for j in range(64):
                constr = constr + MITMPreConstraints.P_guess_forward_indicator0(input1_L[j],input2_L[j],input1_L_dual[j],input2_L_dual[j],Pgu[j],ind[0])
               
        
            # - Constraints for MixColumns
    
            for j in range(8):
                input1_col = row(input1_L_dual, j)
                input2_col = row(input2_L_dual, j)
                out1_col = row(input1_P, j)
                out2_col = row(input2_P, j)           
                
                #determine whether (0,0) belongs the input column, if exists, then EDZ[j] = 1
                AO_col = row(Allzero, j)
                for i in range(8):
                    constr = constr + MITMPreConstraints.Determine_Allzero_indicator0([input1_col[i], input2_col[i]], AO_col[i],ind[0])
                constr = constr + MITMPreConstraints.Determine_ExistOne_indicator0(AO_col, EDZ[j],ind[0])
                
                #if (0,0) belongs  the input column
                constr = constr + [ind[0] + ' = 0 -> ' + BasicTools.plusTerm(out1_col) + ' + 8 ' + EDZ[j] + ' <= 8']
                constr = constr + [ind[0] + ' = 0 -> ' + BasicTools.plusTerm(out2_col) + ' + 8 ' + EDZ[j] + ' <= 8']
                
                #if (0,0) does not belong the input column and determine wether the first input column are all ones
                constr = constr + MITMPreConstraints.Determine_Allone_indicator0(input1_col, Allone1[j],ind[0])
                constr = constr + [ind[0] + ' = 0 -> ' + Sum_one[j] + ' - ' + BasicTools.MinusTerm(input1_col) + ' - ' + BasicTools.MinusTerm(out1_col) + ' = 0']
                constr = constr + [ind[0] + ' = 0 -> ' + Sum_one[j] + ' - 9 ' + Allone1[j] + ' <= 7']
                constr = constr + [ind[0] + ' = 0 -> ' + Sum_one[j] + ' - 16 ' + Allone1[j] + ' >= 0']            
                            
                constr = constr + MITMPreConstraints.Determine_Allone_indicator0(input2_col, Allone2[j],ind[0])
                for i in range(8):
                    constr = constr + [ind[0] + ' = 0 -> ' + out2_col[i] + ' - ' + Allone2[j] + ' = 0']
            
                #consume degrees
                CD_col = row(CD, j)
                for i in range(8):
                    constr = constr + MITMPreConstraints.Consume_degree_indicator0(Allone1[j], out1_col[i], CD_col[i],ind[0])
                    
        # - Constraints for  AK
            for j in range(64):
                constr = constr + MITMPreConstraints.XOR_forward_indicator0([input1_P[j],input1_key[j]],[input2_P[j],input2_key[j]],out1_round[j],out2_round[j],CD_AK[j],ind[0])  

##############################################################################################################################################################

        # - Constraints for  AKL
            for j in range(64):
                constr = constr + MITMPreConstraints.XOR_forward_indicator1([input1_L[j],input1_keyL[j]],[input2_L[j],input2_keyL[j]],input1_P[j],input2_P[j],CD_AK[j],ind[0]) 
                
                
            # - Constraints for  Pguess
            
            for j in range(64):
                constr = constr + MITMPreConstraints.P_guess_forward_indicator1(input1_P[j],input2_P[j],input1_L_dual[j],input2_L_dual[j],Pgu[j],ind[0])    
                

            for j in range(8):
                input1_col = row(input1_L_dual, j)
                input2_col = row(input2_L_dual, j)
                out1_col = row(out1_round, j)
                out2_col = row(out2_round, j)           
                
                #determine whether (0,0) belongs the input column, if exists, then EDZ[j] = 1
                AO_col = row(Allzero, j)
                for i in range(8):
                    constr = constr + MITMPreConstraints.Determine_Allzero_indicator1([input1_col[i], input2_col[i]], AO_col[i],ind[0])
                constr = constr + MITMPreConstraints.Determine_ExistOne_indicator1(AO_col, EDZ[j],ind[0])
                
                #if (0,0) belongs  the input column
                constr = constr + [ind[0] + ' = 1 -> ' + BasicTools.plusTerm(out1_col) + ' + 8 ' + EDZ[j] + ' <= 8']
                constr = constr + [ind[0] + ' = 1 -> ' + BasicTools.plusTerm(out2_col) + ' + 8 ' + EDZ[j] + ' <= 8']
                
                #if (0,0) does not belong the input column and determine wether the first input column are all ones
                constr = constr + MITMPreConstraints.Determine_Allone_indicator1(input1_col, Allone1[j],ind[0])
                constr = constr + [ind[0] + ' = 1 -> ' + Sum_one[j] + ' - ' + BasicTools.MinusTerm(input1_col) + ' - ' + BasicTools.MinusTerm(out1_col) + ' = 0']
                constr = constr + [ind[0] + ' = 1 -> ' + Sum_one[j] + ' - 9 ' + Allone1[j] + ' <= 7']
                constr = constr + [ind[0] + ' = 1 -> ' + Sum_one[j] + ' - 16 ' + Allone1[j] + ' >= 0']            
                            
                constr = constr + MITMPreConstraints.Determine_Allone_indicator1(input2_col, Allone2[j],ind[0])
                for i in range(8):
                    constr = constr + [ind[0] + ' = 1 -> ' + out2_col[i] + ' - ' + Allone2[j] + ' = 0']
            
                #consume degrees
                CD_col = row(CD, j)
                for i in range(8):
                    constr = constr + MITMPreConstraints.Consume_degree_indicator1(Allone1[j], out1_col[i], CD_col[i],ind[0])                
            
                    
                    
        else:
            # - Constraints for  ShiftRow
            constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input1_round), input1_L)
            constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input2_round), input2_L)
            constr = constr + MITMPreConstraints.equalConstraints(out1_round, input1_L)
            constr = constr + MITMPreConstraints.equalConstraints(out2_round, input2_L)
            
                            
        return constr

    def genConstraints_of_backwardRound(self, r):
       
        input1_round = Vars_generator.genVars_input1_of_round(r)
        input2_round = Vars_generator.genVars_input2_of_round(r)
        
        ind = Vars_generator.genVars_indicator(r)        
        
        input1_L = Vars_generator.genVars_input1_of_L(r)
        input2_L = Vars_generator.genVars_input2_of_L(r)
        
        input1_key = Vars_generator.genVars_input1_of_keyround(r+1)
        input2_key = Vars_generator.genVars_input2_of_keyround(r+1)  
        
        input1_keyL = Vars_generator.genVars_input1_of_keyL(r)
        input2_keyL = Vars_generator.genVars_input2_of_keyL(r)        
        
        # input1_P = Vars_generator.genVars_input1_of_next(r)
        # input2_P = Vars_generator.genVars_input2_of_next(r)
        
        Pgu = Vars_generator.genVars_guess(r)
        
        input1_next_dual = Vars_generator.genVars_input1_of_next_dual(r)
        input2_next_dual = Vars_generator.genVars_input2_of_next_dual(r)        
        
        Allone1 = Vars_generator.genVars_AllOne1_of_MixColumn(r)
        Allone2 = Vars_generator.genVars_AllOne2_of_MixColumn(r)       
        
        GSum_one = Vars_generator.genVars_SumOne_of_MixColumn(r)
        
        CD = Vars_generator.genVars_ConsumedDeg_of_MixColumn(r)

        #CD_AK = Vars_generator.genVars_ConsumedDeg_of_Addkey(r)
        
        AZ = Vars_generator.genVars_AllZero_of_MixColumn(r)
        EDZ = Vars_generator.genVars_Exist_dubbleZero(r) 
        
        AZ_MC_KAD = Vars_generator.genVars_AllZero_of_MixColumn_KeyAddition(r)
        OR_MC_KAD = Vars_generator.genVars_OR_MixColumn_KeyAddition(r)
        

        if r < self.TR - 1:
            next_r = r + 1
        else:
            next_r = -1
            
        out1_round = Vars_generator.genVars_input1_of_round(next_r)
        out2_round = Vars_generator.genVars_input2_of_round(next_r)
    
        constr =[]

        # - Constraints for  AK
        # for j in range(64):
            # constr = constr + MITMPreConstraints.XOR_backward([out1_round[j],input1_key[j]],[out2_round[j],input2_key[j]],input1_P[j],input2_P[j],CD_AK[j])            
        if r < self.TR-1:
            # - Constraints for  ShiftRow
            constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input1_round), input1_next_dual)
            constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input2_round), input2_next_dual)
    
    
            # constr = constr + MITMPreConstraints.equalConstraints(out1_round, input1_next)
            # constr = constr + MITMPreConstraints.equalConstraints(out2_round, input2_next) 
            
            # - Constraints for  Pguess
            
            for j in range(64):
                constr = constr + MITMPreConstraints.P_guess_backward(input1_L[j],input2_L[j],input1_next_dual[j],input2_next_dual[j],Pgu[j])        
    
            #- Constraints for MixColumns         
            for j in range(8):
                input1_col = row(out1_round, j)
                input2_col = row(out2_round, j)
                input1_MC_KAD_col = row(input1_key, j)
                input2_MC_KAD_col = row(input2_key, j)            
                out1_col = row(input1_L, j)
                out2_col = row(input2_L, j)
                
                Allzero_col = row(AZ, j)
                Allzero_MC_KAD_col = row(AZ_MC_KAD, j)
                
                CD_col = row(CD, j)
                OR_MC_KAD_col = row(OR_MC_KAD, j)
                
                #constr = constr + self.gensubConstraints_MixColumn_backward(input1_col, input2_col, out1_col, out2_col, Allzero_col, EDZ[j], Allone1[j], Allone2[j], CD_col, GSum_one[j])
                constr = constr + self.gensubConstraints_MixColumn_KeyAddition_backward(input1_col, input2_col, input1_MC_KAD_col, input2_MC_KAD_col, OR_MC_KAD_col, out1_col, out2_col, Allzero_col, Allzero_MC_KAD_col, EDZ[j], Allone1[j], Allone2[j], CD_col, GSum_one[j])
        else:
            # - Constraints for  ShiftRow
            constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input1_round), input1_next_dual)
            constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input2_round), input2_next_dual)
            
            for j in range(64):
                constr = constr + MITMPreConstraints.P_guess_backward(input1_L[j],input2_L[j],input1_next_dual[j],input2_next_dual[j],Pgu[j])             
            
            constr = constr + MITMPreConstraints.equalConstraints(out1_round, input1_L)
            constr = constr + MITMPreConstraints.equalConstraints(out2_round, input2_L)            
        return constr
              

    def genConstraints_of_forwardkey(self, r):

        input1_round = Vars_generator.genVars_input1_of_keyround(r)
        input2_round = Vars_generator.genVars_input2_of_keyround(r)
        
        input1_L = Vars_generator.genVars_input1_of_keyL(r)
        input2_L = Vars_generator.genVars_input2_of_keyL(r)
        
        input1_L_dual = Vars_generator.genVars_input1_of_keyL_dual(r)
        input2_L_dual = Vars_generator.genVars_input2_of_keyL_dual(r)        
        
        input1_next = Vars_generator.genVars_input1_of_keynext(r)
        input2_next = Vars_generator.genVars_input2_of_keynext(r)
        
        Pgu = Vars_generator.genVars_keyguess(r)
        
        Allone1 = Vars_generator.genVars_AllOne1_of_keyMixColumn(r) 
        Allone2 = Vars_generator.genVars_AllOne2_of_keyMixColumn(r)
        
        Sum_one = Vars_generator.genVars_SumOne_of_keyMixColumn(r)
        
        CD = Vars_generator.genVars_ConsumedDeg_of_keyMixColumn(r)
        
        Allzero = Vars_generator.genVars_AllZero_of_keyMixColumn(r)
        EDZ = Vars_generator.genVars_Exist_keydubbleZero(r)
        
       
        next_r = r + 1
        
            
        out1_round = Vars_generator.genVars_input1_of_keyround(next_r)
        out2_round = Vars_generator.genVars_input2_of_keyround(next_r)
        
        constr =[]

        # - Constraints for  ShiftRow
        constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input1_round), input1_L)
        constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input2_round), input2_L)

        # constr = constr + MITMPreConstraints.equalConstraints(out1_round, input1_next)
        # constr = constr + MITMPreConstraints.equalConstraints(out2_round, input2_next)    
        
        # - Constraints for  Pguess
        
        for j in range(64):
            constr = constr + MITMPreConstraints.P_guess_forward(input1_L[j],input2_L[j],input1_L_dual[j],input2_L_dual[j],Pgu[j])
    
        # - Constraints for MixColumns
        if r < self.TR:
            for j in range(8):
                input1_col = row(input1_L_dual, j)
                input2_col = row(input2_L_dual, j)
                out1_col = row(out1_round, j)
                out2_col = row(out2_round, j)           
                
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
                            
        return constr

    def genConstraints_of_backwardkey(self, r):
       
        input1_round = Vars_generator.genVars_input1_of_keyround(r)
        input2_round = Vars_generator.genVars_input2_of_keyround(r)
        
        input1_L = Vars_generator.genVars_input1_of_keyL(r)
        input2_L = Vars_generator.genVars_input2_of_keyL(r)
        
        input1_next = Vars_generator.genVars_input1_of_keynext(r)
        input2_next = Vars_generator.genVars_input2_of_keynext(r)
        
        Pgu = Vars_generator.genVars_keyguess(r)
        
        input1_next_dual = Vars_generator.genVars_input1_of_keynext_dual(r)
        input2_next_dual = Vars_generator.genVars_input2_of_keynext_dual(r)        
        
        Allone1 = Vars_generator.genVars_AllOne1_of_keyMixColumn(r)
        Allone2 = Vars_generator.genVars_AllOne2_of_keyMixColumn(r)       
        
        GSum_one = Vars_generator.genVars_SumOne_of_keyMixColumn(r)
        
        CD = Vars_generator.genVars_ConsumedDeg_of_keyMixColumn(r)
        
        AZ = Vars_generator.genVars_AllZero_of_keyMixColumn(r)
        EDZ = Vars_generator.genVars_Exist_keydubbleZero(r) 
        


        next_r = r + 1

            
        out1_round = Vars_generator.genVars_input1_of_keyround(next_r)
        out2_round = Vars_generator.genVars_input2_of_keyround(next_r)
    
        constr =[]
            
        
        # - Constraints for  ShiftRow
        constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input1_round), input1_L)
        constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input2_round), input2_L)


        # constr = constr + MITMPreConstraints.equalConstraints(out1_round, input1_next)
        # constr = constr + MITMPreConstraints.equalConstraints(out2_round, input2_next) 
        
        # - Constraints for  Pguess
        if r < self.TR:
            for j in range(64):
                constr = constr + MITMPreConstraints.P_guess_backward(out1_round[j],out2_round[j],input1_next_dual[j],input2_next_dual[j],Pgu[j])        

        # - Constraints for MixColumns     
        if r < self.TR:
            for j in range(8):
                input1_col = row(input1_next_dual, j)
                input2_col = row(input2_next_dual, j)
                out1_col = row(input1_L, j)
                out2_col = row(input2_L, j)
                
                Allzero_col = row(AZ, j)
                
                CD_col = row(CD, j)
                
                constr = constr + self.gensubConstraints_MixColumn_backward(input1_col, input2_col, out1_col, out2_col, Allzero_col, EDZ[j], Allone1[j], Allone2[j], CD_col, GSum_one[j])

        return constr
 

    def genConstraints_minus1(self):
        constr = []
        input1 = Vars_generator.genVars_input1_of_round(-1)
        input2 = Vars_generator.genVars_input2_of_round(-1)
        
        out1 = Vars_generator.genVars_input1_of_round(0)
        out2 = Vars_generator.genVars_input2_of_round(0)
        
        key1 = Vars_generator.genVars_input1_of_keyround(0)
        key2 = Vars_generator.genVars_input2_of_keyround(0)       
        
        CD_AK = Vars_generator.genVars_ConsumedDeg_of_Addkey(-1)
        
        
        
        if self.mat_r < self.ini_r:
            constr = constr + [BasicTools.plusTerm(out1[32:64])+ ' = 0']
            constr = constr + [BasicTools.plusTerm(out2[32:64])+ ' = 0']
            
            #constr = constr + MITMPreConstraints.equalConstraints(out1[0:32], input1[0:32])
            #constr = constr + MITMPreConstraints.equalConstraints(out2[0:32], input2[0:32])                

        if self.mat_r > self.ini_r:
            constr = constr + [BasicTools.plusTerm(input1[32:64])+ ' = 0']
            constr = constr + [BasicTools.plusTerm(input2[32:64])+ ' = 0']
            
            #constr = constr + MITMPreConstraints.equalConstraints(out1[0:32], input1[0:32])
            #constr = constr + MITMPreConstraints.equalConstraints(out2[0:32], input2[0:32]) 
        
        for j in range(32):
            if self.mat_r < self.ini_r:
                constr = constr + MITMPreConstraints.XOR_forward([input1[j], key1[j]], [input2[j], key2[j]], out1[j], out2[j], CD_AK[j])

            if self.mat_r > self.ini_r:
                constr = constr + MITMPreConstraints.XOR_backward([out1[j], key1[j]], [out2[j], key2[j]], input1[j], input2[j], CD_AK[j])
     
        return constr
 
    def genConstraints_ini_degree(self):
        
        input1 = Vars_generator.genVars_input1_of_next(self.ini_r)
        input2 = Vars_generator.genVars_input2_of_next(self.ini_r)
        
        input1_key = Vars_generator.genVars_input1_of_keyround(self.ini_k)
        input2_key = Vars_generator.genVars_input2_of_keyround(self.ini_k)
        
        
        d1 = Vars_generator.genVars_degree_forward()
        d2 = Vars_generator.genVars_degree_backward()
        
        d1_key = Vars_generator.genVars_degree_keyforward()
        d2_key = Vars_generator.genVars_degree_keybackward()
        
        constr = []
        
        for j in range(64):
            
            constr = constr + [input1[j] + ' - ' + d1[j] + ' >= 0']
            constr = constr + [input2[j] + ' - ' + input1[j] + ' + ' + d1[j] + ' >= 0']
            constr = constr + [input2[j] + ' + ' + d1[j] + ' <= 1']
            
            constr = constr + [input2[j] + ' - ' + d2[j] + ' >= 0']
            constr = constr + [input1[j] + ' - ' + input2[j] + ' + ' + d2[j] + ' >= 0']
            constr = constr + [input1[j] + ' + ' + d2[j] + ' <= 1']

            constr = constr + [input1_key[j] + ' - ' + d1_key[j] + ' >= 0']
            constr = constr + [input2_key[j] + ' - ' + input1_key[j] + ' + ' + d1_key[j] + ' >= 0']
            constr = constr + [input2_key[j] + ' + ' + d1_key[j] + ' <= 1']
            
            constr = constr + [input2_key[j] + ' - ' + d2_key[j] + ' >= 0']
            constr = constr + [input1_key[j] + ' - ' + input2_key[j] + ' + ' + d2_key[j] + ' >= 0']
            constr = constr + [input1_key[j] + ' + ' + d2_key[j] + ' <= 1']
            
      
        return constr
   
        
    def genConstraints_matching_round(self): 
        constr = []
        input1_round = Vars_generator.genVars_input1_of_round(self.mat_r)
        input2_round = Vars_generator.genVars_input2_of_round(self.mat_r)
        
        input1_key = Vars_generator.genVars_input1_of_keyround(self.mat_r+1)
        input2_key = Vars_generator.genVars_input2_of_keyround(self.mat_r+1)         
        
        if self.mat_r < self.TR -1:
            next_r = self.mat_r+1
        else :
            next_r = -1
        
        out1_round = Vars_generator.genVars_input1_of_round(next_r)
        out2_round = Vars_generator.genVars_input2_of_round(next_r)
        
        CD_AK = Vars_generator.genVars_ConsumedDeg_of_Addkey(self.mat_r)
        
        input1_L = Vars_generator.genVars_input1_of_L(self.mat_r)
        input2_L = Vars_generator.genVars_input2_of_L(self.mat_r)
        
        input1_P = Vars_generator.genVars_input1_of_next(self.mat_r)
        input2_P = Vars_generator.genVars_input2_of_next(self.mat_r)
        
        # - Constraints for  AK
        for j in range(64):
            constr = constr + MITMPreConstraints.XOR_Mat(out1_round[j],out2_round[j],input1_key[j],input2_key[j],input1_P[j],input2_P[j])        
        
       
        # - Constraints for  ShiftRow
        constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input1_round), input1_L)
        constr = constr + MITMPreConstraints.equalConstraints(P_stribog(input2_round), input2_L)
        
        # constr = constr + MITMPreConstraints.equalConstraints(out1_round, input1_next)
        # constr = constr + MITMPreConstraints.equalConstraints(out2_round, input2_next) 

        return constr      
    
    
    def genConstraints_additional(self):
        constr = []
        CD1_f = []
        CD2_b = []
        
        CD1_key_f = []
        CD2_key_b = []
        
        Pguess_f = []
        Pguess_b = []
               
        if self.mat_r < self.ini_r:

            for r in range(0, self.mat_r):
                CD1_f = CD1_f + Vars_generator.genVars_ConsumedDeg_of_MixColumn(r)
                CD1_key_f = CD1_key_f + Vars_generator.genVars_ConsumedDeg_of_Addkey(r)
                Pguess_f = Pguess_f + Vars_generator.genVars_guess(r)
            
            #CD1_key_f = CD1_key_f + Vars_generator.genVars_ConsumedDeg_of_Addkey(self.mat_r)
            CD1_key_f = CD1_key_f + Vars_generator.genVars_ConsumedDeg_of_Addkey(-1)
            
            for r in range(self.ini_r+1, self.TR-1):
                CD1_f = CD1_f + Vars_generator.genVars_ConsumedDeg_of_MixColumn(r) 
                CD1_key_f = CD1_key_f + Vars_generator.genVars_ConsumedDeg_of_Addkey(r)
                Pguess_f = Pguess_f + Vars_generator.genVars_guess(r)
                
                
           
                
            for r in range(self.mat_r + 1, self.ini_r):
                CD2_b = CD2_b + Vars_generator.genVars_ConsumedDeg_of_MixColumn(r)
                #CD2_key_b = CD2_key_b + Vars_generator.genVars_ConsumedDeg_of_Addkey(r)
                Pguess_b = Pguess_b + Vars_generator.genVars_guess(r)
                
            CD1_key_f = CD1_key_f + Vars_generator.genVars_ConsumedDeg_of_Addkey(self.ini_r)    
            CD2_b = CD2_b + Vars_generator.genVars_ConsumedDeg_of_MixColumn(self.ini_r)    
                
        if self.mat_r > self.ini_r:
            for r in range(self.ini_r+1, self.mat_r):
                CD1_f = CD1_f + Vars_generator.genVars_ConsumedDeg_of_MixColumn(r)
                CD1_key_f = CD1_key_f + Vars_generator.genVars_ConsumedDeg_of_Addkey(r)
                Pguess_f = Pguess_f + Vars_generator.genVars_guess(r)
                
            #CD1_key_f = CD1_key_f + Vars_generator.genVars_ConsumedDeg_of_Addkey(self.mat_r)    
            CD2_key_b = CD2_key_b + Vars_generator.genVars_ConsumedDeg_of_Addkey(-1)
                
            for r in range(0, self.ini_r):
                CD2_b = CD2_b + Vars_generator.genVars_ConsumedDeg_of_MixColumn(r)
                #CD2_key_b = CD2_key_b + Vars_generator.genVars_ConsumedDeg_of_Addkey(r)
                Pguess_b = Pguess_b + Vars_generator.genVars_guess(r)
            
            for r in range(self.mat_r + 1, self.TR-1):
                CD2_b = CD2_b + Vars_generator.genVars_ConsumedDeg_of_MixColumn(r)
                #CD2_key_b = CD2_key_b + Vars_generator.genVars_ConsumedDeg_of_Addkey(r)
                Pguess_b = Pguess_b + Vars_generator.genVars_guess(r) 

            Pguess_b = Pguess_b + Vars_generator.genVars_guess(self.TR-1)    

            CD1_key_f = CD1_key_f + Vars_generator.genVars_ConsumedDeg_of_Addkey(self.ini_r)    
            CD2_b = CD2_b + Vars_generator.genVars_ConsumedDeg_of_MixColumn(self.ini_r) 
     
        CD1_f_KS = [] 
        CD2_b_KS = []    

        Pguess_f_KS = []
        Pguess_b_KS = []

        for r in range(0, self.ini_k):
            CD2_b_KS = CD2_b_KS + Vars_generator.genVars_ConsumedDeg_of_keyMixColumn(r)
            Pguess_b_KS = Pguess_b_KS + Vars_generator.genVars_keyguess(r)
        
        for r in range(self.ini_k, self.TR-1):
            CD1_f_KS = CD1_f_KS + Vars_generator.genVars_ConsumedDeg_of_keyMixColumn(r)
            Pguess_f_KS = Pguess_f_KS + Vars_generator.genVars_keyguess(r)
    
        d1 = Vars_generator.genVars_degree_forward()
        d2 = Vars_generator.genVars_degree_backward()     

        d1_key = Vars_generator.genVars_degree_keyforward()
        d2_key = Vars_generator.genVars_degree_keybackward()        
        
        Deg1 = 'GDeg1'
        Deg2 = 'GDeg2'
        if len(CD2_b + Pguess_b + CD2_key_b + CD2_b_KS+Pguess_b_KS) > 0:
            constr = constr + ['GDeg1' + ' - ' + BasicTools.MinusTerm(d1+d1_key) + ' + ' + BasicTools.plusTerm(CD2_b+CD2_key_b+CD2_b_KS+Pguess_b+Pguess_b_KS) + ' = 0']
        else:
            constr = constr + ['GDeg1' + ' - ' + BasicTools.MinusTerm(d1+d1_key) + ' = 0']
            
        if len(CD1_f + Pguess_f + CD1_key_f + CD1_f_KS+Pguess_f_KS) > 0:
            constr = constr + ['GDeg2' + ' - ' + BasicTools.MinusTerm(d2+d2_key) + ' + ' + BasicTools.plusTerm(CD1_f+CD1_key_f+CD1_f_KS+ Pguess_f+Pguess_f_KS) + ' = 0']
        else:
            constr = constr + ['GDeg2' + ' - ' + BasicTools.MinusTerm(d2+d2_key) + ' = 0 ']
            
        constr = constr + ['GDeg1' + ' >= 1']
        constr = constr + ['GDeg2' + ' >= 1']
        
       
        input1_mat = Vars_generator.genVars_input1_of_L(self.mat_r)
        input2_mat = Vars_generator.genVars_input2_of_L(self.mat_r)
        
        out1_mat = Vars_generator.genVars_input1_of_next(self.mat_r)
        out2_mat = Vars_generator.genVars_input2_of_next(self.mat_r)        
        
        # if self.mat_r < self.TR - 1:
            # next = self.mat_r + 1
        # else:
            # next = -1
            
        # out1_mat = Vars_generator.genVars_input1_of_next(next)
        # out2_mat = Vars_generator.genVars_input2_of_next(next)
        
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
        if len(Pguess_b + Pguess_f + Pguess_f_KS + Pguess_b_KS) > 0:
            constr = constr + [GM + ' - ' + BasicTools.MinusTerm(m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8) + ' + ' + BasicTools.plusTerm(Pguess_b + Pguess_f + Pguess_f_KS + Pguess_b_KS) + ' = 0']
        else:
            constr = constr + [GM + ' - ' + BasicTools.MinusTerm(m1 + m2 + m3 + m4 + m5 + m6 + m7 + m8) + ' = 0']
        constr = constr + [GM + ' >= 1']
       
        return [constr, Deg1, Deg2, GM]
           
    def genConstraints_total(self):
        constr = []
        
        constr = constr + self.genConstraints_ini_degree()
        
        #state
        if self.mat_r < self.ini_r:
            for r in range(self.ini_r+1, self.TR):
                constr = constr + self.genConstraints_of_forwardRound(r)
                
            
            for r in range(0, self.mat_r):
                constr = constr + self.genConstraints_of_forwardRound(r)
                
            constr = constr + self.genConstraints_matching_round()
            constr = constr + self.genConstraints_minus1()
            constr = constr + self.genConstraints_of_startRound(self.ini_r)
                
            for r in range(self.mat_r + 1, self.ini_r):
                constr = constr + self.genConstraints_of_backwardRound(r)
                
                
        if self.mat_r > self.ini_r:
            
            for r in range(self.ini_r+1, self.mat_r):
                constr = constr + self.genConstraints_of_forwardRound(r)
                
            constr = constr + self.genConstraints_matching_round()
            constr = constr + self.genConstraints_minus1()
            constr = constr + self.genConstraints_of_startRound(self.ini_r)
            
            for r in range(self.mat_r + 1, self.TR):
                constr = constr + self.genConstraints_of_backwardRound(r)
            
            
            for r in range(0, self.ini_r):
                constr = constr + self.genConstraints_of_backwardRound(r)
             
        #degree
        constr = constr + self.genConstraints_ini_degree()
        
        
        #keyschedual
        for r in range(0, self.ini_k):
            constr = constr + self.genConstraints_of_backwardkey(r)
             
        for r in range(self.ini_k, self.TR-1):
            constr = constr + self.genConstraints_of_forwardkey(r)
        
        #mathcing and additional
        constr = constr + self.genConstraints_additional()[0]
        # input1_key = Vars_generator.genVars_input1_of_keyround(0)
        # input2_key = Vars_generator.genVars_input2_of_keyround(0)
        # constr = constr + [BasicTools.plusTerm(input1_key) + ' = 0']        
        # constr = constr + [BasicTools.plusTerm(input2_key) + ' = 64']
        
        
        return constr     
        

    def genModel(self, filename):

        V = set([])
        constr = list([])
        constr = constr + self.genConstraints_total()
        
        constr = constr + ['GObj - GDeg1 <= 0']
        constr = constr + ['GObj - GDeg2 <= 0']
        constr = constr + ['GObj - GMat <= 0']
        V = BasicTools.getVariables_From_Constraints(constr)
        #fid = open('./Model/mcak1.lp', 'w')
        fid = open('./Model/TR' + str(self.TR) + '_ini' + str(self.ini_r) + '_matr' + str(self.mat_r) + '_ini_k'+ str(self.ini_k) + 'MCAK.lp', 'w')
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
            
        fid.write('Integer' + '\n')
        for gv in GV:
            fid.write(gv + '\n') 
            
        fid.close()

def cmd():
    rd = open('./Model/Result_8_guess_halfround.txt', 'w')
    rd.write('TR, ini_r, ini_k, mat_r: d1, d2, m' + '\n' )
    for TR in range(8, 9):
        for ini_r in range(2, 3):
            for ini_k in range(4, 5): #ini_k<TR
                for mat_r in range(5, 6):
        #a=[]
        #for i in range(0,1):
            # ini_r = random.randrange(0,TR)
            # ini_k = random.randrange(0,TR)
            # mat_r = random.randrange(0,TR-1)
            # ini_r=2
            # mat_r=5
            # ini_k=5
            # b=[ini_r,ini_k,mat_r]
            # if i==0:
                # k=0
                # a=a+[b]
            # if i>=1:
                # k=0
                # for j in a:
                    # if b==j:
                        # k=1
                # if k==0:
                    # a=a+[b]            
                    if mat_r != ini_r:  
                    #if k==0 and mat_r != ini_r:             
                        name = './Model/TR' + str(TR) + '_ini' + str(ini_r) + '_matr' + str(mat_r) + '_ini_k'+ str(ini_k) + 'MCAK'
                        A = Constraints_generator(TR, ini_r, ini_k, mat_r)
                        A.genModel('')
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
                            rd.write(str(TR) + ',' + str(ini_r) + ',' + str(mat_r) + ',' + str(ini_k) + ':') 
                            rd.write(str(Sol['GDeg1'])+','+ str(Sol['GDeg2'])+ ','+ str(Sol['GMat']) + '\n')
                            rd.flush()
if __name__== "__main__":
    cmd()
    
