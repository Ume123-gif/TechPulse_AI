import streamlit as st 
import pandas as pd
from scraper import TechScraper
from analyser import TechAnalyser

if "analysis_data" not in st.session_state:
    st.session_state.analysis_data=None

st.set_page_config(page_title="Tech Pulse AI", layout="wide")
st.subheader("It analyses Tech News!")

url=st.sidebar.text_input("Enter Tech News url: ", value="https://news.ycombinator.com/")

if st.button("Start Analysis!"):
    with st.spinner("Fetching news..."):
        scraper=TechScraper(url)
        analyser=TechAnalyser()
        html=scraper.fetch_html()
        headlines=[headline for headline in scraper.extract_headlines(html,"titleline")]
        if headlines:
            analysis=analyser.analyze_all(headlines)
            st.session_state.analysis_data=pd.DataFrame(analysis)
            st.success("Analysis Completed!")
        else:
            st.error("⚠️ No headlines found. Please check the URL or the CSS selector!")
            st.info("💡 Tip: Some websites use different HTML structures. This app is currently optimized for Hacker News.")
if st.session_state.analysis_data is not None:
    df=st.session_state.analysis_data.copy() 
    search_term=st.sidebar.text_input("Filter by Keyword:")
    if search_term:
        df = df[df['title'].str.contains(search_term, case=False)]
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric("Total Headlines: ", len(df))
    with col2:
        pos_count=len(df[df["label"]=="Positive"])
        st.metric("Positive Vibes:", f"{pos_count}")
    with col3:
        neg_count=len(df[df["label"]=="Negative"])
        st.metric("Negative Vibes:", f"{neg_count}")
    with col4:
        avg_sentiment=df["score"].mean()
        st.metric("Average Sentiment:", f"{avg_sentiment:.2f}")
    tab1,tab2=st.tabs(["📊 Visual Analysis", "📋 Raw Data"])
    with tab1:
        st.write("### Sentiment Distribution")
        st.bar_chart(df["label"].value_counts())
    with tab2:
        st.write("### Detailed Headlines")
        st.dataframe(df, use_container_width=True)