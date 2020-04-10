from person import Person 
import os
import mysql.connector
import calendar
import time

# Database connection
db = mysql.connector.connect(
    host='localhost',
    database="social_network",
    user='udallmo',
    passwd='password',
    auth_plugin="mysql_native_password"
)

# initialize cursors
cursor = db.cursor()

def login():
    """Login with email and password"""

    user = input("ENTER EMAIL: ")
    password = input("ENTER PASSWORD: ")
    profile = getProfile(user, password)

    os.system('clear')
    run(profile)

def run(profile):
    """Begin the login page"""

    print(f"WELCOME {profile.fullName.upper()}")
    loginFeed(profile)

    logout = False

    while (True):
        instructions()
        state = input("ENTER A COMMAND: ").lower()
        os.system('clear')

        if state == "logout":
            print("SIGNING OUT...")
            ts = calendar.timegm(time.gmtime())
            cursor.execute(f"update Users set timeStamp={ts} where userID={profile.id}")
            db.commit()
            exit()
        elif state == "post":
            managePosts(profile)
        elif state == "club":
            manageClubs(profile)
        elif state == "topic":
            manageTopics(profile)
        elif state == 'friends':
            manageFriends(profile)
        else:
            print("NOT VALID TAB!")

        os.system('clear')

def manageTopics(profile):    
    """Manage topic tabs 
        VIEW - view user topics
            ALL - view all topics
            VIEW - view posts from a topic
            EXIT - leaves VIEW mode
        JOIN - join a topic
        CREATE - create a new topic
        REMOVE - remove topic for user topics
    """

    print("TOPICS")
    print("---------------------------------")
    
    while(True):
        t_state = input("ENTER THE FOLLOWING: VIEW, JOIN, CREATE, REMOVE, EXIT: ").lower()

        if t_state == "view":
            print("TOPICS YOU FOLLOW: ")
            cursor.execute(f"select topic from userTopic join Topics using(topicID) where userID='{profile.id}'")

            for topic in cursor:
                print(replaceCursors(str(topic).replace(",", "")).replace("_", " "))

            while(True):
                tv_state = input("ENTER [ALL] TO VIEW ALL TOPICS or ENTER [VIEW] TO VIEW POSTS FROM A TOPIC or [EXIT]: ").lower()

                if tv_state == 'view':
                    topic = input("ENTER A TOPIC: ").lower().replace(" ", "_")
                    cursor.execute(f"select postID, postText, likes, dislikes, responseTo, p.timeStamp, firstName, MiddleName, LastName from Posts p join Users u using(userID) join Topics t using(topicID) where topic='{topic}'")
                    for post in cursor:
                        print(post)
                elif tv_state == 'all':
                    cursor.execute("select topic from Topics")
                    for topic in cursor:
                        print(replaceCursors(str(topic).replace(",", "")).replace("_", " "))
                elif tv_state == 'exit':
                    os.system('clear')
                    print("TOPICS")
                    print("---------------------------------")
                    break
                else:
                    print("INVALID COMMAND! TRY AGAIN!")

        elif t_state == "join":
            t_topic = input("ENTER TOPIC TO JOIN: ").lower().replace(" ", "_")
            
            cursor.execute(f"select topicID from Topics where topic='{t_topic}'")
            topicID = cursor.fetchone()

            if topicID == None:
                print("TOPIC IS NOT FOUND!")
            else:
                topicID = replaceCursors(str(topicID)).replace(',', '')
                cursor.execute(f"select userID from userTopic where userID={profile.id} and topicID={topicID}")
                relation = cursor.fetchone()

                if relation == None:
                    print(f"OK JOINING: {t_topic.upper()}")
                    cursor.execute(f"insert into userTopic(userID, topicID) values({profile.id}, {topicID});")
                    db.commit()
                else:
                    print("YOU ALREADY FOLLOW IT!")

        elif t_state == "create":
            t_create = input("Enter TOPIC TO CREATE ").lower().replace(" ", "_")

            cursor.execute(f"select * from Topics where topic='{t_create}'")
            result = cursor.fetchone()

            if result == None:
                print(f"ADD TOPIC: {t_create}")
                cursor.execute(f"insert into Topics(topic) values('{t_create}')")
            else:
                print("TOPIC ALREADY EXISTS")           

        elif t_state == "remove":
            t_remove = input("ENTER TOPIC TO REMOVE: ").lower().replace(" ", "_")
            
            cursor.execute(f"select topicID from userTopic join Topics using(topicID) where userID={profile.id} and topic='{t_remove}';")
            topicID = cursor.fetchone()

            if topicID == None:
                cursor.execute(f"select topicID from Topics where topic='{t_remove}'")
                error = cursor.fetchone()

                if error == None:
                    print("TOPIC IS NOT FOUND!")
                else:
                    print("NOT FOLLOWING ALREADY")
            else:
                topicID = replaceCursors(str(topicID)).replace(',', '')

                print(f"REMOVING TOPIC: {t_remove.replace('_', ' ')}")
                cursor.execute(f"delete from userTopic where userID={profile.id} and topicID={topicID}")
                db.commit()

        elif t_state == "exit":
            os.system('clear')
            return
        else:
            print("COMMAND NOT FOUND!")
        
