# Git_Team
오픈소스 sw 팀 프로젝트
  * Git과 GitHub를 이용한 프로젝트

## 팀원 

|이름|소속 학과|학번|
|-|-|-|
|이재노|인공지능학과|2022078122|
|왕민|인공지능학과|2022087247|
|송재현|인공지능학과|2022067074|
|손혜성|인공지능학과|2022036962|

## branch protection rule

메인 브랜치에 머지시키는 것은 관리자(팀장)으로 제한해두었다.
단, 팀장은 자기 커밋 내용을 강제로 머지시킬 수 있도록 해두었다.

## 주제

python을 이용한 슈팅 게임 구현

![game](https://github.com/jeno0228/Git_Team/blob/main/code/%EA%B7%B8%EB%A6%BC01.jpg)

게임 

* pygame_test.py 

## 사용 언어

* PYTHON
  * import할 모듈
   
   ++ pygame
   ++ math
   ++ os
   ++ datetime
   ++ json
   ++ random
   ++ time


## 개발 환경

* Visual Studio Code


## 팀원

* 팀장: 이재노

* 팀원: 왕민, 손혜성, 송재현

## 게임 기능

* 기본적인 게임 구동
  * WASD키나 방향키로 우주선을 조종 가능
  * 마우스 클릭으로 미사일을 발사해 적을 파괴 가능
  * 적에 충돌하면 목숨 하나가 줄어들고 목숨이 다 사리지면 게임 종료
  * 아이템을 먹을 수 있음
  
* 회원가입 로그인 랭킹 기능
  * 게임 실행전에 회원가입 및 로그인을 할 수 있음
  * 회원기록은 member.json 파일에 이러한 형식으로 저장되어있다. 
  * 초기 점수값은 0으로 지정

    ```json
    {
      "user": [
        {
           "id": "사용자1 아이디",
           "password": "사용자1 비밀번호",
           "score": 0
        },
        {
           "id": "사용자2 아이디",
           "password": "사용자2 비밀번호",
           "score": 0
        } 
      ]
    }
  
    ```
* 자동발사 기능
  * 마우스 클릭 없이도 미사일을 발사 할 수 있음
* 결과 출력
 * 게임이 종료되면 점수를 측정해 랭킹을 출력
 

## 1주차 프로젝트 진행 상황

* 주제 선정

  > pygame 모듈을 활용한 게임 구현

* 소스 코드 탐색 및 선택 


  > 우주선을 조종하면서 미사일을 발사해 외계인을 파괴하는 슈팅 게임

* github 공동 레파지토리 생성 및 팀원 초대, branch protection 설정
## 2주차 프로젝트 진행 상황

* 사운드 추가 (배경음악,미사일 발사,외계인 파괴,우주선 파괴 사운드 )
* 총알 크기 아이템 
* 난이도 추가 
* 타이머 기능 추가
* 점수 기능 추가


## 3주차 프로젝트 진행 상황

* 랭킹 기능 및 로그인 기능 구현 중
* 우주선 자동 공격 기능 구현 중
* 운석 (체력이 있는 적 개체) 구현 중
* 시작화면 

## 4주차 프로젝트 진행 상황

* 랭킹 기능 계산 및 화면 출력

* 회원가입 및 로그인 기능 추가

* 우주선 목숨 개수 설정

## 추가 개선 희망사항

* 회원가입 및 로그인 기능을 게임창에 출력(pygame으로 입력창을 만들지 못함)

* 자동 움직이는 기능 

* 오토기능을 이용한 인공지능 우주선 팀원

* 일시 정지 기능

* member.json 같이 누구나 접근 가능한 회원기록 없이 회원기록 저장 
