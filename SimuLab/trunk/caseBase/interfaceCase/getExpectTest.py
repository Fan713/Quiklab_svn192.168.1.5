#! /usr/bin/env python
#coding=utf-8
'''
Created on 2019年3月19日

@author: KLJS276
'''
import sys

import trunk.common.lxmlReaderModify as lxmlManager
from trunk.common import readConfig

readIni = readConfig.readIniConfig("Interface")
mainFileDir = readIni.readConfig()[0]

fileName = open(mainFileDir,"r")
dom = lxmlManager.lxmlReaderModify(fileName)                        #实例化lxmlReaderModify类

'''
功能：获取模型个数
'''
def getModelCount():
    modelList = dom.getTabNodeValue("//SubModel")             #获取SubModel节点个数即模型个数
    modelCount = len(modelList)
    return modelCount
   
'''
功能：获取模型相关信息
'''    
def getModelInfo():
    modelNameList = []
    modelNameIdDict = {}
    modelNameTargetDict = {}
    modelId = dom.getTabNodeValue("//SubModel/@ID")                    #获取SubModel节点中的ID值,即模型的序号
    for nmodelid in modelId:
        modelName = dom.getTabNodeValue("//SubModel[@ID=" + nmodelid + "]/@Name")[0]      #获取序号对应的模型名称
        modelNameList.append(modelName)
        modelTarget = dom.getTabNodeValue("//SubModel[@ID=" + nmodelid + "]/SimuConfig/TargetIP/text()")[0]    #获取序号对应的下位机IP
        modelNameIdDict[modelName] = int(nmodelid)
        modelNameTargetDict[modelName] = modelTarget
    return modelNameList,modelNameTargetDict,modelNameIdDict      #返回模型名称列表,模型名称和下位机字典，模型名称和ID字典

'''
功能：获取参数个数
'''
def getParamCount():
    paramList = dom.getTabNodeValue("//Param")                #获取Param节点个数即参数个数
    paramCount = len(paramList)
    return paramCount

'''
功能：获取参数相关信息
'''
def getParamInfo():
    paramNameIdDict = {}
    paramModelNameDict = {}
    modelId = dom.getTabNodeValue("//SubModel/@ID")                #获取SubModel节点中的ID值,即模型的序号
    for nmodelId in modelId:
        nmodelName = dom.getTabNodeValue("//SubModel[@ID=" + nmodelId + "]/@Name")[0]    #获取模型ID对应的模型名称
        paramIdx = dom.getTabNodeValue("//SubModel[@ID=" + nmodelId + "]/DataDictionary/InternalParams/Param/@ID")          #获取配置文件中对应模型的参数ID
        for nparamIdx in paramIdx:
            #获取对应模型对应参数ID下的参数名称
            paramName = dom.getTabNodeValue("//SubModel[@ID=" + nmodelId + "]/DataDictionary/InternalParams/Param[@ID=" + nparamIdx + "]/Name/text()")[0]
            paramId = int(nmodelId) * 100000 + 60000 + int(nparamIdx)    #逻辑中的参数ID公式：模型ID*100000 + 60000 + 配置文件中的参数ID
            paramNameIdDict[paramName] = paramId
            paramModelNameDict[paramName] = nmodelName          #参数名称和模型的对应关系            
    return paramNameIdDict,paramModelNameDict

'''
功能：获取参数的值
'''
def getParamValue():
    paramNameValueDict = {}
    modelName = dom.getTabNodeValue("//SubModel/@Name")               #获取模型名称
    for nmodelName in modelName:
        paramId = dom.getTabNodeValue("//SubModel[@Name='" + nmodelName + "']/DataDictionary/InternalParams/Param/@ID")          #获取模型对应的参数名称
        for nparamId in paramId:
            #获取特定模型特定参数ID的参数名称
            paramName = dom.getTabNodeValue("//SubModel[@Name='" + nmodelName + "']/DataDictionary/InternalParams/Param[@ID=" + nparamId + "]/Name/text()")[0]
            #获取特定模型特定参数ID的参数值
            paramValue = dom.getTabNodeValue("//SubModel[@Name='" + nmodelName + "']/DataDictionary/InternalParams/Param[@ID=" + nparamId + "]/Value/text()")[0]
            paramValue= paramValue.split(",")
            for i in range(0,len(paramValue)):
                paramValue[i] = float(paramValue[i])      #参数值列表中的字符串数据转化为float型数据
            paramNameValueDict[paramName] = paramValue
    return paramNameValueDict
 
'''
功能：获取信号个数
'''
def getOutSigCount():
    outSigList = dom.getTabNodeValue("//OutputSig")
    outSigCount = len(outSigList)
    return outSigCount

'''
功能：获取信号相关信息
'''    
def getOutSigInfo():
    outSigNameIdDict = {}
    outSigModelNameDict = {}
    modelId = dom.getTabNodeValue("//SubModel/@ID")                #获取SubModel节点中的ID值,即模型的序号
    for nmodelId in modelId:
        nmodelName = dom.getTabNodeValue("//SubModel[@ID=" + nmodelId + "]/@Name")[0]    #获取模型ID对应的模型名称
        outSigIdx = dom.getTabNodeValue("//SubModel[@ID=" + nmodelId + "]/DataDictionary/OutputSignals/OutputSig/@ID")          #获取配置文件中对应模型的信号ID
        for noutSigIdx in outSigIdx:
            #获取对应模型对应参数ID下的信号名称
            outSigName = dom.getTabNodeValue("//SubModel[@ID=" + nmodelId + "]/DataDictionary/OutputSignals/OutputSig[@ID=" + noutSigIdx + "]/Name/text()")[0]
            outSigId = int(nmodelId) * 100000 + 40000 + int(noutSigIdx)    #逻辑中的参数ID公式：模型ID*100000 + 40000 + 配置文件中的信号ID
            outSigNameIdDict[outSigName] = outSigId
            outSigModelNameDict[outSigName] = nmodelName          #参数名称和模型的对应关系            
    return outSigNameIdDict,outSigModelNameDict
    
if __name__ == '__main__':
#     getModelCount()
#     getParamCount()
#     getOutSigCount()
#       getModelInfo()
#     getParamInfo()
    print getParamValue()
#    print getOutSigInfo()

    