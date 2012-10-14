#! /usr/bin/env python

"""
Parse FEC data from 2005-2012 of campaign contributions from committees
Data obtained from: http://www.fec.gov/finance/disclosure/ftpdet.shtml

Example usage:
python2.7 parse.py ../Raw\ Data/ ../out
"""

import os.path
import os
import argparse
import glob

from candidate import *
from contribution import *
from committee import *

def validate(rawDir, outDir):
	if not os.path.isdir(rawDir):
		print "Raw data directory does not exist!"
		return 1
	if not os.path.isdir(outDir):
		os.mkdir(outDir)

	cnFiles = glob.glob(rawDir + os.sep + "cn*.txt")
	if len(cnFiles) == 0:
		print "No candidate files!"
		return 1
	cmFiles = glob.glob(rawDir + os.sep + "cm*.txt")
	if len(cmFiles) == 0:
		print "No committee files!"
		return 1
	contribFiles = glob.glob(rawDir + os.sep + "itpas*.txt")
	if len(contribFiles) == 0:
		print "No contribution files!"
		return 1
	return (cnFiles, cmFiles, contribFiles)

def buildCandDicts(cnFiles):
	candDicts = []

	for fileName in cnFiles:
		thisDict = {}
		f = open(fileName, 'r')
		for line in f:
			cand = Candidate(line.strip().split('|'))
			thisDict[cand.CandidateId] = cand
		candDicts.append(thisDict)
		f.close()

	return candDicts

def buildCommDicts(cmFiles):
	commDicts = []

	for fileName in cmFiles:
		thisDict = {}
		f = open(fileName, 'r')
		for line in f:
			comm = Committee(line.strip().split('|'))
			thisDict[comm.CommitteeId] = comm
		commDicts.append(thisDict)
		f.close()

	return commDicts

def buildContribDicts(contribFiles):
	contribDicts = []

	for fileName in contribFiles:
		thisDict = {}
		f = open(fileName, 'r')
		for line in f:
			contrib = Contribution(line.strip().split('|'))
			thisDict[contrib.ContributionFECRecordNumber] = contrib
		contribDicts.append(thisDict)
		f.close()

	return contribDicts

def main(rawDir, outDir):
	r = validate(rawDir, outDir)
	if r == 1:
		return 1
	cnFiles, cmFiles, contribFiles = r

	candDicts = buildCandDicts(cnFiles)
	commDicts = buildCommDicts(cmFiles)
	contribDicts = buildContribDicts(contribFiles)
	print len(contribDicts[-1])
	print len(commDicts[-1])
	print len(candDicts[-1])

	dummyCand = Candidate(range(15))
	dummyComm = Committee(range(15))
	dummyContrib = Contribution(range(22))
	candProps = [x for x in dir(dummyCand) if x[0].isupper()]
	commProps = [x for x in dir(dummyComm) if x[0].isupper()]
	contribProps = [x for x in dir(dummyContrib) if x[0].isupper()]

	outFile = outDir + os.sep + "contributions.csv"
	f = open(outFile, 'w')
	f.write(','.join(contribProps) + ','.join(candProps) + ','.join(commProps) + '\n')
	idx = -1
	candDict = candDicts[idx]
	commDict = commDicts[idx]
	contribDict = contribDicts[idx]
	for key in contribDict.keys()[0:10]:
		contrib = contribDict[key]
		if candDict.has_key(contrib.ContributionCandidateIdNumber):
			cand = candDict[contrib.ContributionCandidateIdNumber]
		else:
			cand = Candidate(['\N'] * 15)
		if commDict.has_key(contrib.ContributionOtherIdNumber):
			comm = commDict[contrib.ContributionOtherIdNumber]
		else:
			comm = Committee(['\N'] * 15)
		line = []
		for p in contribProps:
			line.append(getattr(contrib, p))
		for p in candProps:
			line.append(getattr(cand, p))
		for p in commProps:
			line.append(getattr(comm, p))
		f.write(','.join(line) + '\n')

	f.close()
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Parse candidate contributions data')

	parser.add_argument('rawDataDirectory', type = str, help = 'Directory containing the raw data')
	parser.add_argument('outputDirectory', type = str, help = 'Output directory')

	cmdargs = parser.parse_args().__dict__

	rawDir = cmdargs['rawDataDirectory']
	outDir = cmdargs['outputDirectory']

	exit(main(rawDir, outDir))