def manageFriends(profile):
    """Friends Tab
        VIEW - view user's friends
        FOLLOW - follow a friend
        FIND - find information about a user
        EXIT- leaves Friends tab
    """
    print("FRIENDS")
    print("----------------------------")
    
    while(True):
        f_state = input("ENTER THE FOLLOWING: VIEW, FOLLOW, FIND, REMOVE, EXIT: ").lower()

        if f_state == "view":
            print("FRIENDS: ")
            cursor.execute(f"select firstName, middleName, LastName from userFriends f join Users u on userFOL=u.userID where f.userID={profile.id}")

            for friend in cursor:
                name = replaceCursors(str(friend)).replace(' ', '').split(',')
                middleName = f" {name[1]} " if name[1].lower() != 'none' else ' '
                print(f"{name[0]}{middleName}{name[2]}")

            while(True):
                tv_state = input("ENTER [ALL] TO VIEW ALL USERS or [EXIT]: ").lower()
                
                if tv_state == 'all':
                    cursor.execute("select firstName, MiddleName, LastName from Users")
                    for user in cursor:
                        name = replaceCursors(str(user)).replace(' ', '').split(',')
                        middleName = f" {name[1]} " if name[1].lower() != 'none' else ' '
                        print(f"{name[0]}{middleName}{name[2]}")
                elif tv_state == 'exit':
                    os.system('clear')
                    break
                else:
                    print("INVALID COMMAND! TRY AGAIN!")

        elif f_state == "follow":
            f_user = input("ENTER PERSON TO FOLLOW: ").lower()
            name = f_user.split(" ")

            if len(name)> 2:
                cursor.execute(f"select userID from Users where firstName='{name[0]}' and lastName='{name[len(name) - 1]}' and middleName='{name[1]}'")
            else:
                cursor.execute(f"select userID from Users where firstName='{name[0]}' and lastName='{name[len(name) - 1]}'")

            userID = cursor.fetchone()

            if userID == None:
                print("USER IS NOT FOUND!")
            elif replaceCursors(str(userID)).replace(',', '') == str(profile.id):
                print("CANNOT FOLLOW YOURSELF")
            else:
                userID = replaceCursors(str(userID)).replace(',', '')
                cursor.execute(f"select userID from userFriends where userID={profile.id} and userFOL={userID}")
                relation = cursor.fetchone()

                if relation == None:
                    print(f"OK FOLLOWING: {f_user.upper()}")
                    cursor.execute(f"insert into userFriends(userID, userFOL) values({profile.id}, {userID});")
                    db.commit()
                else:
                    print("YOU ALREADY FOLLOW THEM!")

        elif f_state == "find":
            f_find = input("ENTER USER TO FIND: ").lower()
            name = f_find.split(" ")

            if len(name)> 2:
                cursor.execute(f"select * from Users where firstName='{name[0]}' and lastName='{name[len(name) - 1]}' and middleName='{name[1]}'")
            else:
                cursor.execute(f"select * from Users where firstName='{name[0]}' and lastName='{name[len(name) - 1]}'")

            userData = replaceCursors(str(cursor.fetchone())).split(",")
            for el in userData:
                print(el)

        elif f_state == "remove":
            f_remove = input("Enter person you would like to remove: ").lower()
            name = f_remove.split(" ")

            if len(name)> 2:
                cursor.execute(f"select userFOL from userFriends f join Users u on userFOL =u.userID where f.userID={profile.id} and firstName='{name[0]}' and lastName='{name[len(name) - 1]}' and middleName='{name[1]}'")
            else:
                cursor.execute(f"select userFOL from userFriends f join Users u on userFOL =u.userID where f.userID={profile.id} and firstName='{name[0]}' and lastName='{name[len(name) - 1]}'")
            
            userID = cursor.fetchone()

            if userID == None:
                if len(name)> 2:
                    cursor.execute(f"select userID from Users where firstName='{name[0]}' and lastName='{name[len(name) - 1]}' and middleName='{name[1]}'")
                else:
                    cursor.execute(f"select userID from Users where firstName='{name[0]}' and lastName='{name[len(name) - 1]}'")

                error = cursor.fetchone()

                if error == None:
                    print("USER IS NOT FOUND!")
                else:
                    print("NOT FOLLOWING ALREADY")
            else:
                userID = replaceCursors(str(userID)).replace(',', '')

                print(f"REMOVING FRIEND: {f_remove}")
                cursor.execute(f"delete from userFriends where userID={profile.id} and userFOL={userID}")
                db.commit()
        elif f_state == "exit":
            os.system('clear')
            return
        else:
            print("command not found!")

