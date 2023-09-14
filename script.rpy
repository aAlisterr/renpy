# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define helena = Character("Helena")
define Narrador = Character("Narrador")


# The game starts here.

label start:
   

    scene bg inicio 
    
    "O dia começa"
    

    Narrador 'faça sua primeira escolha'

    menu:
        "snoite": 
            jump escolha1
        "sol": 
            jump escolha2

    label escolha1:
        'Teste'
    return





    label escolha2:
        'Teste2'
            
        'teste3'
        'teste4'
        'teste5'
        'teste6'
        'teste7'
        'teste8'
        'teste9'
        'teste10'
    return

   
    







    show eileen happy


    helena "You've created a new Ren'Py game."

    helena "Once you add a story, pictures, and music, you can release it to the world!"


    return
