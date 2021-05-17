import notes.note as model


class Actions:
    def create(self, user):
        print(f"Ok. {user[1]} !! Let's go to create new note")
        title = input("Introduce the note title: ")
        description = input("Introduce the content of your note:")

        note = model.Note (user[0], title, description)
        tosave = note.tosave()

        if tosave[0] >= 1:
            print(f"\nPerfect. You have saved the note: {note.title}")
        else:
            print(f"\nSorry. I couldn't be possible to create the note")

    def show(self, user):
        print(f"\nOk. {user[1]}!! Here you have your notes: ")

        note = model.Note(user[0])
        notes = note.tolist()

        for note in notes:
            print("\n**********************")
            print(f"Title: {note[2]}")
            print(f"Description: {note[3]}")
            print("\n**********************")

    def delete(self, user):
        print(f"\n Okey {user[1]}!! Let's delete notes")

        title= input("\nIntroduce the title of the note you want to delete: ")
        note = model.Note(user[0], title)
        delete = note.todelete()

        if delete[0] >=1:
            print (f"\nWe have delete the note: {note.title}")
        else:
            print (f"\nIt wasn't possible to delete the note. Try later")