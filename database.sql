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
    password VARCHAR(100) NOT NULL,
    timeStamp INT, 
    primary key (userID)
);    

-- Topics
DROP TABLE IF EXISTS Topics;
CREATE TABLE Topics(
    topicID INT NOT NULL AUTO_INCREMENT,
    topic VARCHAR(100),
    primary key (topicID)
);

DROP TABLE IF EXISTS Clubs;
CREATE TABLE Clubs(
    clubID INT NOT NULL AUTO_INCREMENT,
    club VARCHAR(100),
    primary key (clubID)
);

-- User Topic List
DROP TABLE IF EXISTS userClub;
CREATE TABLE userClub(
    userID INT NOT NULL,
    clubID INT NOT NULL,
    constraint fk_users_c foreign key (userID) references Users(userID),
    constraint fk_club foreign key (clubID) references Clubs(clubID)
);
-- insert into userClub(userID, clubID) values(1, 2);
-- insert into userClub(userID, clubID) values(1, 3);

-- User Topic List
DROP TABLE IF EXISTS userTopic;
CREATE TABLE userTopic(
    userID INT NOT NULL,
    topicID INT NOT NULL,
    constraint fk_users foreign key (userID) references Users(userID),
    constraint fk_topic foreign key (topicID) references Topics(topicID)
);

-- Friends
DROP TABLE IF EXISTS userFriends;
CREATE TABLE userFriends(
    userID INT NOT NULL,
    userFOL INT NULL NULL,
    constraint fk_userID foreign key (userID) references Users(userID),
    constraint fk_userFOL foreign key (userFOL) references Users(userID)
);

-- Posts
DROP TABLE IF EXISTS Posts;
CREATE TABLE Posts (
    postID INT NOT NULL AUTO_INCREMENT,
    userID INT NOT NULL,
    topicID INT NOT NULL,
    postText VARCHAR(1000),
    likes INT,
    dislikes INT,
    responseTo INT,
    timeStamp INT, 
    primary key(postID),
    constraint fk_p_users foreign key (userID) references Users(userID),
    constraint fk_p_topic foreign key (topicID) references Topics(topicID),
    constraint fk_response foreign key (responseTo) references Posts(postID)
);

-- Images
DROP TABLE IF EXISTS postImages;
CREATE TABLE postImages(
    postID INT NOT NULL,
    postImage VARCHAR(100) NOT NULL,
    constraint fk_image foreign key (postID) references Posts(postID)
);

-- Links
DROP TABLE IF EXISTS postLinks;
CREATE TABLE postLinks(
    postID INT NOT NULL,
    postLink VARCHAR(100) NOT NULL,
    constraint fk_link foreign key (postID) references Posts(postID)
);
