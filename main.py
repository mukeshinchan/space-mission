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
        st.header("The History of Space Exploration")
        st.write("We human beings have been venturing into space since October 4, 1957, when the Union of Soviet Socialist Republics (U.S.S.R.) launched Sputnik, the first artificial satellite to orbit Earth. This happened during the period of political hostility between the Soviet Union and the United States known as the Cold War. For several years, the two superpowers had been competing to develop missiles, called intercontinental ballistic missiles (ICBMs), to carry nuclear weapons between continents. In the U.S.S.R., the rocket designer Sergei Korolev had developed the first ICBM, a rocket called the R7, which would begin the space race.")
    with col2:
        df['Date']=pd.to_datetime(df['Date'])
        df['Year']=df['Date'].dt.year
        out = df.groupby(['Year']).count()
        out.reset_index(inplace = True)
        fig=px.area(out,x=out['Year'],y=out['Mission'])
        fig.update_traces(line_color='#39bbf7')
        fig.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
        fig.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
        fig.update_yaxes(range = [min(df['Year']),max(df['Year'])])
        st.plotly_chart(fig)

                
