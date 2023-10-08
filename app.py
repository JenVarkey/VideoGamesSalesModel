from flask import Flask, render_template, request
import base64
from io import BytesIO
from matplotlib.figure import Figure
import data as dt

app = Flask(__name__)

def plot_sales_summary():
    vgdata = dt.VGsales()
    ss = vgdata.get_sales_summary()
    regions = []
    sales = []
    for row in ss:
        regions.append(row['region'])
        sales.append(row['sales'])
    fig = Figure()
    ax = fig.subplots()
    ax.pie(sales,labels=regions,autopct='%1.1f%%',pctdistance=1.25, labeldistance=.6)
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data


def plot_sales_trend():
    vgdata = dt.VGsales()
    ss = vgdata.get_sales_by_year()
    year = []
    sales = []
    for row in ss:
        year.append(row['year'])
        sales.append(row['sales'])
    fig = Figure()
    ax = fig.subplots()
    ax.plot(year, sales)
    buf = BytesIO()
    fig.savefig(buf, format="png")
    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return data

@app.route('/', methods=['GET', 'POST'])
def main():
    print("Filters", str(request.args))
    publisher = request.args.get('publisher')
    genre = request.args.get('genre')
    platform = request.args.get('platform')
    vgdata = dt.VGsales()
    data = {}
    data['publishers'] = vgdata.get_publishers()
    data['genres'] = vgdata.get_genres()
    data['platforms'] = vgdata.get_platforms()
    data['sales_summary'] = plot_sales_summary()
    data['sales_trend'] = plot_sales_trend()
    data['details'] = vgdata.get_sales_details(publisher,genre,platform)
    return render_template(template_name_or_list='index.html',data=data)

if __name__ == "__main__":
    app.run(debug=True)
