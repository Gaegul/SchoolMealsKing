> 대마고 3학년 프로젝트 실무 개인 프로젝트인 내가 바로 전국 급식왕에 대한 문서입니다. 프론트엔드는 구현하지 않고 백엔드 Api만 구현 할 예정입니다.

[노션문서](https://www.notion.so/eunjus/5a25390e25e240108f8b1d3a9aacc3ce)

### Elastic search를 이용한 빅데이터 기반 자료 처리

요즘 같은 시대에 많은 데이터를 다뤄 보는 것이 중요하다. 언제쯤 한번 Elastic search를 사용 해보고 싶어서 이번 프실 개인 프로젝트에 도입하게 되었다.

### Work Flow 및 목표

1. 나이스 api를 이용한 전국의 급식 정보를 파싱하여 Elastic search에 넣는다.
2. 파싱된 급식 정보는 검색이 최적화 될 수 있도록 네임 태그등의 후가공 처리를 한다.
3. 사용자는 elastic search에서 나이스보다 빠르게 급식을 파싱할 수 있다.

### Api

- 학교 리스트 조회

    [학교 리스트 조회[GET]](https://www.notion.so/GET-8872e12fc53949edbe75d8fb077ac410)

- 어떠한 학교의 최근 7일간 급식 정보 조회

    [최근 7일간 급식 조회[GET]](https://www.notion.so/7-GET-a82aba9c345b4f3281eb2c4279d9dc9a)

- 오늘 우리 학교의 급식 조회

    [오늘 우리학교 급식 조회[GET]](https://www.notion.so/GET-a0a33d992f6f451e821c63d1d386ad59)

- 오늘 급식이 제일 맛있는 학교 랭킹(중식 기준)

    [오늘 급식이 제일 맛있는 고등학교[GET] in g](https://www.notion.so/GET-in-g-6e78e49c3e75497cb6d635a2252b3ccf)

- 우리 학교와 똑같은 급식인 학교는?

    [급식이 똑같은 학교 리스트[GET] ing](https://www.notion.so/GET-ing-9785ec0adf8b417a91291e8336534643)

### 급식 파싱

[https://open.neis.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=OPEN17320190722180924242823&infSeq=2](https://open.neis.go.kr/portal/data/service/selectServicePage.do?page=1&rows=10&sortColumn=&sortDirection=&infId=OPEN17320190722180924242823&infSeq=2)

나이스 api 에서 확인 가능