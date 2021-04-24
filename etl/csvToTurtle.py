import sys
import json

def main(args):
    
    animes = []

    try:
        with open(args[1]) as f:
            animes = [anime.split('||') for anime in f.readlines()]

            headers = animes[0]
            animes = animes[1:]

            cleaned_animes = [{headers[idx] : el.strip() for idx, el in enumerate(anime)} for anime in animes]


        print( json.dumps(cleaned_animes, indent=4))
        
    except Exception as e:
        raise e




if __name__ == "__main__":
    main(sys.argv)