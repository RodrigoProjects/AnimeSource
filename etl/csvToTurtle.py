import sys
import csv
import json
from re import *

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
    themesDic = dict()
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

        # Write and Populate genres licensors producers studios
        for d in data:
            obj = data[d]
            ida = obj['anime_id']
            
            if 'genre' in obj:
                lGenre = [x.strip() for x in obj['genre'].split(',')]
                for x in lGenre:
                    if x not in genero:
                        genero[x] = f'genre_{idGener}'
                        idGener += 1
                        out.write(f'###  http://www.semanticweb.org/rodrigop/ontologies/2021/33/animes#{genero[x]}\n')
                        out.write(f':{genero[x]} rdf:type owl:NamedIndividual ,\n')
                        out.write(f'\t\t\t\t:Genre ;\n')
                        out.write(f'\t\t\t:name \"{x}\" .\n\n')

            if 'licensor' in obj:
                lLice = [x.strip() for x in obj['licensor'].split(',')]
                for x in lLice:
                    if x not in licensors:
                        licensors[x] = f'licensor_{idLicense}'
                        idLicense += 1
                        out.write(f'###  http://www.semanticweb.org/rodrigop/ontologies/2021/33/animes#{licensors[x]}\n')
                        out.write(f':{licensors[x]} rdf:type owl:NamedIndividual ,\n')
                        out.write(f'\t\t\t\t:License ;\n')
                        out.write(f'\t\t\t:name \"{x}\" .\n\n')
                
            if 'producer' in obj:
                lProd = [x.strip() for x in obj['producer'].split(',')]
                for x in lProd:
                    if x not in producers and x != "":
                        producers[x] = f'producer_{idProducer}'
                        idProducer += 1
                        out.write(f'###  http://www.semanticweb.org/rodrigop/ontologies/2021/33/animes#{producers[x]}\n')
                        out.write(f':{producers[x]} rdf:type owl:NamedIndividual ,\n')
                        out.write(f'\t\t\t\t:Producer ;\n')
                        out.write(f'\t\t\t:name \"{x}\" .\n\n')
                        
            if 'studio' in obj:
                lStudio = [x.strip() for x in obj['studio'].split(',')]
                for x in lStudio:
                    if x not in studios:
                        studios[x] = f'studio_{idStudio}'
                        idStudio += 1
                        out.write(f'###  http://www.semanticweb.org/rodrigop/ontologies/2021/33/animes#{studios[x]}\n')
                        out.write(f':{studios[x]} rdf:type owl:NamedIndividual ,\n')
                        out.write(f'\t\t\t\t:Studio ;\n')
                        out.write(f'\t\t\t:name \"{x}\" .\n\n')

            themesDic[obj['anime_id']]=[]
            if 'opening_theme' in obj:
                if obj['opening_theme'] != '[]':
                    themes = obj['opening_theme'].split('\', \'')
                    for theme in themes:
                        out.write(f'###  http://www.semanticweb.org/rodrigop/ontologies/2021/33/animes#Theme_{idTheme}\n')
                        out.write(f':Theme_{idTheme} rdf:type owl:NamedIndividual ,\n')
                        themesDic[obj['anime_id']].append(f'Theme_{idTheme}')
                        idTheme += 1
                        out.write(f'\t\t\t\t:Theme_Music ;\n')
                        by = split(r'"?-?\s*?by',theme)
                        theme_name =  sub(r'(\[\')?(#\d+:?)?\s*\"','',by[0])
                        if len(by) >= 2:
                            aux = sub(r'\(.*?[)\r\n]','',by[1])
                            lArtist = [x.strip() for x in aux.split(',')]
                            lArtist[-1] = sub(r'[\'\]]','',lArtist[-1]).strip()
                            for x in lArtist:
                                a = split(r'\s&\s',x)
                                for s in a:
                                    s1 = s.replace('"','')
                                    out.write(f'\t\t\t:artist \"{s1}\" ;\n')
                        out.write(f'\t\t\t:title \"{theme_name}\" .\n\n')

            if 'ending_theme' in obj:
                if obj['ending_theme'] != '[]':
                    themes = obj['ending_theme'].split('\', \'')
                    for theme in themes:
                        out.write(f'###  http://www.semanticweb.org/rodrigop/ontologies/2021/33/animes#Theme_{idTheme}\n')
                        out.write(f':Theme_{idTheme} rdf:type owl:NamedIndividual ,\n')
                        themesDic[obj['anime_id']].append(f'Theme_{idTheme}')
                        idTheme += 1
                        out.write(f'\t\t\t\t:Theme_Music ;\n')
                        by = split(r'"?-?\s*?by',theme)
                        theme_name =  sub(r'(\[\')?(#\d+:?)?\s*\"','',by[0])
                        if len(by) >= 2:
                            aux = sub(r'\(.*?[)\r\n]','',by[1])
                            lArtist = [x.strip() for x in aux.split(',')]
                            lArtist[-1] = sub(r'[\'\]]','',lArtist[-1]).strip()
                            for x in lArtist:
                                a = split(r'\s&\s',x)
                                for s in a:
                                    s1 = s.replace('"','')
                                    out.write(f'\t\t\t:artist \"{s1}\" ;\n')
                        out.write(f'\t\t\t:title \"{theme_name}\" .\n\n')
            
            c += 1
            #print anime
            idAnime = f'anime_{ida}'
            out.write(f'###  http://www.semanticweb.org/rodrigop/ontologies/2021/33/animes#{idAnime}\n')
            out.write(f':{idAnime} rdf:type owl:NamedIndividual ,\n')
            out.write(f'\t\t\t\t:Anime ;\n') 
            if 'genre' in obj:  
                lGenre = [x.strip() for x in obj['genre'].split(',')]
                for x in lGenre:
                    if x != "":
                        out.write(f'\t\t\t:hasGenre :{genero[x]} ;\n')
            if 'licensor' in obj:
                lLice = [x.strip() for x in obj['licensor'].split(',')]
                for x in lLice:
                    if x != "":
                        out.write(f'\t\t\t:hasLicense :{licensors[x]} ;\n')
            if 'producer' in obj:
                lProd = [x.strip() for x in obj['producer'].split(',')]
                for x in lProd:
                    if x != "":
                        out.write(f'\t\t\t:hasProducer :{producers[x]} ;\n')
            if 'studio' in obj:
                lStudio = [x.strip() for x in obj['studio'].split(',')]
                for x in lStudio:
                    if x != "":
                        out.write(f'\t\t\t:hasStudio :{studios[x]} ;\n')

            for x in themesDic[obj['anime_id']]:
                out.write(f'\t\t\t:hasTheme :{x} ;\n')
                
            if 'aired_string' in obj:
                a = obj['aired_string'].replace('"','')
                out.write(f"\t\t\t:aired \"{a}\" ;\n")
            if 'type' in obj:
                t = obj['type'].replace('"','')
                out.write(f"\t\t\t:type \"{t}\" ;\n")
            if 'title_synonyms' in obj and obj['title_synonyms'] != "":
                ts = obj['title_synonyms'].replace('"','')
                out.write(f"\t\t\t:title_synonyms \"{ts}\" ;\n")
            if 'title_japanese' in obj:
                tj = obj['title_japanese'].replace('"','')
                out.write(f"\t\t\t:title_japanese \"{tj}\" ;\n")
            if 'title_english' in obj and obj['title_english'] != "":
                te = obj['title_english'].replace('"','')
                out.write(f"\t\t\t:title_english \"{te}\" ;\n")
            if 'status' in obj:
                st = obj['status'].replace('"','')
                out.write(f"\t\t\t:status \"{st}\" ;\n")
            if 'source' in obj:
                sr = obj['source'].replace('"','')
                out.write(f"\t\t\t:source \"{sr}\" ;\n")
            if 'scored_by' in obj:
                sb = obj['scored_by'].replace('"','')
                out.write(f"\t\t\t:scored_by {sb} ;\n")
            if 'score' in obj:
                sc = obj['score'].replace('"','')
                out.write(f"\t\t\t:score \"{sc}\" ;\n")
            if 'rating' in obj:
                r = obj['rating'].replace('"','')
                out.write(f"\t\t\t:rating \"{r}\" ;\n")
            if 'rank' in obj:
                ra = obj['rank'].replace('"','')
                out.write(f"\t\t\t:rank \"{ra}\" ;\n")
            if 'premiered' in obj:
                p = obj['premiered'].replace('"','')
                out.write(f"\t\t\t:premiered \"{p}\" ;\n")
            if 'popularity' in obj:
                pop = obj['popularity'].replace('"','')
                out.write(f"\t\t\t:popularity {pop} ;\n")
            if 'image_url' in obj:
                img = obj['image_url'].replace('"','')
                out.write(f"\t\t\t:image_url \"{img}\" ;\n")
            if 'favorites' in obj:
                f = obj['favorites'].replace('"','')
                out.write(f"\t\t\t:favorites {f} ;\n")
            if 'episodes' in obj:
                ep = obj['episodes'].replace('"','')
                out.write(f"\t\t\t:episodes {ep};\n")
            if 'duration' in obj:
                d = obj['duration'].replace('"','')
                out.write(f"\t\t\t:duration \"{d}\" ;\n")
            if 'broadcast' in obj and obj['broadcast'] != "":
                br = obj['broadcast'].replace('"','')
                out.write(f"\t\t\t:broadcast \"{br}\" ;\n")
            if 'background' in obj and obj['background'] != "":
                back = obj['background'].replace('"','')
                out.write(f"\t\t\t:background \"{back}\" ;\n")
            if 'members' in obj and obj['members'] != "":
                back = obj['members'].replace('"','')
                out.write(f"\t\t\t:interested_num \"{back}\" ;\n")
                
            t = obj['title'].replace('"','\'')
            out.write(f'\t\t:title "{t}" .\n\n')



        print(f'Tratados\n\t{c} animes\n\t{idGener-1} generos\n\t{idProducer-1} producer\n\t{idLicense-1} licensor\n\t{idStudio-1} studio\n\t{idTheme} Themes')


if __name__ == "__main__":
    toTTL(main(sys.argv[1:]))

