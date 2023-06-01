import pandas as pd                  

data = pd.read_excel('Film.xlsx')                                                # 1920_1997
data.rename(columns={'Subject':'Genre'} ,inplace=True)

data.drop(['Actress'],axis=1 ,inplace=True)
#_____________________________________________________________________________
Director_Data = data.copy()                                                    # Top 10 Directors With Most Films.
Director_Data.dropna(subset=['Director'],inplace=True)   

Directos_Films = {}
Actor_Num = {}
D_Act_Dir = []
Act_Dir = {}



def Actor_Director():

    for i in Director_Data.index:
        Directos_Films[Director_Data['Director'].loc[i]] = Directos_Films.get(Director_Data['Director'].loc[i] , 0) + 1
        Actor_Num[Director_Data['Actor'].loc[i]] = Actor_Num.get(Director_Data['Actor'].loc[i] , 0) + 1

        if Director_Data['Director'].loc[i] == Director_Data['Actor'].loc[i]:
            D_Act_Dir.append(Director_Data['Actor'].loc[i])
            Act_Dir[Director_Data['Director'].loc[i]] = Act_Dir.get(Director_Data['Director'].loc[i] , 0) + 1

    Act_dir ={}                                                               # 10 (Actor_Director) Coincide in a Film.
    for k,v in Act_Dir.items():
        if v >= 2:
            w = k.split(' ')
            w = list(w)

            Act_dir[w[1],w[0]] = v

    Directos_Film_Num = {}
    for k,v in Directos_Films.items():
        if v >= 10 and v < 40:
        
            w = k.split(' ')
            w = list(w)

            if len(w) == 3:
                Directos_Film_Num[w[1],w[2],w[0]] = v
            else:   
                Directos_Film_Num[w[1],w[0]] = v

    Actor = {}
    for k,v in Actor_Num.items():                                               # 18 Actor With Most Film.
        if v >= 10:
            w = k.split(' ')
            w = list(w)

            if 'De' in k:
                w = k.split(',')
                w = list(w)
                Actor[w[1],w[0]] = v

            else:   
                Actor[w[1],w[0]] = v

    with open('10_Directors_MostFilm.csv','a') as wr ,open('18_Actor_MostFilm.csv','a') as W ,open('Act_Dir.csv','a') as Ac :

        for k,v in Directos_Film_Num.items():
            wr.write(f'{k}:{int(v)}\n')

        for k,v in Actor.items():
            W.write(f'{k}:{int(v)}\n')

        for k,v in Act_dir.items():
            Ac.write(f'{k}:{int(v)}\n')              


Actor_Director()
# #_____________________________________________________________________________
Genre_Data = data.copy()                                                            # Genres Types And Quantity its.
Genre_Data.dropna(subset=['Genre'],axis=0,inplace=True)

Genres={}
for i in Genre_Data.index:
    Genres[Genre_Data['Genre'].loc[i]] = Genres.get(Genre_Data['Genre'].loc[i] , 0) + 1

for k,v in Genres.items():
    with open('Genres.csv','a') as w:
        w.write(f'{k}:{int(v)}\n')
#_____________________________________________________________________________
def Prize():                                                                        # Directors That Obtained Award 3time Or More.

    Prize_Data = data.copy()                                                  
    flt = Prize_Data['Awards'] == 'Yes'

    Prize_Data = Prize_Data[flt]
    Prize_Data.dropna(subset='Director',axis=0,inplace=True)

    Dir_Pir ={}
    for i in Prize_Data.index:
        Dir_Pir[Prize_Data['Director'].loc[i]] = Dir_Pir.get(Prize_Data['Director'].loc[i], 0) +1

    Directors_Prize = {}
    for k,v in Dir_Pir.items():

        if v >= 3:
            w = k.split(' ')
            w = list(w)

            if len(w) == 3:
                Directors_Prize[w[1],w[2],w[0]] = v
            else:   
                Directors_Prize[w[1],w[0]] = v

    for k,v in Directors_Prize.items():
        with open('Dir_Prize.csv','a') as Pr:
            Pr.write(f'{k}:{int(v)}\n')


Prize()
#___________________________________________________________________________
def Without_Prize():

    not_Prize = data.copy()                                                             # 10 Directors With Most numbre Film, Without Award.
    flt = not_Prize['Awards'] == 'No'

    not_Prize = not_Prize[flt]
    not_Prize.dropna(subset='Director',axis=0,inplace=True)

    Dir_Not_Pri ={}
    for i in not_Prize.index:
        Dir_Not_Pri[not_Prize['Director'].loc[i]] = Dir_Not_Pri.get(not_Prize['Director'].loc[i], 0) + 1

    Directors_Not_Prize = {}
    for k,v in Dir_Not_Pri.items():

        if v >= 9:
            w = k.split(' ')
            w = list(w)

            if len(w) == 3:
                Directors_Not_Prize[w[1],w[2],w[0]] = v
            else:   
                Directors_Not_Prize[w[1],w[0]] = v

    for k,v in Directors_Not_Prize.items():
        with open('Dir_Not_Prize.csv','a') as Pr:
            Pr.write(f'{k}:{int(v)}\n')


Without_Prize()
#___________________________________________________________________________
def Comprehensive_Data():

    DATA = data.copy()

    DATA.set_index('Year',inplace=True)                               # 25 Film With Most Popularity.
    DATA.sort_values('Year',inplace=True)

    flt = DATA['Popularity'] >= 88                                            
    Pop_data = DATA[flt][['Title','Genre','Popularity']]
    Pop_data.to_csv('25_Best_Film.csv')                                     
                                                               
    flt = DATA['Popularity'] < 2                                      # 30 Film With Most Hate.
    Hate_data = DATA[flt][['Title','Genre','Popularity']]
    Hate_data.to_csv('30_Hate_Film.csv')                   
                                  
    flt = DATA['Length'] < 40                                         # 10 Film Fewer 40min.
    Short_Films = DATA[flt][['Title','Genre','Length']]
    Short_Films.to_csv('10Film_Fewer_40min.csv')
                                  
    flt = DATA['Length'] > 240                                        # 10 Film More Than 4h.
    Long_Films = DATA[flt][['Title','Genre','Length']]
    Long_Films.to_csv('10Film_More_Than_4h.csv')


Comprehensive_Data()
#___________________________________________________________________________
Comedy = data['Genre'] == 'Comedy'                                     # Released Films Based On 5 Originale Genres After 1970.
data_Comedy = data[Comedy]
C = (data_Comedy['Year'] > 1970)

Action = data['Genre'] == 'Action' 
data_Action = data[Action]
A = (data_Action['Year'] >= 1970)

Drama = data['Genre'] == 'Drama' 
data_Drama = data[Drama]
D = (data_Drama['Year'] >= 1970)

Western = data['Genre'] == 'Western' 
data_Western = data[Western]
W = (data_Western['Year'] >= 1970)

Mystery = data['Genre'] == 'Mystery' 
data_Mystery = data[Mystery]
M = (data_Mystery['Year'] >= 1970)

print('\n____________After 1970___________\n')

def Prt(GENRE,LEN):
    print(f'{GENRE:7} ::: {LEN:3} Film')


Prt('Drama',len(data_Drama[D]))
Prt('Comedy',len(data_Comedy[C]))
Prt('Action',len(data_Action[A]))
Prt('Mystery',len(data_Mystery[M]))
Prt('Western',len(data_Western[W]))
