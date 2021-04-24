import sys

def main(args):
    
    animes = []

    try:
        with open(args[1]) as f:
            animes = [anime.split('||') for anime in f.readlines()]

        print(animes[0])
    except Exception as e:
        raise e




if __name__ == "__main__":
    main(sys.argv)