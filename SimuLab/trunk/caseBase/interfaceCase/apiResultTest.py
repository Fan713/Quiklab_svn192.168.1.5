#! /usr/bin/env python
#coding=utf-8
from _ctypes import pointer, byref
from ctypes import c_char_p, c_int, c_double
import ctypes
import os
import sys
import time

# dir = os.path.abspath(os.path.join(os.getcwd(),"../../.."))
# sys.path.append(dir)

from common import readConfig, getInstallDir, loggingWriter,getHostInfo



readIni = readConfig.readIniConfig("Interface")
mainFileDir = readIni.readConfig()[0]                      #从配置文件中获取需要测试的工程路径(配置文件中配置)

installDir = getInstallDir.getInstallDir("RootPath")       #获取SimuLab的安装目录
lib = ctypes.cdll.LoadLibrary(installDir + r"\extern\api\SimuLabAPIEx.dll")

szProName = "s" * 1024
ProjStatus = c_int(0)                #初始化Ctype中的int类类型
nProjStatus = pointer(ProjStatus)    #int类型的指针
modelCount = c_int(0)
pModelCount = pointer(modelCount)
lastErrInfo = "t" * 1024
modelName = "s" * 1024
targetIp = "s" *1024
modelId = c_int(0)
pModelId = pointer(modelId)
timeOffset = c_int(0)
pTimeOffset = pointer(timeOffset)
factDataLen = c_int(1024)
nFactDataLen = pointer(factDataLen)
LogLevel= c_int(0)
LogTime = c_int(0)
RemainLogCount = c_int(0)
# nLogLevel = pointer(LogLevel)
nLogLevel = byref(LogLevel)
ulLogTime = pointer(LogTime)
nRemainLogCount = pointer(RemainLogCount)
simuLogInfo = "s" *1024
nSampleUs = c_int(1000)
nCachedDataCount = c_int(1024)

nOverRunCount = c_int(0)      #超时计数
overRunCount = pointer(nOverRunCount)

nStatus = c_int(0)    #录制组状态
groupStatus = pointer(nStatus)

sys.stdout = loggingWriter.Logger()

'''
功能：创建连接
'''
def creatConnect(szCtrlIp):
    #c_char_p 字符指针
    print "创建与仿真系统的连接通道:\n",lib.KLSL_CreateConnect(szCtrlIp)
    time.sleep(10)

'''
功能：加载工程
'''
def loadProject(szProjCfg):   
    print "加载工程:\n",lib.KLSL_LoadProject(szProjCfg)
    time.sleep(10)

'''
功能：获取工程状态
'''
def getProStatus():
    print "获取工程状态:\n",lib.KLSL_GetProjSimuStatus(szProName,len(szProName),nProjStatus),ProjStatus.value
    return ProjStatus.value
'''
功能：获取模型个数
'''
def getModelCount():
    print "获取模型个数:\n",lib.KLSL_GetProjModelCount(pModelCount),"模型个数:\n",modelCount.value
    mModelCount = modelCount.value
    print mModelCount
    return mModelCount


'''
功能：获取模型信息
'''
def getModelInfo():
    modelNameList = []
    modelNameIdDict = {}
    modelNameTargetDict = {}
    modelCount = getModelCount()
    for i in range(1,modelCount+1):
        print "获取指定模型序号模型名称:\n",lib.KLSL_GetModelInfo(i,modelName,len(modelName))
        nModelName = modelName.split("\x00")[0]                              #模型名称的列表
        print "模型运行的目标机信息:\n",lib.KLSL_GetModelTarget(nModelName,targetIp,len(targetIp))
        modelNameTargetDict[nModelName] = targetIp.split("\x00")[0]          #模型名称和下位机IP的对应关系
        print "通过模型名称获取模型ID:\n",lib.KLSL_GetModelIdByName(nModelName,pModelId)
        modelNameIdDict[nModelName] = modelId.value                    #模型名称和ID的对应关系
        modelNameList.append(modelName.split("\x00")[0])
    print "modelNameList",modelNameList,modelNameTargetDict,modelNameIdDict
    return modelNameList,modelNameTargetDict,modelNameIdDict

