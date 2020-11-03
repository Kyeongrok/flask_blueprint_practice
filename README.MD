
## Package 설치
pip install -r requirements.txt 명령어로 package를 설치 해줍니다.

## DB초기화 방법
CSV파일을 DB에 insert합니다.
```
1.insert_dat/01_insert_into_db.py를 엽니다.
2.db접속정보, csv파일이 들어있는 dir을 입력 합니다.
3.실행 합니다.
``` 

```
dbi = DbInit('postgresql://root:12345678@127.0.0.1:5432/postgres',
 'C:/Users/ocean/Desktop/synthea_cdm_csv/')
```

## Api 사용 방법
swagger : http://127.0.0.1:5000/


