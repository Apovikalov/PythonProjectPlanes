def state_list(self):
    states = []
    for i in [self.register_country, self.call_name, self.flight_speed,
              self.flight_height, self.is_on_ground]:
        states.append(i)
    return states

def filter_aeroplanes(aeroplanes, filter_words):
    filtered_aeroplanes = []
    for plane in aeroplanes:
        if plane.register_country in filter_words:
            filtered_aeroplanes.append(plane)
    return filtered_aeroplanes

def get_aeroplanes_by_altitude(aeroplanes, altitude_range):
    ranged_aeroplanes = []
    for plane in aeroplanes:
        if plane.flight_height in altitude_range:
            ranged_aeroplanes.append(plane)
    return ranged_aeroplanes

def sort_aeroplanes(ranged_aeroplanes):
    sorted_aeroplanes = sorted(ranged_aeroplanes, key=lambda x: x.flight_height)
    return sorted_aeroplanes

def get_top_aeroplanes(sorted_aeroplanes, top_n: int):
    top_aeroplanes = []
    for i in range(0, top_n):
        top_aeroplanes.append(sorted_aeroplanes[i])
    return top_aeroplanes