'''
功能：获取模型仿真状态
变量说明：getModelSimuMoniReturn表示调用接口是否成功
getModelStatusList表示调用接口是否成功的List(多个模型)
nOverRunCount表示超时计数
dMoniData表示模型仿真状态数据
'''
def getModelStatus():
    modelNameList = getModelInfo()[0]
    getModelStatusList = []
    moniData = c_double * 4
    dMoniData = moniData()
    for modelName in modelNameList:
        getModelSimuMoniReturn = lib.KLSL_GetModelSimuMoni(modelName,overRunCount,dMoniData,4)
        getModelStatusList.append(getModelSimuMoniReturn)
        print "获取模型仿真状态",getModelStatusList,modelName,nOverRunCount.value,dMoniData[:]
    print getModelStatusList
    return getModelStatusList
            
'''
功能：获取参数信息
'''
def getParamInfo():
    paramCount = c_int(0)
    pParamCount = pointer(paramCount)
    print "获取参数个数:\n",lib.KLSL_GetProjParamCount(pParamCount),"参数个数:\n",paramCount.value
    paramCount = paramCount.value      #参数个数
    paramName = "s" *1024
    paramId = c_int(0)
    pParamId = pointer(paramId)
    paramLength = c_int(0)
    nParamLength = pointer(paramLength)
    paraNameLengthDict = {}         #参数名称和长度的对应关系
    paramIdDict = {}                #参数名称和ID的对应关系
    paramModelNameDict = {}         #参数名称和模型名称的对应关系
    for i in range(1,paramCount+1):
        print "获取指定序号的参数名称:\n",lib.KLSL_GetParamInfo(i,paramName,len(paramName),nParamLength),"参数名称:\n",paramName.split("\x00")[0]
        nparamName = paramName.split("\x00")[0]
        paraNameLengthDict[nparamName] = paramLength.value
        print "通过参数名称获取参数ID:\n",lib.KLSL_GetParamIdByName(nparamName,pParamId),"参数名为" + nparamName + "的参数ID为",paramId.value
        paramIdDict[nparamName] = paramId.value
        print "通过参数名称获取模型名称:\n",lib.KLSL_GetModelNameByParamName(nparamName,modelName,len(modelName))
        paramModelNameDict[nparamName] = modelName.split("\x00")[0]
    return paraNameLengthDict,paramCount,paramIdDict,paramModelNameDict


'''
功能：注册参数(瞬态)
           获取参数值(瞬态)
           注销参数(瞬态)
'''
def paramLatest():
    regParamLatestReturnList =[]                      #存放调用注册参数(瞬态)接口是否成功（0或非0）
    getParamLatestValueReturnList = []                #存放调用获取参数值(瞬态)接口是否成功(0或非0)
    unParamLatestValueReturnList = []                  #存放调用注销参数(瞬态)接口是否成功(0或非0)
    paramInfo = getParamInfo()
    paraNameDict = paramInfo[0]                        #获取参数名称和长度对应关系
    print paraNameDict
    for paraName in paraNameDict:                                  #循环遍历注册参数/获取参数值/注销参数
        for i in range(0,paraNameDict[paraName] + 1):                   
            regParamLatestReturn = lib.KLSL_RegParamLatestValue(paraName,i)               #调用注册参数(瞬态)接口调用是否成功存入regParamLatestReturn(0或非0)
            regParamLatestReturnList.append(regParamLatestReturn)                                               
            print "注册参数（瞬态）:\n",regParamLatestReturnList,i
            time.sleep(10)
            #声明一个数组类型
            if i == 0:
                pDataValue = c_double * paraNameDict[paraName]
            else:
                pDataValue = c_double * 1 
            #实例化整型数组
            PDataValue = pDataValue()
            print "数组长度",len(PDataValue),PDataValue[0]
            getParamLatestValueReturn = lib.KLSL_GetParamLatestValue(paraName,i,pTimeOffset,PDataValue,paraNameDict[paraName],nFactDataLen)     #调用获取参数值接口是否成功存入getParamLatestValueReturn(0或非0)
            getParamLatestValueReturnList.append(getParamLatestValueReturn)
            print "获取参数值（瞬态）:\n",getParamLatestValueReturnList,"实际数据长度",factDataLen.value,"时间偏移",timeOffset.value
