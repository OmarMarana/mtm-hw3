#### PART 1 ####
# final_grade: Calculates the final grade for each student, and writes the output (while eliminating illegal
# rows from the input file) into the file in `output_path`. Returns the average of the grades.
#   input_path: Path to the file that contains the input
#   output_path: Path to the file that will contain the output

def containOnlyAlphaBet(name: str) -> bool:
    for c in name:
        if( (c < 'a' or c > 'z') and (c < 'A' or c > 'Z' ) ): #if not a letter
            return False
    return True

def valid(line: str) -> bool:
    clear_line = line.replace(' ', '')
    fields = clear_line.split(',')

    id = fields[0]
    if id[0] == '0' or len(id) != 8:
        return False
    
    name = fields[1]
    if containOnlyAlphaBet(name) == False:
        return False

    semester = int(fields[2])
    if semester < 1:
        return False
    
    hw_avg = int(fields[3])
    if hw_avg <= 50 or hw_avg > 100:
        return False
    
    return True

def prepareForOutput(line : str) -> str:
    clean_line = line.replace(' ', '').replace('\n', '')

    fields = clean_line.split(',')

    id = fields[0]
    hw_avg = fields[3]

    last_two_digits = int(id)%100

    final_grade = int ( (last_two_digits + int(hw_avg) ) / 2)
    
    list1 = [id , hw_avg , str(final_grade)]
    final_line = ', '.join(list1)
    
    return final_line

def final_grade(input_path: str, output_path: str) -> int:
    file = open(input_path, 'r')
    f = file.readlines()

    valid_students = { } #map for the valids students

    for line in f:
        if valid(line) == True:
            id = int(line.split(',')[0]) #returns str
            valid_students[id] = line

    #the valid_students map is now initiallized.

    output_file = open(output_path, 'w')
    total_avg = 0
    for key in sorted(valid_students):
        output_string = prepareForOutput(valid_students[key])
        total_avg += int(output_string.split(', ')[2])

        output_file.write(output_string + '\n')

    if len(valid_students) == 0:
        return 0
    return int( total_avg / len(valid_students) )


#### PART 2 ####
# check_strings: Checks if `s1` can be constructed from `s2`'s characters.
#   s1: The string that we want to check if it can be constructed
#   s2: The string that we want to construct s1 from
def check_strings(s1: str, s2: str) -> bool:
    hist_bank = [0] * 26
    hist_word = [0] * 26
    
    for c in s1.lower():
        hist_word[ord(c) - ord('a')] += 1

    for c in s2.lower():
        hist_bank[ord(c) - ord('a')] += 1

    for i, value in enumerate(hist_bank):
        if value < hist_word[i]:
            return False
    return True