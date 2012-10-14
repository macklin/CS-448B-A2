#! /usr/bin/env python

"""
Define a Contribution class
See: http://www.fec.gov/finance/disclosure/metadata/DataDictionaryContributionstoCandidates.shtml
"""

class Contribution:
	def __init__(self, L):
		"""
		L is a list resulting from split()ing the input
		"""
		self.ContributionFilerId = L[0]
		self.ContributionAmendmentInd = L[1]
		self.ContributionReportType = L[2]
		self.ContributionPrimaryGeneralInd = L[3]
		self.ContributionMicrofilmLocation = L[4]
		self.ContributionTransactionType = L[5]
		self.ContributionEntityType = L[6]
		self.ContributionContributorName = L[7]
		self.ContributionCity = L[8]
		self.ContributionState = L[9]
		self.ContributionZipCode = L[10]
		self.ContributionEmployer = L[11]
		self.ContributionOccupation = L[12]
		self.ContributionTransactionDate = L[13]
		self.ContributionTransactionAmount = L[14]
		self.ContributionOtherIdNumber = L[15]
		self.ContributionCandidateIdNumber = L[16]
		self.ContributionTransactionId = L[17]
		self.ContributionReportId = L[18]
		self.ContributionMemoCode = L[19]
		self.ContributionMemoText = L[20]
		self.ContributionFECRecordNumber = L[21]
