from midiutil import MIDIFile
import random
try:
    from src import generateChordProgression  # when run via app.py from the project root
except ImportError:
    import generateChordProgression  # when run directly from src/

FINAL_OUTPUT = "final_merged_output.mid"
import mido

def merge_midi(file1, file2, output_file):
    # Load both MIDI files
    midi1 = mido.MidiFile(file1)
    midi2 = mido.MidiFile(file2)

    # Create a new MIDI file for the merged output
    merged_midi = mido.MidiFile()

    # Copy tracks from both MIDI files
    for track in midi1.tracks:
        merged_midi.tracks.append(track.copy())

    for track in midi2.tracks:
        merged_midi.tracks.append(track.copy())

    # Save the merged MIDI file
    merged_midi.save(output_file)
    print(f"Merged MIDI saved as {output_file}")


def randomFloat():
    return random.randint(1, 101) / 101

def playChord(midi, track, channel, pitches, time, duration, strum):
    currentNote = 1
    for p in pitches:
        #ADDING CHORD EXTENSIONS FOR MORE COMPLEXITY
        if (currentNote > 3):
            extensionChance = randomFloat()
            seventhChance = 0.7
            ninthChance = 0.3
            if (currentNote == 4 and extensionChance < seventhChance):
                midi.addNote(track, channel, p, time + strum * (currentNote - 1), max(duration - strum * (currentNote - 1), 0.05), 75)
                pass
            elif (currentNote == 5 and extensionChance < ninthChance):
                midi.addNote(track, channel, p, time + strum * (currentNote - 1), max(duration - strum * (currentNote - 1), 0.05), 70)
                pass
            else:
                pass
        else:
            pass
            midi.addNote(track, channel, p, time + strum * (currentNote - 1), max(duration - strum * (currentNote - 1), 0.05), 80)
        currentNote += 1

def playBass(midi, track, channel, pitch, time, duration, melody):
    if melody == 0:
        midi.addNote(track, channel, pitch - 24, time - 0.25, duration, 127)
        midi.addNote(track, channel, pitch - 24, time + 0.25, duration, 87)
        midi.addNote(track, channel, pitch - 24, time + 0.75, duration, 127)
        midi.addNote(track, channel, pitch - 24, time + 1.25, duration, 87)
        midi.addNote(track, channel, pitch - 24, time + 1.75, duration, 127)
        midi.addNote(track, channel, pitch - 24, time + 2.00, duration, 87)
    elif melody == 1:
        midi.addNote(track, channel, pitch - 24, time - 0, duration, 110)
        midi.addNote(track, channel, pitch - 24, time + 0.5, duration, 110)
        midi.addNote(track, channel, pitch - 24, time + 1, duration, 110)
        midi.addNote(track, channel, pitch - 24, time + 1.5, duration, 110)
        midi.addNote(track, channel, pitch - 24, time + 2, duration, 110)
    elif melody == 2:
        midi.addNote(track, channel, pitch - 24, time - 0, duration, 110)
        midi.addNote(track, channel, pitch - 24, time + 0.5, duration, 110)
        midi.addNote(track, channel, pitch - 12, time + 1, duration, 110)
        midi.addNote(track, channel, pitch - 23, time + 1.5, duration, 110)
        midi.addNote(track, channel, pitch - 23, time + 2, duration, 110)
    

def playLead(midi, track, channel, pitches, time, duration, melody):

    if melody == 0:
        midi.addNote(track, channel, pitches[0], time - 0.33, duration / 3, 100)
        midi.addNote(track, channel, pitches[2], time + 0.33, duration / 3, 87)
        midi.addNote(track, channel, pitches[3], time + 0.66, duration / 3, 127)
        midi.addNote(track, channel, pitches[2], time + 1, duration / 3, 87)
        midi.addNote(track, channel, pitches[3], time + 1.33, duration / 3, 127)
        midi.addNote(track, channel, pitches[1], time + 1.66, duration / 3, 87)
    elif melody == 1:
        midi.addNote(track, channel, pitches[0], time - 0.25, duration / 2, 100)
        midi.addNote(track, channel, pitches[1], time + 0.25, duration / 2, 87)
        midi.addNote(track, channel, pitches[3], time + 1, duration, 127)
        midi.addNote(track, channel, pitches[0], time + 1.5, duration / 2, 87)
        midi.addNote(track, channel, pitches[1], time + 1.75, duration / 2, 127)
        midi.addNote(track, channel, pitches[3], time + 2.00, duration / 2, 87)
    elif melody == 2:
        midi.addNote(track, channel, pitches[0], time - 0.25, duration / 2, 0)
        midi.addNote(track, channel, pitches[1], time + 0.25, duration / 2, 87)
        midi.addNote(track, channel, pitches[3], time + 1, duration, 127)
        midi.addNote(track, channel, pitches[0], time + 1.125, duration / 2, 87)
        midi.addNote(track, channel, pitches[1], time + 1.25, duration / 2, 0)
        midi.addNote(track, channel, pitches[2], time + 1.75, duration / 2, 87)

    elif melody == 3:
        midi.addNote(track, channel, pitches[3], time - 0.25, duration / 2, 87)
        midi.addNote(track, channel, pitches[2], time + 0.25, duration / 2, 70)
        midi.addNote(track, channel, pitches[1], time + 1, duration, 60)
        midi.addNote(track, channel, pitches[0], time + 1.5, duration / 2, 120)
        midi.addNote(track, channel, pitches[2], time + 1.625, duration / 2, 87)
        midi.addNote(track, channel, pitches[0], time + 1.75, duration / 2, 95)