def manageClubs(profile):
    """"Clubs (aka Groups) Tab
        VIEW - view user's groups
        FOLLOW - follow a group
        CREATE - create a group
        REMOVE - remove user from group
        EXIT - leaves Club tab
    """

    print("Welcome to Clubs")
    print("----------------------------")
    
    while(True):
        c_state = input("ENTER THE FOLLOWING: VIEW, FOLLOW, CREATE, REMOVE, EXIT: ").lower()

        if c_state == "view":
            print("CLUBS YOU ARE IN: ")
            cursor.execute(f"select club from userClub join Clubs using(clubID) where userID='{profile.id}'")

            for club in cursor:
                print(replaceCursors(str(club).replace(",", "")).replace("_", " "))

            while(True):
                tv_state = input("ENTER [ALL] TO VIEW ALL CLUBS OR [EXIT]: ").lower()
                
                if tv_state == 'all':
                    cursor.execute("select club from Clubs")
                    for club in cursor:
                        print(replaceCursors(str(club).replace(",", "")).replace("_", " "))
                elif tv_state == 'exit':
                    os.system('clear')
                    break
                else:
                    print("INVALID COMMAND! TRY AGAIN!")

        elif c_state == "follow":
            c_club = input("ENTER CLUB TO JOIN: ").lower().replace(" ", "_")
            
            cursor.execute(f"select clubID from Clubs where club='{c_club}'")
            clubID = cursor.fetchone()

            if clubID == None:
                print("CLUB IS NOT FOUND!")
            else:
                clubID = replaceCursors(str(clubID)).replace(',', '')
                cursor.execute(f"select userID from userClub where userID={profile.id} and clubID={clubID}")
                relation = cursor.fetchone()

                if relation == None:
                    print(f"OK JOINING: {c_club.upper()}")
                    cursor.execute(f"insert into userClub(userID, clubID) values({profile.id}, {clubID});")
                    db.commit()
                else:
                    print("YOU ALREADY FOLLOW IT!")

        elif c_state == "create":
            c_create = input("ENTER CLUB TO CREATE: ").lower().replace(" ", "_")
            
            cursor.execute(f"select * from Clubs where club='{c_create}'")
            result = cursor.fetchone()

            if result == None:
                print(f"ADD CLUB: {c_create}")
                cursor.execute(f"insert into Clubs(club) values('{c_create}')")
            else:
                print("CLUB ALREADY EXISTS")  

        elif c_state == "remove":
            c_remove = input("ENTER CLUB TO REMOVE: ").lower().replace(" ", "_")
            
            cursor.execute(f"select clubID from userClub join Clubs using(clubID) where userID={profile.id} and club='{c_remove}';")
            clubID = cursor.fetchone()

            if clubID == None:
                cursor.execute(f"select clubID from Clubs where club='{c_remove}'")
                error = cursor.fetchone()

                if error == None:
                    print("CLUB IS NOT FOUND!")
                else:
                    print("NOT FOLLOWING ALREADY")
            else:
                clubID = replaceCursors(str(clubID)).replace(',', '')

                print(f"REMOVING CLUB: {c_remove.replace('_', ' ')}")
                cursor.execute(f"delete from userClub where userID={profile.id} and clubID={clubID}")
                db.commit()
        elif c_state == "exit":
            os.system('clear')
            return
        else:
            print("COMMAND NOT FOUND!")
     
