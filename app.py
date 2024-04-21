import streamlit as st
import pandas as pd
import requests
import pickle

def recommend(product):
    name_index = products[products['name'].str.contains(product)].index[0]
    distances = sorted(list(enumerate(similarity[name_index])),reverse = True ,key=lambda x:x[1])

    recommended_product =[]
    recommended_img = []
    for i in distances[1:6]:
        recommended_product.append(products.iloc[i[0]]['name'])
        recommended_img.append(products.iloc[i[0]]['image_url'])
        
    return recommended_product,recommended_img

st.header('Grocery Recommendation System')

product_dict = pickle.load(open('artifacts/product_dict.pkl','rb'))
products = pd.DataFrame(product_dict)
similarity = pickle.load(open('artifacts/similarity.pkl','rb'))


product_list = products['name'].values
selected_product = st.selectbox('select the product',
                      product_list)


if st.button('Recommend'):
    recommended_product,recommended_img = recommend(selected_product)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_product[0])
        st.image(recommended_img[0])
    with col2:
        st.text(recommended_product[1])
        st.image(recommended_img[1])

    with col3:
        st.text(recommended_product[2])
        st.image(recommended_img[2])
    with col4:
        st.text(recommended_product[3])
        st.image(recommended_img[3])
    with col5:
        st.text(recommended_product[4])
        st.image(recommended_img[4])