#             for j in range (0,len(PDataValue)):
            print "参数值",PDataValue[:]
            time.sleep(5)
            unParamLatestValueReturn = lib.KLSL_UnRegParamLatestValue(paraName,i)           #调用注销接口是否成功返回值存入unParamLatestValueReturn(0或非0)
            unParamLatestValueReturnList.append(unParamLatestValueReturn)
            print "注销参数（瞬态）:\n",unParamLatestValueReturnList,i
    return regParamLatestReturnList, getParamLatestValueReturnList, unParamLatestValueReturnList  
            
'''
功能：注册参数(连续)
           获取参数值(连续)
           注销参数(连续)
'''
def paramPeriod():
    regParamPeriodReturnList = []                  #存放调用注册参数(连续)接口是否成功(0或非0)
    getParamPeriodValueReturnList = []              #存放获取参数(连续)接口是否成功(0或非0)
    unRegParamPeriodReturnList = []                  #存放注销参数(连续)接口是否成功(0或非0)
    paramInfo = getParamInfo()
    paraNameDict = paramInfo[0]                            #获取参数名称和参数长度的对应关系                       
    paramValue = getParamValue()[1]                    #获取参数的值
    print paramValue
    
    for paraName in paraNameDict:                              #循环遍历注册参数/获取参数值/注销参数值
        time.sleep(5)
        for i in range(1,paraNameDict[paraName] + 1):
            regParamPeriodValue = lib.KLSL_RegParamPeriodValue(paraName,i,1000,10)                   #注册参数(连续)接口是否成功存入regParamPeriodValue(0或非0)
            regParamPeriodReturnList.append(regParamPeriodValue)
            print "regParam",regParamPeriodReturnList
            time.sleep(20)
            param_period_time_offset=(c_double*100)()                 #仿真时间偏移变量初始化
            param_period_value =(c_double*100)()                       #存放参数值的缓存pDataValue
            param_period_length=c_int(0)                                 #实际有效数据长度
            j = 0
            #因为注册之后,数据写入缓存中需要一定的时间,注册之后立即从缓存中读取数据无法获得真正的值
            while True:
                getParamPeriodReturn = lib.KLSL_GetParamPeriodValue(paraName,i,1000,byref(param_period_time_offset),byref(param_period_value),3,byref(param_period_length))         #调用获取参数值(连续)接口
                if param_period_value[0] != paramValue[paraName][i-1]:               #如果调用获取参数值(连续)接口获得的参数值与调用获取参数值接口获得的参数值不一致,循环100000次,当100000之后,说明获取参数值(连续)接口失败
                    j = j + 1
                    if j > 100000:
                        getParamPeriodReturn = 1
                        getParamPeriodValueReturnList.append(getParamPeriodReturn)
                        break 
                if param_period_value[0] == paramValue[paraName][i-1]:         #如果调用获取参数值(连续)接口获得的参数值与调用获取参数值接口获得的参数值一致,调用获取参数值(连续)接口成功
                    getParamPeriodValueReturnList.append(getParamPeriodReturn)
                    print  param_period_value[0]
                    break  
            print "参数的值",param_period_value[:] , "调用接口是否成功",getParamPeriodValueReturnList,"时间偏移",param_period_time_offset[:],"实际有效数据长度",param_period_length.value
            unRegParamPeriodValue = lib.KLSL_UnRegParamPeriodValue(paraName,i,1000)      #调用注销参数(连续)接口是否成功
            unRegParamPeriodReturnList.append(unRegParamPeriodValue)       
            print "unRegParam",  unRegParamPeriodReturnList
    return regParamPeriodReturnList,getParamPeriodValueReturnList,unRegParamPeriodReturnList


'''
功能：获取参数值
'''
def getParamValue():
    paramValueDictIndex = {}                 #存放的是偏移为[0，总长度]时获取的参数值
    paramValueDictAll = {}                   #存放的是偏移为0时获取的参数值
    paramAllList = []
    paramInfo = getParamInfo()
    paraNameDict = paramInfo[0]
    print paraNameDict
    for paraName in paraNameDict:          #循环参数名称
        for i in range(0,paraNameDict[paraName] + 1):       #根据参数长度进行获取参数值
            time.sleep(10)
            #声明一个数组类型
            if i == 0:
                pDataValue = c_double * paraNameDict[paraName]
            else:
                pDataValue = c_double * 1 
            #实例化整型数组
            PDataValue = pDataValue()
            lib.KLSL_GetParamValue(paraName,i,PDataValue,paraNameDict[paraName],nFactDataLen),factDataLen.value,paraName
            paramAllList.append(PDataValue[:])
            if i == 0:
                paramValueDictAll[paraName] = PDataValue[:]
        paramValueDictIndex[paraName] = paramAllList
        paramAllList = []
        
    print "模型中所有的参数值为",paramValueDictIndex,paramValueDictAll
    return paramValueDictIndex,paramValueDictAll


