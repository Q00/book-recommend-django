#!/usr/bin/env python
# coding: utf-8

# In[1]:
import pandas as pd
import math
import sys
import os
import codecs
import json
# In[2]:


def recommending_books(book_list, tag_list, author_score_rate=1.0, country_score_rate=0.5, tag_score_rate=1.5, 
                       topn=10, book_path="ebdjango/ebdjango/book_watcha/book.json"):
    print(book_list)
    book = pd.read_json(codecs.open('ebdjango/book_watcha/book.json','r','utf-8-sig'))
    read_book = book[book['title'].isin(book_list)]
    # 읽은 책들에 대한 작가의 등장 횟수로 score계산
    author_score = read_book.author.value_counts().to_dict()
    for author in author_score:
        author_score[author] = math.log(1+author_score[author])
    
    # 읽은 책들에 대한 나라의 등장 횟수로 score계산
    country_score = read_book.country.value_counts().to_dict()
    for country in country_score:
        country_score[country] = math.log(1+country_score[country])
    
    tag_score = {}
    
    # 읽은 책들에 대한 태그의 등장 횟수로 score계산
    for tag_array in read_book.tags:
        for tag in tag_array:
            if tag in tag_score:
                tag_score[tag] += 1
            else:
                tag_score[tag] = 1
                
    # 유저의 태그 목록으로 score 계산
    # 읽은 책들에 대한 태그와의 보정을 위해 책들 수만큼 더해준다.
    for tag in tag_list:
        if tag in tag_score:
            tag_score[tag] += len(book_list)
        else:
            tag_score[tag] = len(book_list)
    for tag in tag_score:
        tag_score[tag] = math.log(1+tag_score[tag])
    
    # print(author_score)
    # print(country_score)
    # print(tag_score)
    
    def calculate_score(row):
        if row['title'] in book_list:
            return -1
        else:
            score = 0
            if row['author'] in author_score:
                score += author_score[row['author']] * author_score_rate
            if row['country'] in country_score:
                score += country_score[row['country']] * country_score_rate
            tags = row['tags']
            for tag in tags:
                if tag in tag_score:
                    # 태그가 많은 책에 대한 보정을 위해 약하게 나누는 항을 추가한다.
                    score += tag_score[tag] * tag_score_rate / math.sqrt(math.log(1+len(tags)))
            return score
        
    top_idx = book.apply(calculate_score, axis=1).sort_values(ascending=False).index[:topn]
    # print(book.loc[top_idx])

    return book.title[top_idx].tolist()

if __name__ == "__main__":
    #test
    recommending_books(['모모',],['판타지',])
