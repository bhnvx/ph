## Accounts Book Service Back-end
* 23/01/05 시점으로 해당 `README.md`가 작성됐습니다. 
* 서버는 Python / Django / RestFrameWork 기반으로 구축되어 있습니다.
* 기본적으로 Typescript 스러운 형식을 위해 Typing 모듈을 함께 사용했습니다.
* 사용된 라이브러리의 버전관리는 `requirements.txt`를 통해 진행합니다.

---

## app 별 코드 설명
#### 기능별 분리
* 서버는 각각의 기능별로 구분된 앱으로 구성됐습니다.
* 앱의 명칭은 소스코드를 보면 알 수 있듯, 모델 네이밍 기반으로 작성하였습니다.

#### TDD 지향
* 서버는 앱별로 `tests.py`가 작성 됐습니다.
* 자세한 내용은 각 앱 내부의 `tests.py` 파일을 참고하시길 바랍니다.

#### 앱 공통
1. 라우팅
    * 가장 먼저 사용자의 요청을 받는 곳은 `payhere` 앱 입니다.
    * 해당 폴더 내의 `urls.py`로 부터 요청 분기가 시작 됩니다.

2. 파일별 역할
    * `views.py` : 주요 Business Logic이 구현됐습니다.
    * `urls.py` : 파일 내부에 자세한 라우팅이 기술됐습니다.
    * `models.py` : 파일 내부에 계정 모델이 기술됐습니다.
    * `serializers.py` : 파일 내부에 각 모델별 serializer가 구현됐습니다.
    * `tests.py` : 파일 내부에 각 앱별 테스트가 기술됐습니다.
   #### users app 특정 파일
    * `managers.py` : 기본 User 모델의 Custom을 위한 코드가 기술됐습니다.
    * `auth.py` : JWT Token 인증을 위한 코드가 기술됐습니다.
    * `exception.py` : error를 핸들링 하기 위한 코드가 기술됐습니다.
   
3. 설정
    * 앱의 세부 설정을 확인하기 위해서는 payhere 내의 settings 모듈을 참고해주세요.
    * settings는 현재 `MySQL` 을 위한 설정으로만 한정됐지만, 추후 필요에 따라 세분화가 가능합니다.
---

## 각 app 설명

### USERS
* 계정 기능을 담당하는 app입니다.
* 계정이 생성될 경우, 생성된 계정은 로그인시 자동으로 JWT Token이 발행됩니다.
* 발행된 토큰은 `set_cookie`를 통해 자동으로 Cookie에 저장됩니다.
* 토큰은 1시간 후에 만료됩니다.

### ACCOUNTS
* 가계부 기능을 담당하는 app입니다.
* 가계부의 CRUD 기능을 담당하고 있습니다.
* 기본적으로 request를 보낸 user가 아니면, permission이 denied 됩니다.

### LINKS
* URL 단축 기능을 담당하는 app입니다.
* 단축된 URL은 30분의 만료기간을 가지고 있습니다.
---

## 사용방법
* 현재 `python:3.11`버전을 통해 작성된 코드입니다.
* `python`이 설치가 안됐다면, 설치 후 진행하시길 바랍니다.

1. `git clone` 을 통한 코드 확보
    ```commandline
    git clone https://github.com/bhnvx/ph.git
    ```
2. 폴더 내 `.env` 파일 작성
3. `virtualenv` 환경 생성
    ```commandline
    virtualenv {VENV_NAME}
   call .{VENV_NAME}/Scripts/activate
    ```
4. 명령을 통해 패키지 의존성 설치
    ```commandline
    pip install -r requirements.txt
    ```
5. 명령을 통한 DB Migrate
   ```commandline
   python manage.py migrate
   ```
6. seeding을 통해 db 더미 데이터 생성
    ```commandline
    python manage.py users_seeding
    python manage.py accounts_seeding
    ```
7. 명령을 통해 구동
    ```commandline
    python manage.py runserver
    ```