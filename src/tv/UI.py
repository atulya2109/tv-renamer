from __future__ import print_function, unicode_literals
from pprint import pprint
from PyInquirer import prompt, Separator
from tvdb_api import BaseUI

class CustomUI(BaseUI):

    def selectSeries(self, allSeries,limit=6):
         
        # print(allSeries)
        seriesList = [{
             'type' : 'list',
             'name' : 'seriesName',
             'message' : 'Select Your Tv Series',
         }]

        choices = []

        for i,show in enumerate(allSeries):
             choices.append({
                 'name': show['seriesName'],
                 'value': i+1
             })

        seriesList[0]['choices'] = choices

        answers = prompt(seriesList)

        return allSeries[answers['seriesName']-1]