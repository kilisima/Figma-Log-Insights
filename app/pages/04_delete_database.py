import library.files as libfiles
import library.db as libdb
import streamlit as st

def main():

    st.title("Delete Database")
    with st.form():
        select_db = st.selectbox("Database", libfiles.get_database_list())
        submitted = st.form_submit_button("削除")

    if submitted :
        with st.spinner("Deleting..."):
            libfiles.remove_database_file(select_db)
        
        st.text(f"File Deleted. Filepath: {select_db}")
        

    pass


if __name__ == "__main__":
    main()
    pass