#!/bin/bash
# 🚀 CV Career Advisor - ONE CLICK RUN!
# ./run.sh

echo "🎯 CV Career Advisor Starting..."
echo "=================================="

# 1. CHECK resume.pdf
if [ ! -f "resume.pdf" ]; then
    echo "❌ resume.pdf नहीं मिला!"
    echo "📝  resume copy: cp your_resume.pdf resume.pdf"
    exit 1
fi

# 2. CHECK Python dependencies
if [ ! -f "requirements.txt" ]; then
    echo "📦 Installing dependencies..."
    pip install langchain-core langchain-community pypdf chromadb ollama
fi

# 3. START Ollama (background)
echo "🤖 Starting Ollama..."
ollama serve &
sleep 3

# 4. PULL model (if not exists)
if ! ollama list | grep -q "llama3.2"; then
    echo "📥 Downloading llama3.2 model..."
    ollama pull llama3.2
fi

# Weekly auto-update skills (first run of week)
if [ ! -f "live_skills.json" ] || [ $(find live_skills.json -mtime +7 | wc -l) -gt 0 ]; then
    echo "🔄 Updating live job skills..."
    python update_skills.py
fi

# 5. RUN Main App
echo "🚀 Analyzing your CV for best roles..."
echo "=================================="
python main.py

echo "✅ DONE! Results Up there"
echo "🔄 want rerun?  use ./run"
