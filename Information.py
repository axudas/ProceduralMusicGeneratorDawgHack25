import random as rand

class Information:

    basses = {'Synth Bass': 38,"Baritone Sax":67,"Synth Bass 2":87,"Fretless Bass":35}
    chords = {"Drawbar Organ":17,"Electric Piano":6,"Fantasia":89,"Shakuhachi":78,"Ocarina":79,"Halo":94}
    leads = {"Solo Vox":85,"Piano":1,"Marimba":12,"Strings":45,"Violin":40}

    def __init__(self, mood="Happy", tempo="Moderate", zany=0, jazzy=0,
                 chord="Drawbar Organ", bass="Synth Bass", lead="Solo Vox"):
        self.mood = mood
        self.tempo = tempo
        self.zany = zany
        self.jazzy = jazzy
        self.set_chord_string(chord)
        self.set_bass_string(bass)
        self.set_lead_string(lead)

    def get_bass_int(self):
        return self.bass_int

    def get_bass_string(self):
        return self.bass_string
    
    def get_chord_int(self):
        return self.chord_int
    
    def get_chord_string(self):
        return self.chord_string
    
    def get_jazzy(self):
        return self.jazzy
    
    def get_lead_int(self):
        return self.lead_int
    
    def get_lead_string(self):
        return self.lead_string
    
    def get_mood(self):
        return self.mood
    
    def get_tempo(self):
        return self.tempo
    
    def get_zany(self):
        return self.zany
    
    def set_bass_int(self,bass):
        self.bass_int = bass

    def set_bass_string(self,bass):
        self.bass_string = bass
        self.set_bass_int(self.basses[bass])

    def set_chord_int(self,chord):
        self.chord_int = chord

    def set_chord_string(self,chord):
        self.chord_string = chord
        self.set_chord_int(self.chords[chord])

    def set_jazzy(self,jazzy):
        self.jazzy = jazzy

    def set_lead_int(self,lead):
        self.lead_int = lead

    def set_lead_string(self, lead):
        self.lead_string = lead
        self.lead_int = self.leads[lead]

    def set_mood(self, mood):
        self.mood = mood

    def set_tempo(self, tempo):
        self.tempo = tempo

    def set_zany(self, zany):
        self.zany = zany


    def randomize(self):
        basses = ['Synth Bass',"Baritone Sax","Synth Bass 2","Fretless Bass"]
        chords = ["Drawbar Organ","Electric Piano","Fantasia","Shakuhachi","Ocarina","Halo"]
        leads = ["Solo Vox","Piano","Marimba","Strings","Violin"]

        temp = ['Very Slow','Slow','Moderate','Fast','Very Fast']
        moods = ['Happy','Cool','Dark','Funky','Dreamy','Sad','Tense']
        self.jazzy = round(rand.random()*100)
        self.mood = rand.choice(moods)
        self.tempo = rand.choice(temp)
        self.set_bass_string(basses[rand.randint(0,len(basses)-1)])
        self.set_chord_string(chords[rand.randint(0,len(chords)-1)])
        self.set_lead_string(leads[rand.randint(0,len(leads) -1)])
        self.zany = round(rand.random()*100)