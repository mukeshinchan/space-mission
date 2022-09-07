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

#st.markdown(page_bg_img, unsafe_allow_html=True)

select=option_menu(
    menu_title='ANALYSIS',
    options=['Home','Sales','Profit','Discount'],
    icons=['house-fill','bag-dash-fill','currency-exchange','percent'] ,
    orientation='horizontal',
    default_index=1,
    menu_icon=['clipboard-data']
    )


plot=st.empty()

with plot.container():
    col1,col2,col3=st.columns(3)
    with col1:
        df['Date']=pd.to_datetime(df['Date'])
        df['Year']=df['Date'].dt.year
        out = df.groupby(['Year']).count()
        out.reset_index(inplace = True)
        fig=px.scatter_3d(out,x=out['Year'],y=out['Mission'])
        fig.update_traces(line_color='#39bbf7')
        fig.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
        fig.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
        st.plotly_chart(fig)

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

                