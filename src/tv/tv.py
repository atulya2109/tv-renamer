from Credentials import *
from functions import *

def main():
    print(processSeries('H:\misc\dev\Game of Thrones','game of thrones'))
# config = {}
# config_file = './config.json'

# def addFolder(path,fileType):

#     global config
#     print(config)
#     if fileType == FileType.MOVIE:

#         config['movies_folders'].append(path)
    
#     elif fileType == FileType.SERIES:
#         config['series_folders'].append(path)

#     updateConfig()

# def updateConfig():

#     with open(config_file, 'w') as f:
#             f.write(json.dumps(config,indent=4,sort_keys=True)) 

# def createConfig():
#     '''
#         Creates a ```config``` config_file
#     '''
#     global config_file,config

#     if not os.path.isfile(config_file):

#         config = {
#                     'username' : USERNAME,
#                     'userkey' : USERKEY,
#                     'key' : KEY,
#                     'token' : TOKEN,
#                     'series_folders' : TV_SHOW_FOLDER,
#                     'movies_folders' : MOVIES_FOLDER
#         }
#         updateConfig()       

# def setToken(token):
    
#     global  config, config_file
#     config['token'] = token

#     with open(config_file, 'w') as f:
#             f.write(json.dumps(config,indent=4,sort_keys=True))

# def loadConfig(refresh = False):
#     '''
#         Loads the ```config``` config_file
#     '''
#     global config, config_file
    
#     if refresh:
#         os.remove(config_file)
    
#     createConfig()

#     with open(config_file,'r') as f:
#         config = json.load(f)


# def main():

#     pass

if __name__ == "__main__":
    main()