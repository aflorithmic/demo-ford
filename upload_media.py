import apiaudio

apiaudio.api_key = "API_KEY"

# Uploads a media file
# -> returns a mediaId which must be supplied to mastering later
response = apiaudio.Media.upload(
  file_path= "./Ford_VO.wav"
 )
print(response)
 

# This media file is already uploaded to your org: Ivan_Mayes-bfc74ca1
# --> {'message': 'Success. Use mediaId to retrieve this file', 'mediaId': '8657aa5e'}