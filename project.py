from pyAudioAnalysis import audioTrainTest as aT
#from collections import defaultdict
import pickle

emo=aT.fileClassification('/home/meraki/Documents/AcadSems/7thSem/WARDI/project/download/emotionswav/happy/03a05Fc.wav','/home/meraki/Documents/AcadSems/7thSem/WARDI/pyAudioAnalysis/pyAudioAnalysis/svmemopikl','svm')

print(emo)
