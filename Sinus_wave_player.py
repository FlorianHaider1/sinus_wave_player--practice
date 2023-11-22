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

#Player
def play_tone(frequency, duration):
    p = pyaudio.PyAudio()
    volume = 0.5     # Bereich von 0.0 bis 1.0
    fs = 44100       # Sampling-Rate
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*frequency/fs)).astype(np.float32)
    stream = p.open(format=pyaudio.paFloat32, channels=1, rate=fs, output=True)
    stream.write(volume*samples)
    stream.stop_stream()
    stream.close()
    p.terminate()

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
    
    return key_board.get(tone)

def bpm_to_modifier(bpm):
    if bpm == 60:
        bpm_mod = 1
        return bpm_mod
    if bpm == 90:
        bpm_mod = 0.75
        return bpm_mod
    if bpm == 120:
        bpm_mod = 0.5
        return bpm_mod
    if bpm == 150:
        bpm_mod = 0.25
        return bpm_mod

def note_value_to_duration(note_value, bpm):
    duration = (1/note_value)*bpm_to_modifier(bpm)
    return duration 

war_ensemble_intro = [
    ("G5", 16), ("F5", 16), ("E5", 16), ("E5", 16),("E5", 16), ("E5", 16),
    ("G5", 16), ("F5", 16), ("E5", 16), ("E5", 16),("E5", 16), ("E5", 16),
    ("G5", 16), ("F5", 16), ("E5", 16), ("E5", 16),("E5", 16), ("E5", 16),
]

katyusha = [
    ("E4", 4), ("F#4", 4), ("G4", 4), ("F#4", 4), 
    ("E4", 4), ("D4", 4), ("E4", 2), ("P", 2), 
    ("E4", 4), ("F#4", 4), ("G4", 4), ("F#4", 4), 
    ("E4", 4), ("D4", 4), ("C#4", 2), ("P", 2), 
    ("D4", 4), ("E4", 4), ("F#4", 4), ("E4", 4), 
    ("D4", 4), ("C#4", 4), ("B3", 2), ("P", 2), 
    ("A3", 4), ("B3", 4), ("C#4", 4), ("D4", 4),
    ("E4", 4), ("C#4", 4), ("A3", 2), ("P", 2)
]

korobeiniki = [
    ("E5", 1), ("B4", 2), ("C5", 2), ("D5", 1), ("C5", 2), ("B4", 2), ("A4", 1), ("A4", 2),("C5", 2), ("E5", 1), 
    ("D5", 2), ("C5", 2), ("B4", 1), ("B4", 2), ("C5", 2), ("D5", 1), ("E5", 1), ("C5", 1), ("A4", 2), ("A4", 0.5), 
    ("P",4), ("D5", 2), ("F5", 2), ("A5", 0.5), ("G5", 1), ("F5", 1), ("E5", 1), ("P",4),("C5", 2), ("E5", 0.5), 
    ("D5",2), ("C5", 2), ("B4",1),("B4", 2), ("C5", 1), ("D5", 1), ("E5", 1), ("C5", 1),("A4", 1), ("A4", 0.5)  
    ]

hobbit = [
    ("C4", 2), ("D4", 2), ("E4", 0.75), ("G4", 2), 
    ("E4", 0.75), ("D4", 2), ("C4", 0.75), ("G4", 2), 
    ("E4", 2), ("C4", 2), ("D4", 4), ("P", 4), 
    ("C4", 2), ("D4", 2), ("E4", 0.75), ("G4", 2), 
    ("E4", 0.75), ("D4", 2), ("C4", 0.75), ("G4", 2), 
    ("E4", 2), ("C4", 2), ("D4", 4), ("P", 4)
]

bpm = 120
times = 5
current = 0

song = korobeiniki

while current < times:
    for note, note_value in song:
        freq = frequency_to_tone(note)
        duration = note_value_to_duration(note_value, bpm)
        print(f"Tone {note} with time {note_value}")
        play_tone(freq, duration)  
    current += 1
