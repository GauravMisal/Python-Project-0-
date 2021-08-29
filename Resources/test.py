with open("movie.txt","r") as file:
    lst1 = []
    for line in file:
        lst = line.split(",")
        lst[4] = lst[4].strip()
        lst1.append(lst)
        
    movie_count = 0    
    rating_count_more4 = 0
    rating_count_between3_4 = 0
    movie_time = 0

    a = set()
    d = {}
    for i in range(len(lst1)):
        for j in range(len(lst1[i])):
            # 1. Find the number of movies released between 1950 and 1960.
            if 1950 <= int(lst1[i][2]) <= 1960:
                movie_count+=1

            # 2. Find the number of movies having rating more than 4.
            if lst1[i][3] == '':
                pass
            elif float(lst1[i][3]) > 4:
                rating_count_more4+=1

            # 3. Find the movies whose rating are between 3 and 4.
            elif 3 <= float(lst1[i][3]) <= 4:
                rating_count_between3_4+=1

            # 4. Find the number of movies with duration more than 2 hours (7200 second).
            if lst1[i][4] == '':
                pass
            elif int(lst1[i][4]) >= 7200:
                movie_time+=1

            # 5. Find the list of years and number of movies released each year.
            a.add(lst1[i][2])
            
    for i in a:
        d[i] = 0

    for i in range(len(lst1)):
        for j in range(len(lst1[i])):
            if lst1[i][2] in d:
                d[lst1[i][2]] += 1
                break

    print("1. Movie Count :", movie_count)
    print("2. Rating Count more than 4 :", rating_count_more4)
    print("3. Rating Count between 3 ND 4 :", rating_count_between3_4)
    print("4. Movie time more than 2 hours :", movie_time)
    print("5. list of years and number of movies released each year :")
    for k , v in d.items():
        print(k , "-->" , v)
    print("6. total number of movies in dataset :", sum(d.values()))




        


