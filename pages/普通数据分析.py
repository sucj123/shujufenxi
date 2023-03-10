from streamlit_pandas_profiling import st_profile_report
from ydata_profiling import ProfileReport
from st_aggrid import AgGrid
import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_echarts import st_echarts
import matplotlib.pyplot as plt
from PIL import Image
st.set_page_config(page_title='普通数据分析系统',layout="wide")
st.header('普通数据分析可视化展示')
option1 = st.sidebar.radio(
        '请选择您需要的数据分析方式',
        ('数据透视分析', '一键快速分析'))
if option1 == '数据透视分析':
        st.markdown('<p class="font">请上传您的数据集，该应用会进行数据透视分析报告</p>', unsafe_allow_html=True)
        def imageShow():
            image = Image.open("zp.jpg")  # 在未导入excel时，展示图片
            st.image(image, clamp=False,
                     channels="RGB", output_format="auto", use_column_width=True)
        file = st.file_uploader("上传分析文件", type="xlsx")
        if file is not None:
            df = pd.read_excel(file, header=0)
            df = df
            #df = pd.read_excel(file, header=0)
            st.info("原始表格信息如下：")
            st.write(df)
            header = df.columns.to_list()
            a = st.selectbox("请选择要对原始表格的哪一列做透视", (header))
            b = st.selectbox("请选择要对原始表格的哪一列做数据处理", (header[1:]))
            if a != b:
                  df2 = df.pivot_table(index=[a], values=[b])
                  bar1 = px.bar(df2.head(15),
                           orientation='h',
                           width=950,
                           height=700,
                           )
                  st.plotly_chart(bar1)
                  fig = px.scatter(
                      df2.head(15),width=950,
                           height=700,
                  )
                  st.plotly_chart(fig)
                  fig1 = px.line(  df2.head(15),
                                  line_shape="spline",
                                  render_mode="svg"
                                   )
                  st.plotly_chart(fig1)
                  fig2 = px.histogram(df2,
                                      barmode="group",  # 柱状图模式
                                     )
                  st.plotly_chart(fig2)
            else:

                  st.warning("你不能只选择对同一列进行数据透视")

            c = st.selectbox("请选择要对表格的哪一列做数据统计重复次数", (header))
            df3 = df.pivot_table(index=[a], aggfunc='size')
            bar_chart1 = px.bar(df3.head(20),
                                orientation='h',
                                width=950,
                                height=700,
                                )
            st.plotly_chart(bar_chart1)
        else:
            imageShow()

elif option1 == '一键快速分析':
        st.markdown('<p class="font">请上传您的数据集，进行数据一键快速分析分析</p>', unsafe_allow_html=True)
        file = st.file_uploader("上传分析文件",
                                type="xlsx")
        def imageShow():
            image = Image.open("lu.jpg")  # 在未导入excel时，展示图片
            st.image(image, clamp=False,
                     channels="RGB", output_format="auto", use_column_width=True)
        if file is not None:
            df = pd.read_excel(file, header=0)
            var_list = list(df.columns)
            option3 = st.sidebar.multiselect(
              '筛选出您希望在数据分析报告中包含的变量',
              var_list)
            st.info("包含的变量信息如下：")
            df = df[option3]
            option2 = st.sidebar.selectbox(
                 '筛选模式，完整分析还是简单分析',
                    ('简单分析', '完整分析'))
            if option2 == '完整分析':
                    mode = 'complete'
                    st.sidebar.warning(
                          '完整分析目前还在研发中，请先使用简单分析')
            elif option2 == '简单分析':
                    mode = 'minimal'
                    st.sidebar.warning(
                         '简单分析由于快速进行数据分析，要是遇到大型的数据集，还会有计算失败的情况出现')
                    grid_response = AgGrid(
                      df,
                    editable=True,
                       height=300,
                      width='100%',
                      )
                    updated = grid_response['data']
                    df1 = pd.DataFrame(updated)
                    if st.button('生成报告'):
                        if mode=='complete':
                             profile=ProfileReport(df,
                                title="User uploaded table",
                                      progress_bar=True,
                             )
                             st_profile_report(profile)
                        elif mode=='minimal':
                            profile=ProfileReport(df1,
                               minimal=True,
                                  title="User uploaded table",
                                  progress_bar=True,
                            )
                        st_profile_report(profile)
        else:
                imageShow()