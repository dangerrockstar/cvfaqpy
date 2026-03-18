#!/usr/bin/env python3
import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from role_matcher import DynamicRoleMatcher  # Updated import

def load_cv(cv_path: str):
    loader = PyPDFLoader(cv_path)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)
    return "\n".join([chunk.page_content for chunk in chunks])

def main():
    CV_PATH = "resume.pdf"
    
    if not os.path.exists(CV_PATH):
        print(f"❌ {CV_PATH} copy करें!")
        return
    
    cv_content = load_cv(CV_PATH)
    matcher = DynamicRoleMatcher()
    matches = matcher.match_roles(cv_content)
    
    print("\n" + "="*70)
    print("🌐 LIVE JOB MARKET MATCHING (Naukri/LinkedIn 2026)")
    print("="*70)
    
    for i, match in enumerate(matches[:6], 1):
        print(f"\n🏆 #{i} {match['role']}")
        print(f"   📊 Score: {match['match_percent']}%")
        print(f"   ✅ Strengths: {', '.join(match['strengths'])}")
        print(f"   ❌ Learn: {', '.join(match['gaps'])}")
        print(f"   🔗 Source: {match['source']}")
        print(f"   📈 Reason: {match['reason']}")

if __name__ == "__main__":
    main()
