import streamlit as st
import library.db as libdb
import library.files as libfiles


def data_load_in_progress():
    st.session_state.data_load_in_progress = True


def main():
    st.session_state.data_load_in_progress = False

    st.set_page_config(
         page_title="Import Data" ,
         layout="wide",
    )

    st.title("Import Data")
    with st.form("import_data", clear_on_submit=True) as form:
        database_file = st.selectbox("import database", libfiles.get_database_list())

        upload_data = st.file_uploader("import figma data", ["csv", "tsv"], False)

        submitted = st.form_submit_button("Import", disabled=st.session_state.data_load_in_progress, on_click=data_load_in_progress())

    if submitted:
        print(f"database_file:{database_file}, upload_data:{upload_data.name}")
        if upload_data is not None and database_file is not None:
            st.session_state.in_progress = True
            with st.spinner("Loading..."):
                if libdb.import_data(upload_data, database_file):
                    st.write("Import Complete!")
                    # TODO 取り込んだデータ件数などを表示する
                else:
                    st.write("Import Failed.")
                
        
        else:
            st.write("Failesd: select database file and Upload import data")
            st.write("登録できません。")
        
        st.session_state.in_progress = False


if __name__ == "__main__":
    main()