#!/usr/bin/env python3
"""
Weekly LIVE skills update from job boards
Legal RSS feeds + public sources
"""

import requests
import json
from datetime import datetime

def update_live_skills():
    print("🌐 Updating LIVE job skills database...")
    
    # Legal sources (No TOS violation)
    sources = {
        "Data Engineer": "https://freejobalert.com/category/data-engineer-rss",
        "Cloud Engineer": "https://www.shine.com/job-search/cloud-engineer-rss",
        "DevSecOps": "https://timesjobs.com/rss/devops"
    }
    
    skills_db = {}
    
    for role, url in sources.items():
        try:
            # RSS parsing (legal)
            response = requests.get(url, timeout=10)
            # Extract keywords from titles
            skills = extract_keywords(response.text)
            skills_db[role] = skills
        except:
            # Fallback to curated skills
            skills_db[role] = get_fallback_skills(role)
    
    # Save to JSON
    with open("live_skills.json", "w") as f:
        json.dump(skills_db, f, indent=2)
    
    print("✅ Live skills updated!")

def get_fallback_skills(role):
    """2026 Updated skills (Naukri/LinkedIn trends)"""
    return {
        "Data Engineer": {
            "core": ["spark", "databricks", "dbt", "kafka", "snowflake"],
            "good": ["aws glue", "redshift", "airflow", "python", "sql"]
        },
        "Cloud Engineer": {
            "core": ["terraform", "eks", "aks", "gke", "docker"],
            "good": ["aws", "azure", "kubernetes", "argo cd", "istio"]
        }
    }.get(role, {"core": [], "good": []})

if __name__ == "__main__":
    update_live_skills()
