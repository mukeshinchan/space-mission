import pandas as pd 
import streamlit as st
from datetime import datetime as dt
import plotly.express as px 
import plotly.graph_objects as go
from numerize import numerize
df=pd.read_csv('space_missions.csv',encoding='ISO-8859-1')


st.set_page_config(layout="wide")

page_bg_img = '''
<style>
body {
background-image: url("https://wallpapers.com/images/high/4k-space-eye-formation-unmdcbrhea9nngay.jpg");
background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

plot=st.empty()

with plot.container():
    col1,col2,col3=st.columns(3)
    with col1:
       st.text('List of World Space Explorations Mission Space Mission is a journey, by a manned or unmanned vehicle, into space to gather scientific data. It is important for global partnerships and exploration capabilities that help global preparedness for protecting the Earth from catastrophic. In this article, we are giving the list of World Space Explorations Mission which is very useful for the competitive examinations like UPSC-prelims, SSC, State Services, NDA, CDS, and Railways etc.)
        
    with col2:
        df['Date']=pd.to_datetime(df['Date'])
        df['Year']=df['Date'].dt.year
        out = df.groupby(['Year']).count()
        out.reset_index(inplace = True)
        fig=px.area(out,x=out['Year'],y=out['Mission'])
        fig.update_traces(line_color='#39bbf7')
        fig.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
        fig.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
        st.plotly_chart(fig)

                
