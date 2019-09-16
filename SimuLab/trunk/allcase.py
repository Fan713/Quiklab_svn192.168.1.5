#! /usr/bin/env python
#coding=utf-8
from trunk.case.interfaceCase import *

def caseData():
    alltestsnames = [modelTest.testmodelInfo,
                     outSigInfoTest.testOutSigInfo,
                     paramInfoTest.testParamInfo,
                     proStatusTest.testProStatus,
                     recordGroupTest.testrecordGroupInfo,
                     runProjectTest.testRunProject]
    print "success read case list"
    return alltestsnames

if __name__ == "__main__":
    caseData()

