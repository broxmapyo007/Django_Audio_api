# Django_Audio_api

This is Test challenge by Filed.com
completed by Adesh Dangi

## Use vedio 
Vedio link : 
- https://drive.google.com/file/d/1Iai41gBoI9tJWTvoajV5ksV6f56qoPsl/view?usp=sharing

##Setup file
1. Download code
    On github-repo : Django_Audio_api
    git clone https://github.com/broxmapyo007/Django_Audio_api.git

2. Requirements
    Langauge : Python 3.8.4
    Editor : Atom / Vs code
    Framewrok : Django
    vitrual env : pip intall pipenv

3. Start Virtual envrionment pipenv
    location> pipenv shell
    location>cd audioapi

4. Migrate database table models
    location/audioapi> ls
        check for manage.py file then,
    location/audioapi > python manage.py migrate
      this will create all tables in db

4. Run-server   
    location/audioapi> python manage.py runserver
      Watching for file changes with StatReloader
      Performing system checks...

      System check identified no issues (0 silenced).
      April 29, 2021 - 18:20:38
      Django version 3.2, using settings 'audioapi.settings'
      Starting development server at http://127.0.0.1:8000/
      Quit the server with CTRL-BREAK.

    Click/Visit on link :  http://127.0.0.1:8000/

#How to start on web-browser

  1. Visit server link :  http://127.0.0.1:8000
 
  2. Audiotype in link :
      Songs
      -  http://127.0.0.1:8000/song
        
      Podcast
      -  http://127.0.0.1:8000/podcast
        
      Audiobooks
      -  http://127.0.0.1:8000/audiobook
        
  3. GET/POST <audiotype>/ [All data of type]
      Songs
      -  http://127.0.0.1:8000/song/song
      Podcasts
      -  http://127.0.0.1:8000/podcast/podcast
      Audiobooks
      -  http://127.0.0.1:8000/audiobook/audiobook
    
  4. DELETE/PUT/PATCH <audiotype>/<audio:id>
        [update or delete specific]
      -  demo :   http://127.0.0.1:8000/song/song/1
        Songs
      -      http://127.0.0.1:8000/song/song/<id:song>
        Podcasts
      -      http://127.0.0.1:8000/podcast/podcast/<id:podcast>
        Audiobooks
      -      http://127.0.0.1:8000/audiobook/audiobook/<id:audiobook>



# challenge Description
  Write a Flask / FastAPI / Django Web API that simulates the behavior of an audio file server while using a MongoDB / SQL database.

  Requirements: You have one of three audio files which structures are defined below

#Audio file type can be one of the following:
    1 – Song
    2 – Podcast
    3 – Audiobook

####Song file fields:
  - ID – (mandatory, integer, unique)
  - Name of the song – (mandatory, string, cannot be larger than 100
  characters)
  - Duration in number of seconds – (mandatory, integer, positive)
  - Uploaded time – (mandatory, Datetime, cannot be in the past)

###Podcast file fields:
  - ID – (mandatory, integer, unique)
  - Name of the podcast – (mandatory, string, cannot be larger than 100
  characters)
  - Duration in number of seconds – (mandatory, integer, positive)
  - Uploaded time – (mandatory, Datetime, cannot be in the past)
  - Host – (mandatory, string, cannot be larger than 100 characters)
  - Participants – (optional, list of strings, each string cannot be larger than
  100 characters, maximum of 10 participants possible)

###Audiobook file fields:
  - ID – (mandatory, integer, unique)
  - Title of the audiobook – (mandatory, string, cannot be larger than 100
  characters)
  - Author of the title (mandatory, string, cannot be larger than 100
  characters)
  - Narrator - (mandatory, string, cannot be larger than 100 characters)
  - Duration in number of seconds – (mandatory, integer, positive)
  - Uploaded time – (mandatory, Datetime, cannot be in the past)
  Implement create, read, upload, and delete endpoints for an audio file as defined
  below:

##Create API:
    The request will have the following fields:
    - audioFileType – mandatory, one of the 3 audio types possible
    - audioFileMetadata – mandatory, dictionary, contains the metadata for one
    of the three audio files (song, podcast, audiobook)

##Delete API:
  - The route will be in the following format:
  “<audioFileType>/<audioFileID>”
  Update API:
  - The route be in the following format: “<audioFileType>/<audioFileID>”
  - The request body will be the same as the upload

##Get API:
  - The route “<audioFileType>/<audioFileID>” will return the specific audio
  file
  - The route “<audioFileType>” will return all the audio files of that type

##The response of these methods should be one of the following:
  - Action is successful: 200 OK
  - The request is invalid: 400 bad request
  - Any error: 500 internal server error
