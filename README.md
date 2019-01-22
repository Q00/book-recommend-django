# django api server - for recommending book api

### how to use
    - Method : post
    - Data : 
        ```
        {
            'books':['book1','book2','book3'],
            'tags':['tag1','tag2','tag3']
        }
        ```
### In nodejs server
    - location : src/util/index.js
    - import CallPython from 'util'
    - How to call
        - CallPython(book_list,tag_list)
        - CallPython(
            {'books':['book1','book2','book3']},
            {'tags':['tag1','tag2','tag3']}
            )
        - return
            - book order by score
            - array
                - ['book1','book2','book3']
