# class definition
class Song:
   def __init__(self, performer, title, album, year):
      self.performer = performer
      self.title = title
      self.album = album
      self.year = year

   def __str__(self):
      result = f"Performer: {self.performer}\n"
      result += f"Title: {self.title}\n"
      result += f"Album: {self.album}\n"
      result += f"Year: {self.year}\n"
      return result

# object creation
song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", "2017")
song2 = Song("Queen", "Bohemian Rhapsody", "A Night at the Opera", "1975")

## object usage
print(song1)
print(song2)