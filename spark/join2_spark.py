def split_show_views(line):
    key_value  = line.split(",")
    show = key_value[0]
    views = int(key_value[1])
    return (show, views)



def split_show_channel(line):
    key_value  = line.split(",")
    show = key_value[0]
    channel = key_value[1]
    return (show, channel)



def extract_channel_views(show_views_channel): 
    channel = show_views_channel[1][0]
    views = int(show_views_channel[1][1])
    return (channel, views)



def some_function(a, b):
    some_result = a + b
    return some_result
