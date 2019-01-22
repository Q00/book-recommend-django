# book-watcha

모든 파일은 encoding='cp949'로 읽는다.

### best_book.csv
첫 로그인 시 유저에게 보여주기 위해 선정된 유명한 책들 목록.

### tags.csv
태그들의 목록

### book.json
책들의 목록 

title, author, country, tags 로 구성되어 있으며 tags에는 tag의 list가 들어있음

## recommend.py -> recommending_books(args)
book_list: 유저가 선정한 책들의 목록

tag_list: 유저가 선정한 tag들의 목록

author_score_rate, country_score_rate, tag_score_rate: score 방식에 영향을 주는 parameter

topn: output으로 상위 몇 개를 가져올 것인가 결정

book_path: "book.json" 파일의 경로
