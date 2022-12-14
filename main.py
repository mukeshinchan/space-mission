import pandas as pd 
import streamlit as st
from datetime import datetime as dt
import plotly.express as px 
import plotly.graph_objects as go
from numerize import numerize
from streamlit_option_menu import option_menu 
import json 
df=pd.read_csv('space_missions.csv',encoding='ISO-8859-1')
st.set_page_config(layout="wide")
country=[]
for i in range(len(df)):
  country.append(df['Location'].str.split(',')[:][i][-1].strip())
df['Country']=country
plot=st.empty()
st.title('Space Mission Analysis ')
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
    fig.update_layout(width=1100)
    st.plotly_chart(fig)

year_out = df.groupby(['Year','Country'],as_index=False,sort=False).agg({'Mission':'count'}) 
year_out_country= year_out.groupby(['Country','Year']).agg({'Mission':'sum'})
year_out_country.reset_index(inplace=True)
a=year_out_country["Year"].min()
year_out_country['per']=(year_out_country['Mission']/year_out_country['Mission'].sum())*100

cn1=list(year_out_country['Country'].unique())
cn2=list(year_out['Country'].unique())
fil1, fil2,fil3= st.columns(3)
with fil1:
  cn_flt_1= st.selectbox('',cn1)
  st.subheader(cn_flt_1)
  k1=year_out_country[(year_out_country['Country']==cn_flt_1 )]
  fil1.metric(label='NO OF MISSIONS',value=k1['Mission'].sum(),delta=int(k1['Mission'].mean()))
  st.subheader(f"{round(k1['per'].sum(),2)} %")

with fil2:
  st.image('https://icons-for-free.com/download-icon-basic+white-rocket-131994932102562159_512.png',width=450)
with fil3:
  cn_flt_2= st.selectbox('',cn2)
  st.subheader(cn_flt_2)
  k2=year_out_country[(year_out_country['Country']==cn_flt_2 )]
  fil3.metric(label='NO OF MISSIONS',value=k2['Mission'].sum(),delta=int(k2['Mission'].mean()))
  st.subheader(f"{round(k2['per'].sum(),2)} % ")
  
plt_3=year_out_country[((year_out_country['Country']==cn_flt_1) | (year_out_country['Country']==cn_flt_2)) & (year_out_country['Year']<=a+22*3) & (year_out_country['Year']>=a+22*2) ]
plt_1=year_out_country[((year_out_country['Country']==cn_flt_1 )| (year_out_country['Country']==cn_flt_2)) & (year_out_country['Year']<=a+22) & (year_out_country['Year']>=a) ]
plt_2=year_out_country[((year_out_country['Country']==cn_flt_1) | (year_out_country['Country']==cn_flt_2)) & (year_out_country['Year']<=a+22*2) & (year_out_country['Year']>=a+22) ]
  
  
col_1, col_2, col_3= st.columns(3)
with col_1:  
    temp_1=plt_1[(plt_1['Year']<=a+22) & (plt_1['Year']>=a) ]
    year_filt_1=temp_1['Year']
    fig_1=px.line(plt_1,x='Year',y='Mission',color='Country')
    fig_1.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
    fig_1.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
    fig.update_traces(line_color='#12e3c0')
    fig_1.update_layout(width=450)
    st.plotly_chart(fig_1)
    
with col_2:
    temp_2=plt_2[(plt_2['Year']<=a+22*2 ) & (plt_2['Year']>=a+22)]
    year_filt_2=temp_2['Year']
    fig_2=px.line(plt_2,x='Year',y='Mission',color='Country')
    fig_2.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
    fig_2.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
    fig_2.update_layout(width=450)
    st.plotly_chart(fig_2)
with col_3:
    temp_3=plt_2[(plt_2['Year']<=a+22*3 ) & (plt_2['Year']>=a+22*2)]
    fig_3=px.line(plt_3,x='Year',y='Mission',color='Country')
    fig_3.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
    fig_3.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
    fig_3.update_layout(width=450)
    st.plotly_chart(fig_3)
   
