from app.rag_agent import (
    keyword_search,
    vector_search,
    hybrid_search
)


# ============================================================
# GENERIC TEST DOCUMENTS
# ============================================================

documents = [
    {
        "title": "Climate Change Causes",
        "url": "https://example.com/climate",
        "snippet": "Climate change is primarily driven by greenhouse gas emissions from human activities."
    },
    {
        "title": "Renewable Energy",
        "url": "https://example.com/energy",
        "snippet": "Solar and wind energy are important renewable energy technologies."
    },
    {
        "title": "French Revolution",
        "url": "https://example.com/history",
        "snippet": "The French Revolution was influenced by economic problems, social inequality, and political changes."
    },
    {
        "title": "Telugu Cinema",
        "url": "https://example.com/movies",
        "snippet": "Telugu cinema includes films from the Telugu-language film industry."
    }
]


# ============================================================
# USER QUERY
# ============================================================

query = input("Enter a search question: ")


print("\n" + "=" * 70)
print("RAG AGENT TEST")
print("=" * 70)

print("\nQuery:")
print(query)


# ============================================================
# KEYWORD SEARCH
# ============================================================

keyword_results = keyword_search(
    query,
    documents,
    top_k=3
)

print("\n" + "=" * 70)
print("KEYWORD SEARCH")
print("=" * 70)

for i, result in enumerate(keyword_results, start=1):

    print(
        f"{i}. {result['title']} "
        f"(score={result.get('keyword_score', 0)})"
    )


# ============================================================
# VECTOR SEARCH
# ============================================================

vector_results = vector_search(
    query,
    documents,
    top_k=3
)

print("\n" + "=" * 70)
print("VECTOR SEARCH")
print("=" * 70)

for i, result in enumerate(vector_results, start=1):

    print(
        f"{i}. {result['title']} "
        f"(score={result.get('vector_score', 0)})"
    )


# ============================================================
# HYBRID SEARCH
# ============================================================

hybrid_results = hybrid_search(
    query,
    documents,
    top_k=3
)

print("\n" + "=" * 70)
print("HYBRID SEARCH")
print("=" * 70)

for i, result in enumerate(hybrid_results, start=1):

    print(
        f"{i}. {result['title']} "
        f"(hybrid_score={result.get('hybrid_score', 0)})"
    )


print("\n" + "=" * 70)
print("RAG TEST COMPLETE")
print("=" * 70)