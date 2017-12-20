import glob
import comuWOsc
import random

def read_files(is_train, username, num):
    fetch_type = "r"
    folder_names = [
        "AdditiveWave",
        "EmbeddedIteration",
        "IncrementDecrement",
        "Interpolate",
        "Perspective",
        "RadialGradient",
        "RandomGaussian",
        "Relativity",
        "Saturation"]
    if is_train == "t":
        all_origin_processing_file_pathes = glob.glob('data/origin/TOKKO/*.pde')
    else:
        if username == "a":
            # listen watch listen watch
            folder_names = ["Interpolate", "Perspective", "RandomGaussian", "Saturation"]
        elif username == "b":
            #listen watch listen watch
            folder_names = ["RandomGaussian", "Saturation", "Interpolate", "Perspective"]
        elif username == "c":
            #watch listen watch listen
            folder_names = ["Perspective", "RandomGaussian", "Saturation", "Interpolate"]
        elif username == "d":
            #watch listen watch listen
            folder_names = ["Saturation", "Interpolate", "Perspective", "RandomGaussian"]
        #folder_name = random.randint(0, len(folder_names))
        #all_origin_processing_file_pathes = glob.glob('data/change/' + folder_names[folder_name] + '/*.pde')
        #print(folder_names[folder_name])
        all_origin_processing_file_pathes = glob.glob('data/change/' + folder_names[int(num)] + '/*.pde')


    if fetch_type == "r":
        n_ran = random.randint(0,len(all_origin_processing_file_pathes))
        if n_ran == len(all_origin_processing_file_pathes):
            n_ran = 0
        origin_processing_file_pathes = [all_origin_processing_file_pathes[n_ran]]
    for p in origin_processing_file_pathes:
        f = open(p)
        lines = f.readlines()
        f.close()

    comuWOsc.setup_osc(lines)
    return lines
