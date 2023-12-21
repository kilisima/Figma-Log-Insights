import streamlit as st
import library.db as libdb
import library.files as libfiles
import time

def main():
    st.set_page_config(
         page_title="Database Create and Data Import" ,
         layout="wide",
    )
    st.title("Database Create and Data Import")
    # st.header("Select Database")
    # st.selectbox("Database List",st.session_state.dbs , )


    st.header("Create Database")
    with st.form("create_database"):
        st.text("ここでファイル名にグループ名や会社名などを付与するとわかりやすくなります。")
        filename = st.text_input("filename（拡張子は不要）",placeholder="XXXX株式会社、や、XXX_corp等")
        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
                with st.spinner("作成中") as spinner:
                    if libdb.create_database(filename) :
                        st.write("作成しました。")
                    else:
                        st.write("失敗しました。")
        


if __name__ == "__main__":
    main()





