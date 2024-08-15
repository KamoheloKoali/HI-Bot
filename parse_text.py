def parse(text):
    """
    Parse text to ensure it follows the format "Part X".
    
    Args:
        text (str): The input text to parse.
    
    Returns:
        str: The parsed string in the format "Part X".
    """
    if not isinstance(text, str):
        raise ValueError("Input text must be a string.")

    parsed_string = ""

    try:
        # Normalize the text to lowercase and split into words
        words = text.lower().split()
        
        # Ensure the first word is "part" and the second word is a number
        if words and len(words) == 2 and words[0].isdigit():
            parsed_string = f"Part {words[0]}"
        elif words and len(words) == 2 and words[1].isdigit():
            parsed_string = f"Part {words[1]}"
        else:
            raise ValueError("Text must be in the format 'Part X' where X is a number.")
        
    except Exception as e:
        raise ValueError(f"Error parsing text: {e}")

    return parsed_string