def main(inputTempo, mood, jazziness, zaniness, chord, bass, lead, play=True):
    #SYNTH IS BEING PLAYED ON CHANNEL AND TRACK 0
    #BASS IS BEING PLAYED ON TRACK

    tempoOptions = {"Very Slow": [80, 100],
                    "Slow": [100, 125],
                    "Moderate": [125, 150],
                    "Fast": [150, 180],
                    "Very Fast": [180, 210]}

    tempo = random.randint(tempoOptions[inputTempo][0], tempoOptions[inputTempo][1])


    # Create a MIDI file with two tracks
    midi = MIDIFile(4, deinterleave=False)
    midi.addTempo(0, 0, tempo)  # Track 0, time 0, 120 BPM
    midi.addProgramChange(0, 1, 0, chord)
    #midi.addProgramChange(0, 1, 0, 37)
    keyRootsToPitch = {"C" : 49,
                       "Db" : 50,
                       "D" : 51,
                       "Eb" : 52,
                       "F" : 53,
                       "Gb" : 54,
                       "G" : 55,
                       "Ab" : 56,
                       "A" : 57,
                       "Bb" : 58,
                       "Bb" : 59}



    gmShifts = {
        "Happy" : 0,
        "Cool" : 1,
        "Dark" : 2,
        "Dreamy" : 3,
        "Funky" : 4,
        "Sad" : 5,
        "Tense" : 6
    }


    #SONG INFORMATION
    key = random.randint(43,53)
    root = key
    zanyChance = 1 - zaniness
    greekMode = gmShifts[mood]
    beat = generateChordProgression.createChordBeat(mood)
    print("BEAT: " + str(beat))

    happyScaleDegrees = [[root, root + 4, root + 7, root + 11, root + 14], #1 TONIC
                        [root + 2, root + 5, root + 9, root + 12, root + 16], #2 SUPERTONIC
                        [root + 4, root + 7, root + 11, root + 14, root + 17], #3 MEDIANT
                        [root + 5, root + 9, root + 12, root + 16, root + 19], #4 SUBDOMINANT
                        [root + 7, root + 11, root + 14, root + 17, root + 21], #5 DOMINANT
                        [root + 9, root + 12, root + 16, root + 19, root + 23], #6 SUBMEDIANT
                        [root + 11, root + 14, root + 17, root + 21, root + 24]] #7 LEADING TONE

    zanyScaleDegrees = [[root, root + 4, root + 7, root + 11, root + 14], #1 TONIC
                        [root + 2, root + 5, root + 8, root + 12, root + 16], #2 SUPERTONIC
                        [root + 4, root + 6, root + 11, root + 13, root + 17], #3 MEDIANT
                        [root + 6, root + 9, root + 12, root + 16, root + 19], #4 SUBDOMINANT
                        [root + 7, root + 11, root + 14, root + 17, root + 21], #5 DOMINANT
                        [root + 8, root + 12, root + 16, root + 19, root + 23], #6 SUBMEDIANT
                        [root + 11, root + 14, root + 17, root + 22, root + 24]] #7 LEADING TONE

    sadScaleDegrees = [[root, root + 3, root + 7, root + 10, root + 14], #1 TONIC
                        [root + 2, root + 5, root + 8, root + 12, root + 15], #2 SUPERTONIC
                        [root + 3, root + 7, root + 10, root + 14, root + 17], #3 MEDIANT
                        [root + 5, root + 8, root + 12, root + 15, root + 19], #4 SUBDOMINANT
                        [root + 7, root + 10, root + 14, root + 17, root + 20], #5 DOMINANT
                        [root + 8, root + 12, root + 15, root + 19, root + 22], #6 SUBMEDIANT
                        [root + 10, root + 14, root + 17, root + 20, root + 24]] #7 LEADING TONE

    if (greekMode == 0 or greekMode == 3 or greekMode == 4):
        scaleDegrees = happyScaleDegrees
        scale = "major"
    else:
        scaleDegrees = sadScaleDegrees
        scale = "minor"

    phrases = 4
    bars = 4
    firstDegree = 0
    time = 0
    for i in range (0, phrases):

        sequence = generateChordProgression.generateChordProgression(beat[2], firstDegree, scale)

        for i in range (0, len(sequence)):
            root = key
            time = time + beat[0]*2 + beat[1]*2

            octaveModChance = random.randint(1, 101) / 101
            if (octaveModChance < 0.20):
                root -= 12 #DROPS an Octave
            elif (octaveModChance > 0.85):
                root += 12 #DROPS an Octave


            firstPhrase = scaleDegrees[((sequence[i] + greekMode) % 7) - 1][0]

            zanyRoll = (random.randint(1, 101) / 101) * 0.65
            if zanyRoll > zanyChance:
                playChord(midi, 1, 0, zanyScaleDegrees[((sequence[i] + greekMode) % 7) - 1], time, beat[0]*2, 0.0)
            else:
                playChord(midi, 1, 0, scaleDegrees[((sequence[i] + greekMode) % 7) - 1], time, beat[0]*2, 0.0)
                #playNote(1, 1, scaleDegrees[((sequence[i] + greekMode) % 7) - 1][3] - 24, time, bars)

    time = time + beat[0]*2 + beat[1]*2
    playChord(midi, 1, 0, scaleDegrees[((sequence[-1] + greekMode) % 7) - 1], time, beat[0]*5, 0.02)

    # Save to file
    filenumber = 19

    with open("./chord1.mid", "wb") as output_file:
        midi.writeFile(output_file)

    print("MIDI file 'chord1.mid' saved successfully.")

    midi2 = MIDIFile(4, deinterleave=False)
    midi2.addTempo(0,0 , tempo)  # Track 0, time 0, 120 BPM
    midi2.addProgramChange(0, 0, 0, bass)
    time = 0
    for i in range (0, phrases):

        for i in range (0, len(sequence)):
            root = key
            time = time + beat[0]*2 + beat[1]*2

            octaveModChance = random.randint(1, 101) / 101
            if (octaveModChance < 0.20):
                root -= 12 #DROPS an Octave
            elif (octaveModChance > 0.85):
                root += 12 #DROPS an Octave


            firstPhrase = scaleDegrees[((sequence[i] + greekMode) % 7) - 1][0]

            zanyRoll = (random.randint(1, 101) / 101) * 0.65
            floatRoll = randomFloat()
            if floatRoll < 0.33:
                melody = 0
            elif floatRoll < 0.66:
                melody = 1
            else:
                melody = 2

            if zanyRoll > zanyChance:
                playBass(midi2, 0, 0, zanyScaleDegrees[((sequence[i] + greekMode) % 7) - 1][0], time + 0.05, beat[0]*2, melody)
            else:
                playBass(midi2, 0, 0, scaleDegrees[((sequence[i] + greekMode) % 7) - 1][0], time + 0.05, beat[0]*2, melody)
                #playNote(1, 1, scaleDegrees[((sequence[i] + greekMode) % 7) - 1][3] - 24, time, bars)


    with open("./bass1.mid", "wb") as output_file:
        midi2.writeFile(output_file)

    midi3 = MIDIFile(4, deinterleave=False)
    midi3.addTempo(2, 0, tempo)  # Track 0, time 0, 120 BPM
    midi3.addProgramChange(2, 0, 0, lead)
    time = 0
    for i in range(0, phrases):

        for i in range(0, len(sequence)):
            root = key
            time = time + beat[0] * 2 + beat[1] * 2

            octaveModChance = random.randint(1, 101) / 101
            if (octaveModChance < 0.20):
                root -= 12  # DROPS an Octave
            elif (octaveModChance > 0.85):
                root += 12  # DROPS an Octave

            firstPhrase = scaleDegrees[((sequence[i] + greekMode) % 7) - 1][0]

            zanyRoll = (random.randint(1, 101) / 101) * 0.65
            floatRoll = randomFloat()
            if floatRoll < 0.25:
                melody = 0
            elif floatRoll < 0.5:
                melody = 1
            elif floatRoll < 0.75:
                melody = 2
            else:
                melody = 3
                
            if zanyRoll >zanyChance:
                playLead(midi3, 0, 0, zanyScaleDegrees[((sequence[i] + greekMode) % 7) - 1], time,beat[0] * 2, melody)
            else:
                playLead(midi3, 0, 0, scaleDegrees[((sequence[i] + greekMode) % 7) - 1], time, beat[0] * 2, melody)

    with open("./lead1.mid", "wb") as output_file:
        midi3.writeFile(output_file)

    file1 = r"./chord1.mid"  # Replace with your first MIDI file
    file2 = r"./bass1.mid"  # Replace with your second MIDI file
    file3 = r"./lead1.mid"  # Replace with your second MIDI file
    output_file = "merged_output.mid"  # Replace with your desired output file
    final_output_file = FINAL_OUTPUT

    merge_midi(file1, file2, output_file)
    merge_midi(output_file, file3, final_output_file)

    if play:
        play_midi(final_output_file)
    return final_output_file


def play_midi(path=FINAL_OUTPUT):
    """Play a MIDI file through the local pygame mixer and wait until it finishes.

    Optional: only used when running this module directly. Requires pygame (or pygame-ce)
    plus a Timidity configuration on the system. The Streamlit app plays music in the browser instead.
    """
    import pygame
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.wait(100)


#main("Very Fast", "Funky",jazziness = 0.5, zaniness = 0.2, chord = 78, bass = 35, lead = 9)



