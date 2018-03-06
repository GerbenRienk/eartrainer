'''
Created on 3 jun. 2017

@author: GerbenRienk
'''
from midiutil import MIDIFile
import random

#degrees  = [60, 62, 63, 64, 65, 67, 69, 71, 72] # MIDI note number
degrees  = [59, 60, 61, 62, 63, 64, 65, 66, 67]
track    = 0
channel  = 0
time     = 1   # In beats
duration = 1   # In beats
tempo    = 60  # In BPM
volume   = 100 # 0-127, as per the MIDI standard

total_number_of_sequences = 1000
notes_per_sequence = 2
note_counter = 0
sequence_counter = 0

random.seed
MyMIDI = MIDIFile(1,adjust_origin=True) # One track, defaults to format 1 (tempo track automatically created)
MyMIDI.addTempo(track,time, tempo)

while sequence_counter <= total_number_of_sequences:
    # get a random number
    i = random.randint(0,len(degrees)-1)
    print(time, degrees[i])
    # find the corresponding note
    random_note = degrees[i]
    MyMIDI.addNote(track, channel, random_note, time, duration, volume)
    time = time + 1
    note_counter = note_counter + 1
    # check if we have a sequence
    if (note_counter == notes_per_sequence):
        note_counter = 0
        sequence_counter = sequence_counter + 1
        # add rest to midi track
        time = time + notes_per_sequence 

with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)

if __name__ == '__main__':
    pass