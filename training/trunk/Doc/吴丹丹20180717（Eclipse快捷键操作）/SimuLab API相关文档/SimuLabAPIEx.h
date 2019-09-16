 /*!
 * \file SimuLabAPI_Ex.h
 * \brief SimuLab 3.0的接口。只服务于LabView调用
 * \date 2018/12/12
 */

#pragma once
#pragma pack(4)

#ifndef SIMULABAPIEX_H
#define SIMULABAPIEX_H

#ifdef SimuLabAPIEX_LIB
# define API_EXPORT  __declspec(dllexport)
#else
# define API_EXPORT  __declspec(dllimport)
#endif

extern "C"
{
	/************************************************************************/
	/*				1、创建连接							                    */
	/************************************************************************/
	/// \details 创建与仿真系统的连接	
	/// \param[in]  szCtrlIp 仿真系统上位机服务端ip
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功
	int API_EXPORT KLSL_CreateConnect(const char szCtrlIp[]);
	
	/// \details 断开连接
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功
	int API_EXPORT KLSL_DisConnect();
	
	/// \details 获取最后错误信息
	/// \param[out] szBuff 用于存放错误信息的缓存
	/// \param[in]   nBuffLen 缓存的大小
	/// \retval != 0  函数调用失败
	/// \retval = 0   函数调用成功
	int API_EXPORT KLSL_GetLastErrInfo(char szBuff[],  int nBuffLen);
	
	/// \details 获取仿真系统日志信息
	/// \param[out] nLogLevel 日志级别
	///				nLogLevel = 1 出错
	///				nLogLevel = 2 警告
	///				nLogLevel = 3 提示
	///				nLogLevel = 4 信息
	///				nLogLevel = 5 调试
	/// \param[out] szLogInfo 存放日志信息缓存
	/// \param[in]   nLogBuffLen 日志缓存长度
	/// \param[out] ulLogTime 日志产生时间
	/// \param[out] nRemianLogCount 剩余日志数目
	/// \retval != 0  函数调用失败
	/// \retval = 0   函数调用成功
	int API_EXPORT KLSL_GetSimuLogInfo(int *nLogLevel, char szLogInfo[], int nLogBuffLen, unsigned long *ulLogTime, int *nRemainLogCount);

	/************************************************************************/
	/*				2、工程控制，获取仿真状态							                    */
	/************************************************************************/
	/// \details 获取工程状态
	/// \param[out] szProjCfg 用于存放工程配置文件的缓存
	/// \param[in]  nProjCfgBuffLen 缓存工程名称的长度
	/// \param[out] nProjStatus 用于存放工程状态的缓存指针
	/// \				    nProjStatus = 1  未加载
	/// \				    nProjStatus = 2  暂停
	/// \				    nProjStatus = 3  运行
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功	
	int API_EXPORT KLSL_GetProjSimuStatus(char szProjCfg[], int nProjCfgBuffLen, int *nProjStatus);

	/// \details 获取模型仿真状态
	/// \param[out]  szModelName 模型名称
	/// \param[out]  nOverRunCount 超时计数
	/// \param[out]  dMoniData 模型仿真状态数据信息
	///						dMoniData[0] 当前仿真时间偏移，单位秒
	///						dMoniData[1] 上一步运行总时间，单位秒
	///						dMoniData[2] 上一步模型执行时间，单位秒
	///						dMoniData[3] 上一步空闲等待时间，单位秒
	/// \param[in]   nDataBuffLen dMoniData的长度
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功
	int API_EXPORT KLSL_GetModelSimuMoni(const char szModelName[],int *nOverRunCount,double dMoniData[], int nDataBuffLen);

	/// \details 加载：工程状态为未加载时，才可调用
	/// \param[in]   szProjCfg 仿真工程配置文件全路径
	/// \retval != 0  函数调用失败
	/// \retval = 0   函数调用成功
	int API_EXPORT KLSL_LoadProject(const char szProjCfg[]);

	/// \details 开始，工程状态为暂停时，才可调用
	/// \retval != 0  函数调用失败
	/// \retval = 0   函数调用成功
	int API_EXPORT KLSL_ExecProject();

	/// \details 暂停，工程状态为执行时，才可调用
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功
	int API_EXPORT KLSL_PauseProject();

	/// \details 停止（重置）,连接成功后的任何时候均可调用
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功
	int API_EXPORT KLSL_StopProject();

	/************************************************************************/
	/*					3、获取模型、参数、信号信息							    */
	/************************************************************************/
	/// \details 获取模型个数
	/// \retval 模型个数
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功
	int API_EXPORT KLSL_GetProjModelCount(int *nCount);

	/// \details 获取所有参数个数
	/// \retval 参数个数
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功
	int API_EXPORT KLSL_GetProjParamCount(int *nCount);

	/// \details 获取所有输出个数
	/// \retval 输出个数
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功
	int API_EXPORT KLSL_GetProjOutSigCount(int *nCount);

	/// \details 获取指定模型序号模型信息
	/// \param[in]  nModelIdx 数组序号, 大于0
	/// \param[in]  szModelName 模型名称
	/// \param[in]  nNameBuffLen 名称Buff长度
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功
	int API_EXPORT KLSL_GetModelInfo(int nModelIdx, char szModelName[], int nNameBuffLen);
	
	/// \details 获取指定模型的目标机信息
	/// \param[in]   szModelName 模型名称
	/// \param[out] szTargetIp 存放目标机IP地址缓存
	/// \param[in]   nTargetBuffLen 目标机Buff长度
	/// \retval != 0  函数调用失败
	/// \retval = 0   函数调用成功
	int API_EXPORT KLSL_GetModelTarget(const char szModelName[], char szTargetIp[], int nTargetBuffLen);

	/// \details 获取指定模型序号模型信息
	/// \param[in]   nParamIndex 数组序号，大于0
	/// \param[in]   szParamName 参数名称
	/// \param[in]   nNameBuffLen 名称Buff长度
	/// \param[out] nParamLength 参数大小
	/// \retval != 0  函数调用失败
	/// \retval = 0   函数调用成功
	int API_EXPORT KLSL_GetParamInfo(int nParamIndex, char szParamName[], int nNameBuffLen, int *nParamLength);

	/// \details 获取输出信号信息
	/// \param[in]   nOutSigIdx 数组序号，大于0
	/// \param[in]   szSigName 存放输出信号名称缓存
	/// \param[in]   nSigNameBuffLen 名称缓存长度
	/// \param[out] nOutSigLength 输出信号大小
	/// \retval != 0  函数调用失败
	/// \retval = 0   函数调用成功
	int API_EXPORT KLSL_GetOutSigInfo(int nOutSigIdx, char szSigName[], int nSigNameBuffLen, int *nOutSigLength);

	/// \details 获取模型ID通过名称
	/// \param[in]   szModelName 模型名称
	/// \param[out] nModelId 模型ID
	/// \retval != 0  函数调用失败
	/// \retval = 0   函数调用成功
	int API_EXPORT KLSL_GetModelIdByName(const char szModelName[], int *nModelId);

	/// \details 获取参数ID通过名称
	/// \param[in]   szParamName 参数名称
	/// \param[out] nParamId 参数ID
	/// \retval != 0  函数调用失败
	/// \retval = 0   函数调用成功
	int API_EXPORT KLSL_GetParamIdByName(const char szParamName[], int *nParamId);

	/// \details 获取输出信号ID通过名称
	/// \param[in]  szOutSigName 输出信号名称
	/// \param[out] nOutSigId 输出信号ID
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功
	int API_EXPORT KLSL_GetOutSigIdByName(const char szOutSigName[], int *nOutSigId);
	
	/// \details 获取模型名称根据参数名称
	/// \param[in]   szParamName 参数名称
	/// \param[out] szModelName 存放模型名称的缓存
	/// \param[in]   nNameBuffLen 名称缓存长度
	/// \retval != 0  函数调用失败
	/// \retval = 0   函数调用成功
	int API_EXPORT KLSL_GetModelNameByParamName(const char szParamName[], char szModelName[], int nNameBuffLen);

	/// \details 获取模型名称根据输出信号名称
	/// \param[in]   szOutSigName 输出信号名称
	/// \param[out] szModelName 存放模型名称缓存
	/// \param[in]   nNameBuffLen 名称缓存长度
	/// \retval != 0  函数调用失败
	/// \retval = 0   函数调用成功
	int API_EXPORT KLSL_GetModelNameByOutSigName(const char szOutSigName[], char szModelName[], int nNameBuffLen);

	/************************************************************************/
	/*					4、设置参数值，获取参数信号值							*/
	/************************************************************************/

	/// \details 调参
	/// \param[in]  szParamName 参数名称
	/// \param[in]  nOffSet 数组偏移：取值范围 [0，总长度]，0表示数组全部,其余表示单个
	/// \param[in]  pDataValue 参数数值
	/// \param[in]  nDataSize 传入参数的数组大小：若此值与数组偏移不匹配则函数会返回失败
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功
	int API_EXPORT KLSL_SetParamValue(const char szParamName[], int nOffSet,double pDataValue[], int nDataSize);
	
	/// \details 获取参数值
	/// \param[in]    szParamName 参数名称
	/// \param[in]    nOffSet 数组偏移：取值范围 [0，总长度]，0表示数组全部,其余表示单个
	/// \param[out]  pDataValue 存放参数的缓存
	/// \param[in]    nDataBuffLen 参数缓存长度
	/// \param[out]   nFactDataLen 实际获取到的长度
	/// \retval != 0   函数调用失败
	/// \retval = 0    函数调用成功
	int API_EXPORT KLSL_GetParamValue(const char szParamName[], int nOffSet, double pDataValue[], int nDataBuffLen, int *nFactDataLen);

	/// \details 获取信号值
	/// \param[in]    szOutSigName 信号名称
	/// \param[in]    nOffSet 数组偏移：取值范围 [0，总长度]，0表示数组全部,其余表示单个
	/// \param[out]   pDataValue 存放信号的缓存
	/// \param[in]    nDataBuffLen 信号缓存长度
	/// \param[out]   nFactDataLen 实际获取到的长度
	/// \retval != 0   函数调用失败
	/// \retval = 0    函数调用成功
	int API_EXPORT KLSL_GetOutSigValue(const char szOutSigName[], int nOffSet, double pDataValue[], int nDataBuffLen,int *nFactDataLen);

	/************************************************************************/
	/*					5、注册参数信号,获取数据								*/
	/************************************************************************/
	/// \details 注册参数（瞬态）
	/// \param[in]  szParamName 参数名称
	/// \param[in]  nOffSet 数组偏移：取值范围 [0，总长度]，0表示数组全部,其余表示单个
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功
	int API_EXPORT KLSL_RegParamLatestValue(const char szParamName[], int nOffSet);

	/// \details 注销参数（瞬态）
	/// \param[in]  szParamName 参数名称
	/// \param[in]  nOffSet 数组偏移：取值范围 [0，总长度]，0表示数组全部,其余表示单个
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功
	int API_EXPORT KLSL_UnParamLatestValue(const char szParamName[], int nOffSet);

	/// \details 注册参数（连续）
	/// \param[in]  szParamName 参数名称
	/// \param[in]  nOffSet 数组偏移：取值范围 [1，总长度]
	/// \param[in]  nSampleUs 采样时间,单位微秒 
	/// \param[in]  nCachedDataCount 设定缓存数据个数
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功
	int API_EXPORT KLSL_RegParamPeriodValue(const char szParamName[], int nOffSet, int nSampleUs, int nCachedDataCount);

	/// \details 注销参数（连续）
	/// \param[in]  szParamName 参数名称
	/// \param[in]  nOffSet 数组偏移：取值范围 [1，总长度]
	/// \param[in]  nSampleUs 采样时间,单位微秒 
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功	
	int API_EXPORT KLSL_UnRegParamPeriodValue(const char szParamName[], int nOffSet, int nSampleUs);

	/// \details 注册输出信号（瞬态）
	/// \param[in]  szOutSigName 输出信号名称
	/// \param[in]  nOffSet 数组偏移：取值范围 [0，总长度]，0表示数组全部,其余表示单个
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功
	int API_EXPORT KLSL_RegOutSigLatestValue(const char szOutSigName[], int nOffSet);

	/// \details 注销输出信号（瞬态）
	/// \param[in]  szOutSigName 输出信号名称
	/// \param[in]  nOffSet 数组偏移：取值范围 [0，总长度]，0表示数组全部,其余表示单个
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功
	int API_EXPORT KLSL_UnRegOutSigLatestValue(const char szOutSigName[], int nOffSet);


	/// \details 注册输出信号（连续）
	/// \param[in]  szOutSigName 输出信号名称
	/// \param[in]  nOffSet 数组偏移：取值范围 [1，总长度]
	/// \param[in]  nSampleUs 采样时间,单位微秒 
	/// \param[in]  nCachedDataCount 设定缓存数据个数
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功
	int API_EXPORT KLSL_RegOutSigPeriodValue(const char szOutSigName[], int nOffSet, int nSampleUs, int nCachedDataCount);
	
	/// \details 注销输出信号（连续）
	/// \param[in]  szOutSigName 输出信号名称
	/// \param[in]  nOffSet 数组偏移：取值范围 [1，总长度]
	/// \param[in]  nSampleUs 采样时间,单位微秒 
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功	
	int API_EXPORT KLSL_UnRegOutSigPeriodValue(const char szOutSigName[], int nOffSet, int nSampleUs);
	
	/// \details 获取参数值（瞬态）
	/// \param[in]   szParamName 参数名称
	/// \param[in]   nOffSet 数组偏移：取值范围 [0，总长度]，0表示数组全部,其余表示单个
	/// \param[out] pTimeOffset 仿真时间偏移
	/// \param[out] pDataValue 存放参数值的缓存，建议大于或等于实际应获取数组大小
	/// \param[in]   nDataBuffLen 参数值的缓存大小
	/// \param[out] nFactDataLen pDataValue实际有效数据长度
	/// \retval != 0  函数调用失败
	/// \retval = 0   函数调用成功	
	int API_EXPORT KLSL_GetParamLatestValue(const char szParamName[],int nOffSet, double *pTimeOffset,double pDataValue[], int nDataBuffLen, int *nFactDataLen);

	/// \details 获取参数值 （连续）
	/// \param[in]   szParamName 参数名称
	/// \param[in]   nOffSet 数组偏移：取值范围 [1，总长度]
	/// \param[in]   nSampleUs 采样时间,单位微秒 
	/// \param[out] pTimeOffset 仿真时间偏移
	/// \param[out] pDataValue 存放参数值的缓存，建议大于或等于实际注册该参数时的数组大小
	/// \param[in]   nDataBuffLen 参数值的缓存
	/// \param[out] nFactDataLen pDataValue实际有效数据长度
	/// \retval != 0  函数调用失败
	/// \retval = 0   函数调用成功	
	int API_EXPORT KLSL_GetParamPeriodValue(const char szParamName[],int nOffSet,int nSampleUs,double pTimeOffset[], double pDataValue[], int nDataBuffLen, int *nFactDataLen);

	/// \details 获取输出信号值（瞬态）
	/// \param[in]   szOutSigName 输出信号名称
	/// \param[in]   nOffSet 数组偏移：取值范围 [0，总长度]，0表示数组全部,其余表示单个
	/// \param[out] pTimeOffset 仿真时间偏移
	/// \param[out] pDataValue 存放参数值的缓存，建议大于或等于实际应获取数组大小
	/// \param[in]   nDataBuffLen 参数值的缓存大小
	/// \param[out] nFactDataLen pDataValue实际有效数据长度
	/// \retval != 0  函数调用失败
	/// \retval = 0   函数调用成功	
	int API_EXPORT KLSL_GetOutSigLatestValue(const char szOutSigName[],int nOffSet, double *pTimeOffset,double pDataValue[], int nDataBuffLen, int *nFactDataLen);
	
	/// \details 获取输出信号值 （连续）
	/// \param[in]   szOutSigName 输出信号名称
	/// \param[in]   nOffSet 数组偏移：取值范围 [1，总长度]
	/// \param[in]   nSampleUs  采样时间,单位微秒 
	/// \param[out] pTimeOffset 仿真时间偏移
	/// \param[out] pDataValue 存放参数值的缓存，建议大于或等于实际注册该参数时的数组大小
	/// \param[in]   nDataBuffLen 参数值的缓存
	/// \param[out] nFactDataLen pDataValue实际有效数据长度
	/// \retval != 0  函数调用失败
	/// \retval = 0   函数调用成功	
	int API_EXPORT KLSL_GetOutSigPeriodValue(const char szOutSigName[],int nOffSet, int nSampleUs, double pTimeOffset[], double pDataValue[], int nDataBuffLen, int *nFactDataLen);


	/************************************************************************/
	/*					6、参数、信号数据录制								    */
	/************************************************************************/
	/// \details 注册录制组
	/// \param[in]  szGroupName 录制组名称
	/// \param[in]  nSampleUs 录制采样率
	/// \param[in]  dRecordTimeSec 录制时长，单位秒
	/// \param[in]  nDataFormat 数据格式
	/// \			nDataFormat = 1, 数据以","分隔
	/// \			nDataFormat = 2, 数据以"|"分隔
	/// \param[in]  szFileDir 本地存储录制文件的路径
	/// \param[in]  szFileName 录制文件名
	/// \param[in]  nOutSigParamIdList 参数/输出信号ID列表（参数/输出信号ID必须是属于同一子模型）
	/// \param[in]  nOutSigParamOffsetList 参数/输出信号偏移， 取值范围 [1，总长度]
	/// \param[in]  nListLen 列表长度，有效取值范围[1,20]
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功	
	int API_EXPORT KLSL_RegRecordGroup(const char szGroupName[],int nSampleUs,double dRecordTimeSec,int nDataFormat,const char szFileDir[],const char szFileName[], 
			int nOutSigParamIdList[], int nOutSigParamOffsetList[], int nListLen);

	/// \details 获取录制组状态
	/// \param[in]  szGroupName 录制组名称
	/// \param[out] nStatus 录制组状态
	/// \           nStatus = 1,注册中
	/// \           nStatus = 2,录制中
	/// \           nStatus = 3,正在下载文件
	/// \           nStatus = 4,录制完成
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功	
	int API_EXPORT KLSL_GetRecordGroupStatus(const char szGroupName[], int *nStatus);

	/// \details 强制注销录制组
	/// \param[in]  szGroupName 录制组名称
	/// \retval != 0 函数调用失败
	/// \retval = 0  函数调用成功	
	int API_EXPORT KLSL_UnRegRecordGroup(const char szGroupName[]);

}
#endif // API_H
