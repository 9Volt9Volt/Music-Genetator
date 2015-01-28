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

def change_octave(scale, direction, num):
    if direction == 'up':
        return [[scale[i][0], scale[i][1]*(2**num)] for i in range(len(scale))]
    if direction == 'down':
        return [[scale[i][0], scale[i][1]//(2**num)] for i in range(len(scale))]
