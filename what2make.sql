# Julian Velez
# This is a database for my reverse recipe look-up "What to Make"

CREATE DATABASE what2make;

# Table for User data
CREATE TABLE Users (
    userID integer(255),
    fName varchar(255),
    lName varchar(255),
    password varchar(255),
    email varchar(255),
    PRIMARY KEY (userID)
);

# Table for Site data 
CREATE TABLE Sites (
    siteID integer(255),
    siteName varchar(255)
);

# Table for Recipe data
CREATE TABLE Recipes (
    recipeID integer(255),
    title varchar(255),
    siteID varchar(255),
    url varchar(255),
    PRIMARY KEY (recipeID),
    FOREIGN KEY (siteID) REFERENCES Sites(siteID)
);

# Table for types of ingredients
CREATE TABLE IngredientTypes (
    typeID integer(255),
    typeName varchar(255),
    PRIMARY KEY (typeID)
);

# Table for ingredients
CREATE TABLE Ingredients (
    ingID integer(255),
    ingName varchar(255),
    typeID integer(255),
    cost integer(1),
    PRIMARY KEY (ingID),
    FOREIGN KEY (typeID) REFERENCES IngredientTypes(typeID)
);

# Table linking Users to their saved Recipes
CREATE TABLE SavedRecipes (
    userID integer(255),
    recipeID integer(255),
    rating integer(1)
    PRIMARY KEY (userID, recipeID),
    FOREIGN KEY (userID) REFERENCES Users(userID),
    FOREIGN KEY (recipeID) REFERENCES Recipes(recipeID)
);

# Table linking recipes with the ingredients that they contain
CREATE TABLE RecipeIngredients (
    recipeID integer(255),
    ingID integer(255),
    PRIMARY KEY (recipeID, ingID),
    FOREIGN KEY (recipeID) REFERENCES Recipes(recipeID),
    FOREIGN KEY (ingID) REFERENCES Ingredients(ingID)
);

# Table linking Users with their blocked ingredients
CREATE TABLE BlockedIngredients(userID, ingID) (
    userID integer(255),
    ingID integer(255),
    PRIMARY KEY (userID, ingID),
    FOREIGN KEY (userID) REFERENCES Users(userID),
    FOREIGN KEY (ingID) REFERENCES Ingredients(ingID)
);
