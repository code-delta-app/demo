package main

import (
	"flag"
	"fmt"
	"os"

	"github.com/meridian/helpdesk/cli/internal/store"
)

func main() {
	if len(os.Args) < 2 {
		usage()
		os.Exit(2)
	}

	ts := store.NewTicketStore()
	ts.Seed()

	switch os.Args[1] {
	case "list":
		for _, t := range ts.ListOpen() {
			fmt.Printf("#%04d  P%d  %s\n", t.ID, t.Priority, t.Subject)
		}
	case "show":
		fs := flag.NewFlagSet("show", flag.ExitOnError)
		id := fs.Int("id", 0, "ticket id")
		_ = fs.Parse(os.Args[2:])
		if t, ok := ts.Get(*id); ok {
			fmt.Printf("#%d %s\nStatus: %s\n\n%s\n", t.ID, t.Subject, t.Status, t.Body)
		} else {
			fmt.Fprintln(os.Stderr, "no such ticket")
			os.Exit(1)
		}
	case "close":
		fs := flag.NewFlagSet("close", flag.ExitOnError)
		id := fs.Int("id", 0, "ticket id")
		_ = fs.Parse(os.Args[2:])
		if ts.Close(*id) {
			fmt.Printf("closed #%d\n", *id)
		} else {
			fmt.Println("no such ticket")
		}
	default:
		usage()
		os.Exit(2)
	}
}

func usage() {
	fmt.Println("usage: helpdesk <list|show|close> [-id N]")
}
