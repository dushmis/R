package main

import (
	"flag"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strings"
)

func cp(dst, src string) error {
	s, err := os.Open(src)
	if err != nil {
		return err
	}
	// no need to check errors on read only file, we already got everything
	// we need from the filesystem, so nothing can go wrong now.
	defer s.Close()
	d, err := os.Create(dst)
	if err != nil {
		return err
	}
	if _, err := io.Copy(d, s); err != nil {
		d.Close()
		return err
	}
	return d.Close()
}

var (
	destFolder = "/opt/dushyant/imessage/downloads_"
	m          = make(map[string]string)
)

func visit(path string, f os.FileInfo, err error) error {
	if !f.IsDir() {
		//
		newfile := getFileName(path, f)

		s, err := os.Open(newfile)
		defer s.Close()
		if os.IsNotExist(err) {
			m[path] = newfile
			// fmt.Printf("file does not exit %s\n", path)
			// fmt.Printf("Visited: %s - %#v \n", path, getFileName(path, f))
			fmt.Print(".")
			cp(newfile, path)
		}
	}
	return nil
}

func getFileName(path string, f os.FileInfo) string {
	t := f.ModTime().Format("Mon_Jan_02_15-04-05-2006")
	if strings.HasSuffix(destFolder, "/") {
		return fmt.Sprintf("%s%s-%s", destFolder, t, f.Name())
	} else {
		return fmt.Sprintf("%s/%s-%s", destFolder, t, f.Name())
	}
}

func main() {
	flag.Parse()
	root := flag.Arg(0)
	if root != "" {

		filepath.Walk(root, visit)
		len_ := len(m)
		if len_ > 0 {
			fmt.Printf("%d files copied...\n", len_)
		} else {
			fmt.Printf("%d new files...\n", len_)
		}
	}
	// fmt.Printf("filepath.Walk() returned %v\n", err)
}
