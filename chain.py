from langchain_google_genai import GoogleGenerativeAI
from langchain_community.document_loaders import WebBaseLoader
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
import pandas as pd
import dotenv
import os
os.environ["USER_AGENT"] = "MyApp/1.0"




from dotenv import load_dotenv
load_dotenv()
os.environ["GOOGLE_API_KEY"]="AIzaSyC6h9AGg2HRjqhS55lgd2gYHZZPDgeEJgs"



class Chain:
   def __init__(self):
        self.llm=GoogleGenerativeAI(
        temperature=0.6,
        model="gemini-2.0-flash"
    )
    
   def extract_jobs(self, cleaned_text):
       prompt_extract=PromptTemplate.from_template(
          """
          ###SCRAPED TEXT FROM WEBSITE
          {page_data}
          ### INSTRUCTION
          The scraped text is from Career page of a Website.
          Your job is to correct the job postings and return them in JSON format containing  following keys:
          'role','experience','skills', and 'description'.
          only return the valid JSON
          ### VALID JSON (NO PREAMBLE)
          """
        )
       chain_extract= prompt_extract | self.llm
       res=chain_extract.invoke({'page_data':cleaned_text})
       try:
           json_parser=JsonOutputParser()
           json_res=json_parser.parse(res)
       except OutputParserException:
           raise OutputParserException("Context too big. Unable to parse jobs.")
       return json_res if isinstance(res, list) else [json_res]
           
   def write_mail(self, job, links):
       prompt_email=PromptTemplate.from_template(
        """
            ### JOB DESCRIPTION:
            {job_description}
        
            ### INSTRUCTION:
            You are Mohan, a business development executive at AtliQ. AtliQ is an AI & Software Consulting company dedicated to facilitating
            the seamless integration of business processes through automated tools. 
            Over our experience, we have empowered numerous enterprises with tailored solutions, fostering scalability, 
            process optimization, cost reduction, and heightened overall efficiency. 
            Your job is to write a cold email to the client regarding the job mentioned above describing the capability of AtliQ 
            in fulfilling their needs.
            Also add the most relevant ones from the following links to showcase Atliq's portfolio: {link_list}
            Remember you are Mohan, BDE at AtliQ. 
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
        
        """
        )

       chain_email= prompt_email | self.llm
       rest=chain_email.invoke({"job_description": str(job), "link_list":links})
       return rest
       



