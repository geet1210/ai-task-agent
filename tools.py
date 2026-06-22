from Bio import Entrez

# Always tell NCBI who you are - required by their API rules
Entrez.email = "geetmadhukar@gmail.com"

def search_pubmed(topic, max_results=10, latest=True, years=None):
	"""Search PubMed and return a list of articles"""

	# Add date filter if years is specified
	if years:
		topic=f"{topic} AND (\"{years}\"[Date - Publication] : \"3000\"[Date - Publication])"

	handle=Entrez.esearch(db='pubmed', term=topic, retmax=max_results,sort="pub+date" if latest else "relevance")
	record=Entrez.read(handle)
	handle.close()

	ids=record["IdList"]
	return ids


def fetch_details(id_list):
	"""Fetch article details for a list of PubMed IDs"""
	ids=",".join(id_list)

	handle=Entrez.efetch(db='pubmed', ids=ids, rettype="abstract", retmode="xml")
	records=Entrez.read(handle)
	handle.close()

	return records