def managePosts(profile):
    """POST tab
        VIEW - view user's posts
        CREATE - create a post
        REMOVE - remove a post
        REPONSE - response to a post
        EXIT - leave post tab
    """
    print("POSTS")
    print("------------------------")

    while(True):
        p_state = input("Enter the following: VIEW, CREATE, REMOVE, RESPONSE, EXIT: ").lower()

        if p_state == "view":
            print("YOUR POSTS: ")
            cursor.execute(f"Select postID, postText from Posts where userID={profile.id}")
            posts = cursor.fetchall()

            for post in posts:
                info = replaceCursors(str(post)).split(",")
                print(f"ID: {info[0]}")
                print(f"TEXT: {info[1]}")
                cursor.execute(f"Select postImage from postImages where postID={info[0]}")
                images = cursor.fetchall()
                if len(images) > 0:
                    print("IMAGES:")
                    for image in images:
                        print(replaceCursors(str(image)).replace(",", ""))

                cursor.execute(f"Select postLink from postLinks where postID={info[0]}")
                links = cursor.fetchall()
                if len(links)>0:    
                    print("LINKS:")
                    for link in links:
                        print(replaceCursors(str(link)).replace(",", ""))

                print("------------------------------------------")

        elif p_state == "create":
            p_topic  = input("ENTER TOPIC TO POST TO: ").lower().replace(" ", "_")

            cursor.execute(f"Select topicID from Topics where topic='{p_topic}'")
            result = cursor.fetchone()

            if result == None:
                print("TOPIC NOT FOUND!")
            else:
                topicID = replaceCursors(str(result)).replace(",", "")
                createPost(profile, topicID)

        elif p_state == "response":
            p_response = input("ENTER POSTID TO RESPONSE TO: ").lower()
            
            if p_response.isdigit():
                cursor.execute(f"select postID, topicID, likes, dislikes from Posts where postID={p_response}")
                result = cursor.fetchone()
                
                if result == None:
                    print("NOT VALID POST ID")
                else:
                    postInfo = replaceCursors(str(result)).split(",")
                    responsePost(profile, postInfo[0], postInfo[1], postInfo[2],postInfo[3])    
            else:
                print("NOT VALID POST ID")

        elif p_state == "remove":
            p_remove = input("ENTER POST ID TO REMOVE: ")

            if p_remove.isdigit():
                cursor.execute(f"delete from postImages where postID={p_remove}")
                cursor.execute(f"delete from postLinks where postID={p_remove}")
                cursor.execute(f"delete from Posts where postID={p_remove} and userID={profile.id}")
                result = cursor.rowcount

                if result >= 1:
                    print("REMOVING POST")
                    db.commit()
                else:
                    print("NO POST EXISTS OR YOU DON'T HAVE ACCESS TO")

            else:
                print("NOT VALID!")

        elif p_state == "exit":
            return
        else:
            print("COMMAND NOT FOUND!")