'''
功能：修改参数值
''' 
def setParamValue():

    paramValueDict = getParamValue()[1] 
    paramNameList = paramValueDict.keys()   #获取所有的参数名称
    for paramName in paramNameList:
        paramValueList = paramValueDict[paramName]      #获取参数所对应的参数值
        pDataValue = c_double * len(paramValueList)
        PDataValue = pDataValue()
        for i in range(0,len(paramValueList)):
            PDataValue[i] = paramValueList[i] + 1                         #构造修改之后的参数(原先的参数值加1)
        lib.KLSL_SetParamValue(paramName,0,PDataValue,len(PDataValue))    #调用修改参数值接口方法
        paramValueDict[paramName] = PDataValue[:]
    print "修改之后的参数值",paramValueDict
    return paramValueDict
        
               
'''
功能：获取输出信号信息
'''
def getOutSigInfo():
    OutSigCount = c_int(0)
    pOutSigCount = pointer(OutSigCount)
    print "获取所有输出信号个数:\n",lib.KLSL_GetProjOutSigCount(pOutSigCount),"信号个数:\n",OutSigCount.value
    outSigCount = OutSigCount.value
    
    outSigName = "s" *1024
    outSigId = c_int(0)
    pOutSigId = pointer(outSigId)
    nOutSigNameLengthDict = {}
    nOutSigIdDict = {}
    nOutSigModelnameDict = {}
    OutSigLength = c_int(0)
    pOutSigLength = pointer(OutSigLength)
    for i in range(1,OutSigCount.value+1):
        print "获取指定序号的信号名称:\n",lib.KLSL_GetOutSigInfo(i,outSigName,len(outSigName),pOutSigLength),"信号名称:\n",outSigName.split("\x00")[0],OutSigLength.value
        nOutSigName = outSigName.split("\x00")[0]
        nOutSigNameLengthDict[nOutSigName] = OutSigLength.value
        print "通过信号名称获取信号ID:\n",lib.KLSL_GetOutSigIdByName(nOutSigName,pOutSigId),"信号名为" + nOutSigName + "的信号ID为",outSigId.value
        nOutSigIdDict[nOutSigName] = outSigId.value
        print "通过信号名称获取模型名称:\n",lib.KLSL_GetModelNameByOutSigName(nOutSigName,modelName,len(modelName)),"模型名称为:",modelName.split("\x00")[0]
        nOutSigModelnameDict[nOutSigName] = modelName.split("\x00")[0]
    return outSigCount,nOutSigNameLengthDict,nOutSigIdDict,nOutSigModelnameDict

'''
功能：注册输出信号(瞬态)
           获取参输出信号(瞬态)
           注销输出信号(瞬态)
'''
def outSigLatest():
    regOutSigLatestReturnList = []              #调用注册输出信号(瞬态)接口是否成功(0或非0)存入regOutSigLatestReturnList
    getOutSigLatestValueReturnList = []           #调用获取输出信号(瞬态)接口是否成功(0或非0)存入getOutSigLatestValueReturnList
    unRegOutSigLatestReturnList = []              #调用注销输入信号(瞬态)接口是否成功(0或非0)存入unRegOutSigLatestReturnList
    outSigInfo = getOutSigInfo()                  #获取输出信号和信号长度的对应关系
    nOutSigNameDict = outSigInfo[1]               
    for outSigName in nOutSigNameDict:                                 #循环遍历输出信号调用注册信号/获取信号值/注销信号
        for i in range(0,nOutSigNameDict[outSigName] + 1):
            regOutSigLatestReturn = lib.KLSL_RegOutSigLatestValue(outSigName,i)
            regOutSigLatestReturnList.append(regOutSigLatestReturn)
            print "注册输出信号（瞬态）:\n",regOutSigLatestReturnList,i
            time.sleep(10)
            #声明一个数组类型
            if i == 0:
                pDataValue = c_double * nOutSigNameDict[outSigName]
            else:
                pDataValue = c_double * 1 
            #实例化整型数组
            PDataValue = pDataValue()
            print "数组长度",len(PDataValue)
            getOutSigLatestValueReturn = lib.KLSL_GetOutSigLatestValue(outSigName,i,pTimeOffset,PDataValue,nOutSigNameDict[outSigName],nFactDataLen)
            getOutSigLatestValueReturnList.append(getOutSigLatestValueReturn)
            print "获取输出信号值（瞬态）:\n",getOutSigLatestValueReturnList,"实际数据长度",factDataLen.value,"时间偏移",timeOffset.value
