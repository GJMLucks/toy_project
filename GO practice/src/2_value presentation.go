package main

import (
	"fmt"
	"math"
	"unsafe"
)

func main() {

	// 정수 표기
	var int1 = 9
	var int2 = -10
    var int3 = 011	// 8진수
	var int4 = 0x12 // 16진수

	fmt.Println("9 ->", int1, "| -10 -> ", int2, "| 011 -> ", int3, "| 0x12 -> ", int4)

	// 실수 표기
	var float1 = 0.13
    var float2 = .14
    var float3 = 1.5

    var float4 = 1e6
	var float5 = .17E+1
	var float6 = 1.8e-2

	fmt.Println("0.13 -> ", float1, "| .14 -> "	  , float2, "| 1.5 -> "	  , float3)
	fmt.Println("1e6 -> " , float4, "| .17E+1 -> ", float5, "| 1.8e-2 -> ", float6)
	fmt.Println()

	// rounding error 처리
	var example_float = 10.0
	const machine_epsilon = 1e-14	// go의 machine_epsilon, 값의 차가 이보다 작으면 같은값으로 간주함

	for i := 0; i < 10; i++ {
		example_float = example_float - 0.1
	}

	fmt.Println("example_float - 9.0 == 0? : ", example_float == 9.0)
	fmt.Println("example_float : ", example_float)
	fmt.Println("example_float == 9.0? : ", math.Abs(example_float - 9.0) <= machine_epsilon)
	fmt.Println()

	// 복소수 표기
	var complex1 = 1 + 2i
	var complex2 = 3.4 + 5.6i
	var complex3 = complex(7, 8)
	var complex4 = complex(.9, 1.2)

	fmt.Println(complex1, complex3)
	fmt.Println("(", real(complex2), "+", imag(complex2), "i) (", real(complex4), "+", imag(complex4), "i)")
	fmt.Println()

	// byte 표기
	var byte1 = 10
	var byte2 = 0x10
    var byte3 = 'a'
//	var byte3 = "a"	 ==>	컴파일 오류
//	var byte3 = 'ab' ==>	컴파일 오류
//	var byte3 = "ab" ==>	컴파일 오류

	fmt.Println("10 ->", byte1, "| 0x10 ->", byte2, "| 'a' ->", byte3)
	fmt.Println()

	// rune 표기
    var rune1 = '\ud55c'	// 한
    var rune2 = '\U0000d55c'// 한
	var rune3 = '한'
//	var rune3 = "한"   ==>	컴파일 오류
//	var rune3 = '한국' ==>	컴파일 오류
//	var rune3 = "한국" ==>	컴파일 오류

	fmt.Println("ud55c ->", rune1, "| U0000d55c ->", rune2, "| 한 ->", rune3)
	fmt.Println()

	// arithmetic calculation	: +, -, *, /, %, <<, >>, ^
	var num1 int = 1
	var num2 float32 = 2.3

	// 같은 자료형만 연산이 가능하다.
//	fmt.Println( num1 + num2 ) ==>	컴파일 오류
	fmt.Println( "float32(num1) + num2 : "	, float32(num1) + num2 )
	fmt.Println( "num1 + int(num2) : "		, num1 + int(num2) )
	fmt.Println()

	// overflow, underflow
//	var num unit8 = math.MaxInt8 + 1  ==>	컴파일 오류
//	var num unit8 = 0 - 1			  ==>	컴파일 오류

	// size of data
	var data1 int8 = 1
	var data2 int16 = 2
    var data3 int32 = 3
	var data4 int64 = 4
    var data5 int = 5

	fmt.Println("size of int8 : "	, unsafe.Sizeof(data1))
	fmt.Println("size of int16 : "	, unsafe.Sizeof(data2))
	fmt.Println("size of int32 : "	, unsafe.Sizeof(data3))
	fmt.Println("size of int64 : "	, unsafe.Sizeof(data4))
	fmt.Println("size of int : "	, unsafe.Sizeof(data5))
	fmt.Println()
}