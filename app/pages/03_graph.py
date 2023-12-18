import streamlit as st
import library.db as libdb
import library.files as libfiles

import plotly.express as px
import polars as pl
import plotly.graph_objs as go

def in_progress():
    st.session_state.graph_in_progress = True


def main():
    st.session_state.graph_in_progress = False
    st.set_page_config(
        page_title="Graph" ,
        layout="wide",
    )
        
    st.title("Graph")
    
    with st.form("graph"):
        database_file = st.selectbox("select database", libfiles.get_database_list())

        submitted = st.form_submit_button("表示する", disabled=st.session_state.graph_in_progress, on_click=in_progress())

    if submitted:
        with st.spinner("[team event summary]loading..."):
            
            show_graph_team_event_summary(database_file=database_file)
        
        with st.spinner("[event count summary]loading..."):
            show_graph_event_count_summary(database_file=database_file)


        with st.spinner("[email event summaryloading..."):
            show_graph_email_event_summary(database_file=database_file)

    pass



def show_graph_team_event_summary(database_file:str):
    data = libdb.get_tean_event_sumamry(database_file=database_file)

    # Polars DataFrameにデータを変換
    df_de_summary = pl.DataFrame(data)
    df_de_summary.head()
    df_de_summary = df_de_summary.with_columns(
        pl.col("year_month").str.to_datetime("%Y-%m")
    )
    
    # 積み上げグラフを作成
    fig = go.Figure()

    # 各カテゴリーごとにバーを追加
    for category in df_de_summary["team_name"].unique():
        category_data = df_de_summary.filter(df_de_summary["team_name"] == category)
        fig.add_trace(go.Bar(
            x=category_data["year_month"],
            y=category_data["count"],
            name=category
        ))

    # 積み上げグラフの設定
    fig.update_layout(barmode='stack', title='アクション数時系列（Teamで色分け）')
    fig.update_layout(xaxis=dict(tickformat='%Y-%m', tickvals=df_de_summary["year_month"]))


    # グラフの表示
    # fig.show()
    st.plotly_chart(fig)


def show_graph_event_count_summary(database_file:str):
    data = libdb.get_tean_event_sumamry(database_file=database_file)

    # Polars DataFrameにデータを変換
    df_de_summary = pl.DataFrame(data)
    df_de_summary.head()
    df_de_summary = df_de_summary.with_columns(
        pl.col("year_month").str.to_datetime("%Y-%m")
    )

    # 積み上げグラフを作成
    fig = go.Figure()

    # 各カテゴリーごとにバーを追加
    for category in df_de_summary["event"].unique():
        category_data = df_de_summary.filter(df_de_summary["event"] == category)
        fig.add_trace(go.Bar(
            x=category_data["year_month"],
            y=category_data["count"],
            name=category
        ))

    # 積み上げグラフの設定
    fig.update_layout(barmode='stack', title='イベント数集計')
    fig.update_layout(xaxis=dict(tickformat='%Y-%m', tickvals=df_de_summary["year_month"]))

    # グラフの表示
    # fig.show()
    st.plotly_chart(fig)

def show_graph_email_event_summary(database_file:str):
    data = libdb.get_email_event_summary(database_file=database_file)
    df_email_event_summary = pl.DataFrame(data).sort("count", descending=True)
    df_email_event_summary.head()

    pivot_data = df_email_event_summary.pivot(values="count", index="email", columns="event")
    pivot_data.head()

    fig = px.histogram(
        data_frame=df_email_event_summary,
        x='count',
        y='email',
        color='event',
        title='ユーザーごとのアクション数集計（全データ）'
    )

    fig.update_layout(width=1500, height=2000)
    fig.update_yaxes(categoryorder='total ascending')

    st.plotly_chart(fig)



if __name__ == "__main__":
    main()