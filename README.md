# Barcode-Reader
## 目標
使用python3實現用webcam讀取條碼，並將條碼與時間等資訊紀錄寫入`txt`中
## 安裝
* 程式碼：https://drive.google.com/drive/folders/1i99Q-e0AlbgPH3AbBgJGHDwupZQ6y3Gj?usp=sharing
* 安裝opencv2
```
pip3 install opencv-python
```
* 安裝條碼解碼library
```
sudo apt-get install libzbar0
pip3 install pyzbar
```
* 安裝蜂鳴器library
```
sudo apt-get install beep
```

* ubuntu系統為了避免吵雜，預設會將蜂鳴器關閉，需要將此選項關閉，輸入下列指令開啟設定檔
```
sudo gedit /etc/modprobe.d/blacklist.conf
```
* 在設定檔中找到`blacklist pcspkr`並將其註解，如下圖
![](https://i.imgur.com/uoEFdFz.png)
* 在輸入下列指令，蜂鳴器即可正常運行
```
sudo modprobe pcspkr
```
* 下圖須註解
![](https://i.imgur.com/BZyf63I.png)

## 使用方法
在程式碼位置輸入下列指令
```
python3 test.py
```
* 使用結果如下，掃描到卡號會顯示至終端機並寫入`txt`中
![](https://i.imgur.com/c55N7BY.png)
