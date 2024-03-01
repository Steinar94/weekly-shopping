from jinja2 import Environment, FileSystemLoader
from config import settings
from datetime import datetime


def render_plaintext(data):
    s = "Middags Planlegger\n"
    s += f"{datetime.today()}\n\n"
    s += "Middager\n"
    s += f"Mandag:  {data['Middager'][0]}\n"
    s += f"Tirsdag: {data['Middager'][1]}\n"
    s += f"Onsdag:  {data['Middager'][2]}\n"
    s += f"Torsdag: {data['Middager'][3]}\n"
    s += f"Fredag:  {data['Middager'][4]}\n"
    s += f"Lørdag:  {data['Middager'][5]}\n"
    s += f"Søndag:  {data['Middager'][6]}\n"

    for ingredient in data["Handleliste"]:
        s += f"{ingredient}"

    s += "\n\n© Steinar Brandvik\n"

    return s


def render_template(data):
    env = Environment(loader=FileSystemLoader(settings.template_path))
    template = env.get_template("email_template.html")
    return template.render(
        title="Middags Planlegger",
        date=f"{datetime.today()}",
        Mandag=data["Middager"][0],
        Tirsdag=data["Middager"][1],
        Onsdag=data["Middager"][2],
        Torsdag=data["Middager"][3],
        Fredag=data["Middager"][4],
        Lørdag=data["Middager"][5],
        Søndag=data["Middager"][6],
        ingredients=data["Handleliste"],
    )
