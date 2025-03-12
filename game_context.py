# 4️⃣ game_context.py → Stores & Retrieves Game Knowledge
# Uses FAISS (Vector Database) to store past game conversations & key moments
# Helps AI remember past interactions
# AI can retrieve relevant data when needed

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")  # Load embedding model
index = faiss.IndexFlatL2(384)  # Create FAISS index

game_memory = []  # Store game events

def store_game_memory(text):
    global game_memory
    vector = model.encode([text])  # Convert text to vector
    game_memory.append(text)
    index.add(np.array(vector, dtype=np.float32))  # Add to FAISS

def get_game_advice(query):
    global game_memory, index
    
    if len(game_memory) == 0:
        return "No advice stored yet."

    # Convert query into FAISS-friendly format
    query_vector = model.encode([query])

    # Perform similarity search
    result = index.search(query_vector, 1)[1]  # Get indices of closest match

    print(f"Query: {query}")
    print(f"FAISS Result: {result}")

    if len(result) == 0 or len(result[0]) == 0:
        return "No advice found."

    return game_memory[result[0][0]] if result[0][0] < len(game_memory) else "No advice found."


# Function to add new game advice
def add_game_advice(advice):
    global game_memory
    game_memory.append(advice)