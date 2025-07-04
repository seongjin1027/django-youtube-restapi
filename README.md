# django-youtube-restapi

## (1) Project Settings

-Github

## Model 구조 => ORM

 (1) User => users

- email
- password
- nickname
- is_business

 (2) Video => videos

- title
- description
- link
- views_count
- thumbnail
- video_file: link
- User: FK

ex) 파일(이미지, 동영상)
=> 장고에 부하가 걸림.
=> S3 Bucker(저렴, 속도가 빠름) -> 결과물:링크

 (3) Reaction => reactions

- User: Fk
- video: FK
- reaction (like, dislike, cancel) => 실제 youtube rest api

 (4) Comment => comments

- User: FK
- Video: FK
- content
- like
- dislike

 (5) Subscription => subscriptions
 
 - User: FK => subscriber (내가 구독한 사람)
 - User: FK => subscribed_to (나를 구독한 사람)

 (6) Common => common
 
- created_at
- updated_at

 모델을 먼저 정의한 이유는 DB migration(테이블 구조 정의) => REST API