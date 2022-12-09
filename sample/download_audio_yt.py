
import argparse

def download(channel_list):

    for channel in channel_list:

        breakpoint()
        pass

def parse_file(channel_file):

    with open(channel_file, 'r', encoding='utf-8') as f:
        channel_list = f.readlines()

    return channel_list

def main(args):
    
    channel_file = args.channel_file
    
    channel_list = parse_file(channel_file)
    download(channel_list)

if __name__ == '__main__':

    '''Download and rip audio from Youtube channels using specific keywords.'''
    
    parser = argparse.ArgumentParser(description='Provide a text file containing \
        a list of relevant channels.')
    
    parser.add_argument('-ch', '--channel_file', required=True, help='Text file \
        containing a list with YT channels.')
    
    args = parser.parse_args()

    main(args)