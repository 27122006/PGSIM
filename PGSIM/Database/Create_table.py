import mysql.connector
import configparser


config = configparser.ConfigParser()
config.read('config.ini')

def create_information_table():
    connect = mysql.connector.connect(
    host=config['database']['host'],
    user=config['database']['user'],
    password=config['database']['password'],
    database=config['database']['database']
)
    cursor = connect.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS information (
            `Citizen ref` INT NOT NULL AUTO_INCREMENT,
            `Citizen Name` VARCHAR(255) NOT NULL,
            `Citizen ID` VARCHAR(255) NOT NULL,
            `DOB` DATE NOT NULL,
            `Gender` VARCHAR(10) NOT NULL,
            `Address` VARCHAR(255) NOT NULL,
            `Marriage Status` VARCHAR(255) NOT NULL,
            `Status` VARCHAR(255) NOT NULL,
            PRIMARY KEY (`Citizen ID`)
        )
    """)
    connect.commit()
    cursor.close()
    connect.close()

def create_marriage_table():
    connect = mysql.connector.connect(
    host=config['database']['host'],
    user=config['database']['user'],
    password=config['database']['password'],
    database=config['database']['database']
)
    cursor = connect.cursor()
    cursor.execute("""
        Citizen1_ID` INT(10),
        `Citizen2_ID` INT(10),
        `Date` DATE,
        FOREIGN KEY (`Citizen1_ID`) REFERENCES `information`(`Citizen ID`),
        FOREIGN KEY (`Citizen2_ID`) REFERENCES `information`(`Citizen ID`)
    )
""")

def create_death_table():
    connect = mysql.connector.connect(
    host=config['database']['host'],
    user=config['database']['user'],
    password=config['database']['password'],
    database=config['database']['database']
)
    cursor = connect.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS death (
        `Citizen_ID` INT(10),
        `Date of Death` DATE,
        `Place of Death` VARCHAR(100),
        `Cause of Death` VARCHAR(100),
        FOREIGN KEY (`Citizen_ID`) REFERENCES `information`(`Citizen ID`)
    )
""")
    connect.commit()
    cursor.close()
    connect.close()

def create_birth_table():
    connect = mysql.connector.connect(
    host=config['database']['host'],
    user=config['database']['user'],
    password=config['database']['password'],
    database=config['database']['database']
)
    cursor = connect.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS birth (
        `Name` VARCHAR(50),
        `ID` INT(10) PRIMARY KEY,
        `Father Name` VARCHAR(50),
        `Mother Name` VARCHAR(50),
        `Date of Birth` DATE,
        `Place of Birth` VARCHAR(100),
        `Gender` ENUM('M', 'F')
    )
""")
    connect.commit()
    cursor.close()
    connect.close()
