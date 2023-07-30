import sys
import whisper


if __name__ == '__main__':
    argv_size = len(sys.argv)
    model_name = None
    root_url = None

    if argv_size >= 2:
        model_name = sys.argv[1]

    if argv_size >= 3:
        root_url = sys.argv[2]

    if model_name is None:
        model_name = 'tiny'

    whisper.load_model(name=model_name, download_root=root_url)