#             for j in range (0,len(PDataValue)):
            print PDataValue[:]
            unRegOutSigLatestReturn = lib.KLSL_UnRegOutSigLatestValue(outSigName,i)
            unRegOutSigLatestReturnList.append(unRegOutSigLatestReturn)
            print "注销输出信号（瞬态）:\n",unRegOutSigLatestReturnList,i
            
    return regOutSigLatestReturnList,getOutSigLatestValueReturnList,unRegOutSigLatestReturnList
            
'''
功能：注册输出信号(连续)
           获取参输出信号(连续)
           注销输出信号(连续)
'''
def outSigPeriod():
    regOutSigPeriodReturnList = []                         #存放调用注册输出信号(连续)是否成功(0或非0)
    getOutSigPeriodReturnList = []                         #存放获取信号值(连续)是否成功(0或非0)
    unRegOutSigPeriodReturnList = []                        #存放注销信号值(连续)是否成功(0或非0)
    outSigInfo = getOutSigInfo()
    nOutSigNameDict = outSigInfo[1]                    #获取信号名称和信号长度的对应关系
    for outSigName in nOutSigNameDict:                                   #循环遍历信号调用注册信号/获取信号值/注销信号
        for i in range(1,nOutSigNameDict[outSigName] + 1):
            time.sleep(10)
            regOutSigPeriodReturn = lib.KLSL_RegOutSigPeriodValue(outSigName,i,1000,10)
            regOutSigPeriodReturnList.append(regOutSigPeriodReturn)
            print "注册输出信号（连续）:\n",regOutSigPeriodReturnList,i
            signal_period_time_offset=(c_double*100)()
            signal_period_value=(c_double*100)()
            signal_period_length=c_int(0)
            getOutSigPeriodReturn = lib.KLSL_GetOutSigPeriodValue(outSigName,i,1000,byref(signal_period_time_offset),byref(signal_period_value),3,byref(signal_period_length))
            getOutSigPeriodReturnList.append(getOutSigPeriodReturn)
            print "获取输出信号值 （连续）:\n",getOutSigPeriodReturnList,signal_period_value[:],"时间偏移",signal_period_time_offset[:],"实际数据长度",signal_period_length.value
            unRegOutSigPeriodReturn = lib.KLSL_UnRegOutSigPeriodValue(outSigName,i,1000)
            unRegOutSigPeriodReturnList.append(unRegOutSigPeriodReturn)
            print "注销输出信号（连续）:\n",unRegOutSigPeriodReturnList
            
    return regOutSigPeriodReturnList,getOutSigPeriodReturnList,unRegOutSigPeriodReturnList
            
'''
功能：获取信号值
'''
def getOutSigValue():
    outSigValueDict = {}
    outSigValueAllList = []
    getOutSigValueReturnList = []
    outSigInfo = getOutSigInfo()
    outSigValueDict = outSigInfo[1]
    print outSigValueDict
    for outSigName in outSigValueDict:          #循环信号名称
        for i in range(0,outSigValueDict[outSigName] + 1):       #根据信号长度进行注册信号/获取信号值/注销信号
            time.sleep(10)
            #声明一个数组类型
            if i == 0:
                pDataValue = c_double * outSigValueDict[outSigName]
            else:
                pDataValue = c_double * 1 
            #实例化整型数组
            PDataValue = pDataValue()
            print "数组长度",len(PDataValue),PDataValue[0]
            getOutSigValueReturn = lib.KLSL_GetOutSigValue(outSigName,i,PDataValue,outSigValueDict[outSigName],nFactDataLen)
            getOutSigValueReturnList.append(getOutSigValueReturn)
            print "获取信号值:\n",getOutSigValueReturnList,factDataLen.value,outSigName
            outSigValueAllList.append(PDataValue[:])
            print outSigValueAllList
        outSigValueDict[outSigName] = outSigValueAllList
        print outSigValueDict
        outSigValueAllList = []
        
    print outSigValueDict,getOutSigValueReturnList
    return outSigValueDict,getOutSigValueReturnList

