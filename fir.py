season = str(input())
def symbol_sequence(symbol, symbol_count):
    output_sequence = ""
    for _ in range(symbol_count):
        output_sequence += symbol
    return output_sequence
def crown_level(symbol, number, count):
    string_len = count * 2 - 1
    symbol_count = number * 2 - 1
    space_count = (string_len - symbol_count) / 2
    symbols = symbol_sequence(symbol, symbol_count)
    spaces = symbol_sequence(" ", int(space_count))
    return spaces + symbols + spaces
   
def framing(string, symbol, symbol_count):
    frame = symbol_sequence(symbol,symbol_count)
    return frame + string + frame
def crown(season_first_letter, level_count):
    for level_counter in range(level_count):
        string = crown_level(season_first_letter, level_counter + 1, level_count)
        string = framing(string, " ",int(level_count / 2)) 
        print(string)
        level_counter += 1
def summer_crown(level_count):
    crown('L', level_count)

def autumn_crown(level_count):
    crown('O', level_count)

def winter_crown(level_count):
    crown('3', level_count)
    
def spring_crown(level_count):
    crown('B', level_count)
def trunk(level_count):
    string = crown_level('H',1,level_count)
    string = framing(string, " ", int(level_count / 2))
    print(string)
if season == 'spring':
    spring_crown(8)
if season == 'summer':
    summer_crown(8)
if season == 'winter':
    winter_crown(8)
if season == 'autumn':
    autumn_crown(8)
trunk(8)