import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')


def list_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if not rows:
            print("No videos found in the database.")
    else:
        print("~" * 70)
        for idx, (video_id, name, time) in enumerate(rows, start=1):
            print(f"{idx}. {name}, Duration: {time}")
        print("~" * 70)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    conn.commit()

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. exit app")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_videos()
            case '2':
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                add_video(name, time)
            case '3':
                list_videos()
                video_id = input("Enter video ID to update: ")
                name = input("Enter the video name: ")
                time = input("Enter the video time: ")
                update_video(video_id, name, time)
            case '4':
                list_videos()
                video_id = input("Enter video ID to delete: ")
                delete_video(video_id)
            case '5':
                break
            case _:
                print("Invalid Choice")

    conn.close()

if __name__ == "__main__":
    main()