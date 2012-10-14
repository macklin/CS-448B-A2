#! /usr/bin/env python

"""
Define a Committee class
See: http://www.fec.gov/finance/disclosure/metadata/DataDictionaryCommitteeMaster.shtml
"""

class Committee:
	def __init__(self, L):
		"""
		L is a list resulting from split()ing the input
		"""
		self.CommitteeId = L[0]
		self.CommitteeName = L[1]
		self.CommitteeTreasurer = L[2]
		self.CommitteeStreet1 = L[3]
		self.CommitteeStreet2 = L[4]
		self.CommitteeCity = L[5]
		self.CommitteeState = L[6]
		self.CommitteeZipCode = L[7]
		self.CommitteeDesignation = L[8]
		self.CommitteeType = L[9]
		self.CommitteeParty = L[10]
		self.CommitteeFilingFreq = L[11]
		self.CommitteeInterestGroupCat = L[12]
		self.CommitteeConnectedOrgName = L[13]
		self.CommitteeCandidateId = L[14]
