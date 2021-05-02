import sys
import csv
import json

def main(argv):
    size = len(argv)

    if size >= 3:
        imput_file = argv[0]
        output1 = argv[1]
        in_owl = argv[2]
    else: 
        print('ler.csv output.owl skeleton.owl')
        return

    i = open(imput_file)

    csv_f = csv.DictReader(i)

    c = 0
    dic = dict()

    for row in csv_f:
        
        dic[int(row['anime_id'])] = {
            "anime_id": int(row['anime_id']),
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

    #print('Total de linhas lidas '+ str(c))
    #print(json.dumps(dic, indent=4, sort_keys=False,ensure_ascii=False))
    #with open(output1, 'w') as out:
    #    json.dump(dic,out)
    r = dict()
    r['data'] = dic
    r['output'] = output1
    r['inOwl'] = in_owl
    return r


def toTTL(r):
    data = r['data']
    output = r['output']
    anime = dict()
    genero = dict()
    licensors = dict()
    producers = dict()
    references = dict() # nao percebi as referencias ?? --TODO
    studios = dict()
    themes = dict() # Por fazer --TODO
    c = 0
    idGener = 1
    idLicense = 1
    idProducer = 1
    idStudio = 1
    idTheme = 1
    file_header = open(r['inOwl']).read()

    with open(output, "w") as out:

        out.write(file_header) # Classes and Object properties definitions.

        out.write("#################################################################\n")
        out.write("#    Individuals\n")
        out.write("#################################################################\n\n")

        # Write Animes and populate genres licensors producers studios
        for d in data:
            obj = data[d]
            ida = obj['anime_id']
            idAnime = f'anime_{ida}'
            out.write(f'###  http://www.semanticweb.org/rodrigop/ontologies/2021/33/animes#{idAnime}\n')
            out.write(f':{idAnime} rdf:type owl:NamedIndividual ,\n')
            out.write(f'\t\t\t\t:Anime ;\n')     
            if 'genre' in obj:
                lGenre = [x.strip() for x in obj['genre'].split(',')]
                for x in lGenre:
                    if x not in genero:
                        genero[x] = f'genre_{idGener}'
                        idGener += 1
                    out.write(f'\t\t\t:hasGenre :{genero[x]} ;\n')
            if 'licensor' in obj:
                if obj['licensor'] not in licensors:
                    licensors[obj['licensor']] = f'licensor_{idLicense}'
                    idLicense += 1
                l = obj['licensor']
                out.write(f'\t\t\t:hasLicense :{licensors[l]} ;\n')
            if 'producer' in obj:
                lProd = [x.strip() for x in obj['producer'].split(',')]
                for x in lProd:
                    if x not in genero:
                        producers[x] = f'producer_{idProducer}'
                        idProducer += 1
                    out.write(f'\t\t\t:hasProducer :{producers[x]} ;\n')
            if 'studio' in obj:
                if obj['studio'] not in studios:
                    studios[obj['studio']] = f'studio_{idStudio}'
                    idStudio += 1
                s = obj['studio']
                out.write(f'\t\t\t:hasStudio :{studios[s]} ;\n')
            t = obj['title']
            out.write(f'\t\t:title "{t}" .\n\n')
            c += 1

        # Write genres
        for genro in genero:
            out.write(f'###  http://www.semanticweb.org/rodrigop/ontologies/2021/33/animes#{genero[genro]}\n')
            out.write(f':{genero[genro]} rdf:type owl:NamedIndividual ,\n')
            out.write(f'\t\t\t\t:Genre ;\n')
            out.write(f'\t\t\t:name \"{genro}\" .\n\n')
        # Write licensors
        for licensor in licensors:
            out.write(f'###  http://www.semanticweb.org/rodrigop/ontologies/2021/33/animes#{licensors[licensor]}\n')
            out.write(f':{licensors[licensor]} rdf:type owl:NamedIndividual ,\n')
            out.write(f'\t\t\t\t:Genre ;\n')
            out.write(f'\t\t\t:name \"{licensor}\" .\n\n')
        # Write producers
        for producer in producers:
            out.write(f'###  http://www.semanticweb.org/rodrigop/ontologies/2021/33/animes#{producers[producer]}\n')
            out.write(f':{producers[producer]} rdf:type owl:NamedIndividual ,\n')
            out.write(f'\t\t\t\t:Producer ;\n')
            out.write(f'\t\t\t:name \"{producer}\" .\n\n')
        # Write studios
        for studio in studios:
            out.write(f'###  http://www.semanticweb.org/rodrigop/ontologies/2021/33/animes#{studios[studio]}\n')
            out.write(f':{studios[studio]} rdf:type owl:NamedIndividual ,\n')
            out.write(f'\t\t\t\t:Studio ;\n')
            out.write(f'\t\t\t:name \"{studio}\" .\n\n')
        print(f'Tratados\n\t{c} animes\n\t{idGener-1} generos\n\t{idProducer-1} producer\n\t{idLicense-1} licensor\n\t{idStudio-1} studio')


if __name__ == "__main__":
    toTTL(main(sys.argv[1:]))

