#! /usr/bin/env python
# -*- encoding: UTF-8 -*-


import qi
import argparse
import sys
import time
    

def main(session):
    """
    Example : using soundset
    """
    # Get the services 
    audio_player_service = session.service("ALAudioPlayer")

    # list the soundsets
    existing_soundsets = audio_player_service.getInstalledSoundSetsList()
    
    # load the soundsets
    for exsoundset in existing_soundsets:
        audio_player_service.loadSoundSet(exsoundset)

    # list loaded soundets
    loaded_soundsets   = audio_player_service.getLoadedSoundSetsList()

    print loaded_soundsets

    for soundset in loaded_soundsets:
        filenames = audio_player_service.getSoundSetFileNames(soundset)
        for f in filenames:
            print f
            # warning there are lots of sounds
            #audio_player_service.playSoundSetFile(soundset, f, _async=True)
        print str(len(filenames)) + " sounds loaded"


    """
    Loop on, wait until manual interruption.
    """
    print "Starting script"
    try:
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        print "Interrupted by user, stopping script"
        # unsubscribe what is needed here

        #stop
        sys.exit(0)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)

    # run script
    main(session)

