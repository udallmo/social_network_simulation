-- insert users
insert Users values(1, 'umo@uwaterloo.ca', 'udall', NULL, 'mo', "01-01-1998", 22, 'student', 'pass123', 1);
insert Users values(2, 'ece356@uwaterloo.ca', 'derek', NULL, 'ray', "04-22-1999", 21, '', 'test', 1582512121);
insert Users values(3, 'mj@uwaterloo.ca', 'mary', NULL, 'jane', "12-01-1996", 24, "nurse",'ma21234', 1582517861);
insert Users values(4, 'drag24@uwaterloo.ca', 'draven', 'david', 'ragious', "02-01-1998", 22, 'manager', 'ddd123', 1582515820);
insert Users values(5, 'aab@uwaterloo.ca', 'aby', NULL, 'byles', "01-01-1998", 22, '', 'abab', 1582517861);
insert Users values(6, 'lemon@uwaterloo.ca', 'leena', NULL, 'mont', "01-03-1998", 22, 'student', 'lemon', 1581317861);

-- insert topics
insert into Topics values(1, 'canada');
insert into Topics values(2, 'us_politics');
insert into Topics values(3, 'technology');
insert into Topics values(4, 'music');
insert into Topics values(5, 'education');
insert into Topics values(6, 'health');
insert into Topics values(7, 'environment');
insert into Topics values(8, 'religion');

-- insert groups
insert into Clubs values(1, 'university_of_waterloo');
insert into Clubs values(2, 'toronto_jobs');
insert into Clubs values(3, 'motorcycle_society');
insert into Clubs values(4, 'waterloo_chem_club');
insert into Clubs values(5, 'subtle_curry_food');
insert into Clubs values(6, 'new_york_city_housing');

-- insert user to group
insert into userClub(userID, clubID) values(1, 1);
insert into userClub(userID, clubID) values(2, 1);
insert into userClub(userID, clubID) values(3, 1);
insert into userClub(userID, clubID) values(4, 1);
insert into userClub(userID, clubID) values(5, 1);
insert into userClub(userID, clubID) values(6, 1);
insert into userClub(userID, clubID) values(1, 2);
insert into userClub(userID, clubID) values(2, 2);
insert into userClub(userID, clubID) values(3, 2);
insert into userClub(userID, clubID) values(3, 3);
insert into userClub(userID, clubID) values(1, 6);
insert into userClub(userID, clubID) values(1, 5);
insert into userClub(userID, clubID) values(1, 4);
insert into userClub(userID, clubID) values(2, 3);

-- insert user to topics
insert into userTopic(userID, topicID) values(1, 2);
insert into userTopic(userID, topicID) values(1, 4);
insert into userTopic(userID, topicID) values(2, 2);
insert into userTopic(userID, topicID) values(3, 7);
insert into userTopic(userID, topicID) values(4, 6);
insert into userTopic(userID, topicID) values(5, 8);
insert into userTopic(userID, topicID) values(6, 1);
insert into userTopic(userID, topicID) values(1, 3);
insert into userTopic(userID, topicID) values(1, 5);
insert into userTopic(userID, topicID) values(2, 4);
insert into userTopic(userID, topicID) values(4, 2);
insert into userTopic(userID, topicID) values(1, 7);

-- insert user to friends
insert into userFriends(userID, userFOL) values(1, 2);
insert into userFriends(userID, userFOL) values(2, 3);
insert into userFriends(userID, userFOL) values(1, 3);
insert into userFriends(userID, userFOL) values(1, 4);
insert into userFriends(userID, userFOL) values(1, 5);
insert into userFriends(userID, userFOL) values(1, 6);
insert into userFriends(userID, userFOL) values(2, 5);
insert into userFriends(userID, userFOL) values(5, 6);
insert into userFriends(userID, userFOL) values(3, 4);
insert into userFriends(userID, userFOL) values(4, 2);
insert into userFriends(userID, userFOL) values(6, 2);
insert into userFriends(userID, userFOL) values(6, 3);
insert into userFriends(userID, userFOL) values(3, 1);
insert into userFriends(userID, userFOL) values(3, 6);

-- insert Posts
insert into Posts(postID, userID, topicID, postText, likes, dislikes, timeStamp) values(
    1,
    2, 
    5, 
    "Waterloo's School of Public Health & Health Systems professors are helping adapt health-response guidelines for lower-resource areas. ",
    30, 
    10, 
    1582817861
);
insert into Posts(postID, userID, topicID, postText, likes, dislikes, timeStamp) values(
    2,
    6, 
    5, 
    "A reminder: For those who need to pick up belongings, please do so before end of day on Friday. Read more from Waterloo Residences here:",
    10, 
    70, 
    1582817861
);
insert into Posts(postID, userID, topicID, postText, likes, dislikes, timeStamp) values(
    3,
    3, 
    2, 
    "Bernie Sanders ended his presidential campaign for the 2020 Democratic nomination",
    182, 
    10, 
    1582817861
);
insert into Posts(postID, userID, topicID, postText, likes, dislikes, timeStamp) values(
    4,
    2, 
    3, 
    "Technology is the sum of techniques, skills, methods, and processes used in the production of goods or services or in the accomplishment of objectives, such as scientific investigation.", 
    142, 
    50, 
    1582817861
);
insert into Posts(postID, userID, topicID, postText, likes, dislikes, timeStamp) values(
    5,
    3, 
    4, 
    "A little inspiration for your day.",
    142, 
    50, 
    1582817861
);
insert into Posts(postID, userID, topicID, postText, likes, dislikes, timeStamp) values(
    6,
    4, 
    6, 
    "Coronavirus disease (COVID-19) is an infectious disease caused by a new virus.",
    150, 
    5000, 
    1582817861
);
insert into Posts(postID, userID, topicID, postText, likes, dislikes, timeStamp) values(
    7,
    5, 
    1, 
    "Thank you to everyone who shared your images of rainbows! Rainbow Your messages of hope were echoed around the world. #StayStrong #Everythingwillbeokay",
    200, 
    30, 
    1582817861
);
insert into Posts(postID, userID, topicID, postText, likes, dislikes, timeStamp) values(
    8,
    1, 
    5, 
    "What began as words on a sticky note from a group of Waterloo Engineering students' fourth-year project, has now become a working prototype of a portable, low-cost #ventilator which could soon help save lives during the #COVID_19 crisis.", 
    142, 
    50, 
    1582817861
);

insert into postImages values(5, 'music_image.png');
insert into postImages values(7, 'help_image.png');
insert into postImages values(7, 'help1_image.png');
insert into postImages values(7, 'help2_image.png');

insert into postLinks values(8, 'https://bit.ly/2Xn0mWT');
insert  into postLinks values(1, 'https://bit.ly/2UW3sPP');