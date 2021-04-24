import sys
import csv
import json

def main(argv):
    size = len(argv)

    if size >= 2:
        imput_file = argv[0]
        output1 = argv[1]
    else: 
        print('ler.csv output.json')
        return

    i = open(imput_file)

    csv_f = csv.DictReader(i)

    c = 0
    dic = {}

    for row in csv_f:
        
        dic[int(row['anime_id'])] = {
            "anime_id": row['anime_id'],
            "title": row['title'],
            "title_english": row['title_english'],
            "title_japanese": row['title_japanese'],
            "title_synonyms": row['title_synonyms'],
            "image_url": row['image_url'],
            "type": row['type'],
            "source": row['source'],
            "episodes": row['episodes'],
            "status": row['status'],
            "airing": row['airing'],
            "aired_string": row['aired_string'],
            "aired": row['aired'],
            "duration": row['duration'],
            "rating": row['rating'],
            "score": row['score'],
            "scored_by": row['scored_by'],
            "rank": row['rank'],
            "popularity": row['popularity'],
            "members": row['members'],
            "favorites": row['favorites'],
            "background": row['background'],
            "premiered": row['premiered'],
            "broadcast": row['broadcast'],
            "related": row['related'],
            "producer": row['producer'],
            "licensor": row['licensor'],
            "studio": row['studio'],
            "genre": row['genre'],
            "opening_theme": row['opening_theme'],
            "ending_theme": row['ending_theme'],
            "duration_min": row['duration_min'],
            "aired_from_year": row['aired_from_year'],
        }
        c += 1


    print('Total de linhas lidas '+ str(c))
    #print(json.dumps(dic, indent=4, sort_keys=False,ensure_ascii=False))
    with open(output1, 'w') as out:
        json.dump(dic,out)

if __name__ == "__main__":
    main(sys.argv[1:])