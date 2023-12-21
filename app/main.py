import streamlit as st


def main():
    st.set_page_config(layout="wide", page_title="Figma InsightViz Hub")
    st.title("Figma InsightViz Hub")
    st.header("概要")
    st.text("Figmaのログを可視化するためのツールです")
    st.subheader("使い方")
    with st.container(border=1):
        st.markdown("""
    1. create_databaseからDBを作成する
    2. import_dataからFigmaのログをImportする
    3. graphからグラフを表示する
    4. グラフから何かを感じ取る
""")



if __name__ == "__main__":
    main()