#! /usr/bin/env python

"""
Define a Candidate class
See: http://www.fec.gov/finance/disclosure/metadata/DataDictionaryCandidateMaster.shtml
"""

class Candidate:
	def __init__(self, L):
		"""
		L is a list resulting from split()ing the input
		"""
		self.CandidateId = L[0]
		self.CandidateName = L[1]
		self.CandidatePartyAffiliation = L[2]
		self.CandidateYearOfElection = L[3]
		self.CandidateState = L[4]
		self.CandidateOffice = L[5]
		self.CandidateDistrict = L[6]
		self.CandidateIncumbentChallengerStatus = L[7]
		self.CandidateStatus = L[8]
		self.CandidatePrincipalCampaignCommittee = L[9]
		self.CandidateStreet1 = L[10]
		self.CandidateStreet2 = L[11]
		self.CandidateCity = L[12]
		self.CandidateState = L[13]
		self.CandidateZipCode = L[14]
