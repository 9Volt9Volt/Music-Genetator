import random
import time

master = [['c', 261], ['c_sharp', 277], ['d', 293], ['d_sharp', 311], \
          ['e', 329], ['f', 349], ['f_sharp', 370], ['g', 392], \
          ['g_sharp', 415], ['a', 440], ['a_sharp', 466], ['b', 493]]

def create_scale(root, type):
    # Find root note index in master list
    start = 0
    for i in range(len(master)):
        if master[i][0] == root:
            start = i
            break
    # Create scale index from user input
    if type == 'major':
        scale_index = [0, 2, 4, 5, 7, 9, 11, 12]
    if type == 'minor':
        scale_index = [0, 2, 3, 5, 7, 8, 10, 12]
    if type == 'pentatonic':
        scale_index = [0, 3, 5, 7, 10, 12]
    if type == 'harmonic_minor':
        scale_index = [0, 2, 3, 5, 7, 8, 11, 12]
    # Update scale index with root starting point
    scale_index = [(x + start) for x in scale_index]
    # Parse master list into desired scale
    scale = []
    for index in scale_index:
        try:
            scale += [master[index]]
        except:
            index = index - 12
            note = master[index][0]
            frequency = master[index][1] * 2
            scale += [[note, frequency]]
    return scale

def create_note_lengths(bpm):
    half_note = 120000//bpm
    quarter_note = 60000//bpm
    eighth_note = 30000//bpm
    sixteenth_note = 15000//bpm
    dotted_quarter_note = 90000//bpm
    dotted_eighth_note = 45000//bpm
    dotted_sixteenth_note = 22500//bpm
    triplet_quarter_note = 40000//bpm
    triplet_eighth_note = 20000//bpm
    triplet_sixteenth_note = 10000//bpm
    return [half_note, quarter_note, eighth_note, sixteenth_note, \
            dotted_quarter_note, dotted_eighth_note, dotted_sixteenth_note, \
            triplet_quarter_note, triplet_eighth_note, triplet_sixteenth_note]
        
def create_phrase(scale, note_lengths, phrase_length):
    remaining = phrase_length
    phrase = []
    while remaining > note_lengths[-1]:
        time = random.choice(note_lengths)
        note = random.choice(scale)
        phrase += [[note, time]]
        remaining = remaining - time
    last_remaining = remaining + phrase[-1][1]
    phrase[-1][1] = last_remaining
    return phrase

def create_song(key, quality, bpm, num_phrases):
    #start_time = time.time()
    scale = create_scale(key, quality)
    lengths = create_note_lengths(bpm)
    phrase_length = 16 * lengths[0]
    scale_frequencies = [x[1] for x in scale]
    song = []
    for i in range(num_phrases):
        song += [create_phrase(scale_frequencies, lengths, phrase_length)]
    #elapsed_time = time.time() - start_time
    return song
    #return elapsed_time

def raise_phrase(phrase):
    return [[phrase[i][0] * 2, phrase[i][1]] for i in range(len(phrase))]

def lower_phrase(phrase):
    return [[phrase[i][0] // 2, phrase[i][1]] for i in range(len(phrase))]

def average_time(phrases):
    test = create_song('a', 'major', 120, 1)
    try:
        test = test + 1
        time = create_song('a', 'major', 120, phrases)
        return time
    except:
        print('Please modify "create_song" to include time monitoring')
