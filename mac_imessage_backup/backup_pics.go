package main

import "fmt"
import "os"

import "os/exec"

var (
	destFolder = "/opt/dushyant/imessage/downloads/test"
)

func main() {
	getDir("/Users/dushyant/Library/Messages/Attachments/")
}

func fileYouThere(fileName string) bool {
	if _, err := os.Stat(fileName); err == nil {
		return true
	}
	return false
}

func sameFile(firstFile, secondFile string) bool {
	first := fileYouThere(firstFile)
	second := fileYouThere(secondFile)
	if !first || !second {
		return false
	}
	s1, _ := os.Stat(firstFile)
	s2, _ := os.Stat(secondFile)
	if s1.Size() == s2.Size() && s1.Name() == s2.Name() {
		return true
	}
	return false
}
func backUpExist(fileName string) bool {
	return fileYouThere(fmt.Sprintf("%s_", fileName))
}

/*func copyFileFunc(firstFile, secondFile string) {
	cpCmd := exec.Command("cp", "-p", firstFile, secondFile)
	err := cpCmd.Run()
	if err != nil {
		fmt.Println(err.Error())
	}
}*/

func cp(src, dst string) error {
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

func getDir(location string) {
	a, _ := os.Open(location)
	defer a.Close()

	var b []os.FileInfo
	b, _ = a.Readdir(-1)
	for x := range b {
		n := b[x]
		where := fmt.Sprintf("%s%s", location, n.Name())
		if n.IsDir() {
			where = fmt.Sprintf("%s%s", where, "/")
			getDir(fmt.Sprintf("%s", where))
		} else {
			m, errorOpen := os.Open(where)
			if errorOpen != nil {
				fmt.Printf("ERR OPEN %s", errorOpen.Error())
				return
			}
			defer m.Close()
			var k os.FileInfo
			k, err := m.Stat()
			if err != nil {
				fmt.Printf("XYZ %s", err)
				return
			}
			origFile := where
			fileName := k.Name()
			copyFile := fmt.Sprintf("%s%s", destFolder, fileName)
			if _, err := os.Stat(copyFile); os.IsNotExist(err) {
				fmt.Printf("Copied new file %s\n",copyFile)
				copyFileFunc(origFile, copyFile)
			} else {
				if !sameFile(copyFile, origFile) {
					fmt.Println("File available with same name")
					if !backUpExist(copyFile) {
						fmt.Println("File available with same name, backup doesn't exit")
						fmt.Printf("saving to new file %s\n",fmt.Sprintf("%s_", copyFile))
						copyFileFunc(origFile, fmt.Sprintf("%s_", copyFile))
					}
				}else{
					fmt.Print(".")
				}
			}
		}
	}
}
