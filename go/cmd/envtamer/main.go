package main

import (
	"fmt"
	"os"

	"https://github.com/syro83/envtamer-workshop/internal/command"
)

func main() {
	rootCmd := command.NewRootCmd()

	if err := rootCmd.Execute(); err != nil {
		fmt.Fprintln(os.Stderr, err)
		os.Exit(1)
	}
}
