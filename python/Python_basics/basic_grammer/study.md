# Basic grammer about python
## 1. 기본 문법
- 세미콜론
- 주석
- 들여쓰기
- 코드 블록

## 2. 숫자 자료형
- 정수(int)
    - 소수점 이하는 버림
- 실수(float)
    - 실수 정수 사칙연산시 값의 타입은 실수
- 복소수(complex)
    - 공학에서는 j사용
    - ex) 1.2+1.3j => (1.2+1.3j)
- 사칙연산
    - '+' : 더하기
    - '-' : 빼기
    - '*' : 곱하기
    - '/' : 나누기(실수)
    - '//' : 몫(버림)
    - '%' : 나머지
        - divmod(target, div number)
    - '**' : 거듭제곱

## 3. 진수 표현
- 2진수: 숫자 앞에 0b를 붙이며 0과 1을 사용합니다.
    - 0b110 => 6
- 8진수: 숫자 앞에 0o(숫자 0과 소문자 o)를 붙이며 0부터 7까지 사용합니다.
    - 0o10 => 8
- 16진수: 숫자 앞에 0x 또는 0X를 붙이며 0부터 9, A부터 F까지 사용합니다(소문자 a부터 f도 가능).
    - 0xF => 15

## 4. 변수 설정
- 영문 문자와 숫자를 사용할 수 있습니다.
- 대소문자를 구분합니다.
- 문자부터 시작해야 하며 숫자부터 시작하면 안 됩니다.
- _(밑줄 문자)로 시작할 수 있습니다.
- 특수 문자(+, -, *, /, $, @, &, % 등)는 사용할 수 없습니다.
- 파이썬의 키워드(if, for, while, and, or 등)는 사용할 수 없습니다
- 변수 삭제는 del
- 빈 변수 만들기
    - ex) x = None
- input 값을 변수에 할당할 때 type은 string
- map을 이용해서 각각 들어가는 타입 변경가능

## 5. 출력
- sep
- end
- format
