# cd to a file
# cdf /tmp/file/where/you/want/to/go.txt
# it'll go to /tmp/file/where/you/want/to/ folder
# put this in .zshrc or .bashrc, source this or add it in those files
cdf() {
  echo "$(dirname "$1")";
  cd "$(dirname "$1")";
}
