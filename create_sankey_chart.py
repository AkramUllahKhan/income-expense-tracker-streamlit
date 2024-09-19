import plotly.graph_objects as go

def create_sankey_chart(incomes_data, expenses_data):
    """Creates a Sankey chart based on income and expense data."""
    # Create lists dynamically
    label = list(incomes_data.keys()) + ["Total Income"] + list(expenses_data.keys())
    source = list(range(len(incomes_data))) + [len(incomes_data)] * len(expenses_data)
    target = [len(incomes_data)] * len(incomes_data) + [label.index(expense) for expense in expenses_data.keys()]
    value = list(incomes_data.values()) + list(expenses_data.values())

    # Create Sankey chart
    link = dict(source=source, target=target, value=value)
    node = dict(label=label, pad=20, thickness=30, color="#E694FF")
    data = go.Sankey(link=link, node=node)

    # Plot it!
    fig = go.Figure(data)
    fig.update_layout(margin=dict(l=0, r=0, t=5, b=5))
    return fig
