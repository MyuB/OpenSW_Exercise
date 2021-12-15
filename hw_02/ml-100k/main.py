import numpy as np
import pandas as pd
from copy import copy

#data file 읽어오기
data = pd.read_csv('u.data', sep="\t", encoding='utf-8', header=None)
data.columns = ['user id', 'movie id', 'rating', 'timestamp']
#item file 읽어오기
item = pd.read_csv('u.item', sep="|", encoding='ISO-8859-1', header=None)
item.columns = ['movie id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'unknown', 'Action',
                'Adventure', 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy', 'Film-Noir',
                'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
genre_list = ['unknown', 'Action', 'Adventure', 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary',
              'Drama', 'Fantasy', 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi',
              'Thriller', 'War', 'Western']
#user file 읽어오기
user = pd.read_csv('u.user', sep="|", encoding='utf-8', header=None)
user.columns = ['user id', 'age', 'gender', 'occupation', 'zip code']
#occupation file 읽어오기
occupation = pd.read_csv('u.occupation', sep="|", encoding='utf-8', header=None)
occupation.columns = ['Occupations']
occupation_list = list(occupation['Occupations'])

#merge the 'data' table with 'user' table
data_user = pd.merge(data[['user id', 'movie id', 'rating']], user[['user id', 'gender', 'occupation']], on='user id')
#data_user.drop(columns=['user id'], inplace=True)

#merge the 'Data_User' dataframe with 'Item' dataframe to get each rating, occupation of user and movie title
data_user_item = pd.merge(data_user[['user id', 'movie id', 'rating', 'gender', 'occupation']], item[['movie id', 'movie title']], on='movie id')
data_user_item.drop(columns= ['movie id'], inplace=True)

data_user_item_sorted_user = data_user_item.groupby(['user id', 'movie title'], as_index=False)['rating'].mean().sort_values('rating', ascending=False)
user_df = data_user_item_sorted_user.sort_values(['user id', 'movie title'], ascending=[True, True])

data_user_item_sorted_occ = data_user_item.groupby(['occupation', 'movie title'], as_index=False)['rating'].mean().sort_values('rating', ascending=False)
occupation_df = data_user_item_sorted_occ.sort_values(['occupation', 'movie title'], ascending=[True, True])

data_user_item_sorted_gender = data_user_item.groupby(['gender', 'movie title'], as_index=False)['rating'].mean().sort_values('rating', ascending=False)
gender_df = data_user_item_sorted_gender.sort_values(['gender', 'movie title'], ascending=[True, True])

'''
value_count() 메서드 사용해야함?
'''


# #2-b번
# user_list = [i for i in range(1, 944)]
# for u in user_list:
#     condition = (user_df['user id'] == u)
#     by_user = user_df[condition]
#     by_user = by_user.sort_values('rating', ascending=False)
#     # if len(by_user) > 100:
#     #     print(by_user[:100])
#     # else:
#     #     print(by_user)
#
# gender_list = ['F', 'M']
# for g in gender_list:
#     condition = (gender_df.gender == g)
#     by_gender = gender_df[condition]
#     by_gender = by_gender.sort_values('rating', ascending=False)
#     # if len(by_gender) > 100:
#     #     print(by_gender[:100])
#     # else:
#     #     print(by_gender)
#
# for occ in occupation_list:
#     condition = (occupation_df.occupation == occ)
#     by_occ = occupation_df[condition]
#     by_occ = by_occ.sort_values('rating', ascending=False)
#     # if len(by_occ) > 100:
#     #     #print(by_occ[:100])
#     # else:
#     #     #print(by_occ)

#2-b번 완성

user_list = [i for i in range(1, 944)]
for u in user_list:
    condition = (data_user_item['user id'] == u)
    by_user = data_user_item[condition]
    by_user = by_user.groupby(['movie title', 'user id'], as_index=False).size().sort_values('size', ascending=False)
    if len(by_user) > 100:
        print(by_user[:100])
    else:
        print(by_user)

#3-b번

data_item = pd.merge(data[['user id', 'movie id', 'rating']], item, on='movie id')
data_item.drop(columns = ['movie id', 'release date', 'video release date', 'IMDb URL'], inplace=True)

# #For each genre get the top 100 movies by average rating
# for gen in genre_list:
#     g_r = data_item[data_item[gen] == 1]
#     new_gen = pd.DataFrame(g_r.groupby(['movie title'], as_index=False)['rating'].mean().sort_values(['rating', 'movie title'], ascending=[False, True]))
#     new_gen.insert(0, 'genre', gen)
#     print(new_gen)
#     #top_3_genre = top_3_genre.append(new_gen, ignore_index=True)

#print(top_3_genre)



