import json
import boto3
import os

outputPath = 'output/'

polly_client = boto3.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name='us-west-2').client('polly')

# response = polly_client.synthesize_speech(VoiceId='Joanna',
#                                           OutputFormat='mp3',
#                                           Text='Bitmex Perpetual swap Funding in 5 minutes')

# file = open('speech.mp3', 'wb')
# file.write(response['AudioStream'].read())
# file.close()

with open('Markets.json') as f:
    markets = json.load(f)

    for market in markets['markets']:
        market['Sessions'].append({"Title": "Closed"})
        for session in market['Sessions']:

            ###########################################################
            string0MinAdvance = market['Title'] + " " + session['Title']
            string0MinAdvance = string0MinAdvance.replace('/', ' ')
            print(string0MinAdvance)
            filename0MinAdvance = string0MinAdvance.replace(' ', '_') + '.mp3'

            # Doesn't already exists
            if(not os.path.isfile(filename0MinAdvance)):
                print('Calling')
                response = polly_client.synthesize_speech(VoiceId='Joanna',
                                                          OutputFormat='mp3',
                                                          Text=string0MinAdvance)

                print('Saving')
                file0MinAdvance = open(outputPath + filename0MinAdvance, 'wb')
                file0MinAdvance.write(response['AudioStream'].read())
                file0MinAdvance.close()
                print('Done')

###########################################################
            string1MinAdvance = market['Title'] + \
                " " + session['Title'] + " in 1 minute"
            string1MinAdvance = string1MinAdvance.replace('/', ' ')
            print(string1MinAdvance)
            filename1MinAdvance = string1MinAdvance.replace(' ', '_') + '.mp3'

            # Doesn't already exists
            if(not os.path.isfile(filename1MinAdvance)):
                print('Calling')
                response = polly_client.synthesize_speech(VoiceId='Joanna',
                                                          OutputFormat='mp3',
                                                          Text=string1MinAdvance)

                print('Saving')
                file1MinAdvance = open(outputPath + filename1MinAdvance, 'wb')
                file1MinAdvance.write(response['AudioStream'].read())
                file1MinAdvance.close()
                print('Done')

###########################################################
            for x in range(2, 31):
                stringxMinAdvance = market['Title'] + " " + \
                    session['Title'] + " in " + str(x) + " minutes"
                stringxMinAdvance = stringxMinAdvance.replace('/', ' ')
                print(stringxMinAdvance)
                filenamexMinAdvance = stringxMinAdvance.replace(
                    ' ', '_') + '.mp3'

                # Doesn't already exists
                if(not os.path.isfile(filenamexMinAdvance)):
                    print('Calling')
                    response = polly_client.synthesize_speech(VoiceId='Joanna',
                                                              OutputFormat='mp3',
                                                              Text=stringxMinAdvance)

                    print('Saving')
                    filexMinAdvance = open(
                        outputPath + filenamexMinAdvance, 'wb')
                    filexMinAdvance.write(response['AudioStream'].read())
                    filexMinAdvance.close()
                    print('Done')
