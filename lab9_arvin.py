import turtle

DNA = {
    'Human':'ATGGTGCATCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAG',
    'Rat':'ATGGTGCACCTGACTGATGCTGAGAAGGCTGCTGTTAATGGCCTGTGGGGAAAGGTGAACCCTGATGATGTTGGTGGCGAG',
    'Rhesus':'ATGGTGCATCTGACTCCTGAGGAGAAGAATGCCGTCACCACCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAG',
    'Chimpanzee':'ATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAG'
}

DNA_TO_CODE_DICT = {'T':'00','C':'01','A':'10','G':'11'}

def dna_to_code(dna):
    coded = ''
    for c in dna:
        coded = coded + DNA_TO_CODE_DICT[c]
    return coded

def draw_0(t):
    t.right(80)
    t.forward(20)
    t.left(80)

def draw_1(t):
    t.left(80)
    t.forward(20)
    t.right(80)

def draw_coded(coded, color):
    t = turtle.Turtle()
    t.penup()
    t.speed(0)
    t.goto(-300, -200)
    t.color(color)
    t.pendown()

    for c in coded:
        if c == '1':
            draw_1(t)
        else:
            draw_0(t)

def visualize(dna, color):
    code = dna_to_code(dna)
    draw_coded(code, color)

if __name__ == "__main__":
    screen = turtle.Screen()
    visualize(DNA['Human'], 'red')
    visualize(DNA['Rat'], 'green')
    visualize(DNA['Rhesus'], 'blue')
    visualize(DNA['Chimpanzee'], 'pink')
    screen.mainloop()
