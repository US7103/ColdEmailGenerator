import os
import pandas as pd
import uuid
import chromadb
from chromadb.config import Settings
import logging

# Suppress ChromaDB warning logs
logging.getLogger("chromadb").setLevel(logging.ERROR)


class Portfolio:
    def __init__(self, file_path="resources/my_portfolio.csv"):
        self.file_path = file_path
        self.data = pd.read_csv(file_path)

        # Initialize ChromaDB client
        self.chroma_client = chromadb.PersistentClient(
            path="vectorstore",
            settings=Settings(
                anonymized_telemetry=False
            )
        )

        self.collection = self.chroma_client.get_or_create_collection(name="portfolio")

    def load_portfolio(self):
        if not self.collection.count():
            for _, row in self.data.iterrows():
                doc = str(row["Techstack"]).strip()
                # Split comma-separated skills into space-separated string
                doc = " ".join([skill.strip() for skill in doc.split(",") if skill.strip()])
                link = str(row["Links"]).strip()
                if doc:  # only add non-empty documents
                    self.collection.add(
                        documents=[doc],
                        metadatas=[{"links": link}],
                        ids=[str(uuid.uuid4())]
                    )

    def query_links(self, skills):
        # Clean and filter skills
        skills = [s.strip() for s in skills if s.strip()]
        if not skills:
            return []
        result = self.collection.query(query_texts=skills, n_results=2)
        # Extract links from the result
        metadatas = result.get("metadatas", [])  # list of lists
        links = []
        for sublist in metadatas:
         for item in sublist:  # item is a dict
            if "links" in item:
                links.append(item["links"])
         return links
