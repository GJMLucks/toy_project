package main

import "fmt"

/*
	GO는 작성스타일이 강제되어있음
	괄호"{}" 시작시 반드시 같은 줄에서 시작해야함
*/

func main() {

	// 세미콜론을 붙이는게 원칙이지만, 구문이 한개인 경우 생략하더라도 컴파일러가 자동으로 추가함
	fmt.Println("Hello World");

	// 변수 선언은 3가지 방식이 있다.
	var name1 string = "name1"	// 1. 정석 - var [변수명] [자료형]
	var name2 = "name2"			// 2. 초기값이 있으면 [자료형] 생략가능
	name3 := "name3"			// 3. 짧은선언
	
	fmt.Println(name1, name2, name3)

	// 변수 여러개 선언
	var x, y, z int = 1, 2, 3	// 콤마로 여러개 선언을 구분한다. 선언과 대입 수가 같아야 한다.
    var l, n, m = 4, 5, 6		// 역시 초기값이 있으면 [자료형] 생략가능
	// 짧은선언도 가능하다.
	v_int, v_float, v_string, v_bool := 24, 3.14, "gong", false
	
	// 'var()'으로도 선언이 가능하다
	var (
		t_int int
		t_float, t_string = 1.314, "t_name"
	)

	// 병렬할당 : 여러개 변수를 한번에 대입가능하다.
	var t_bool bool
	t_int, t_bool = 7, true

	fmt.Println("(x, y, z) = ", x, y, z)
	fmt.Println("(l, n, m) = ", l, n, m)
	fmt.Println("v_int, v_float, v_string, v_bool = ", v_int, v_float, v_string, v_bool)
	fmt.Println("t_int, t_float, t_string, t_bool = ", t_int, t_float, t_string, t_bool)
	
	// 안쓰는 임시변수 처리
	var useless_var int = 8
	_ = useless_var				// 원래, 선언한 변수를 사용하지 않으면 컴파일 에러
}