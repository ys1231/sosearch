rm -rf out build *.log searchso.spec
pyinstaller -F  -w ./main.py --distpath=out -n sosearch
cp ./out/sosearch ~/.bin
sudo chmod a+x ~/.bin/sosearch