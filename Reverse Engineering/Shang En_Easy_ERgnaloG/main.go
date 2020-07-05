package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	welcome := `
====================================================
TOP SECRET Super HAxx0r DATABASE
WELCOME ANON 47
ENTER YOUR PASSWORD TO CONTINUE
====================================================
`
	password := "5up32_53cu23_p455w02d_f81"
	fmt.Println(welcome)
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter Password: ")
	text, _ := reader.ReadString('\n')
	flag := "YCEP{1_1uv_5721n95}"
	// convert CRLF to LF
	text = strings.Trim(text, " \r\n")
	if strings.Compare(password, text) == 0 {
		fmt.Printf("ACCESS GRANTED\nFlag: %s\n", flag)
	} else {
		fmt.Println("ACCESS DENIED")
	}
}
