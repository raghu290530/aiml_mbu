class Playlist:
  def __init__(self, name):
    self.name = name
    self.songs = []

  def add_song(self, song):
    self.songs.append(song)
    print(f"Added: {song}")

  def remove_song(self, song):
    if song in self.songs:
      self.songs.remove(song)
      print(f"Removed: {song}")

  def show_songs(self):
    print(f"Playlist '{self.name}':")
    for song in self.songs:
      print(f"- {song}")

my_playlist = Playlist("Favorites")
while True:
    m = int(input("Enter 1-add\n2-remove\n3-playlist\n0-Exit"))
    match m:
        case 1 : my_playlist.add_song(input("Enter Song:"))
        case 2 : my_playlist.remove_song(input("Enter Song:"))
        case 3 : my_playlist.show_songs()
        case 0 : break
