# Julian Velez
# This is a database for my reverse recipe look-up "What to Make"

CREATE DATABASE what2make;

# Table for User data
CREATE TABLE Users (
    userID varchar(255),
    fName varchar(255),
    lName varchar(255),
    password varchar(255),
    email varchar(255),
    PRIMARY KEY (userID)
);

# Table for Site data 
CREATE TABLE Sites (
    siteID varchar(255),
    siteName varchar(255)
);

# Table for Recipe data
CREATE TABLE Recipes (
    recipeID varchar(255),
    title varchar(255),
    siteID varchar(255),
    url varchar(255),
    PRIMARY KEY (recipeID),
    FOREIGN KEY (siteID) REFERENCES Sites(siteID)
);

# Table linking Users to their saved Recipes
CREATE TABLE UserSavedRecipes (
    userID varchar(255),
    recipeID varchar(255),
    rating integer(1)
    PRIMARY KEY (userID, recipeID),
    FOREIGN KEY (userID) REFERENCES Users(userID),
    FOREIGN KEY (recipeID) REFERENCES Recipes(recipeID)
);

