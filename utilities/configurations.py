import configparser
import mysql.connector

# accessing base url from url_properties.ini file
def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/url_properties.ini')
    return config


# for DB connection
connection_details = {
    'host': getConfig()['SQL']['host'],
    'database': getConfig()['SQL']['database'],
    'user': getConfig()['SQL']['user'],
    'password': getConfig()['SQL']['password']
}

def get_db_connection():
    try:
        # ** is given to tell its dict
        connection_from_config = mysql.connector.connect(**connection_details)
        if connection_from_config.is_connected():
            print("connection successful")
            return connection_from_config
    except mysql.connector.Error as e:
        print(f"connection failed: {e}")

def get_data_for_addBook(query):
    conn = get_db_connection()
    cursor_obj = conn.cursor()
    cursor_obj.execute(query)
    row_data = cursor_obj.fetchone()
    print(f"add book::::::::::::: {row_data}")
    return row_data
