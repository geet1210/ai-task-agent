from google import genai
from google.genai import types
from dotenv import load_dotenv
from tools import search_pubmed, fetch_details, count_by_year
import os


# Load API key from .env file

load_dotenv()
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Gemini model
def run_agent(topic):
	"""Main agent function that orchestrates all tools"""
	print(f"\n Searching PubMed for: {topic}")

	# Step 1: Search PubMed
	
	ids=search_pubmed(topic, max_results=10, latest=True)

	if not ids:
		print("No articles found for this topic")
		return

	print (f" found {len(ids)} articles")

	# Step 2: Fetch article details

	print("fetching articles...")
	records=fetch_details(ids)

	# Step 3: Count by year

	year_counts=count_by_year(records)

	print("\n Publications by year:")
	for year, count in year_counts.items():
		print(f"	{year}:	{count}	articles")


	# Step 4: Extract abstracts for Gemini

	print("\n Summarizing findings with Gemini...")

	abstracts=[]

	for article in records["PubmedArticle"]:
		try:
			abstract=article["MedlineCitation"]["Article"]["Abstract"]["AbstractText"][0]
			abstracts.append(str(abstract))
		except KeyError:
			pass

	# Step 5: Send to Gemini for summarization
	combined = "\n\n".join(abstracts)
	
	system_prompt = f"""You are an expert medical research assistant analyzing PubMed literature.
	Given abstracts about '{topic}', automatically decide the most useful analysis to provide.
	Always include:
	- Most important findings
	- Key patterns across studies
	- What this means for the field
	Be concise, scientific and objective."""

	user_prompt = input("\nAny specific aspect you want to focus on? (press Enter to skip): ").strip()

	if user_prompt:
		final_prompt = f"{system_prompt}\n\nUser also wants to know: {user_prompt}\n\nAbstracts:\n{combined}"
	else:
		final_prompt = f"{system_prompt}\n\nAbstracts:\n{combined}"

	response = client.models.generate_content(model="gemini-2.0-flash-lite", contents=final_prompt)
	print("\n Summary of findings:")
	print(response.text)

if __name__ == "__main__":
    topic = input("Enter a medical topic to research: ")
    run_agent(topic)