def responsePost(profile, postID, topicID, likes, dislikes):
    vote = input("UP or DOWN or NONE: ").lower()
    if vote == "up":
        cursor.execute(f"update Posts set likes={int(likes)+1} where postID={postID}")
    elif vote == "down":
        cursor.execute(f"update Posts set dislikes={int(dislikes)+1} where postID={postID}")
    elif vote == 'none':
        print("NO VOTE")
    else:
        print("NOT VALID")           
    db.commit()

    while(True):
        response = input("RESPONSE TO POST, YES or NO: ").lower()

        if response == "yes":
            createPost(profile, topicID, postID)
            return
        elif response == "no":
            return
        else:
            print("INVALID COMMAND")

def createPost(profile, topicID, postID=0):
    post_text = input("TEXT: ")
    ts = calendar.timegm(time.gmtime())

    if postID == 0:
        cursor.execute(f"insert into Posts(userID, topicID, postText, likes, dislikes, timeStamp) values({profile.id}, {topicID}, '{post_text}', 0, 0, {ts})")
    else:
        cursor.execute(f"insert into Posts(userID, topicID, postText, likes, dislikes, responseTo, timeStamp) values({profile.id}, {topicID}, '{post_text}', 0, 0,{postID}, {ts})")
    
    cursor.execute("select max(postID) from Posts")
    result = cursor.fetchone()
    postID = replaceCursors(str(result)).replace(",", "")

    while(True):
        image = input("ENTER IMAGE OR STOP: ").lower()
        if image == "stop" or image.strip() == '':
            break
        cursor.execute(f"insert into postImages(postID, postImage) values({postID}, '{image}')")
    
    while(True):
        link = input("ENTER LINK OR STOP: ").lower()
        if link == "stop" or link.strip() == '':
            break
        print(link)
        cursor.execute(f"insert into postLinks(postID, postLink) values({postID}, '{link}')")
    
    db.commit()

def instructions():
    print("------COMMANDS-------")
    print("POST - MANAGE YOUR POSTS")
    print("CLUB - MANAGE YOUR CLUBS")
    print("TOPIC - MANAGE YOUR TOPICS")
    print("FRIENDS - MANAGE YOUR FRIENDS")
    print("LOGOUT - SIGN OUT")
    print("---------------------")

def loginFeed(profile):
    """"Generations login feed since last login"""
    print("FEED")
    posts = []

    cursor.execute(f"select userFOL from userFriends where userID={profile.id}")
    friends = cursor.fetchall()
    cursor.execute(f"select topicID from userTopic where userID={profile.id}")
    topics = cursor.fetchall()
    cursor.execute(f"select clubID from userClub where userID={profile.id}")
    clubs = cursor.fetchall()

    for friend in friends:
        friendID = replaceCursors(str(friend)).replace(",", "")
        cursor.execute(f"select * from Posts where userID={friendID} and timeStamp>{profile.lastLogin}")
        for post in cursor:
            print(post)

    for topic in topics:
        topicID = replaceCursors(str(topic)).replace(",", "")
        cursor.execute(f"select * from Posts where topicID={topicID} and timeStamp>{profile.lastLogin}")
        for topic in cursor:
            print(post)

def getProfile(user, password):
    """Gets the user profile"""
    users = []
    cursor.execute(f"SELECT userID, email, firstName, middleName, lastName, birthdate, age, occupation, timeStamp FROM Users where email='{user}' and password='{password}'")

    for result in cursor:
        users.append(result)
    
    if len(users) == 1:
        print("LOGIN...")
        return convertObject(users[0])
    
    print("INVALID EMAIL OR PASSWORD!")
    exit()

def replaceCursors(text):
    """HELPER FUNCTION: used for cursor object conversion"""
    return text.replace('(', '').replace(')', '').replace("'", "").replace(" ", "")

def convertObject(cursorObject):
    """HELPER FUNCTION: creates a person object"""
    sections = replaceCursors(str(cursorObject)).split(",")

    user = Person(
        sections[0],
        sections[1], 
        sections[2], 
        sections[3],
        sections[4],
        sections[5],
        sections[6],
        sections[7],
        sections[8]
    )

    return user

login()