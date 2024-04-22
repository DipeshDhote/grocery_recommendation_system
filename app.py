import streamlit as st
import pandas as pd
import requests
import pickle

def recommend(product):
    name_index = products[products['name'].str.contains(product)].index[0]
    distances = sorted(list(enumerate(similarity[name_index])),reverse = True ,key=lambda x:x[1])

    r_product =[]
    recommended = []
    r_img = []
    r_variant = []
    r_mrp = []

    for i in distances[1:4]:
        r_product.append(products.iloc[i[0]]['name'])
        recommended.append(products.iloc[i[0]]['image_url'])
        r_variant.append(products.iloc[i[0]]['variant'])
        r_mrp.append(products.iloc[i[0]]['mrp'])

    for i in recommended:
        r_img.append(i.replace(" ",""))
        
    return r_product,r_img,r_variant,r_mrp

st.header('Grocery Recommendation System')

product_dict = pickle.load(open('artifacts/product_dict.pkl','rb'))
products = pd.DataFrame(product_dict)
similarity = pickle.load(open('artifacts/similarity.pkl','rb'))


product_list = products['name'].values
selected_product = st.selectbox('select product ',
                      product_list)


if st.button('Recommend'):
    r_product,r_img,r_variant,r_mrp = recommend(selected_product)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(r_product[0])
        st.image(r_img[0])
        st.text('Quantity :{}'.format(r_variant[0]))
        st.text('MRP :{}'.format(r_mrp[0]))
    with col2:
        st.text(r_product[1])
        st.image(r_img[1])
        st.text('Quantity :{}'.format(r_variant[1]))
        st.text('MRP :{}'.format(r_mrp[1]))
        
    with col3:
        st.text(r_product[2])
        st.image(r_img[2])
        st.text('Quantity :{}'.format(r_variant[2]))
        st.text('MRP :{}'.format(r_mrp[2]))
