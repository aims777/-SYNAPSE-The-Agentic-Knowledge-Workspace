import streamlit as st

def analytics_card(analytics):
    with st.expander("📊 Document Analytics", expanded=True):
        st.subheader("💡 Key Insights")
        for insight in analytics.get("insights", []):
            st.markdown(f"- {insight}")
        
        st.subheader("👤 Entities")
        for entity in analytics.get("entities", []):
            st.markdown(f"- {entity}")
            
        st.subheader("📝 Summary")
        st.markdown(analytics.get("summary", ""))
        
        st.subheader("🔗 Sources")
        for source in analytics.get("sources", []):
            st.markdown(f"- {source}")
