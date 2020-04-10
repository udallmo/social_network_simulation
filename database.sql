DROP DATABASE if EXISTS social_network;
CREATE DATABASE IF NOT EXISTS social_network;
USE social_network;

-- Create the initial tables

-- User's Personal Information
DROP TABLE IF EXISTS Users;           
CREATE TABLE Users(
    userID INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(100) NOT NULL,
    firstName VARCHAR(100) NOT NULL,
    middleName VARCHAR(100),
    lastName VARCHAR(100) NOT NULL,
    birthdate VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    occupation VARCHAR(100),
    timeStamp INT, 
    password VARCHAR(100) NOT NULL,
    primary key (userID)
);    

insert into Users(email, firstName, lastName, birthdate, age, password, timeStamp) values('umo@uwaterloo.ca', 'udall', 'mo', '01-01-1998',12, 'test', 1582517861);
insert into Users(email, firstName, lastName, birthdate, age, password, timeStamp) values('lemon@uwaterloo.ca', 'lemone', 'sd', '01-01-1998',12, 'test', 1582517861);
insert into Users(email, firstName, lastName, birthdate, age, password, timeStamp) values('jake@uwaterloo.ca', 'jake', 'sd', '01-01-1998',12, 'test', 1582517861);

-- Topics
DROP TABLE IF EXISTS Topics;
CREATE TABLE Topics(
    topicID INT NOT NULL AUTO_INCREMENT,
    topic VARCHAR(100),
    primary key (topicID)
);

insert into Topics(topic) values('waterloo');
insert into Topics(topic) values('windsor');
insert into Topics(topic) values('canada');
insert into Topics(topic) values('detroit');


DROP TABLE IF EXISTS Clubs;
CREATE TABLE Clubs(
    clubID INT NOT NULL AUTO_INCREMENT,
    club VARCHAR(100),
    primary key (clubID)
);

insert into Clubs(club) values('crown');
insert into Clubs(club) values('wing');
insert into Clubs(club) values('dragon');
insert into Clubs(club) values('poop');

-- User Topic List
DROP TABLE IF EXISTS userClub;
CREATE TABLE userClub(
    userID INT NOT NULL,
    clubID INT NOT NULL,
    constraint fk_users_c foreign key (userID) references Users(userID),
    constraint fk_club foreign key (clubID) references Clubs(clubID)
);
insert into userClub(userID, clubID) values(1, 2);
insert into userClub(userID, clubID) values(1, 3);

-- User Topic List
DROP TABLE IF EXISTS userTopic;
CREATE TABLE userTopic(
    userID INT NOT NULL,
    topicID INT NOT NULL,
    constraint fk_users foreign key (userID) references Users(userID),
    constraint fk_topic foreign key (topicID) references Topics(topicID)
);

insert into userTopic(userID, topicID) values(1, 2);
insert into userTopic(userID, topicID) values(1, 4);

-- Friends
DROP TABLE IF EXISTS userFriends;
CREATE TABLE userFriends(
    userID INT NOT NULL,
    userFOL INT NULL NULL,
    constraint fk_userID foreign key (userID) references Users(userID),
    constraint fk_userFOL foreign key (userFOL) references Users(userID)
);

insert into userFriends(userID, userFOL) values(1, 2);
insert into userFriends(userID, userFOL) values(2, 3);

-- Posts
DROP TABLE IF EXISTS Posts;
CREATE TABLE Posts (
    postID INT NOT NULL AUTO_INCREMENT,
    userID INT NOT NULL,
    topicID INT NOT NULL,
    postText VARCHAR(100),
    likes INT,
    dislikes INT,
    responseTo INT,
    timeStamp INT, 
    primary key(postID),
    constraint fk_p_users foreign key (userID) references Users(userID),
    constraint fk_p_topic foreign key (topicID) references Topics(topicID),
    constraint fk_response foreign key (responseTo) references Posts(postID)
);

insert into Posts(userID, topicID, postText, likes, dislikes, timeStamp) values(1, 2, "words words wrods", 2, 1, 1582817861);
insert into Posts(userID, topicID, postText, likes, dislikes, timeStamp) values(1, 3, "words 2 wrods", 5, 1, 1582518861);
insert into Posts(userID, topicID, postText, likes, dislikes, timeStamp) values(2, 1, "words 3 wrods", 2, 3, 1582517891);

-- Images
DROP TABLE IF EXISTS postImages;
CREATE TABLE postImages(
    postID INT NOT NULL,
    postImage VARCHAR(100) NOT NULL,
    constraint fk_image foreign key (postID) references Posts(postID)
);

insert into postImages(postID, postImage) values(1, 3);
insert into postImages(postID, postImage) values(2, 523);
insert into postImages(postID, postImage) values(1, 2);

-- Links
DROP TABLE IF EXISTS postLinks;
CREATE TABLE postLinks(
    postID INT NOT NULL,
    postLink VARCHAR(100) NOT NULL,
    constraint fk_link foreign key (postID) references Posts(postID)
);

insert into postLinks(postID, postLink) values(1, 32);
insert into postLinks(postID, postLink) values(2, 5232);
insert into postLinks(postID, postLink) values(2, 22);
