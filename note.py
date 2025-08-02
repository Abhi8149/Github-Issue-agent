from langchain_core.tools import tool

@tool
def save_note(note):
    '''Save a note to a local while along with the heading of note
    
    Args-
    note: The note to save.
    '''
    with open("notes.txt", 'a') as f:
        f.write(note + '\n')