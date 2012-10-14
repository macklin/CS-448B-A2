#! /usr/bin/env python

"""
Parse FEC data from 2005-2012 of campaign contributions from committees
Data obtained from: http://www.fec.gov/finance/disclosure/ftpdet.shtml
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
			cand = Candidate(line.split('|'))
			thisDict[cand.CandidateId] = cand
		candDicts.append(thisDict)

	return candDicts

def buildCommDicts(cmFiles):
	commDicts = []

	for fileName in cmFiles:
		thisDict = {}
		f = open(fileName, 'r')
		for line in f:
			comm = Committee(line.split('|'))
			thisDict[comm.CommitteeId] = comm
		commDicts.append(thisDict)

	return commDicts

def buildContribDicts(contribFiles):
	contribDicts = []

	for fileName in contribFiles:
		thisDict = {}
		f = open(fileName, 'r')
		for line in f:
			contrib = Contribution(line.split('|'))
			thisDict[contrib.ContributionFECRecordNumber] = contrib
		contribDicts.append(thisDict)

	return contribDicts

def main(rawDir, outDir):
	r = validate(rawDir, outDir)
	if r == 1:
		return 1
	cnFiles, cmFiles, contribFiles = r

	candDicts = buildCandDicts(cnFiles)
	print len(candDicts)
	print len(candDicts[0].keys())
	print len(candDicts[-1].keys())
	commDicts = buildCommDicts(cmFiles)
	print len(commDicts)
	print len(commDicts[0].keys())
	print len(commDicts[-1].keys())
	contribDicts = buildContribDicts(contribFiles)
	print len(contribDicts)
	print len(contribDicts[0].keys())
	print len(contribDicts[-1].keys())
	
if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = 'Parse candidate contributions data')

	parser.add_argument('rawDataDirectory', type = str, help = 'Directory containing the raw data')
	parser.add_argument('outputDirectory', type = str, help = 'Output directory')

	cmdargs = parser.parse_args().__dict__

	rawDir = cmdargs['rawDataDirectory']
	outDir = cmdargs['outputDirectory']

	exit(main(rawDir, outDir))
