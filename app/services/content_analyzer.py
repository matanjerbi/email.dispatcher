def analyze_content(sentences):
    """
    מנתח את המשפטים וזיהוי תוכן חשוד (hostage/explosive)
    """
    result = {
        'is_suspicious': False,
        'type': None,
    }

    for sentence in sentences:
        sentence_lower = sentence.lower()

        if 'hostage' in sentence_lower:
            result['is_suspicious'] = True
            result['type'] = 'hostage'
            break

        if 'explos' in sentence_lower:
            result['is_suspicious'] = True
            result['type'] = 'explosive'
            break

    return result