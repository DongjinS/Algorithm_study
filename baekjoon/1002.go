package main

import (
	"fmt"
	"math"
)

func main() {
	var n, x1, y1, r1, x2, y2, r2 int
	var sum_r, sub_r float64
	fmt.Scanf("%d", &n)
	for i := 0; i < n; i++ {
		answer := 0
		fmt.Scanf("%d %d %d %d %d %d", &x1, &y1, &r1, &x2, &y2, &r2)
        d := math.Sqrt(float64((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)))
        sum_r = float64(r1 + r2)
		if r1 < r2 {
            sub_r = float64(r2 - r1)
		} else {
            sub_r = float64(r1 - r2)
		}
		if d == 0 && r1 == r2 {
			answer = -1
			if r1 == 0 {
				answer = 1
			}
		} else if sum_r == d || sub_r == d {
			answer = 1
		} else if sum_r > d && sub_r < d {
			answer = 2
		}

		fmt.Println(answer)
	}
}
