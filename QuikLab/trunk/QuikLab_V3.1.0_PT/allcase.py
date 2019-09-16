#! /usr/bin/env python
#coding=GB18030
from case.uiCase import tcpIpSmoke
# from case.interfaceCase import platFormInfo,testProInfoTest,fileResourcesTest,\
# testCaseInfoTest,testTaskInfoTest,excTestCaseTest,signalInfoTest
def caseData():
#     print "ss"
#     alltestsnames = [platFormInfo.Test,testProInfoTest.Test,fileResourcesTest.Test,testCaseInfoTest.Test,\
#                      testTaskInfoTest.Test,signalInfoTest.TestSignalInfo,excTestCaseTest.Test]
    alltestsnames = [ tcpIpSmoke.Test ]
    print "success read case list"
    return alltestsnames

if __name__ == "_main_":
    print caseData()
