import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

HR_df = pd.read_csv("/Users/christiannielsen/Documents/GitHub/christiannielsen98.github.io/HRDataset_v14.csv")
print(HR_df)

def perfcorr():

    fig = px.bar(HR_df, x="ManagerName", y="EmpID", color="PerformanceScore", barmode="group",
    #              facet_row="time", facet_col="PerformanceScore",
    #              #category_orders={"day": ["Thur", "Fri", "Sat", "Sun"],
    #                               "time": ["Lunch", "Dinner"]})
                  )


    #fig = go.Figure(go.Bar(x=HR_df.ManagerName, y= HR_df.PerformanceScore.str.contains('PIP'), name='PIP'))

    fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    # fig.show()
    fig.write_html("/Users/christiannielsen/Documents/GitHub/christiannielsen98.github.io/docs/Python/HTML/PerfomanceManagerCorrelation.html")

perfcorr()

