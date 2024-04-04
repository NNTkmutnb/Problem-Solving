import folium
import sqlite3

sqlfile = 'ETO_DB.db'

mapOjp = folium.Map(location=(14.160987545426053, 101.39271798051362), zoom_start= 13.5)


def get_latitude():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
        sqlite_select_query = """SELECT latitude 
                                FROM marker;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        latitude  = []
        for i in record:
            for n in i :
                latitude.append(n)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
            return (latitude)
         

latitude = get_latitude()
# print(latitude)


def get_longitude():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
        sqlite_select_query = """SELECT longitude 
                                FROM marker;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        longitude   = []
        for i in record:
            for n in i :
                longitude .append(n)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
            return (longitude )
         

longitude  = get_longitude()
# print(longitude)

def get_marker_color():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
        sqlite_select_query = """SELECT marker_color 
                                FROM marker;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        marker_color   = []
        for i in record:
            for n in i :
                marker_color.append(n)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
            return (marker_color )
         

marker_color = get_marker_color()

def get_marker_icon():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
        sqlite_select_query = """SELECT icon 
                                FROM marker;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        icon   = []
        for i in record:
            for n in i :
                icon.append(n)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
            return (icon )
         

marker_icon = get_marker_icon()

def get_marker_name():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
        sqlite_select_query = """SELECT marker_name 
                                FROM marker;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        marker_name  = []
        for i in record:
            for n in i :
                marker_name.append(n)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
            return (marker_name)
         

marker_name = get_marker_name()

def get_marker_image():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
        sqlite_select_query = """SELECT image 
                                FROM marker;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        image  = []
        for i in record:
            for n in i :
                image.append(n)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
            return (image)
         

marker_image = get_marker_image()
# print(marker_image)

def get_marker_discription():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
        sqlite_select_query = """SELECT discription 
                                FROM marker;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        discription = []
        for i in record:
            for n in i :
                discription.append(n)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
            return (discription)
         

marker_discription = get_marker_discription()

def get_marker_link():
    try:
        sqliteConnection = sqlite3.connect(sqlfile)
        cursor = sqliteConnection.cursor()
        # print("Connected to SQLite")
        sqlite_select_query = """SELECT link 
                                FROM marker;"""
        cursor.execute(sqlite_select_query)
        record = cursor.fetchall()
        link = []
        for i in record:
            for n in i :
                link.append(n)
    except sqlite3.Error as error:
        print("Failed to read single row from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            # print("The SQLite connection is closed")
            return (link)
        
marker_link = get_marker_link()


for name, lat, long, discrip, link, color, icon, img in zip(marker_name, latitude, longitude, marker_discription, marker_link, 
                                                            marker_color, marker_icon, marker_image):

    folium.Marker([lat, long],
    tooltip='Click me!', 
    popup=folium.Popup(f"""
                  <img src="{img}" alt="Bootstrap" style="max-width:100%;max-height:100%"><br/>     
                  <h4>{name}<br/></h4>
                  <h5>{discrip} <a href="{link}" target="_blank">คลิ๊กที่นี่</a></h5>
                  """, max_width=500), 
    icon=folium.Icon(icon=icon, color=color)).add_to(mapOjp)



mapOjp
mapOjp.save("index.html")