'''
功能：注册录制组
'''
def regRecordGroup(groupName,dataFormat,szFileDir,szFileName):
    paramIdDict = getParamInfo()[2]                       #参数名称和参数ID的字典
    outSigIdDict = getOutSigInfo()[2]                     #信号名称和信号ID的字典
    print paramIdDict,outSigIdDict
    outSigParamIdList = c_int * len(paramIdDict)
    nOutSigParamIdList = outSigParamIdList()            #定义参数/输出信号ID列表数组
    print paramIdDict.values()
    for i in range(0,len(paramIdDict.values())):
        nOutSigParamIdList[i] = paramIdDict.values()[i]         #将参数ID存入ID列表数组
    print nOutSigParamIdList
    outSigParamOffsetList = c_int * len(nOutSigParamIdList)
    nOutSigParamOffsetList = outSigParamOffsetList()            #参数/输出信号偏移， 取值范围 [1，总长度]
    for i in range(0,len(nOutSigParamIdList)):
        nOutSigParamOffsetList[i] = 1                           #每个参数只录制偏移为1的数据
    print os.path.exists(szFileDir),len(nOutSigParamIdList)
    regRecordGroupReturn = lib.KLSL_RegRecordGroup(groupName,1000,c_double(10),dataFormat,szFileDir,szFileName,nOutSigParamIdList,nOutSigParamOffsetList,len(nOutSigParamIdList))
#     print "注册录制组",lib.KLSL_RegRecordGroup(groupName,1000,c_double(10),dataFormat,szFileDir,szFileName,nOutSigParamIdList,nOutSigParamOffsetList,len(nOutSigParamIdList))
    return regRecordGroupReturn
'''
功能：获取录制组状态
'''
def getRecordStatus(groupName):
    getStatus = lib.KLSL_GetRecordGroupStatus(groupName,groupStatus)
    return nStatus.value,getStatus                  #调用接口工程与否(getStatus),录制组状态(nStatus.value)

'''
功能：注销录制组
'''
def unRegRecordGroup(groupName):
    function = lib.KLSL_UnRegRecordGroup(groupName)
    return function
    


'''
功能：获取最后的错误信息
'''
def getErrInfo():
    print "获取最后错误信息:\n",lib.KLSL_GetLastErrInfo(lastErrInfo,len(lastErrInfo)),lastErrInfo.split("\x00")[0]

'''
功能：获取仿真系统日志信息
'''
def getSimuLogInfo():
    print "获取仿真系统日志信息:\n",lib.KLSL_GetSimuLogInfo(nLogLevel,simuLogInfo,len(simuLogInfo),ulLogTime,nRemainLogCount)
    print LogLevel.value,LogTime.value,RemainLogCount.value,simuLogInfo.split("\x00")[0]

    for i in range(1,RemainLogCount.value):
        lib.KLSL_GetSimuLogInfo(nLogLevel,simuLogInfo,len(simuLogInfo),ulLogTime,nRemainLogCount)
    #     print LogLevel.value,LogTime.value,RemainLogCount.value,simuLogInfo.split("\x00")[0]

'''
功能：开始运行
'''
def execProject():
    print "开始运行:\n",lib.KLSL_ExecProject()
    
'''
功能：停止运行
'''
def stopProject():
    print "停止运行:\n",lib.KLSL_StopProject()
    
'''
功能：暂停运行
'''
def pauseProject():
    print "暂停运行:\n",lib.KLSL_PauseProject()
    
'''
功能：断开连接
'''
def disConnect():
    print "断开连接:\n",lib.KLSL_DisConnect()
    

if __name__ == "__main__":
    hostInfo = getHostInfo.getHostInfo()
    
    hostIp = hostInfo.getHostIp()
    creatConnect(hostIp)
    loadProject(mainFileDir)
    execProject()
    outSigPeriod()
    stopProject()
    disConnect()
