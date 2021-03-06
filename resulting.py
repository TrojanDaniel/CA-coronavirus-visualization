
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from bokeh.models import Div, DatePicker, ColumnDataSource, TableColumn, DataTable, HoverTool
from bokeh.plotting import figure, curdoc
from bokeh.layouts import column, row
from bokeh.core.properties import value
from bokeh.io import show


cdph_total = "https://raw.githubusercontent.com/datadesk/california-coronavirus-data/master/cdph-state-totals.csv"
total_file = pd.read_csv(cdph_total)
newest_update_date = total_file.iloc[1, 0]

desc= Div(text="""All data are provided by Los Angeles Times.
Repo Link:https://github.com/datadesk/california-coronavirus-data.
<b>Date of last update:{}</b>""".format(newest_update_date),
        width=600, height=90)


date_picker = DatePicker(title='Select Date', value="2020-08-16", min_date="2020-07-01", max_date=newest_update_date)
picked_date=date_picker.value

####### Question 1

day_confirmed_cases=0
for i in range(len(total_file["date"])-1):
        if total_file["date"][i]==picked_date:
                day_confirmed_cases=total_file["confirmed_cases"][i]-total_file["confirmed_cases"][i+1]
                break

data1=dict(date=[picked_date],day_confirmed_cases=[day_confirmed_cases])
col1=[TableColumn(field="date",title="DATE"),TableColumn(field="day_confirmed_cases",title="DAY CONFIRMED CASES")]
source1=ColumnDataSource(data1)
dt1=DataTable(source=source1,columns=col1,width=500,height=200)
ht1 = HoverTool(
	tooltips=[
		("date", "@date"),
		("new cases", "@day_confirmed_cases")
	]
)

p1 = figure(x_range=data1["date"],y_range=(0,20000),plot_width=500, plot_height=500,
            tools="", title="Confirmed Cases in Selected Day")
p1.add_tools(ht1)
p1.circle(x='date',y='day_confirmed_cases',source=source1,
                         size=20, color="#DB7093")



######## Question 2

desc2 = Div(text = """For a particular day, <b> 1. the %percent cases by race compared to their representation in the
general population  2. the %percent deaths by race compared to their representation in the
general population 3.population percent</b> are shown in the figure""")

cdph_race = "https://raw.githubusercontent.com/datadesk/california-coronavirus-data/master/cdph-race-ethnicity.csv"
race_file = pd.read_csv(cdph_race)

table_race = race_file[(race_file["age"] == "all") & (race_file["date"] == picked_date)]
race_types=table_race.race.tolist()
race_cols=list(table_race) # all column name
race_cols.remove('date')
race_cols.remove('age')
race_cols.remove('deaths_total')

cols2 = [TableColumn(field="race", title="RACE"),
    TableColumn(field="confirmed_cases_percent", title="CONFIRMED CASES PERCENT")
    ,TableColumn(field="deaths_percent", title="DEATHS PERCENT"),TableColumn(field="population_percent", title="POPULATION PERCENT")]


source2= ColumnDataSource(data = table_race[race_cols])

# dt_race = DataTable(source = source2, columns=cols2, width=600, height=200)


ht2 = HoverTool(
    tooltips=[('confirmed_cases_percent', '@confirmed_cases_percent'), ('deaths_percent', '@deaths_percent'), ('population percent', '@population_percent')])

colors=["#DB7093","#6A5ACD","#3CB371"]
new_cols= ["confirmed_cases_percent","deaths_percent","population_percent"]
p2 = figure(x_range=table_race[race_cols]["race"],plot_width=500, plot_height=500,title="",tools=[ht2])


p2.vbar_stack(new_cols,x='race',source=source2,
                         width=0.3, color=colors,legend_label=["%s" % x for x in new_cols])
p2.legend.orientation = "vertical"
p2.legend.location = "top_left"




def call_back(attr, old, new):
    global picked_date
    picked_date=date_picker.value
    day_confirmed_cases = 0
    for i in range(len(total_file["date"]) - 1):
        if total_file["date"][i] == picked_date:
            day_confirmed_cases = total_file["confirmed_cases"][i] - total_file["confirmed_cases"][i + 1]
            break
    data1=dict(data=[picked_date],day_confirmed_cases=[day_confirmed_cases])
    source1.data= data1

    #quesition2
    table_race =race_file[(race_file["age"] == "all") & (race_file["date"] == picked_date)]
    race_cols = list(table_race)  # all column name
    race_cols.remove('date')
    race_cols.remove('age')
    race_cols.remove('deaths_total')
    race_data = table_race[race_cols]
    source2.data=race_data


date_picker.on_change("value",call_back)
q2=column(desc2,p2)
layout=column(desc,date_picker,dt1,row(p1,q2))
curdoc().add_root(layout)
