import pandas as pd
import numpy as np

f = open("u.user", 'r')
d = f.readlines()
f.close()
n = np.array(d)
user_index = ["user id", "age", "gender", "occupation", "zip_code"]
user = np.char.strip(n)
user = np.char.split(user, '|', 4)
user_df = pd.DataFrame(list(user), columns=user_index)
user_df["user id"] = user_df["user id"].astype('int')

f = open("u.data", 'r')
d = f.readlines()
f.close()
n = np.array(d)
data = np.char.strip(n)
data = np.char.split(data, '\t')
data_index = ["user id", "movie id", "rating", "timestamp"]
data_df = pd.DataFrame(list(data), columns=data_index)
for col in data_index:
    data_df[col] = data_df[col].astype('int')

data_df = data_df.drop(['timestamp'], axis=1)

f = open("u.item", 'r', encoding="ISO-8859-1")
d = f.readlines()
f.close()
n = np.array(d)
item_index = ['movie id', 'movie title', 'release date', 'video release date',
    'IMDb URL', 'unknown', 'Action', 'Adventure', 'Animation', "Children's",
    'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
    'Film-Noir', 'Horror ', 'Musical', 'Mystery', 'Romance', 'Sci-Fi',
    'Thriller', 'War', 'Western']
item = np.char.strip(n)
item = np.char.split(item, '|')
item_df = pd.DataFrame(list(item), columns=item_index)
#item_df["user id"] = item_df["user id"].astype('int')
#item_df = item_df.drop(['release date'], axis=1)

# 2-a top100 popular movies by all user
# for i in range(1, 944):
#     user_dat = data_df[data_df.user_id == i]
#     user_dat = user_dat.sort_values(by=['rating'], ascending=False)
#     if len(user_dat) > 100:
#         user_dat = user_dat[:100]


# 2-b
# male = pd.DataFrame(columns=["user_id", "item_id", "rating"])
# female = pd.DataFrame(columns=["user_id", "item_id", "rating"])
#
# for i in range(0, 100000):
#     u_i = data_df.iloc[i].user_id
#     user_r = user_df.loc[user_df.user_id == u_i]
#     gen = user_r.iloc[0]['gender']
#     if gen == 'M':
#         male.loc[len(male)] = data_df.iloc[i]
#     else:
#         female.loc[len(female)] = data_df.iloc[i]

#2-c occupation
data_user = pd.merge(data_df[['user id', 'movie id', 'rating']], user_df[['user id', 'occupation']], on='user id')
data_user.drop(columns=['user id'], inplace=True)

data_user_item = pd.merge(data_user[['user id', 'movie id', 'rating']], item_df[['movie id', 'movie title']], on='movie id')
data_user_item.drop(columns=['user id'], inplace=True)


data_user_item_sorted = data_user_item.groupby(['occupation', 'movie title'], as_index=False)['rating'].mean().sort_values('rating', ascending=False)

top_3_occ = data_user_item_sorted.groupby(['occupation']).head(3).sort_values(['occupation', 'movie title'], ascending=[True, True]).reset_index()
top_3_occ.drop(['index'], axis=1, inplace=True)

