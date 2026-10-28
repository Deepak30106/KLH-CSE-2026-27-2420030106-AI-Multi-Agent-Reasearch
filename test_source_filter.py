from app.source_filter import filter_sources


sources = [
    {
        "title": "NASA Climate Science",
        "url": "https://science.nasa.gov/climate-change/",
        "snippet": "Scientific information about climate change."
    },
    {
        "title": "University Research",
        "url": "https://example.edu/research/climate",
        "snippet": "University research about climate change."
    },
    {
        "title": "Social Media Post",
        "url": "https://www.instagram.com/example/",
        "snippet": "A social media post about climate change."
    },
    {
        "title": "Research Organization",
        "url": "https://example.org/research",
        "snippet": "Research and evidence about climate change."
    },
    {
        "title": "Duplicate NASA Source",
        "url": "https://science.nasa.gov/climate-change/",
        "snippet": "Same NASA source."
    }
]


print("=" * 70)
print("SOURCE FILTER TEST")
print("=" * 70)

print(f"\nOriginal sources: {len(sources)}")


filtered = filter_sources(sources)


print(f"Filtered sources: {len(filtered)}")

print("\n" + "=" * 70)
print("FILTERED SOURCES")
print("=" * 70)


for i, source in enumerate(filtered, start=1):

    print(f"\n{i}. {source.get('title')}")
    print(f"URL: {source.get('url')}")
    print(f"Quality score: {source.get('quality_score')}")


print("\n" + "=" * 70)
print("SOURCE FILTER TEST COMPLETE")
print("=" * 70)