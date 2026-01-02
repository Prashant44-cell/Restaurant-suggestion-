import streamlit as st
import langchain_helper

st.title("Restaurant Suggestion Generator")


cuisine  =st.sidebar.selectbox("pick a menu",("Indian","Nepali","Chinese","Italian","Mexican","American","Japanese","Thai","French","Spanish"))

if cuisine :
    response = langchain_helper.generator_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())
    menu_items = response["menu_items"].split(",")
    st.write("***Menu Items*")

    for item in menu_items:
        st.write("-",item)
