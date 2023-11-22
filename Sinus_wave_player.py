# Music Player using sound card to play simple melodys.
# Practice oop
# Features:
# - Notes insertable by calling it its 'natural' name, so C,C#, Db, E, etc.
# - adding octave: 1, 2, 3
# - adding length of notes by adding a Number, i.e. 16, 8, 4, 2, 1
# - adding pauses: P
# - Notes then saved in tuples, (C2,8)(P,1)(Eb2,8) for (C2 Eightnote), (Full Pause), (Eb2 Eightnote) 
# - Radiobutton for 60, 90, 120, 150 bpm, changing the length of notes accordingly

import pyaudio
import numpy as np

class Player:
    def __init__(self):
        self.pyaudio_instance = pyaudio.PyAudio()


    def play_tone(self, frequency, duration):
        volume = 0.8     # Bereich von 0.0 bis 1.0
        fs = 44100       # Sampling-Rate
        samples = (np.sin(2*np.pi*np.arange(fs*duration)*frequency/fs)).astype(np.float32)
        stream = self.pyaudio_instance.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
        stream.write(volume*samples)
        stream.stop_stream()
        stream.close()
    
    def audio_terminate(self):
        self.pyaudio_instance.terminate()


class Note: 
    def __init__(self, note, duration):
        self.note = note
        self.duration = duration

    @staticmethod
    def frequency_to_tone(tone):
        key_board = {
            "C3": 130.81,
            "C#3": 138.59, "Db3": 138.59,
            "D3": 146.83,
            "D#3": 155.56, "Eb3": 155.56,
            "E3": 164.81,
            "F3": 174.61,
            "F#3": 185.00, "Gb3": 185.00,
            "G3": 196.00,
            "G#3": 207.65, "Ab3": 207.65,
            "A3": 220.00,
            "A#3": 233.08, "Bb3": 233.08,
            "B3": 246.94,
            "C4": 261.63,
            "C#4": 277.18, "Db4": 277.18,
            "D4": 293.66,
            "D#4": 311.13, "Eb4": 311.13,
            "E4": 329.63,
            "F4": 349.23,
            "F#4": 369.99, "Gb4": 369.99,
            "G4": 392.00,
            "G#4": 415.30, "Ab4": 415.30,
            "A4": 440.00,
            "A#4": 466.16, "Bb4": 466.16,
            "B4": 493.88,
            "C5": 523.25,
            "C#5": 554.37, "Db5": 554.37,
            "D5": 587.33,
            "D#5": 622.25, "Eb5": 622.25,
            "E5": 659.26,
            "F5": 698.46,
            "F#5": 739.99, "Gb5": 739.99,
            "G5": 783.99,
            "G#5": 830.61, "Ab5": 830.61,
            "A5": 880.00,
            "A#5": 932.33, "Bb5": 932.33,
            "B5": 987.77,
            "P": 0
        }
        
        return key_board.get(tone, 0)

class Song:
    def __init__(self, notes, bpm):
        self.notes = [Note(note,value) for note, value in notes]
        self.bpm = bpm

    def play(self, player):
        for note in self.notes:
            freq = Note.frequency_to_tone(note.note)
            duration = self.note_value_to_duration(note.duration)
            print(f"Tone {note.note} with time {note.duration}")
            player.play_tone(freq, duration)

    def bpm_to_modifier(self):
        bpm_modifiers = {60: 1, 90: 0.75, 120: 0.5, 150: 0.25}
        return bpm_modifiers.get(self.bpm, 1)

    def note_value_to_duration(self, note_value):
        return (1/note_value)*5*self.bpm_to_modifier()

class Song_collection:

        war_ensemble_intro = [
            ("G5", 16), ("F5", 16), ("E5", 16), ("E5", 16),("E5", 16), ("E5", 16),
            ("G5", 16), ("F5", 16), ("E5", 16), ("E5", 16),("E5", 16), ("E5", 16),
            ("G5", 16), ("F5", 16), ("E5", 16), ("E5", 16),("E5", 16), ("E5", 16),
        ]

        katyusha = [
            ("A4", 3), ("B4", 8), ("C5", 3), ("A4", 8), ("C5", 8), ("C5", 8), ("B4", 8), ("A4", 8), ("B4", 2), ("E4", 2), 
            ("B4", 3), ("C5", 8), ("D5", 3), ("B4", 8), ("D5", 8), ("D5", 8), ("C5", 8), ("B4", 8), ("A4", 2), ("P",4),
            ("E5", 4), ("A5", 4), ("G5", 4), ("A5", 8), ("G5", 8), ("F5", 8), ("F5", 8), ("E5", 4), ("D5", 4),("E5", 4),("A4",2),
            ("P", 8), ("F5", 8), ("P", 8), ("D5", 8), ("E5", 3), ("C5", 8), ("D5",8),("D5",8),("C5",8),("B4",8),("A4",2),
            ("E5", 4), ("A5", 4), ("G5", 4), ("A5", 8), ("G5", 8), ("F5", 8), ("F5", 8), ("E5", 4), ("D5", 4),("E5", 4),("A4",2),
            ("P", 8), ("F5", 8), ("P", 8), ("D5", 8), ("E5", 3), ("C5", 8), ("D5",8),("D5",8),("C5",8),("B4",8),("A4",2)  
        ]

        korobeiniki = [
            ("E5", 1), ("B4", 2), ("C5", 2), ("D5", 1), ("C5", 2), ("B4", 2), ("A4", 1), ("A4", 2),("C5", 2), ("E5", 1), 
            ("D5", 2), ("C5", 2), ("B4", 1), ("B4", 2), ("C5", 2), ("D5", 1), ("E5", 1), ("C5", 1), ("A4", 1), ("A4", 0.75), 
            ("P",2), ("D5", 2), ("F5", 2), ("A5", 0.75), ("G5", 2), ("F5", 2), ("E5", 2), ("P",4),("C5", 2), ("E5", 0.75), 
            ("D5",2), ("C5", 2), ("B4",1),("B4", 2), ("C5", 1), ("D5", 1), ("E5", 1), ("C5", 1),("A4", 1), ("A4", 0.5)  
            ]

        the_shire = [
            ("D4", 6), ("E4", 6), ("F#4", 2), ("A4", 2),("F#4", 2), ("E4", 2), ("D4", 1),
            ("P", 2),("F#4", 5), ("A4", 5), ("B4", 0.9), ("D5", 3),("C#5", 3), ("A4", 2), 
            ("F#4", 2), ("P",6), ("G4", 5), ("F#4", 5),("E4", 3),("P",4)
        ]

song_1 = Song(Song_collection.korobeiniki, 150)
song_2 = Song(Song_collection.the_shire, 90)
song_3 = Song(Song_collection.katyusha, 90)
song_4 = Song(Song_collection.war_ensemble_intro, 150)

player = Player()

def playback(song, times):
    x = 1
    while x <= times:
        song.play(player)
        x += 1
    player.audio.terminate()

playback(song_3, 1)
