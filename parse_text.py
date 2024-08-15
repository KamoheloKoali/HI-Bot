def parse(text):
    """
        parse text
        
        Args:
            text (str): text
        
        Returns:
            parsed string
    """
    parsed_string = ""
    parse_string = text.lower()
    parse_string = list(parse_string)
    parse_string[0] = parse_string[0].upper()
    for letter in parse_string:
        parsed_string += letter
    return parsed_string

parse("part 3")