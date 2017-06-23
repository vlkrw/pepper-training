import qi
import argparse
import sys

"""
    Adapt this code to listen to signal ALUserSession::focusedUser

    qi::Signal<int> ALUserSession::focusedUser
    Sent when a user is focused.
    int ID: UserSession ID of the focused user, -1 if no user is focused anymore.

"""

def main(session):
    """
    this example shows ALUserSession API
    """
    print "Creating alusersession service"
    us = session.service("ALUserSession")

    print "Let's check who is the focused user"
    id = us.getFocusedUser()
    print "USID of focused user is " + str(id)

    print "doUsersExist"
    print us.doUsersExist([id])
    
    print "getUserList"
    print us.getUserList()

    print "getNumUsers"
    print us.getNumUsers()
       
    print "getOpenUserSessions"
    print us.getOpenUserSessions()
    
    # NOT WORKING IN naoqi 2.1
    print "isUserSessionOpen"
    print "User " + str(id) + " is permanent"
    
    print "isUserSessionOpen"
    print us.areUserSessionsOpen([id])
    
    # NOT WORKING IN naoqi 2.1
    print "isUserPermanent"
    print us.isUserPermanent(id)
    
    print "areUsersPermanent"
    print us.areUsersPermanent([id])
    
    print "getPermanentUserList"
    print us.getPermanentUserList()

    print "getPpidFromUsid"
    ppid = us.getPpidFromUsid(id)
    print ppid
    
    print "getUsidFromPpid"
    print us.getUsidFromPpid(id)
    
    # print us.getBindingList()
    # print us.doesBindingExist()
    # print us.getUserBindings()
    # print us.getUserBinding()
    # print us.findUsersWithBinding()
    # print us.getUserCreationDate()
    # print us.getFirstEncounterDate()
    # print us.getCurrentEncounterDate()
    # print us.getLastEncounterDate()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot's IP address. If on a robot or a local Naoqi - use '127.0.0.1' (this is the default value).")
    parser.add_argument("--port", type=int, default=9559,
                        help="port number, the default value is OK in most cases")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://{}:{}".format(args.ip, args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments."
               " Run with -h option for help.".format(args.ip, args.port))
        sys.exit(1)
    except KeyboardInterrupt:
        print "Interrupted by user, shutting down"
        #stop
        sys.exit(0)

    main(session)
