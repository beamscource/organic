
import argparse
import os
import librosa
import soundfile
from tqdm import tqdm

def process_files(input_path, output_path, file_list, clip_length):

    for _, file in enumerate(tqdm(file_list)):

        # defaults are mono and 22050 Hz during loading
        y, sr = librosa.load(os.path.join(input_path, file))

        # number of samples in the specified clip length in seconds
        sound_clip = sr*clip_length
        parts = round(len(y)/sound_clip)

        start = 0
        end = sound_clip

        track_name, _ = file.split('.wav')
        for i in range(parts):
            part = y[start:end]
            output_file = os.path.join(input_path, output_path, \
                track_name+'_'+str(i+1)+'.wav')
            soundfile.write(output_file, part, sr)
            start += sound_clip+1
            end = start+sound_clip

def get_file_list(input_path):

    if os.path.isdir(input_path):
        file_list = []

    for file in os.listdir(input_path):
        if file.endswith('.wav'):
            file_list.append(file)
    return file_list

def main(args):

    input_path = args.input
    output_path = args.output
    clip_length = args.clip_length
    file_list = get_file_list(input_path)

    if not os.path.isdir(os.path.join(input_path, output_path)):
        os.makedirs(os.path.join(input_path, output_path))

    process_files(input_path, output_path, file_list, clip_length)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Split audio into multiple files.')
    parser.add_argument('-i', '--input', type=str)
    parser.add_argument('-c', '--clip_length', type=int, default=7)
    parser.add_argument('-o', '--output', type=str, default='output')
    args = parser.parse_args()

    main(args)