import base64

import streamlit as st
import streamlit.components.v1 as components
from Information import Information
from src import main as composer


info = Information()
message = st.empty()

c_logo = st.container()
c_title = st.container()
c_values = st.container()
c_inst = st.container()
c_buttons = st.container()
c_logo.image("Recources/Bach.png", width = 200)

# Title of the app
c_title.title(':blue[Bach]')

# A message
c_title.write('Create music with little effort . . . no AI')
c_title.write('Enter parameters below and press create!')

# Tempo Drop
# st.selectbox( label , inputs , index )
tempos = ["Very Fast","Fast","Moderate","Slow","Very Slow"]
tempo = c_values.selectbox( 'Tempo', tempos , 2)
info.set_tempo(tempo)

# Moods Drop
# st.selectbox( label , inputs)
moods = ["Happy","Cool","Dark","Dreamy","Funky","Sad","Tense"]
mood = c_values.selectbox( 'Mood', moods , 0)
info.set_mood(mood)

# Chords Drop
# st.selectbox( label , inputs)
chords_ = ["Drawbar Organ","Electric Piano","Fantasia","Shakuhachi","Ocarina","Halo"]
chord = c_inst.selectbox( 'Chord', chords_ , 0)
info.set_chord_string(chord)

# Bass Drop
# st.selectbox( label , inputs)
basses_ = ['Synth Bass',"Baritone Sax","Synth Bass 2","Fretless Bass"]
bass = c_inst.selectbox( 'Bass', basses_ , 0)
info.set_bass_string(bass)

# leads Drop
# st.selectbox( label , inputs)
leads_ = ["Solo Vox","Piano","Marimba","Strings","Violin"]
lead = c_inst.selectbox( 'Lead', leads_ , 0)
info.set_lead_string(lead)

# Jazz slider
jazz = c_values.slider('Jazz')
info.set_jazzy(jazz)

# Zane Slider
zany = c_values.slider('Zany')
info.set_zany(zany)

#enable file buttons
if 'button_enabled' not in st.session_state:
    st.session_state.button_enabled = False

def create(params):
    """Compose a new piece from the given parameters and keep the MIDI bytes in session state."""
    path = composer.main(params.get_tempo(), params.get_mood(),
                        jazziness=params.get_jazzy() / 100,
                        zaniness=params.get_zany() / 100,
                        chord=params.get_chord_int(),
                        bass=params.get_bass_int(),
                        lead=params.get_lead_int(),
                        play=False)
    with open(path, "rb") as f:
        st.session_state.midi_bytes = f.read()
    st.session_state.button_enabled = True

def describe(params):
    return ", ".join([params.get_tempo(), params.get_mood(),
                      "Jazz " + str(params.get_jazzy()), "Zany " + str(params.get_zany()),
                      params.get_chord_string(), params.get_bass_string(), params.get_lead_string()])

# Random
if c_buttons.button("Randomize"):
    info.randomize()
    create(info)
    message.success("Random with: " + describe(info))

# Create Midi Button
if c_buttons.button("Create"):
    create(info)
    message.success("Created with: " + describe(info))

# Play and Download buttons
if st.session_state.button_enabled:
    # In-browser MIDI player (html-midi-player + Magenta SoundFont); no system audio setup needed
    midi_b64 = base64.b64encode(st.session_state.midi_bytes).decode()
    components.html(f"""
        <script src="https://cdn.jsdelivr.net/combine/npm/tone@14.7.58,npm/@magenta/music@1.23.1/es6/core.js,npm/focus-visible@5,npm/html-midi-player@1.5.0"></script>
        <midi-player src="data:audio/midi;base64,{midi_b64}" sound-font style="width:100%"></midi-player>
    """, height=70)

    c_buttons.download_button("Download", data=st.session_state.midi_bytes,
                              file_name="bach_song.mid", mime="audio/midi")
