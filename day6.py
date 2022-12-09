with open('day6 input.txt',mode='r') as file:
    ds_buffer = file.read()

for x in range(13,len(ds_buffer)):
    search_marker = ds_buffer[x-13:x+1]
    for character in search_marker:
        marker_found = True
        if search_marker.count(character) > 1:
            marker_found = False
            break
    if marker_found:
        print(f"Marker is at position {x+1}")
        break