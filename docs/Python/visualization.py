import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
HR_df = pd.read_csv("/Users/christiannielsen/Documents/GitHub/christiannielsen98.github.io/HRDataset_v14.csv")


def PerfomanceManagerCorrelation():
    fig = px.bar(HR_df, x="ManagerName", y="EmpID", color="PerformanceScore")
    fig.update_layout(barmode='stack', xaxis={'categoryorder': 'total descending'})
    return fig.write_html("/Users/christiannielsen/Documents/GitHub/christiannielsen98.github.io/docs/Python/HTML/PerfomanceManagerCorrelation.html")
PerfomanceManagerCorrelation()

def EquitablePayByGroups():
    trace_position_m = go.Box(x=HR_df.loc[HR_df['Sex'] == "M "].Position,
                            y=HR_df.loc[HR_df['Sex'] == "M "].Salary,
                            name='Men',
                            marker_color='blue'
                            )

    trace_position_f = go.Box(x=HR_df.loc[HR_df['Sex'] == "F"].Position,
                            y=HR_df.loc[HR_df['Sex'] == "F"].Salary,
                            name='Women',
                            marker_color='red'
                            )

    trace_race_m = go.Box(x=HR_df.loc[HR_df['Sex'] == "M "].RaceDesc,
                              y=HR_df.loc[HR_df['Sex'] == "M "].Salary,
                              name='Men',
                              marker_color='blue'
                          )
    trace_race_f = go.Box(x=HR_df.loc[HR_df['Sex'] == "F"].RaceDesc,
                              y=HR_df.loc[HR_df['Sex'] == "F"].Salary,
                              name='Women',
                              marker_color= 'red'
                          )

    trace_maritalstatus_m = go.Box(x=HR_df.loc[HR_df['Sex'] == "M "].MaritalDesc,
                          y=HR_df.loc[HR_df['Sex'] == "M "].Salary,
                          name='Men',
                          marker_color='blue'
                                   )
    trace_maritalstatus_f = go.Box(x=HR_df.loc[HR_df['Sex'] == "F"].MaritalDesc,
                          y=HR_df.loc[HR_df['Sex'] == "F"].Salary,
                          name='Women',
                          marker_color='red'
                                   )

    traces = [trace_position_m, trace_position_f, trace_race_m, trace_race_f, trace_maritalstatus_m, trace_maritalstatus_f]


    updatemenus = list([
        dict(active=0,
             buttons=list([
                 dict(label='Position',
                      method='update',
                      args=[{'visible': [True, True, False, False, False, False]},
                            {'title': 'Salary for every position'}]),
                 dict(label='Race',
                      method='update',
                      args=[{'visible': [False, False, True, True, False, False]},
                            {'title': 'Salary for every race'}]),
                 dict(label='Marital status',
                      method='update',
                      args=[{'visible': [False, False, False, False, True, True]},
                            {'title': 'Salary for every marital status'}]),
             ]),
             )
    ])

    layout = dict(title='Salary pay', showlegend=True,
                  updatemenus=updatemenus,
                  yaxis_title='Yearly salary in dollars',
                  boxmode='group',
                  xaxis_type='category'
                  )

    fig = go.Figure(data=traces, layout=layout)
    fig.update_xaxes(showgrid=True)

    fig.show()
    return fig.write_html(
        "/Users/christiannielsen/Documents/GitHub/christiannielsen98.github.io/docs/Python/HTML/EquitablePayByGroups.html")

EquitablePayByGroups()

def Heatmap():
    fig = px.density_heatmap(HR_df, x="Position", y="RaceDesc")
    fig.show()
