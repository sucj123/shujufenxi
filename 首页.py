import streamlit as st

st.set_page_config(page_title = "数据可视化分析系统", page_icon="🌏", layout="wide")

sysmenu = '''
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
'''
st.markdown(sysmenu,unsafe_allow_html=True)

st.header("数据分析是什么")
c1, c2 = st.columns(2)
with c2:
    st.image("sj.jpg", use_column_width=True)
with c1:
    st.info("""
        数据分析是分析数据趋势获取知识和洞察力以做出更好决策的过程。这个复杂的过程由数据分析师和数据科学家以及非技术人员协作进行的。该过程通常从原始数据开始，这些数据经过数据挖掘，寻求有价值的洞察力——事实上，竞争优势是业务数据分析的主要目标。\n
        数据分析主要包括以下内容：数据挖掘， 文本分析， 数据可视化， 商业智能， 数据目录，数据仓库，数据湖，数据网格， 数据建模， 人工智能(AI)，机器学习(ML)
   
    """)

st.header("可采用的工具（包含但不限于）")
c1, c2 = st.columns(2)
with c1:
    st.info("""
        1、Excel作为最基础也数据分析工具，同时也是最主要的数据分析工具。\n
        2、R是一门用于统计计算与作图的语言，其实R不单单是一门语言，还是一个数据计算与分析的环境。\n
        3、SAS功能强大并且可以编程，很受高级用户的欢迎，也正因为此，它是比较难掌握的软件之一，在企业工作中用的比较多，需要编写SAS程序去处理数据。\n
        4、Python是一种面向对象、解释型计算机程序设计的语言。它的语法简洁清晰，Python在数据分析和数据可视化等方面都显得比较活跃。
    """)
with c2:
    st.image("bt.jpg",use_column_width=True)