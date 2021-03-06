DROP TABLE IF EXISTS `Categories`;
DROP TABLE IF EXISTS `Tags`;
DROP TABLE IF EXISTS `Reactions`;
DROP TABLE IF EXISTS `PostReactions`;
DROP TABLE IF EXISTS `Posts`;
DROP TABLE IF EXISTS `PostTags`;
DROP TABLE IF EXISTS `Comments`;
DROP TABLE IF EXISTS `Subscriptions`;
DROP TABLE IF EXISTS `DemotionQueue`;
DROP TABLE IF EXISTS `Users`;
DROP TABLE IF EXISTS `AccountTypes`;
CREATE TABLE "AccountTypes" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);
CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "password" varchar,
  "bio" varchar,
  "username" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit,
  "account_type_id" INTEGER,
  FOREIGN KEY(`account_type_id`) REFERENCES `AccountTypes`(`id`)
);
CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);
CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit
);
CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  "subject" varchar,
  "created_on" DATETIME,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);
CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);
CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);
CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);
CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);
CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);
INSERT INTO Categories ('label')
VALUES ('News');
INSERT INTO Categories ('label')
VALUES ('Opinion');
INSERT INTO Categories ('label')
VALUES ('How-To');
INSERT INTO Categories ('label')
VALUES ('Editorial');
INSERT INTO Categories ('label')
VALUES ("Here's something dumb");
INSERT INTO Tags ('label')
VALUES ('JavaScript');
INSERT INTO Tags ('label')
VALUES ('React');
INSERT INTO Tags ('label')
VALUES ('Angular');
INSERT INTO Tags ('label')
VALUES ('Vue');
INSERT INTO Tags ('label')
VALUES ('Node');
INSERT INTO Tags ('label')
VALUES ('C#');
INSERT INTO Tags ('label')
VALUES ('.NET');
INSERT INTO Tags ('label')
VALUES ('Python');
INSERT INTO Tags ('label')
VALUES ('Data Science');
INSERT INTO Tags ('label')
VALUES ('Django');
INSERT INTO Tags ('label')
VALUES ('Flask');
INSERT INTO Tags ('label')
VALUES ('Open Source');
INSERT INTO Tags ('label')
VALUES ('Check this out!');
INSERT INTO Tags ('label')
VALUES ('Beginners');
INSERT INTO Tags ('label')
VALUES ('Weird');
INSERT INTO Tags ('label')
VALUES ('Ugh');
INSERT INTO Tags ('label')
VALUES ('Cool!');
INSERT INTO Tags ('label')
VALUES ('Why tho?');
INSERT INTO Tags ('label')
VALUES ('C#');
INSERT INTO Tags ('label')
VALUES ('.NET');
INSERT INTO Tags ('label')
VALUES ('Rust');
INSERT INTO Tags ('label')
VALUES ('Ruby');
INSERT INTO Tags ('label')
VALUES ('Rails');
INSERT INTO Tags ('label')
VALUES ('Go');
INSERT INTO Tags ('label')
VALUES ('C++');
INSERT INTO Tags ('label')
VALUES ('History Lesson');
INSERT INTO Reactions ('label', 'image_url')
VALUES ('happy', 'https://pngtree.com/so/happy');
INSERT INTO Reactions ('label', 'image_url')
VALUES (
    'heart',
    'https://lh3.googleusercontent.com/proxy/BlwtWdiO1ucoroiKKuJN5CpiAUFA4tdHYRT_yXzxWLpNVTJS7UEVp1JV-lYshjAPeS7wd1pqXk6mpxY6rrSAPXD5NbBoE9hTf-1PpzofQbzNyH__1miggtO2IQKktovnAyPzjCW6T9mQG6JvgdHklZUaMd-YnIxeBPuP1lBw2E7fp9d6AR68'
  );
INSERT INTO AccountTypes ('label')
VALUES ('Admin');
INSERT INTO AccountTypes ('label')
VALUES ('Author');
INSERT INTO Posts (
    "user_id",
    "category_id",
    "title",
    "publication_date",
    "image_url",
    "content",
    "approved"
  )
VALUES (
    1,
    1,
    "WonderDog",
    1471300214792,
    "https://wonderdogtraining.com/wp-content/uploads/2020/09/wonderdog-circle-logo-09.png",
    "Wonder dog is a dog. He's wonderful.",
    1
  );
INSERT INTO Posts (
    'user_id',
    'category_id',
    'title',
    'publication_date',
    'image_url',
    'content',
    'approved'
  )
VALUES (
    2,
    1,
    "american fighting",
    134235634622,
    "https",
    "the great battle",
    1
  );
INSERT INTO Posts (
    'user_id',
    'category_id',
    'title',
    'publication_date',
    'image_url',
    'content',
    'approved'
  )
VALUES (
    3,
    2,
    "The American Dream v2",
    134235634640,
    "https//",
    "We all want the Amereican dream but what exactly is that?",
    1
  );
DROP TABLE IF EXISTS `Users`;
SELECT *
FROM Posts;
INSERT INTO Users (
    'first_name',
    'last_name',
    'email',
    'password',
    'bio',
    'username',
    'profile_image_url',
    'created_on',
    'active',
    'account_type_id'
  )
VALUES (
    "Patrick",
    "Stewart",
    "not@real.email",
    "password",
    "I'm not a nice person",
    "patrick",
    "http://",
    "1598458543321",
    1,
    2
  );

SELECT
  p.id,
  p.user_id,
  p.category_id,
  p.title,
  p.publication_date,
  p.image_url,
  p.content,
  p.approved,
  u.id,
  u.first_name,
  u.last_name,
  u.email,
  u.password,
  u.bio,
  u.username,
  u.profile_image_url,
  u.created_on,
  u.active,
  u.account_type_id,
  c.label
FROM posts p
JOIN users u
    ON u.id = p.user_id
JOIN categories c
    ON c.id = p.category_id