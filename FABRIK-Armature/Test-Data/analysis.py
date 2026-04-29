import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib

docs = ['Unconstrained_Final_Model_1.csv', 'Unconstrained_Final_Model_2.csv', 
        'Position_Only_Model_1.csv','Position_Only_Model_2.csv',
        'Rotation_Only_Model_1.csv','Rotation_Only_Model_2.csv',
        'Position_Only_With_Reset_Model_1.csv','Position_Only_With_Reset_Model_2.csv',
        'Rotation_With_Reset_Model_1.csv', 'Rotation_With_Reset_Model_2.csv',
        'PR_Constrained_Final_Model_1.csv', 'PR_Constrained_Final_Model_2.csv',
        'Fully_Constrained_Final_Model_1.csv', 'Fully_Constrained_Final_Model_2.csv']

for doc in docs:
        df = pd.read_csv(doc, index_col='Frame')

        LHMean = df['LeftArmDistance'].abs().mean()
        RHMean = df['RightArmDistance'].abs().mean()
        RLMean = df['RightLegDistance'].abs().mean()
        LLMean = df['LeftLegDistance'].abs().mean()
        SMean = df['ShouldersDistance'].abs().mean()
        LKMean = df['LeftKneeDistance'].abs().mean()
        RKMean = df['RightKneeDistance'].abs().mean()
        LEMean = df['LeftElbowDistance'].abs().mean()
        REMean = df['RightElbowDistance'].abs().mean()

        TotalMean = (LHMean + RHMean + RLMean + LLMean + SMean + LKMean + RKMean + LEMean + REMean)/9
        IntermediateMean = (LKMean + LEMean + REMean + RKMean)/4
        EndEffectorMean = (LHMean + RHMean + LLMean + RLMean + SMean)/5

        print('---------------')
        print(doc)
        print(f'Hands: {(LHMean + RHMean)/2} \nFeet: {(RLMean + LLMean)/2} \nElbows: {(LEMean + REMean)/2} \nKnees: {(LKMean + RKMean)/2} \nShoulder: {SMean} \n')
        # print(f"Left Hand: {LHMean}, Right Hand: {RHMean}, \nRight Leg: {RLMean}, Left Leg: {LLMean}, \nShoulders: {SMean}")
        # print(f"Left Knee: {LKMean} \nRight Knee: {RKMean} \nLeft Elbow: {LEMean} \nRight Elbow: {REMean}")
        print(f"Total Mean Distance: {TotalMean}")
        print(f"Intermediate Mean {IntermediateMean}")
        print(f"End Effector Mean {EndEffectorMean}")
