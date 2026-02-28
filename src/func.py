def filter_aeroplanes(aeroplanes, filter_words):
    filtered_aeroplanes = []
    for plane in aeroplanes:
        if plane.register_country in filter_words:
            filtered_aeroplanes.append(plane)
    return filtered_aeroplanes