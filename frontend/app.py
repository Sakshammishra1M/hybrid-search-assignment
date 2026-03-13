import streamlit as st
import requests

st.title("Hybrid Search Engine")

query = st.text_input("Search")

alpha = st.slider("Hybrid Weight", 0.0, 1.0, 0.5)

if st.button("Search"):

    r = requests.post(
        "http://127.0.0.1:8000/search",
        json={"query": query, "alpha": alpha}
    )

    data = r.json()

    for res in data["results"]:

        st.subheader(res["title"])
        st.write("Hybrid Score:", res["hybrid_score"])
        st.write("BM25:", res["bm25_score"])
        st.write("Vector:", res["vector_score"])
        st.divider()