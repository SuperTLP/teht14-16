from urllib import request
from project import Project
import pytoml as toml
class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        data = toml.loads(content)
        name = data["tool"]["poetry"]["name"]
        description = data["tool"]["poetry"]["description"]

        dep = list(data["tool"]["poetry"]["dependencies"].keys())
        devdep = list(data["tool"]["poetry"]["dev-dependencies"].keys())

        return Project(name, description, dep, devdep)