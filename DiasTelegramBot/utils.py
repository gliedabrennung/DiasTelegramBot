def sanitize_markdown(text):
    import re
    backtick_count = text.count('`')
    if backtick_count % 2 != 0:
        text += '`'
    text = re.sub(r'```(\w*)\n', '`', text)
    text = text.replace('```', '`')
    asterisk_count = text.count('*')
    if asterisk_count % 2 != 0:
        text += '*'
    underscore_count = text.count('_')
    if underscore_count % 2 != 0:
        text += '_'
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'\1: \2', text)
    return text
