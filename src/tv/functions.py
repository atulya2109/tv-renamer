import os
import json
import tvdb_api
import re
import logging
from UI import CustomUI

logger = logging.getLogger(__name__)

fh = logging.FileHandler('Logs.log',mode='w')
f_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
fh.setFormatter(f_format)
logger.addHandler(fh)
logger.setLevel(logging.INFO)
tvdb = tvdb_api.Tvdb(banners=True,custom_ui=CustomUI)


def readFile(path):

    with open(path, 'r') as f:
            return f.read()

def writeFile(path,data,mode = 'w'):

    with open(path, mode) as f:
            f.write(data)

def checkSeason(text):

    text = re.sub(r'[._]',' ',text)
    season = re.findall(r'\bs(?:eason)?\s?([0-9]{1,2})?|(\b\d{1,2})x\d{1,2}\b',text,re.IGNORECASE)

    if len(season[0][0]) > 0:
        return int(season[0][0])
    elif len(season[0][1]) > 0:
        return int(season[0][1])
    else:
         return 0

def  checkEpisode(text):
    
    text = re.sub('[._]',' ',text)
    
    episode = re.findall(r"e(?:pisode)?\s?(\d{1,2})\b|\b\d{1,2}x(\d{1,2})\b",text,re.IGNORECASE)
    if not len(episode):
        return 0
    elif len(episode[0][0]) > 0:
        return int(episode[0][0])
    elif len(episode[0][1]) > 0:
        return int(episode[0][1])

def rename(src,name):

    name = re.sub('[^\w\-_\. ]','',name)
    dest = f'{os.path.dirname(src)}\{name}'

    if src != dest:
        os.rename(src,dest)

def processEpisode(ep_no,season_no,series,f,file_path):

    episode = series[season_no][ep_no]
    episodeName = episode['episodeName']
    seriesName = series['seriesName']
    ext = f[f.rfind('.'):]
    
    new_name = f'{seriesName} - {str(season_no).zfill(2)}x{str(ep_no).zfill(2)} - {episodeName}{ext}'

    logger.info(f'Renaming Episode {ep_no} => {episodeName}')
    rename(file_path,new_name)

def processSeason(series,season_no,content_path):

    seriesName = series['seriesName']
    avail_ep = []
    new_path = f'{seriesName}\Season {season_no}'

    
    files = os.listdir(content_path)

    for f in files:
        
        file_path = f'{content_path}\{f}'
        if os.path.isfile(file_path):
            ep_no = checkEpisode(f)

            if ep_no:
                processEpisode(ep_no,season_no,series,f,file_path)
                avail_ep.append(ep_no)
    
    rename(content_path,f'Season {season_no}')

    return avail_ep         
    

def processSeries(folderPath, id):
    """ Fetches data from TVDB and renames the files appropriately.


    Parameters
    ----------

    folderPath : str
        Path to the Tv Series

    id : str
        As accurate as possible name of Tv Series
    """
    
    global tvdb

    series = tvdb[id]
    seriesName = series['seriesName']

    contents = os.listdir(folderPath)
    season_info = {}
    rename(folderPath,seriesName)

    for content in contents:

        content_path = f'{folderPath}\{content}'
        avail_season = []
        if os.path.isdir(content_path):

            season_no = checkSeason(content)

            if season_no:
                
                avail_ep = processSeason(series,season_no,content_path)
                season_info[str(season_no)] = avail_ep
                avail_season.append(season_no)
    
    return (seriesName)