
import argparse
import pafy


def download(channel_list):

    for channel in channel_list:
        pass

def parse(channel_file):

    with open(channel_file, 'r', encoding='utf-8') as f:
        channel_list = f.readlines()

    return channel_list

def main(args):
    pass

if __name__ = '__main__':

    '''Download and rip audio from Youtube channels using specific keywords.'''
    
    parser = argparse.ArgumentParser(description='Provide a text file containing
        a list of relevant channels.')
    
    parser.add_argument('-ch', '--channel_file', required=True, help='Text file
        containing a list with YT channels.')
    
    args = parser.parse_args()

    main(args)