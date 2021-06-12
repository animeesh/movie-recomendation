

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv("movie_dataset1.csv")
df.head()


def get_data():
    df['title'] = df['title'].str.lower()
    return df


get_data()

# In[3]:


features = ['keywords', 'cast', 'genres', 'director']
for feature in features:
    df[feature] = df[feature].fillna("")


# In[4]:


def combine_features(row):
    return row['keywords'] + "" + row['cast'] + "" + row['genres'] + "" + row['director']


df["combine_features"] = df.apply(combine_features, axis=1)
# df["combine_features"].head()
data_combine = df["combine_features"]

data_combine


# combine_features()


# In[5]:


def combine_features(row):
    data = row['keywords'] + "" + row['cast'] + "" + row['genres'] + "" + row['director']
    df["combine_features"] = df.apply(data, axis=1)
    # df["combine_features"].head()
    data_combine = df["combine_features"]
    return data_combine


data_combine

# In[6]:


from sklearn.feature_extraction.text import CountVectorizer


def transform_data(data_combine):
    cv = CountVectorizer()
    cv_matrix = cv.fit_transform(df["combine_features"])
    # print(cv_matrix.toarray())
    similirity_scores = cosine_similarity(cv_matrix)
    return similirity_scores


# print(similirity_scores)

transform_data(data_combine)

# In[7]:


# import pickle
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer()

cv_matrix = cv.fit_transform(df["combine_features"])

# print(cv_matrix.toarray())
similirity_scores = cosine_similarity(cv_matrix)


#print((similirity_scores).shape)
# pickle.dump(similirity_scores,open("sim_score.pickle",'wb'))


# In[19]:


def get_title_from_index(index):
    return df[df.index == index]["title"].values[0]


def get_index_from_title(title):
    return df[df.title == title]["index"].values[0]


def recommend(movies_user_like):
    # movie_user_like= x

    # movies_user_like=input("movie_name:  ")
    movies_user_like = movies_user_like.lower()
    # return movies_user_like

    # movie_user_like=movie_user_like
    global movielist
    # movies_user_like=movies_user_like.lower()
    movielist = []

    movie_index = get_index_from_title(movies_user_like)
    similar_movies = list(enumerate(similirity_scores[movie_index]))
    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)

    i = 0

    # for movie in sorted_similar_movies:
    for num, movie in enumerate(sorted_similar_movies, start=1):
        your_movie = (" {}: {}".format(num, get_title_from_index(movie[0])))

        # your_movie=get_title_from_index(movie[0])
        movielist.append(your_movie)

        # get_title_from_index(movie[0]).to_dict('records')
        # print(records)
        i = i + 1
        if i > 10:
            break
    return


def movie_list():
    return movielist
#print(movielist)

